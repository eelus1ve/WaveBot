#=============================================================================================импорты

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       --> token стёпы <---             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      #нахуя?       #нужно было!     #нахуя?    #чтобы токен поменять!
import asyncio
from BTSET import TOKEN, ADMINS, BOTVERSION
from discord.ext import commands
from msilib.schema import Component
import py_compile
import discord
import random
import json
import time
import os
import sys
import asyncio
from discord import Spotify
from discord.utils import get
from distutils.log import error
import re
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption

#=======================================================================================================================
intents=discord.Intents.all()
def get_prefix(bot, message):
    with open('users.json', 'r') as file:
        data = json.load(file)
    prefix = data[str(message.guild.id)]['PREFIX']
    return prefix
bot =ComponentsBot(command_prefix = get_prefix, intents=intents)
bot.remove_command('help')
#=======================================================================================================================
@bot.event
async def on_ready():
    bot.load_extension('module.loader')
    print(f'{bot.user.name} connected')
    
    if not os.path.exists('users.json'):
        with open('users.json', 'w') as file:
            file.write('{}')
    await bot.change_presence(activity=discord.Game('Portal 2'))
    while 1:
        dtaa = {}
        for guild in bot.guilds:
            with open('users.json', 'r') as file:
                data = json.load(file)
                if not(str(guild.id) in [k for k in data.keys()]):
                    data.update({
                        guild.id: {
                            'COLOR': '0x0000FF',
                            'ErCOLOR': '0x8B0000',
                            'JoinRoles': [],
                            'ROLES': {},
                            'actmoduls': '',
                            'nCaps': -1,
                            'nWarns': 10,
                            'idAdminchennel': '0',
                            'idMainch': '0',
                            'selfRoom': '0',
                            'BADWORDS': [],
                            'LINKS': [],
                            'PREFIX': '~',
                            'JNMSG': '',
                            'SelfTitle': '*Выберите ваши роли:* ',
                            'Selfrooms': {},
                            'Mafrooms': {},
                            'IgnoreChannels': [],
                            'IgnoreRoles': [],
                            'card': 'wave.png',
                            'text_color': '#d0ed2b',
                            'bar_color': '#ec5252',
                            'blend': 1,
                            'USERS': {},
                        }})

            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)
            for member in guild.members:
                with open('users.json', 'r') as file:
                    dat = json.load(file)
                if not(str(member.id) in [str(k) for k in dat[str(guild.id)]['USERS'].keys()]):
                    dat[str(guild.id)]['USERS'].update({
                        str(member.id): {
                            'WARNS': 0,
                            'CAPS': 0,
                            "SCR": 0,
                            'LvL': 1
                        }})
                with open('users.json', 'w') as file:
                    json.dump(dat, file, indent=4)
                    
        await asyncio.sleep(20)
        

@bot.command()
async def a(ctx):
    with open('users.json', 'r') as file:
        dataServerID = json.load(file)
        COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
    await ctx.send(embed=discord.Embed(
        title="Степ не волнуйся все плохо)",
        color=COLOR
        ))

@bot.event
async def on_command_error(ctx, error):
    with open('users.json', 'r') as file:
        dataServerID = json.load(file)
        ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
    if isinstance(error, commands.errors.CommandNotFound):
        found = re.findall(r'Command \s*"([^\"]*)"', str(error))
        await ctx.send(embed=discord.Embed(
            title="Ошибка",
            description=f"*Команды `{''.join(found)}` не существует*",
            color = ErCOLOR
        ))
#=======================================================================================================================
#           1)рейтинг (--)
#           3)присоединение и отключение учасника
#           4)доделать варны
#           5)отслеживание стримов
#           6)SQL           global
#           7)сайт          global
#           8)Переделать румы
#           9)Шахматы
#=======================================================================================================================

#=======================================================================================================================
bot.run(TOKEN)
#=======================================================================================================================