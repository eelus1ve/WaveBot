import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import json
import discord
import json
import asyncio
from discord.ext import commands
from BTSET import BD, Lang, InteractionComponents
from system.Bot import WaveBot
rtask = None


class Roomedit(commands.Cog):
    def __init__(self, bot: WaveBot, color):
        self.bot = bot
        self.color = color

    async def command_room(self, ctx: commands.Context):
        stb_gld: discord.Guild = self.bot.get_guild(981511419042361344)
        emb = discord.Embed(title='***⚙️ {}***'.format(Lang(ctx).language['roomedit_craate_title']),
                            description='👑 - {} \n🗒 - {} \n👥 - {} \n🔒 - {} \n✏️ - {} \n👁‍🗨 - {} \n🚪 - {} \n🎙 - {}'.format(Lang(ctx).language['roomedit_craate_des_1'], Lang(ctx).language['roomedit_craate_des_2'], Lang(ctx).language['roomedit_craate_des_3'], Lang(ctx).language['roomedit_craate_des_4'], Lang(ctx).language['roomedit_craate_des_5'], Lang(ctx).language['roomedit_craate_des_6'], Lang(ctx).language['roomedit_craate_des_7'], Lang(ctx).language['roomedit_craate_des_8']),
                            color=self.color)
        await ctx.send(embed=emb)
    #     components = [
    #         [
    #             Button(emoji=await stb_gld.fetch_emoji(1020971032309403758)),
    #             Button(emoji=await stb_gld.fetch_emoji(1020971040416993280)),
    #             Button(emoji=await stb_gld.fetch_emoji(1020971037741043713)),
    #             Button(emoji=await stb_gld.fetch_emoji(1020971036252053524))
    #         ],
    #         [
    #             Button(emoji=await stb_gld.fetch_emoji(1020971043856330782)),
    #             Button(emoji=await stb_gld.fetch_emoji(1020971035014746162)),
    #             Button(emoji=await stb_gld.fetch_emoji(1020971033756450866)),
    #             Button(emoji=await stb_gld.fetch_emoji(1020971039141920819))
    #         ]
    # ]
    # )

    #тут все идеальнео можно больше не трогать
    async def listener_on_voice_state_update_roomedit_move(self, member: discord.Member, before, after):
        try:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            role = self.bot.db_get_firstrole(after) # возможно здесь нужно писать мембера
            if not(role in member.guild.roles):
                role = member.guild.roles[0]
            try:
                SelfRooms = data[str(before.channel.guild.id)]['Selfrooms']
                SelfRoom = int(data[str(before.channel.guild.id)]['selfRoom']["vc"])
            except:
                SelfRooms = data[str(after.channel.guild.id)]['Selfrooms']
                SelfRoom = int(data[str(after.channel.guild.id)]['selfRoom']["vc"])
            try:
                if after.channel.id == SelfRoom:
                    chlen = await after.channel.guild.create_voice_channel(name=f'{member.name}', category=[i for i in member.guild.categories if i.id == int(data[str(after.channel.guild.id)]['selfRoom']["ctp"])][0])
                    await member.move_to(chlen)
                    ow1 = discord.PermissionOverwrite()
                    ow1.connect = True
                    ow1.view_channel = True
                    await member.voice.channel.set_permissions(target=role, overwrite=ow1)
                    data[str(member.guild.id)]['Selfrooms'].update({
                        str(chlen.id): str(member.id)})
            except:
                if before.channel.id == SelfRoom:
                    chlen = await after.channel.guild.create_voice_channel(name=f'{member.name}', category=[i for i in member.guild.categories if i.id == int(data[str(after.channel.guild.id)]['selfRoom']["ctp"])][0])
                    await member.move_to(chlen)
                    ow1 = discord.PermissionOverwrite()
                    ow1.connect = True
                    ow1.view_channel = True
                    await member.voice.channel.set_permissions(target=role, overwrite=ow1)
                    data[str(member.guild.id)]['Selfrooms'].update({
                        str(chlen.id): str(member.id)})

            if before.channel.name in [i.name for i in before.channel.guild.voice_channels if i.id in [int(k) for k in SelfRooms.keys()]]:
                if not (before.channel.members):
                    await before.channel.delete()
                    data[str(member.guild.id)]['Selfrooms'].pop(str(before.channel.id))
            with open(f'{BD}users.json', 'w') as file:
                json.dump(data, file, indent=4)
        except:
            pass

    async def roomedit_on_button_click(self, interaction: discord.Interaction):                     #эту санину надо переписать!
        inter = InteractionComponents(interaction)
        stb_gld: discord.Guild = self.bot.get_guild(981511419042361344)
        if str(interaction.user.id) == self.bot.db_get_selfrooms(interaction)[str(interaction.user.voice.channel.id)]:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            ownRoom = int(self.bot.db_get_selfrooms(interaction)[str(interaction.user.voice.channel.id)])
            role = self.bot.db_get_firstrole(interaction)

            if not(role in interaction.guild.roles):
                role = interaction.guild.roles[0]

            async def write(n):
                ow2 = discord.PermissionOverwrite()
                if not n:
                    ow2.send_messages = False
                else:
                    ow2.send_messages = True
                await interaction.channel.set_permissions(target=interaction.user, overwrite=ow2)

            def check(msg: discord.Message):
                return msg.author == interaction.user and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)
            
            async def get_mes():
                await write(1)
                ms: discord.Message = await self.bot.wait_for(event='message', check=check)
                await write(0)
                return ms

            if str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971032309403758)): #New owner in room
                await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                    title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                    description=Lang(ctx=interaction).language['roomedit_edit_new_own'],
                    color=self.color
                ))
                ms: discord.Message = await get_mes()
                data[str(interaction.guild.id)]['Selfrooms'][str(interaction.user.voice.channel.id)] = [str(i.id) for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
                await ms.delete()

            elif str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971040416993280)):       #ignore member
                await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                    title=Lang(ctx=interaction).language['roomedit_edit_ignore_member_1'],
                    color=self.color
                ))
                ms: discord.Message = await get_mes()
                pr = discord.PermissionOverwrite()
                if [i for i in ms.guild.members if ms.content == i.mention and not(i.guild_permissions.administrator)][0] in interaction.guild.members: ## тут проверяем на  все сразу
                    if [i for i in ms.guild.members if ms.content == i.mention][0] in ms.author.voice.channel.members:
                        if interaction.user.voice.channel.permissions_for([i for i in ms.guild.members if ms.content == i.mention][0]).connect:
                            pr.connect = False
                            await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                                title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                                description='{} {} {}'.format(Lang(ctx=interaction).language['roomedit_edit_ignore_member_2'], ms.content, Lang(ctx=interaction).language['roomedit_edit_ignore_member_3']),
                                color=self.color
                            ))
                            [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                        else:
                            pr.connect = True
                            await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                                title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                                description='{} {} {}'.format(Lang(ctx=interaction).language['roomedit_edit_ignore_member_2'], ms.content, Lang(ctx=interaction).language['roomedit_edit_ignore_member_4']),
                                color=self.color
                            ))
                        await interaction.user.voice.channel.set_permissions(target=[i for i in ms.guild.members if ms.content == i.mention][0], overwrite=pr)
                        await ms.delete()
                    else:
                        if interaction.user.voice.channel.permissions_for([i for i in ms.guild.members if ms.content == i.mention][0]).connect:
                            pr.connect = False
                            await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                                title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                                description='{} {} {}'.format(Lang(ctx=interaction).language['roomedit_edit_ignore_member_2'], ms.content, Lang(ctx=interaction).language['roomedit_edit_ignore_member_3']),
                                color=self.color
                            ))
                        else:
                            pr.connect = True
                            await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                                title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                                description='{} {} {}'.format(Lang(ctx=interaction).language['roomedit_edit_ignore_member_2'], ms.content, Lang(ctx=interaction).language['roomedit_edit_ignore_member_4']),
                                color=self.color
                            ))
                        await interaction.user.voice.channel.set_permissions(target=[i for i in ms.guild.members if ms.content == i.mention][0], overwrite=pr)
                        await ms.delete()
                else:
                    await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                        title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                        description='{} {} {}'.format(Lang(ctx=interaction).language['roomedit_edit_doesnt_exist_1'], ms.content, Lang(ctx=interaction).language['roomedit_edit_doesnt_exist_2']),
                        color=self.color
                    ))       #тут переписать через вывод ошибки
                    await ms.delete()

            elif str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971037741043713)):
                await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                    title=Lang(ctx=interaction).language['roomedit_edit_user_lim_1'],
                    color=self.color
                ))
                ms: discord.Message = await get_mes()
                # if int(ms.content) <= 99:
                try:
                    await ms.author.voice.channel.edit(user_limit=int(ms.content))
                    await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                        title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                        description='{} {}.'.format(Lang(ctx=interaction).language['roomedit_edit_user_lim_2'], ms.content),
                        color=self.color
                    ))
                except TypeError:
                    await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                        title=Lang(ctx=interaction).language['roomedit_edit_title_f'],
                        description='{} {}.'.format(Lang(ctx=interaction).language['roomedit_edit_user_lim_1'], ms.content),
                        color=self.bot.db_get_moderercolor(interaction)
                    ))
                # else:
                    # await embpy(ctx=interaction, comp='e', des=f'Укажите число от 1 до 99')
                await ms.delete()

            elif str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971036252053524)):
                fr = role
                pr = interaction.user.voice.channel.overwrites_for(fr)
                if interaction.user.voice.channel.overwrites_for(fr).connect:
                    pr.connect = False
                    await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                        title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                        description=Lang(ctx=interaction).language['roomedit_edit_block_inv_1'],
                        color=self.color
                    ))
                else:
                    pr.connect = True
                    await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                        title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                        description=Lang(ctx=interaction).language['roomedit_edit_block_inv_2'],
                        color=self.color
                    ))

                await interaction.user.voice.channel.set_permissions(target=fr, overwrite=pr)

            elif str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971043856330782)):
                await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                    title=Lang(ctx=interaction).language['roomedit_edit_new_name'],
                    color=self.color
                ))
                ms: discord.Message = await get_mes()
                await ms.author.voice.channel.edit(name=f'{ms.content}')
                await ms.delete()

            elif str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971035014746162)):
                fr = role
                pr: discord.abc.PermissionOverwrite = interaction.user.voice.channel.overwrites_for(fr)
                
                if interaction.user.voice.channel.overwrites_for(fr).view_channel:
                    pr.view_channel = False
                    await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                        title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                        description=Lang(ctx=interaction).language['roomedit_edit_block_watch_1'],
                        color=self.color
                    ))
                else:
                    pr.view_channel = True
                    await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                        title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                        description=Lang(ctx=interaction).language['roomedit_edit_block_watch_2'],
                        color=self.color
                    ))

                await interaction.user.voice.channel.set_permissions(target=fr, overwrite=pr)

            elif str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971033756450866)): #селект
                await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                    title=Lang(ctx=interaction).language['roomedit_edit_title_s'],
                    description=Lang(ctx=interaction).language['roomedit_edit_kick_1'],
                    color=self.color
                ))
                ms: discord.Message = await get_mes()
                [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                await ms.delete()

            elif str(inter.emoji) == str(await stb_gld.fetch_emoji(1020971039141920819)):  #селект
                await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                    title=Lang(ctx=interaction).language['roomedit_edit_block_voice_1'],
                    color=self.color
                ))
                ms: discord.Message = await get_mes()
                pr = discord.PermissionOverwrite()
                
                if interaction.user.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).speak:
                    
                    member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    if member.voice.mute is False:
                        pr.speak = False
                        await member.edit(mute = True)
                        await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                    else:
                        await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                            title=Lang(ctx=interaction).language['roomedit_edit_title_f'],
                            description='{} {} {}'.format(Lang(ctx=interaction).language['roomedit_edit_block_voice_2'], member, Lang(ctx=interaction).language['roomedit_edit_block_voice_3']),
                            color=self.color
                        ))
                else:
                    pr.speak = True
                    member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    await member.edit(mute = False)
                    
                    await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                    
                await interaction.user.voice.channel.set_permissions(
                    target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
                await ms.delete()
        else:
            await interaction.response.send_message(ephemeral=True, embed=discord.Embed(
                title=Lang(ctx=interaction).language['roomedit_edit_title_f'],
                description=Lang(ctx=interaction).language['roomedit_edit_error'],
                color=self.color
            ))

    async def listener_roomedit_start(self, interaction: discord.Interaction):
        global rtask
        if rtask:
            rtask.cancel()
        rtask = asyncio.create_task(Roomedit(bot=self.bot).roomedit_on_button_click(interaction))

    async def listener_on_voice_state_update_roomedit_mute(self, member: discord.Member, before, after):
        try:
            Selfrooms = self.bot.db_get_selfrooms(after)
            if (not after and not before.channel.permissions_for(member).speak and str(before.channel.id) in [k for k in Selfrooms.keys()]) or (after.channel != before.channel and not(before.channel.permissions_for(member).speak) and str(before.channel.id) in [k for k in Selfrooms.keys()]):
                await member.edit(mute = False)
        except:
            pass