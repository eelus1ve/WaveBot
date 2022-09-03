from asyncio import tasks
from turtle import rt
from unicodedata import category
import discord
from operator import index
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select
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
from BD import bdmpy, bdpy
from BTSET import embpy
rtask = None
class Roomedit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def room(self, ctx):
    #     with open('users.json', 'r') as file:
    #         dataServerID = json.load(file)
    #         COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
    #         ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
    #         SelfRoom = int(dataServerID[str(ctx.author.guild.id)]['selfRoom'])

    #     emb = discord.Embed(title='***⚙️ Управление приватными комнатами***',
    #                         description='👑 - назначить нового создателя комнаты \n\
    #                         🗒 - ограничить/выдать доступ к комнате \n\
    #                         👥 - задать новый лимит участников \n\
    #                         🔒 - закрыть/открыть комнату \n\
    #                         ✏️ - изменить название комнаты \n\
    #                         👁‍🗨 - скрыть/открыть комнату \n\
    #                         🚪 - выгнать участника из комнаты \n\
    #                         🎙 - ограничить/выдать право говорить',
    #                         color = COLOR)
    #     await ctx.send(embed=emb,
    #     components = [
    #         [
    #             Button(emoji = '👑', style=1),
    #             Button(emoji = '🗒', style=1),
    #             Button(emoji = '👥', style=1),
    #             Button(emoji = '🔒', style=1)
    #         ],
    #         [
    #             Button(emoji = '✏️', style=1),
    #             Button(emoji = '👁‍🗨', style=1),
    #             Button(emoji = '🚪', style=1),
    #             Button(emoji = '🎙', style=1)
    #         ]
    #     ]
    # )


    @commands.Cog.listener('on_voice_state_update')
    async def roomedit_move_on_voice_state_update(self, member, defore, after):
        try:
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            role = bdmpy(mr=member)['FirstRole']
            try:
                SelfRooms = dataServerID[str(defore.channel.guild.id)]['Selfrooms']
                SelfRoom = int(dataServerID[str(defore.channel.guild.id)]['selfRoom']["vc"])
            except:
                SelfRooms = dataServerID[str(after.channel.guild.id)]['Selfrooms']
                SelfRoom = int(dataServerID[str(after.channel.guild.id)]['selfRoom']["vc"])
            try:
                if after.channel.id == SelfRoom:
                    chlen = await after.channel.guild.create_voice_channel(name=f'{member.name}', category=[i for i in member.guild.categories if i.id == int(dataServerID[str(after.channel.guild.id)]['selfRoom']["ctp"])][0])
                    await member.move_to(chlen)
                    ow1 = discord.PermissionOverwrite()
                    ow1.connect = True
                    ow1.view_channel = True
                    if role in member.guild.roles:
                        TARGET=role
                    else:
                        TARGET = member.guild.roles[0]
                    await member.voice.channel.set_permissions(target=TARGET, overwrite=ow1)
                    dataServerID[str(member.guild.id)]['Selfrooms'].update({
                        str(chlen.id): str(member.id)})
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)
            except:
                if defore.channel.id == SelfRoom:
                    chlen = await after.channel.guild.create_voice_channel(name=f'{member.name}', category=[i for i in member.guild.categories if i.id == int(dataServerID[str(after.channel.guild.id)]['selfRoom']["ctp"])][0])
                    await member.move_to(chlen)
                    ow1 = discord.PermissionOverwrite()
                    ow1.connect = True
                    ow1.view_channel = True
                    if role in member.guild.roles:
                        TARGET=role
                    else:
                        TARGET = member.guild.roles[0]
                    await member.voice.channel.set_permissions(target=TARGET, overwrite=ow1)
                    dataServerID[str(member.guild.id)]['Selfrooms'].update({
                        str(chlen.id): str(member.id)})
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)

            if defore.channel.name in [i.name for i in defore.channel.guild.voice_channels if i.id in [int(k) for k in SelfRooms.keys()]]:
                if not (defore.channel.members):
                    await defore.channel.delete()
                    dataServerID[str(member.guild.id)]['Selfrooms'].pop(str(defore.channel.id))
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)
        except:
            pass

    async def roomedit_on_button_click(self, interaction):
        if str(interaction.author.id) == bdpy(ctx=interaction)['Selfrooms'][str(interaction.author.voice.channel.id)]:
            role = bdmpy(mr=interaction.author)['FirstRole']
            if role in interaction.guild.roles:
                TARGET=role
            else:
                TARGET = interaction.guild.roles[0]
            async def write():
                ow2 = discord.PermissionOverwrite()            
                if interaction.channel.overwrites_for(TARGET).send_messages:
                    ow2.send_messages = False
                else:
                    ow2.send_messages = True
                await interaction.channel.set_permissions(target=TARGET, overwrite=ow2)
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                ownRoom = int(dataServerID[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)])

            if str(interaction.component.emoji) == '👑': #тут селект
                await interaction.send(embed=embpy(ctx=interaction, comp='n', des='Укажите нового создателя этого канала @участник '))
                await write()
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write()
                dataServerID[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)] = [str(i.id) for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)
                await ms.delete()

            elif str(interaction.component.emoji) == '🗒':
                await interaction.send(embed=embpy(ctx=interaction, comp='n', des='Напишите @участник которому хотите ограничить право входить в комнату'))
                await write()
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write()
                pr = discord.PermissionOverwrite()
                if [i for i in ms.guild.members if ms.content == i.mention][0] in interaction.guild.members:
                    if [i for i in ms.guild.members if ms.content == i.mention][0] in ms.author.voice.channel.members:
                        if interaction.author.voice.channel.permissions_for([i for i in ms.guild.members if ms.content == i.mention][0]).connect:
                            pr.connect = False
                            await interaction.send(embed=embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был заблокирован доступ к комнате!'))
                            [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                        else:
                            pr.connect = True
                            await interaction.send(embed=embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был разблокирован доступ к комнате!'))
                        await interaction.author.voice.channel.set_permissions(target=[i for i in ms.guild.members if ms.content == i.mention][0], overwrite=pr)
                        await ms.delete()
                    else:
                        if interaction.author.voice.channel.permissions_for([i for i in ms.guild.members if ms.content == i.mention][0]).connect:
                            pr.connect = False
                            await interaction.send(embed=embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был заблокирован доступ к комнате!'))
                        else:
                            pr.connect = True
                            await interaction.send(embed=embpy(ctx=interaction, comp='s', des=f'Участнику {ms.content} был разблокирован доступ к комнате!'))
                        await interaction.author.voice.channel.set_permissions(target=[i for i in ms.guild.members if ms.content == i.mention][0], overwrite=pr)
                        await ms.delete()
                else:
                    embpy(ctx=interaction, comp='e', des=f'Участника {ms.content} не существует!')
                    await ms.delete()


            elif str(interaction.component.emoji) == '👥':
                await interaction.send(embed = embpy(ctx=interaction, comp='n', des='напишите число участников'))
                await write()
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write()
                try:
                    await ms.author.voice.channel.edit(user_limit=int(ms.content))
                    await interaction.send(embed = embpy(ctx=interaction, comp='s', des=f'Количество людей в комнате ограничено на {ms.content}'))
                except TypeError:
                    await interaction.send(embed = embpy(ctx=interaction, comp='e', des='Укажите число от 1 до 99'))
                await ms.delete()

            elif str(interaction.component.emoji) == '🔒':
                fr = TARGET
                pr = interaction.author.voice.channel.overwrites_for(fr)
                if interaction.author.voice.channel.overwrites_for(fr).connect:
                    pr.connect = False
                    await interaction.send(embed = embpy(ctx=interaction, comp='s', des=f'Доступ к комнате ограничен!'))
                else:
                    pr.connect = True
                    await interaction.send(embed = embpy(ctx=interaction, comp='s', des=f'Ограничение к комнате снято!'))

                await interaction.author.voice.channel.set_permissions(target=fr, overwrite=pr)

            elif str(interaction.component.emoji) == '✏️':
                botmes = await interaction.send(embed = embpy(ctx=interaction, comp='n', des='напишите новое название комнаты'))
                await write()
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write()
                await ms.author.voice.channel.edit(name=f'{ms.content}')
                await botmes.edit('123')
                await ms.delete()


            elif str(interaction.component.emoji) == '👁‍🗨':
                fr = TARGET
                pr = interaction.author.voice.channel.overwrites_for(fr)
                
                if interaction.author.voice.channel.overwrites_for(fr).view_channel:
                    pr.view_channel = False
                    await interaction.send(embed = embpy(ctx=interaction, comp='s', des=f'Доступ к просмотру комнаты ограничен!'))
                else:
                    pr.view_channel = True
                    await interaction.send(embed = embpy(ctx=interaction, comp='s', des=f'Ограничение к просмотру комнаты снято!'))

                await interaction.author.voice.channel.set_permissions(target=fr, overwrite=pr)

            elif str(interaction.component.emoji) == '🚪': #селект
                await interaction.send(embed = embpy(ctx=interaction, comp='s', des='напишите @участник  которого хотите выгнать'))
                await write()
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write()
                [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                await ms.delete()


            elif str(interaction.component.emoji) == '🎙':  #селект
                await interaction.send(embed = embpy(ctx=interaction, comp='n', des='напишите @участник которому хотите ограничить право говорить'))
                await write()
                def check(msg: discord.Message):
                    return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

                ms = await self.bot.wait_for(event='message', check=check)
                await write()
                pr = discord.PermissionOverwrite()
                
                if interaction.author.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).speak:
                    
                    member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    if member.voice.mute == False:
                        pr.speak = False
                        await member.edit(mute = True)
                        await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                    else:
                        await interaction.send(embed = embpy(ctx=interaction, comp='e', des=f'Пользователь {member} уже был замучен на сервере!'))
                else:
                    pr.speak = True
                    member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                    await member.edit(mute = False)
                    
                    await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                    
                await interaction.author.voice.channel.set_permissions(
                    target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
                await ms.delete()
        else:
            await interaction.send(embed=embpy(ctx=interaction, comp='e', des='Вы не создатель этой комнаты!'))

    @commands.Cog.listener('on_button_click')
    async def roomedit_start(self, interaction):
        global rtask
        if rtask:
            rtask.cancel()
        rtask = asyncio.create_task(Roomedit(bot=self.bot).roomedit_on_button_click(interaction))
        
    @commands.Cog.listener('on_voice_state_update')
    async def roomedit_mute_on_voice_state_update(self, member, before, after):
        Selfrooms = bdmpy(mr=member)['Selfrooms']
        try:
            if (not(after) and not(before.channel.permissions_for(member).speak) and str(before.channel.id) in [k for k in Selfrooms.keys()]) or (after.channel != before.channel and not(before.channel.permissions_for(member).speak) and str(before.channel.id) in [k for k in Selfrooms.keys()]):
                    await member.edit(mute = False)
        except:
            pass
def setup(bot):
    bot.add_cog(Roomedit(bot))