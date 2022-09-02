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
from BD import bdmpy
from BTSET import embpy

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
    async def ion_voice_state_update(self, a, b, c):
        try:
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            try:
                SelfRooms = dataServerID[str(b.channel.guild.id)]['Selfrooms']
                SelfRoom = int(dataServerID[str(b.channel.guild.id)]['selfRoom']["vc"])
            except:
                SelfRooms = dataServerID[str(c.channel.guild.id)]['Selfrooms']
                SelfRoom = int(dataServerID[str(c.channel.guild.id)]['selfRoom']["vc"])
            try:
                if c.channel.id == SelfRoom:
                    chlen = await c.channel.guild.create_voice_channel(name=f'{a.name}', category=[i for i in a.guild.categories if i.id == int(dataServerID[str(c.channel.guild.id)]['selfRoom']["ctp"])][0])
                    await a.move_to(chlen)
                    dataServerID[str(a.guild.id)]['Selfrooms'].update({
                        str(chlen.id): str(a.id)})
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)
            except:
                if b.channel.id == SelfRoom:
                    chlen = await c.channel.guild.create_voice_channel(name=f'{a.name}', category=[i for i in a.guild.categories if i.id == int(dataServerID[str(c.channel.guild.id)]['selfRoom']["ctp"])][0])
                    await a.move_to(chlen)
                    dataServerID[str(a.guild.id)]['Selfrooms'].update({
                        str(chlen.id): str(a.id)})
                with open('users.json', 'w') as file:
                    json.dump(dataServerID, file, indent=4)

            if b.channel.name in [i.name for i in b.channel.guild.voice_channels if i.id in [int(k) for k in SelfRooms.keys()]]:
                if not (b.channel.members):
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
            ownRoom = int(
                dataServerID[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)])
            print(str(interaction.component.emoji))

        if str(interaction.component.emoji) == '👑':
            await interaction.send('укажите нового создателя этого канала @участник ')

            def check(msg: discord.Message):
                return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

            ms = await self.bot.wait_for(event='message', check=check)
            dataServerID[str(interaction.guild.id)]['Selfrooms'][str(interaction.author.voice.channel.id)] = [str(i.id) for i in ms.author.voice.channel.members if ms.content == i.mention][0]
            with open('users.json', 'w') as file:
                json.dump(dataServerID, file, indent=4)
            await ms.delete()

        elif str(interaction.component.emoji) == '🗒':
            await interaction.send('напишите @участник которому хотите ограничить право входить в комнату')

            def check(msg: discord.Message):
                return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

            ms = await self.bot.wait_for(event='message', check=check)
            pr = discord.PermissionOverwrite()
            if interaction.author.voice.channel.permissions_for(
                    [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).connect:
                pr.connect = False
            else:
                pr.connect = True
            await interaction.author.voice.channel.set_permissions(
                target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
            await ms.delete()


        elif str(interaction.component.emoji) == '👥':
            await interaction.send('напишите число участников')

            def check(msg: discord.Message):
                return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

            ms = await self.bot.wait_for(event='message', check=check)
            await ms.author.voice.channel.edit(user_limit=int(ms.content))
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

            def check(msg: discord.Message):
                return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

            ms = await self.bot.wait_for(event='message', check=check)
            await ms.author.voice.channel.edit(name=f'{ms.content}')
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

            def check(msg: discord.Message):
                return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

            ms = await self.bot.wait_for(event='message', check=check)
            [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
            await ms.delete()


        elif str(interaction.component.emoji) == '🎙':
            await interaction.send('напишите @участник которому хотите ограничить право говорить')

            def check(msg: discord.Message):
                return msg.author == interaction.author and msg.channel == interaction.channel and msg.author == interaction.guild.get_member(ownRoom)

            ms = await self.bot.wait_for(event='message', check=check)
            pr = discord.PermissionOverwrite()
            
            if interaction.author.voice.channel.permissions_for([i for i in ms.author.voice.channel.members if ms.content == i.mention][0]).speak:
                
                member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                if member.voice.mute == False:
                    pr.speak = False
                    await member.edit(mute = True)
                    await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                else:
                    await interaction.send(embpy(ctx=interaction, comp='e', des=f'Пользователь {member} уже был замучен на сервере!'))
            
                
            else:
                pr.speak = True
                member: discord.Member = [i for i in ms.author.voice.channel.members if ms.content == i.mention][0]
                await member.edit(mute = False)
                
                await ms.author.voice.channel.set_permissions(target=member, overwrite=pr)
                
            await interaction.author.voice.channel.set_permissions(
                target=[i for i in ms.author.voice.channel.members if ms.content == i.mention][0], overwrite=pr)
            await ms.delete()
            
    @commands.Cog.listener('on_voice_state_update')
    async def iiion_voice_state_update(self, member, before, after):
        Selfrooms = bdmpy(mr=member)['Selfrooms']
        try:
            if (not(after) and not(before.channel.permissions_for(member).speak) and str(before.channel.id) in [k for k in Selfrooms.keys()]) or (after.channel != before.channel and not(before.channel.permissions_for(member).speak) and str(before.channel.id) in [k for k in Selfrooms.keys()]):
                    await member.edit(mute = False)
        except:
            pass
def setup(bot):
    bot.add_cog(Roomedit(bot))