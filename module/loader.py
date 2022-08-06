import discord
import json
import os
import asyncio
from discord.ext import commands
from BTSET import TOKEN, ADMINS

dir_name1 = "D:\Windows\Рабочий стол\wave1\module"

list = []
class loader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def load(self, ctx, arg = None):
        with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
                prefix = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"D:\Windows\Рабочий стол\wave1\module\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py") and filename[:-3] == str(arg):
                                    if not(filename[:-3] in list):
                                        list.append(f'{filename[:-3]}')           
                                        self.bot.load_extension(f'module.{dirs}.{filename[:-3]}')
                                        await ctx.send(embed=discord.Embed(
                                            title="Успешно",
                                            description=f"*модуль {arg} успешно загружен!*",
                                            color=COLOR
                                        ))
                                    else:
                                        await ctx.send(embed=discord.Embed(
                                            title="Ошибка",
                                            description=f"*модуль {arg} уже был загружен!*",
                                            color=COLOR
                                        ))
                    #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"D:\Windows\Рабочий стол\wave1\module\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if not(filename[:-3] in list):
                                        list.append(f'{filename[:-3]}')
                                        self.bot.load_extension(f'module.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    msg = await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description="*Модули успешно загружены!*",
                        color=COLOR
                    ))
                elif arg == None:
                    msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Использование:* {prefix} *load (_имя модуля_)*",
                        color=ErCOLOR
                        ))
                else:
                    msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Моудля {arg} не существует!*" ,
                        color=ErCOLOR
                        ))
            else:
                msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*" ,
                        color=ErCOLOR
                        ))

        except:
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Модуль:* " + arg + " *уже был загружен*",
                color=ErCOLOR
            ))

    @commands.command()
    async def reload(self, ctx, arg = None):
        with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
                prefix = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"D:\Windows\Рабочий стол\wave1\module\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{arg}' in list:         
                                        self.bot.reload_extension(f'module.{dirs}.{filename[:-3]}')
                                        await ctx.send(embed=discord.Embed(
                                        title="Успешно",
                                        description=f"*модуль {arg} успешно перезагружен!*",
                                        color=COLOR
                                    ))
                                    else:
                                        msg = await ctx.send(embed=discord.Embed(
                                            title="Ошибка",
                                            description=f"*Модуль {arg} не существует!*",
                                            color=COLOR
                                        ))
                #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"D:\Windows\Рабочий стол\wave1\module\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{filename[:-3]}' in list:
                                        self.bot.reload_extension(f'module.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    msg = await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description="*Модули успешно перезагружены!*",
                        color=COLOR
                    ))
                elif arg == None:
                   msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Использование:* {prefix} *load (_имя модуля_)*",
                        color=ErCOLOR
                        ))

                else:
                    msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Моудля {arg} не существует!*" ,
                        color=ErCOLOR
                        ))
            else:
                msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*" ,
                        color=ErCOLOR
                        ))
        except:
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Модуль:* " + arg + " *уже был загружен*",
                color=ErCOLOR
            ))

    @commands.command()
    async def unload(self, ctx, arg = None):
        with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
                prefix = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"D:\Windows\Рабочий стол\wave1\module\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py") and filename[:-3] == str(arg):
                                    if f'{filename[:-3]}' in list:
                                        list.remove(f'{filename[:-3]}')            
                                        self.bot.unload_extension(f'module.{dirs}.{filename[:-3]}')
                                        await ctx.send(embed=discord.Embed(
                                            title="Успешно",
                                            description=f"*модуль {arg} успешно отключен!*",
                                            color=COLOR
                                        ))
                                    else:
                                        msg = await ctx.send(embed=discord.Embed(
                                        title="Ошибка",
                                        description=f"*Модуль {arg} не был загружен!*",
                                        color=COLOR
                                    ))
                #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"D:\Windows\Рабочий стол\wave1\module\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{filename[:-3]}' in list:
                                        list.remove(f'{filename[:-3]}')
                                        self.bot.unload_extension(f'module.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    msg = await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description="*Модули успешно отключены!*",
                        color=COLOR
                    ))
                elif arg == None:
                    msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Использование:* {prefix} *load (_имя модуля_)*",
                        color=ErCOLOR
                        ))

                else:
                    msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Моудля {arg} не существует!*" ,
                        color=ErCOLOR
                        ))
            else:
                msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*" ,
                        color=ErCOLOR
                        ))

        except:
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Модуль:* " + arg + " *уже был отключен*",
                color=ErCOLOR
            ))

    @commands.command()
    async def mods(self, ctx):
        with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if str(ctx.author.id) in ADMINS:
            await ctx.send(embed=discord.Embed(
                title="Список загруженых модулей",
                description=f"```{', '.join(list)}```",
                color=COLOR
            ))
        else:
            msg = await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*У вас не достаточно прав!*" ,
                    color=ErCOLOR
                    ))
def setup(bot):
    bot.add_cog(loader(bot))