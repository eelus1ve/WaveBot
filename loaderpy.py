import discord
import json
import os
from discord.ext import commands
from BTSET import ADMINS, IGNORE, bdpy
import interactions
dir_name1py = "module"
lstpy = []
class Loaderpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def load(self, ctx, arg = None):
        COLOR = bdpy(ctx)['COLOR']
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        prefix = bdpy(ctx)['PREFIX']
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1py)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1py}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py") and filename[:-3] == str(arg):
                                    if not(filename[:-3] in lstpy) and not(filename[:-3] in IGNORE):
                                        lstpy.append(f'{filename[:-3]}')           
                                        self.bot.load_extension(f'module.{dirs}.{filename[:-3]}')
                    if filename[:-3] in lstpy:
                        await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*модуль {arg} успешно загружен!*",
                            color=COLOR
                        ))
                    else:
                        await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description=f"*Модуля не существует*",
                            color=ErCOLOR
                        ))
                    #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1py)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1py}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if not(filename[:-3] in lstpy) and not(filename[:-3] in IGNORE):
                                        lstpy.append(f'{filename[:-3]}')
                                        self.bot.load_extension(f'module.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    if arg == 'all':
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

        except Exception as Exept:
            msg = await ctx.send(embed=discord.Embed(
                title=f"Ошибка-{Exept}",
                description="*Модуль:* " + arg + " *уже был загружен*)",
                color=ErCOLOR
            ))

    @commands.command()
    async def reload(self, ctx, arg = None):
        COLOR = bdpy(ctx)['COLOR']
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        prefix = bdpy(ctx)['PREFIX']
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1py)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1py}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{arg}' in lstpy:         
                                        self.bot.reload_extension(f'module.{dirs}.{filename[:-3]}')
                    if f'{arg}' in lstpy:
                        await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*модуль {arg} успешно перезагружен!*",
                            color=COLOR
                        ))
                    else:
                        msg = await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description=f"*Модуль {arg} не существует!*",
                            color=ErCOLOR
                        ))
                #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1py)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1py}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{filename[:-3]}' in lstpy:
                                        self.bot.reload_extension(f'module.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    if arg == 'all':
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
                            description=f"*Моудля {arg} не существует!*",
                            color=ErCOLOR
                            ))
            else:
                msg = await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*",
                        color=ErCOLOR
                        ))
        except Exception as Except:
            msg = await ctx.send(embed=discord.Embed(
                title=f"Ошибка-{Except}",
                description="",
                color=ErCOLOR
            ))

    @commands.command()
    async def unload(self, ctx, arg = None):
        COLOR = bdpy(ctx)['COLOR']
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        prefix = bdpy(ctx)['PREFIX']
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1py)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1py}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py") and filename[:-3] == str(arg):
                                    if f'{filename[:-3]}' in lstpy:
                                        lstpy.remove(f'{filename[:-3]}')            
                                        self.bot.unload_extension(f'module.{dirs}.{filename[:-3]}')
                    if not(f'{filename[:-3]}' in lstpy):
                        await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*модуль {arg} успешно отключен!*",
                            color=COLOR
                        ))
                #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1py)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"module\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{filename[:-3]}' in lstpy:
                                        lstpy.remove(f'{filename[:-3]}')
                                        self.bot.unload_extension(f'module.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    if arg == 'all':
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

        except Exception as Except:
            msg = await ctx.send(embed=discord.Embed(
                title=f"Ошибка-{Except}",
                description="*Модуль:* " + arg + " *уже был отключен*",
                color=ErCOLOR
            ))

    @commands.command()
    async def mods(self, ctx):
        COLOR = bdpy(ctx)['COLOR']
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        if str(ctx.author.id) in ADMINS:
            await ctx.send(embed=discord.Embed(
                title="Список загруженых модулей py",
                description=f"```{', '.join(lstpy)}```",
                color=COLOR
            ))
            # from loaderint import lstint
            # await ctx.send(embed=discord.Embed(
            #     title="Список загруженых модулей interactions",
            #     description=f"```{', '.join(lstint)}```",
            #     color=COLOR
            # ))
        else:
            msg = await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*У вас не достаточно прав!*" ,
                    color=ErCOLOR
                    ))
    @commands.command()
    async def ignore_mods(self, ctx):
        COLOR = bdpy(ctx)['COLOR']
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        from BTSET import IGNORE
        if str(ctx.author.id) in ADMINS:
            await ctx.send(embed=discord.Embed(
                title="Список игнорируемых модулей",
                description=f"```{', '.join(IGNORE)}```",
                color=COLOR
            ))
        else:
            msg = await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*У вас н~е достаточно прав!*" ,
                    color=ErCOLOR
                    ))
def setup(bot):
    bot.add_cog(Loaderpy(bot))