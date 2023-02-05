from asyncio import tasks
from decimal import Inexact
from re import T
from turtle import rt
from unicodedata import category
import discord
from operator import index
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select, Interaction
from discord_components import SelectOption as Sel
from discord.utils import get
from email.errors import InvalidMultipartContentTransferEncodingDefect
import asyncio
import json
from discord_components import ComponentsBot
import interactions
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption, Option
from youtube_dl import YoutubeDL
import os
import discord
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption, Interaction
import interactions
from interactions import Modal, TextInput
import json
import asyncio
from discord.ext import commands
from BTSET import Moderation, embpy, bdpy, BD
rtask = None
class Roomedit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_room(self, ctx: commands.Context):
        stb_gld: discord.Guild = self.bot.get_guild(981511419042361344)
        emb = discord.Embed(title='***⚙️ Управление приватными комнатами***',
                            description='👑 - назначить нового создателя комнаты \n\
                            🗒 - ограничить/выдать доступ к комнате \n\
                            👥 - задать новый лимит участников \n\
                            🔒 - закрыть/открыть комнату \n\
                            ✏️ - изменить название комнаты \n\
                            👁‍🗨 - скрыть/открыть комнату \n\
                            🚪 - выгнать участника из комнаты \n\
                            🎙 - ограничить/выдать право говорить',
                            color = Moderation(ctx.author).color)
        await ctx.send(embed=emb,
        components = [
            [
                Button(emoji=await stb_gld.fetch_emoji(1020971032309403758)),
                Button(emoji=await stb_gld.fetch_emoji(1020971040416993280)),
                Button(emoji=await stb_gld.fetch_emoji(1020971037741043713)),
                Button(emoji=await stb_gld.fetch_emoji(1020971036252053524))
            ],
            [
                Button(emoji=await stb_gld.fetch_emoji(1020971043856330782)),
                Button(emoji=await stb_gld.fetch_emoji(1020971035014746162)),
                Button(emoji=await stb_gld.fetch_emoji(1020971033756450866)),
                Button(emoji=await stb_gld.fetch_emoji(1020971039141920819))
            ]
    ]
    )
    
    
    #тут все идеальнео можно больше не трогать
    async def listener_on_voice_state_update_roomedit_move(self, member: discord.Member, before, after):
        try:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            role = bdpy(ctx=member)['FirstRole']
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

    async def roomedit_on_button_click(self, interaction: Interaction):                     #эту санину надо переписать!
        stb_gld: discord.Guild = self.bot.get_guild(981511419042361344)
        if str(interaction.author.id) == bdpy(ctx=interaction)['Selfrooms'][str(interaction.author.voice.channel.id)]:
            role = bdpy(ctx=interaction)['FirstRole']
            if not(role in interaction.guild.roles):
                role = interaction.guild.roles[0]
            async def write(n):
                ow2 = discord.PermissionOverwrite()
                if not(n):
                    ow2.send_messages = False
                else:
                    ow2.send_messages = True
                await interaction.channel.set_permissions(target=interaction.author, overwrite=ow2)
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
                ownRoom = int(bdpy(ctx=interaction)['Selfrooms'][str(interaction.author.voice.channel.id)])

            if str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971032309403758)): #тут селект
                await embpy(ctx=interaction, comp='n', des='Укажите нового создателя этого канала @участник ')
                await write(1)
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write(0)
                data[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)] = [str(i.id) for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
                await ms.delete()

            elif str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971040416993280)):
                await embpy(ctx=interaction, comp='n', des='Напишите @участник которому хотите ограничить право входить в комнату')
                await write(1)
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write(0)
                pr = discord.PermissionOverwrite()
                if [i for i in ms.guild.members if ms.content == i.mention and not(i.guild_permissions.administrator)][0] in interaction.guild.members: ## тут проверяем на  все сразу
                    if [i for i in ms.guild.members if ms.content == i.mention][0] in ms.author.voice.channel.members:
                        if interaction.author.voice.channel.permissions_for([i for i in ms.guild.members if ms.content == i.mention][0]).connect:
                            pr.connect = False
                            await embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был заблокирован доступ к комнате!')
                            [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                        else:
                            pr.connect = True
                            await embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был разблокирован доступ к комнате!')
                        await interaction.author.voice.channel.set_permissions(target=[i for i in ms.guild.members if ms.content == i.mention][0], overwrite=pr)
                        await ms.delete()
                    else:
                        if interaction.author.voice.channel.permissions_for([i for i in ms.guild.members if ms.content == i.mention][0]).connect:
                            pr.connect = False
                            await embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был заблокирован доступ к комнате!')
                        else:
                            pr.connect = True
                            await embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был разблокирован доступ к комнате!')
                        await interaction.author.voice.channel.set_permissions(target=[i for i in ms.guild.members if ms.content == i.mention][0], overwrite=pr)
                        await ms.delete()
                else:
                    await embpy(ctx=interaction, comp='e', des=f'Участника {ms.content} не существует!')
                    await ms.delete()


            elif str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971037741043713)):
                await embpy(ctx=interaction, comp='n', des='напишите число участников от 0 до 99')
                await write(1)
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write(0)
                # if int(ms.content) <= 99:
                try:
                    await ms.author.voice.channel.edit(user_limit=int(ms.content))
                    await embpy(ctx=interaction, comp='s', des=f'Количество людей в комнате ограничено на {ms.content}')
                except TypeError:
                    await embpy(ctx=interaction, comp='e', des='Укажите число от 1 до 99')
                # else:
                    # await embpy(ctx=interaction, comp='e', des=f'Укажите число от 1 до 99')
                await ms.delete()
                

            elif str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971036252053524)):
                fr = role
                pr = interaction.author.voice.channel.overwrites_for(fr)
                if interaction.author.voice.channel.overwrites_for(fr).connect:
                    pr.connect = False
                    await embpy(ctx=interaction, comp='s', des=f'Доступ к комнате ограничен!')
                else:
                    pr.connect = True
                    await embpy(ctx=interaction, comp='s', des=f'Ограничение к комнате снято!')

                await interaction.author.voice.channel.set_permissions(target=fr, overwrite=pr)

            elif str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971043856330782)):
                await embpy(ctx=interaction, comp='n', des='напишите новое название комнаты')
                await write(1)
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write(0)
                await ms.author.voice.channel.edit(name=f'{ms.content}')
                await ms.delete()


            elif str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971035014746162)):
                fr = role
                pr = interaction.author.voice.channel.overwrites_for(fr)
                
                if interaction.author.voice.channel.overwrites_for(fr).view_channel:
                    pr.view_channel = False
                    await embpy(ctx=interaction, comp='s', des=f'Доступ к просмотру комнаты ограничен!')
                else:
                    pr.view_channel = True
                    await embpy(ctx=interaction, comp='s', des=f'Ограничение к просмотру комнаты снято!')

                await interaction.author.voice.channel.set_permissions(target=fr, overwrite=pr)

            elif str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971033756450866)): #селект
                await embpy(ctx=interaction, comp='s', des='напишите @участник  которого хотите выгнать')
                await write(1)
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write(0)
                [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                await ms.delete()


            elif str(interaction.component.emoji) == str(await stb_gld.fetch_emoji(1020971039141920819)):  #селект
                await embpy(ctx=interaction, comp='n', des='напишите @участник которому хотите ограничить право говорить')
                await write(1)
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write(0)
                pr = discord.PermissionOverwrite()
                
                if interaction.author.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).speak:
                    
                    member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    if member.voice.mute == False:
                        pr.speak = False
                        await member.edit(mute = True)
                        await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                    else:
                        await embpy(ctx=interaction, comp='e', des=f'Пользователь {member} уже был замучен на сервере!')
                else:
                    pr.speak = True
                    member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    await member.edit(mute = False)
                    
                    await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                    
                await interaction.author.voice.channel.set_permissions(
                    target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
                await ms.delete()
        else:
            await embpy(ctx=interaction, comp='e', des='Вы не создатель этой комнаты!')


    async def listener_roomedit_start(self, interaction: Interaction):
        global rtask
        if rtask:
            rtask.cancel()
        rtask = asyncio.create_task(Roomedit(bot=self.bot).roomedit_on_button_click(interaction))

    async def listener_on_voice_state_update_roomedit_mute(self, member: discord.Member, before, after):
        try:
            Selfrooms = bdpy(ctx=member)['Selfrooms']
            if (not(after) and not(before.channel.permissions_for(member).speak) and str(before.channel.id) in [k for k in Selfrooms.keys()]) or (after.channel != before.channel and not(before.channel.permissions_for(member).speak) and str(before.channel.id) in [k for k in Selfrooms.keys()]):
                await member.edit(mute = False)
        except:
            pass
        
# class Roomeditint(interactions.Extension):
#     def __init__(self, client):
#         self.client = client
    
#     @interactions.extension_listener('on_button_click')
#     async def ddddd(self, interaction):
#         print(interaction)
#         print(dir(interaction))
#         if str(interaction.component.emoji) == '👥':
#             await interaction.popup(Modal(
#                             custom_id='button1',
#                             title=' ',
#                             components=[
#                                 TextInput(
#                                     style=TextStyleType.SHORT,
#                                     custom_id='qwertyuiop',
#                                     label='число'
#                                 )
#                             ]
#                         ))

