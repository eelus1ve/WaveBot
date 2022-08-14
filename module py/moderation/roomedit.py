import discord
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption, Interaction
import interactions
from interactions import Modal, TextInput
import json
import asyncio
from discord.ext import commands
class roomedit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def room(self, ctx):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            SelfRoom = int(dataServerID[str(ctx.author.guild.id)]['selfRoom'])

        emb = discord.Embed(title='***⚙️ Управление приватными комнатами***',
                            description='👑 - назначить нового создателя комнаты \n\
                            🗒 - ограничить/выдать доступ к комнате \n\
                            👥 - задать новый лимит участников \n\
                            🔒 - закрыть/открыть комнату \n\
                            ✏️ - изменить название комнаты \n\
                            👁‍🗨 - скрыть/открыть комнату \n\
                            🚪 - выгнать участника из комнаты \n\
                            🎙 - ограничить/выдать право говорить',
                            color = COLOR)
        await ctx.send(embed=emb,
        components = [
            [
                Button(emoji = '👑', style=1),
                Button(emoji = '🗒', style=1),
                Button(emoji = '👥', style=1),
                Button(emoji = '🔒', style=1)
            ],
            [
                Button(emoji = '✏️', style=1),
                Button(emoji = '👁‍🗨', style=1),
                Button(emoji = '🚪', style=1),
                Button(emoji = '🎙', style=1)
            ]
        ]
    )

    @commands.Cog.listener('on_voice_state_update')
    async def ion_voice_state_update(self, a, b, c):
        try:
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                try:
                    SelfRoom = int(dataServerID[str(b.channel.guild.id)]['selfRoom'])
                except:
                    SelfRoom = int(dataServerID[str(c.channel.guild.id)]['selfRoom'])
            try:
                if c.channel.id == SelfRoom:
                    chlen = await c.channel.guild.create_voice_channel(name = f'\./ {a.name}')
                    await a.move_to(chlen)
                    dataServerID[str(a.guild.id)]['Selfrooms'].update({
                        str(chlen.id): str(a.id)})
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)
            except:
                if b.channel.id == SelfRoom:
                    chlen = await c.channel.guild.create_voice_channel(name = f'\./ {a.name}')
                    await a.move_to(chlen)
            
            if b.channel.name in [i.name for i in b.channel.guild.voice_channels if i.name.startswith('\./')]:
                if not(b.channel.members):
                    await b.channel.delete()
                    dataServerID[str(a.guild.id)]['Selfrooms'].pop(str(b.channel.id))
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)
        except:
            pass

    @commands.Cog.listener('on_button_click')
    async def aon_button_click(self, interaction):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            ownRoom = int(dataServerID[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)])
            SelfRoom = int(dataServerID[str(interaction.channel.guild.id)]['selfRoom'])
            print(str(interaction.component.emoji))

        if str(interaction.component.emoji) == '👑':
            await interaction.send('укажите нового создателя этого канала @участник ')
            ms = await self.bot.wait_for(event='message')
            if ms.author == interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel:
                dataServerID[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)] = [str(i.id) for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)
                await ms.delete()
            else:
                while ms.author != interaction.guild.get_member(ownRoom):
                    if ms.author != interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel: continue
                    ms = await self.bot.wait_for(event='message')
                    try:
                        dataServerID[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)] = \
                        [str(i.id) for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                        with open('users.json', 'w') as file:
                            json.dump(dataServerID, file, indent=4)
                    except:
                        pass
                    await ms.delete()

        elif str(interaction.component.emoji) == '🗒':
            await interaction.send('напишите @участник которому хотите ограничить право входить в комнату')
            ms = await self.bot.wait_for(event='message')
            if ms.author == interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel:
                pr = discord.PermissionOverwrite()
                if interaction.author.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).connect:
                    pr.connect = False
                else:
                    pr.connect = True
                await interaction.author.voice.channel.set_permissions(
                    target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
                await ms.delete()
            else:
                while ms.author != interaction.guild.get_member(ownRoom):
                    if ms.author != interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel: continue
                    pr = discord.PermissionOverwrite()
                    try:
                        pr = discord.PermissionOverwrite()
                        if interaction.author.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).connect:
                            pr.connect = False
                        else:
                            pr.connect = True
                        await interaction.author.voice.channel.set_permissions(
                            target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0],
                            overwrite=pr)
                    except:
                        pass
                    await ms.delete()

        elif str(interaction.component.emoji) == '👥':
            await interaction.send('напишите число участников')
            ms = await self.bot.wait_for(event='message')
            if ms.author == interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel:
                await ms.author.voice.channel.edit(user_limit=int(ms.content))
                await ms.delete()
            else:
                while ms.author != interaction.guild.get_member(ownRoom) and ms.channel != interaction.channel:
                    ms = await self.bot.wait_for(event='message')
                    if ms.author != interaction.guild.get_member(ownRoom) or ms.channel != interaction.channel: continue
                    try:
                        await ms.author.voice.channel.edit(user_limit=int(ms.content))
                    except:
                        pass
                    await ms.delete()

        elif str(interaction.component.emoji) == '🔒':
            pr = discord.PermissionOverwrite()
            if interaction.author.voice.channel.permissions_for(interaction.guild.get_member(ownRoom)).connect:
                pr.connect = False
            else:
                pr.connect = True
            await interaction.author.voice.channel.set_permissions(target=interaction.guild.roles[0], overwrite=pr)

        elif str(interaction.component.emoji) == '✏️':
            await interaction.send('напишите новое название комнаты')
            ms = await self.bot.wait_for(event='message')
            if ms.author == interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel:
                await ms.author.voice.channel.edit(name=f'\./{ms.content}')
                await ms.delete()
            else:
                while ms.author != interaction.guild.get_member(ownRoom):
                    if ms.author != interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel: continue
                    ms = await self.bot.wait_for(event='message')
                    try:
                        await ms.author.voice.channel.edit(name=f'\./{ms.content}')
                    except:
                        pass
                    await ms.delete()

        elif str(interaction.component.emoji) == '👁‍🗨':
            pr = discord.PermissionOverwrite()
            if interaction.author.voice.channel.permissions_for(interaction.guild.get_member(ownRoom)).view_channel:
                pr.view_channel = False
            else:
                pr.view_channel = True
            await interaction.author.voice.channel.set_permissions(target=interaction.guild.roles[0], overwrite=pr)

        elif str(interaction.component.emoji) == '🚪':
            await interaction.send('напишите @участник  которого хотите выгнать')
            ms = await self.bot.wait_for(event='message')
            if ms.author == interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel:
                [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                await ms.delete()
            else:
                while ms.author != interaction.guild.get_member(ownRoom):
                    if ms.author != interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel: continue
                    ms = await self.bot.wait_for(event='message')
                    try:
                        [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                    except:
                        pass
                    await ms.delete()

        elif str(interaction.component.emoji) == '🎙':
            await interaction.send('напишите @участник которому хотите ограничить право говорить')
            ms = await self.bot.wait_for(event='message')
            if ms.author == interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel:
                pr = discord.PermissionOverwrite()
                if interaction.author.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).speak:
                    pr.speak = False
                    fthfhty = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    await fthfhty.move_to(interaction.guild.get_channel(SelfRoom))
                    await asyncio.sleep(1)
                    await fthfhty.move_to(interaction.author.voice.channel)
                else:
                    pr.speak = True
                    fthfhty = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    await fthfhty.move_to(interaction.guild.get_channel(SelfRoom))
                    await asyncio.sleep(1)
                    await fthfhty.move_to(interaction.author.voice.channel)
                await interaction.author.voice.channel.set_permissions(target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
                await ms.delete()
            else:
                while ms.author != interaction.guild.get_member(ownRoom):
                    if ms.author != interaction.guild.get_member(ownRoom) and ms.channel == interaction.channel: continue
                    try:
                        pr = discord.PermissionOverwrite()
                        if interaction.author.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).speak:
                            pr.speak = False
                            fthfhty = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                            await fthfhty.move_to(interaction.guild.get_channel(SelfRoom))
                            await asyncio.sleep(1)
                            await fthfhty.move_to(interaction.author.voice.channel)
                        else:
                            pr.speak = True
                            fthfhty = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                            await fthfhty.move_to(interaction.guild.get_channel(SelfRoom))
                            await asyncio.sleep(1)
                            await fthfhty.move_to(interaction.author.voice.channel)
                        await interaction.author.voice.channel.set_permissions(
                            target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
                    except:
                        pass
                    await ms.delete()
def setup(bot):
    bot.add_cog(roomedit(bot))