from time import sleep
import discord
from discord.ext import commands
import json
from BTSET import embpy, bdpy, BD, Lang, DEFGUILD, DEFMODROLE
import asyncio
from system.Bot import WaveBot
from module.moderation.commands.newstngs import NewStngs, NewStngsviewer
class Stngs(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_server_set(self, ctx: commands.Context):
        emb = discord.Embed(
            title='',
            description='',
            color=self.bot.db_get_modercolor(ctx)
        )

    async def command_set(self, ctx: commands.Context, arg: str=None, clArg: str=None, roleClass: str=None, emo=None):

        #сюда if
        arg = arg.lower()
        # roles = self.bot.db_get_joinroles(ctx)
        COLOR = self.bot.db_get_modercolor(ctx)
        description1 = 0
        description2 = 0
        title = 0

        some_des = "***Параметры:*** \n\
                                add_class (название класса): Добавить класс с ролей\n\
                                remove_class (название класса): Удалить класс с ролями\n\
                                add_role (id роли) (название класса): Добавить роль в класс\n\
                                remove_role (id роли) (название класса): Удалить роль из класса\n\
                                color (Ваш цвет в HEX): Цвет обычных сообщений бота \n\
                                ercolor (Ваш цвет в HEX): Цвет сообщений с ошибками бота \n\
                                IDА (ID Админ чата): Добавляет ID Админ чата \n\
                                nCaps: Максимальное число капсов для предупреждения \n\
                                nWarns: Максимальное число варнов до бана \n\
                                add_badword (слово)\n\
                                remove_badword (слово котороe нужно исключить из списка плохих слов) \n\
                                selfroom (Id воис канала): Сделать комнату для создания личных каналов\n\
                                selftitle (Текст): Текст, который будет указан при выборе ролей \n\
                                join_message (Текмт): Изменить текст отправляемый учаснику при присоединении \n\
                                add_join_role (Id роли): Добавить роль в автовыдачу\n\
                                remove_join_role (id роли): Убрать роль из автовыдачи \n\
                                join_roles: Список всех ролей в автовыдаче"


        #print([SelectOption(label=i, value=i) for i in ctx.author.guild.roles])
        
        if arg==None:
            await ctx.send(embb = discord.Embed(title=f'Настройка сервера ***{str(ctx.message.guild)}***',      #ПЕРЕДЕЛАТЬ
                description=some_des,
                color=COLOR))
            
        if arg == 'add_role' or arg == 'remove_role':
            description1 = NewStngs(self.bot).add_rem_role(ctx, arg, clArg, roleClass, emo)

        elif arg == 'add_class' or arg == 'remove_class':
            description1 = NewStngs(self.bot).add_rem_class(ctx, arg, clArg)

        elif arg in [i.lower() for i in DEFGUILD.keys() if "COLOR" in i]:
            description1 = NewStngs(self.bot).set_color(ctx, arg, clArg)

        elif arg in ['adminchannel', 'ncaps', 'nwarns', 'prefix', 'selftitle', 'selfroom']:
            description1 = NewStngs(self.bot).text_set(ctx, arg, clArg)

        elif arg in ['add_badword', 'remove_badword']:
            description1 = NewStngs(self.bot).add_rem_badword(ctx, arg, clArg)

        elif arg in ['add_join_role', 'remove_join_role']:
            description1 = NewStngs(self.bot).add_rem_join_role(ctx, arg, clArg)

        elif arg in ['add_ignorechannel', 'remove_ignorechannel']:
            description1 = NewStngs(self.bot).add_rem_ignorechannel(ctx, arg, clArg)

        elif arg in ['add_IgnoreRole', 'remove_IgnoreRole']:
            description1 = NewStngs(self.bot).add_rem_ignoreRole(ctx, arg, clArg)

        elif arg == 'modrole':
            description1 = NewStngs(self.bot).set_modrole(ctx, arg, clArg)

        elif arg == 'set_mods':
            description1 = NewStngs(self.bot).set_mods(ctx, arg, clArg, roleClass, emo)

        elif arg == 'join_message':
            description1 = NewStngs(self.bot).set_join_message(ctx, arg, clArg)

        if description1 == 0:
            if arg == 'join_roles':
                emb = NewStngsviewer(self.bot).view_join_roles(ctx)

            # #? что за class и classes
            elif arg == 'class':
                emb = NewStngsviewer(self.bot).view_class(ctx, arg, clArg)

            elif arg == 'IgnoreRoles':
                emb = NewStngsviewer(self.bot).view_ignoreroles(ctx, arg)
                
            # #? что за class и classes
            elif arg == 'classes':
                emb = NewStngsviewer(self.bot).view_classes(ctx, arg)

            elif arg == 'ignorechannels':
                emb = NewStngsviewer(self.bot).view_ignorechannels(ctx, arg)

        if description1==0 and emb == 0:
            embb = discord.Embed(title=f'Ошибка',
                            description=some_des,
                            )
        if description1:
            await ctx.send(embed=discord.Embed(title="Успешно", description=description1, color=COLOR))
        if description2:
            await embpy(ctx, comp='e', des=description2)
        if title:
            await embpy(ctx, comp='n', des=title)