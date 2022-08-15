import os
from discord.ext import commands
from BTSET import ADMINS
import interactions
from BD import bdint, bdpy
from BTSET import IGNORE
from typing import Optional
dir_name1int = "D:\Windows\Рабочий стол\wave1\module int"
lstint = []
class Loaderint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="load",
        description="...",
    )
    async def load(self, ctx: interactions.context, arg = 'all'):
        print(arg)
        print(ctx)
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        prefix = bdint(ctx)['PREFIX']
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1int)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1int}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py") and filename[:-3] == str(arg):
                                    if not(filename[:-3] in lstint) and not(filename[:-3] in IGNORE):
                                        lstint.append(f'{filename[:-3]}')           
                                        self.client.load(f'module int.{dirs}.{filename[:-3]}')
                    if filename[:-3] in lstint:
                        await ctx.send(embeds=interactions.Embed(
                            title="Успешно",
                            description=f"*модуль {arg} успешно загружен!*",
                            color=COLOR
                        ))
                    else:
                        await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Модуля не существует*",
                            color=ErCOLOR
                        ))
                    #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1int)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1int}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if not(filename[:-3] in lstint) and not(filename[:-3] in IGNORE):
                                        lstint.append(f'{filename[:-3]}')
                                        self.client.load(f'module int.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    if arg == 'all':
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Успешно",
                            description="*Модули успешно загружены!*",
                            color=COLOR
                        ))
                    elif arg == None:
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Использование:* {prefix} *load (_имя модуля_)*",
                            color=ErCOLOR
                            ))
                    else:
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Моудля {arg} не существует!*" ,
                            color=ErCOLOR
                            ))
            else:
                msg = await ctx.send(embeds=interactions.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*" ,
                        color=ErCOLOR
                        ))

        except:
            msg = await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*Модуль:* " + arg + " *уже был загружен*",
                color=ErCOLOR
            ))

    @interactions.extension_command(
        name="reload",
        description="...",
    )
    async def reload(self, ctx: interactions.context, arg = None):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        prefix = bdint(ctx)['PREFIX']
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1int)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1int}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{arg}' in lstint:
                                        self.client.reload(f'module int.{dirs}.{filename[:-3]}')
                    if f'{arg}' in lstint:
                        await ctx.send(embeds=interactions.Embed(
                            title="Успешно",
                            description=f"*модуль {arg} успешно перезагружен!*",
                            color=COLOR
                        ))
                    else:
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Модуль {arg} не существует!*",
                            color=ErCOLOR
                        ))
                #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1int)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1int}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{filename[:-3]}' in lstint:
                                        self.client.reload(f'module py.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    if arg == 'all':
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Успешно",
                            description="*Модули успешно перезагружены!*",
                            color=COLOR
                        ))
                    elif arg == None:
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Использование:* {prefix} *load (_имя модуля_)*",
                            color=ErCOLOR
                            ))
                    else:
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Моудля {arg} не существует!*" ,
                            color=ErCOLOR
                            ))
            else:
                msg = await ctx.send(embeds=interactions.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*" ,
                        color=ErCOLOR
                        ))
        except:
            msg = await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="",
                color=ErCOLOR
            ))

    @interactions.extension_command(
        name="unload",
        description="...",
    )
    async def unload(self, ctx: interactions.context, arg = None):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        prefix = bdint(ctx)['PREFIX']
        try:
            # -----------------------------селект
            if str(ctx.author.id) in ADMINS:
                if arg != 'all':
                    modules = os.listdir(dir_name1int)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1int}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py") and filename[:-3] == str(arg):
                                    if f'{filename[:-3]}' in lstint:
                                        lstint.remove(f'{filename[:-3]}')            
                                        self.client.unload(f'module py.{dirs}.{filename[:-3]}')
                    if not(f'{filename[:-3]}' in lstint):
                        await ctx.send(embeds=interactions.Embed(
                            title="Успешно",
                            description=f"*модуль {arg} успешно отключен!*",
                            color=COLOR
                        ))
                #------------------------------------все модули
                elif arg == 'all':
                    modules = os.listdir(dir_name1int)
                    for dirs in modules:
                        if dirs.endswith("") and dirs != "__pycache__" and not(dirs.endswith(".py")):
                            dir_name2 = f"{dir_name1int}\{dirs}"
                            mods = os.listdir(dir_name2)
                            for filename in mods:
                                if filename.endswith(".py"):
                                    if f'{filename[:-3]}' in lstint:
                                        lstint.remove(f'{filename[:-3]}')
                                        self.client.unload(f'module py.{dirs}.{filename[:-3]}')
                                    else:
                                        pass
                    if arg == 'all':
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Успешно",
                            description="*Модули успешно отключены!*",
                            color=COLOR
                        ))
                    elif arg == None:
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Использование:* {prefix} *load (_имя модуля_)*",
                            color=ErCOLOR
                            ))

                    else:
                        msg = await ctx.send(embeds=interactions.Embed(
                            title="Ошибка",
                            description=f"*Моудля {arg} не существует!*" ,
                            color=ErCOLOR
                            ))
            else:
                msg = await ctx.send(embeds=interactions.Embed(
                        title="Ошибка",
                        description=f"*У вас не достаточно прав!*" ,
                        color=ErCOLOR
                        ))

        except:
            msg = await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*Модуль:* " + arg + " *уже был отключен*",
                color=ErCOLOR
            ))
def setup(client):
    Loaderint(client)
