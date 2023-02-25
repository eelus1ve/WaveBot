from time import sleep
import discord
from discord.ext import commands
import json
from BTSET import Moderation, embpy, bdpy, BD, Lang
import asyncio
from discord_components import ComponentsBot

class Stngs(commands.Cog):
    def __init__(self, bot: ComponentsBot):
        self.bot = bot

    async def command_server_set(self, ctx: commands.Context):
        emb = discord.Embed(
            title='',
            description='',
            color=Moderation(ctx).color
        )

    async def command_set(self, ctx: commands.Context, arg: str=None, clArg: str=None, roleClass: str=None, emo=None):
        #сюда if
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        roles = data[str(ctx.author.guild.id)]['JoinRoles']
        COLOR = data[str(ctx.author.guild.id)]['COLOR']
        prefix = data[str(ctx.author.guild.id)]['PREFIX']
        description1 = 0
        description2 = 0
        title = 0
        command_name = 'setting'

        


        #print([SelectOption(label=i, value=i) for i in ctx.author.guild.roles])
        embb = discord.Embed(title=f'Настройка сервера ***{str(ctx.message.guild)}***',      #ПЕРЕДЕЛАТЬ
                            description="***Параметры:*** \n\
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
                                join_roles: Список всех ролей в автовыдаче",

                           )
        if arg==None:   
            await ctx.send(embed=embb)

            
        elif arg == 'add_role' or arg == 'remove_role':
            if not(clArg and roleClass):
                raise commands.MissingRequiredArgument("*{}* {}{} {} {}".format(Lang(ctx).language[f'settings_command_set_role_{arg}_error_1'], Moderation(ctx.author).prefix), command_name, arg, Lang(ctx).language[f'settings_command_set_role_{arg}_error_2'])
            if not(roleClass in data[str(ctx.author.guild.id)]['ROLES']):
                raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_role_{arg}_not_ex_1'], roleClass, Lang(ctx).language[f'settings_command_set_role_{arg}_not_ex_2']))
            description1 = "*{} {} {} {}*".format(Lang(ctx).language[f'settings_command_set_role_{arg}_1'], roleClass, Lang(ctx).language[f'settings_command_set_role_{arg}_2'], clArg)
            if arg == 'add_role':
                if len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26 and not(clArg in data[str(ctx.author.guild.id)]['ROLES'][roleClass]):
                    data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].append(str(clArg))
                    if emo:
                        data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(str(emo))
                    else:
                        data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(' ')
                    
                elif not(len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26):
                    raise commands.BadArgument(Lang(ctx).language[f'settings_command_set_role_{arg}_error_much'])
                else:
                    raise commands.BadArgument("{} {} {}".format(Lang(ctx).language[f'settings_command_set_role_{arg}_error_been_1'], clArg, Lang(ctx).language[f'settings_command_set_role_{arg}_error_been_2']))
            else:
                if not(clArg in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]):
                    raise commands.BadArgument("*{} {} {} {}!*".format(Lang(ctx).language[f'settings_command_set_role_{arg}_error_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_role_{arg}_error_not_ex_2'], roleClass))
                data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(clArg)))
                data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(clArg)))
            

        elif arg == 'add_class' or arg == 'remove_class':
            if not(clArg):
                raise commands.MissingRequiredArgument("*{} {}{} {} {}*".format(Lang(ctx).language[f'settings_command_set_class_{arg}_error_1'], Moderation(ctx.author).prefix, command_name, arg, Lang(ctx).language[f'settings_command_set_class_{arg}_error_2']))
            ermes = "*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_class_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_class_{arg}_not_ex_2'])
            if arg == 'add_class': 
                if clArg in data[str(ctx.author.guild.id)]['ROLES']:
                    raise commands.BadArgument(ermes)
                data[str(ctx.author.guild.id)]['ROLES'].update({clArg: [[],[]]})
            else:
                if not(clArg in data[str(ctx.author.guild.id)]['ROLES']):
                    raise commands.BadArgument(ermes)
                data[str(ctx.author.guild.id)]['ROLES'].pop(clArg)
            description1 = "*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_class_{arg}_1'], clArg, Lang(ctx).language[f'settings_command_set_class_{arg}_2'])


        elif arg == 'color' or arg == 'ercolor':       
            if [i for i in [clArg[ii] for ii in range(len(clArg))] if not(i in '#0123456789abcdef' or i in '#0123456789abcdef'.upper())]:
                raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_color_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_color_{arg}_not_ex_2']))

            if [clArg[i] for i in range(len(clArg))][0] == '#':
                if len(clArg) != 7:
                    raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_color_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_color_{arg}_not_ex_2']))
                
                data[str(ctx.author.guild.id)][arg.upper()] ='0x' + str(''.join([clArg[i] for i in range(len(clArg))][1:])) 
            else:
                if len(clArg) != 6:                    
                    raise commands.BadArgument("*{}* {}{} {} {}".format(Lang(ctx).language[f'settings_command_set_color_{arg}_error_1'], prefix, command_name, arg, Lang(ctx).language[f'settings_command_set_color_{arg}_error_2']))
                
                data[str(ctx.author.guild.id)][arg.upper()] ='0x' + str(clArg)
            description1="*{} {}*".format(Lang(ctx).language[f'settings_command_set_color_{arg}'], clArg)
        
        #тут надо будет подправить что бы в тексте не было название arg

        elif arg in ['adminchannel', 'ncaps', 'nwarns', 'prefix', 'selftitle', 'selfroom']:
            if not(clArg):
                raise commands.BadArgument("*{} {}{} {}*".format(Lang(ctx).language[f'settings_command_set_{arg}_error_1'], Moderation(ctx.author).prefix, command_name, Lang(ctx).language[f'settings_command_set_{arg}_error_2']))
            data[str(ctx.author.guild.id)][arg.upper()] = str(clArg)
            description1="*{} {}*".format(Lang(ctx).language[f'settings_command_set_{arg}'], clArg)

        elif arg == 'join_message':
            if not(clArg):
                raise commands.BadArgument(f"*Использование:* {prefix}settings join_message (Id сообщения с текстом)")
            msg: discord.Message = await ctx.channel.fetch_message(clArg)
            data[str(ctx.author.guild.id)]['JNMSG'] = str(msg.content)
            description1=f"*Текст отправляемый пользователю при присоединении успешно изменён на:* \n\
            {msg.content}"


        elif arg in ['add_badword', 'remove_badword']:
            if not(clArg):
                raise commands.BadArgument("*{} {}{} {}*".format(Lang(ctx).language[f'settings_command_set_badword_{arg}_error_1'], prefix, command_name, Lang(ctx).language[f'settings_command_set_badword_{arg}_error_2']))
            if arg == 'add_badword':
                if clArg in data[str(ctx.author.guild.id)]['BADWORDS']:
                    raise commands.BadArgument("*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_2']))
                data[str(ctx.author.guild.id)]['BADWORDS'].append(str(clArg))
            else:
                if not(clArg in data[str(ctx.author.guild.id)]['BADWORDS']):
                    raise commands.BadArgument("*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_2']))
                data[str(ctx.author.guild.id)]['BADWORDS'].pop(data[str(ctx.author.guild.id)]['BADWORDS'].index(str(clArg)))
            description1=="*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{arg}_1'], clArg, Lang(ctx).language[f'settings_command_set_badword_{arg}_2'])



        elif arg == 'add_join_role':
            if not(clArg):
                raise commands.BadArgument(f"Использование: {prefix}settings add_join_role (ID роли)")
            if clArg in data[str(ctx.author.guild.id)]['JoinRoles']:
                raise commands.BadArgument(f"Роль {rl1} уже была добавлена!")
            data[str(ctx.author.guild.id)]['JoinRoles'].append(str(clArg))
            rl1 = ctx.guild.get_role(int(clArg))
            description1=f"Роль {rl1} успешно добавлена!"


        elif arg == 'remove_join_role':
            if not(clArg in data[str(ctx.author.guild.id)]['JoinRoles']):
                raise commands.BadArgument(f"Такого ID не существует!")
            data[str(ctx.author.guild.id)]['JoinRoles'].pop(data[str(ctx.author.guild.id)]['JoinRoles'].index(str(clArg)))
            rl2 = ctx.guild.get_role(int(clArg))
            description1=f"Роль {rl2} успешно добавлена"

                
        elif arg == 'join_roles':
            embb = discord.Embed(title = f'Успешно',
            description1=f'*Роли:*',
            color = COLOR)
            for i in roles:
                embb.add_field(name = f'{ctx.guild.get_role(int(i))}', value =f'{i}', inline=True)
            await ctx.send(embed = embb)


        elif arg == 'class':
            if not(clArg in data[str(ctx.author.guild.id)]['ROLES']):
                raise commands.BadArgument(f"Класса {clArg} не существует!")
            SelRoles = data[str(ctx.author.guild.id)]['ROLES'][str(clArg)]
            embb = discord.Embed(title = f'Успешно',
                description2=f'*Роли:*',
                color = COLOR)
            
            for i in SelRoles:
                embb.add_field(name = f'{ctx.guild.get_role(int(i))}', value =f'{i}', inline=True)
            await ctx.send(embed = embb)


        elif arg == 'classes':
            Classes = data[str(ctx.author.guild.id)]['ROLES']
            description1=f'*Роли:*'
            for i in Classes:
                ClassesRoles = data[str(ctx.author.guild.id)]['ROLES'][str(i)][0]
                embb.add_field(name = f'{str(i)}', value =''.join(ClassesRoles), inline=True)
            await ctx.send(embed = embb)

        elif arg == 'IgnoreChannels':
            IGCH =data[str(ctx.author.guild.id)]['IgnoreChannels']
            embb = discord.Embed(title="*Игнориеумые каналы:*",
                color=COLOR)
            for i in IGCH:
                embb.add_field(name=ctx.guild.get_channel(i), value=''.join(i), inline=True)
            await ctx.send(embed=embb)


        elif arg in ['add_ignorechannel', 'remove_ignorechannel']:
            if not(clArg):
                raise commands.BadArgument(f"*Использование: {prefix}settings add_IgnoreChannel (название канала)*")
            
            if clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']:
                raise commands.BadArgument(f"*Канал {clArg} уже добавлен*")
            
            data[str(ctx.author.guild.id)]['IgnoreChannels'].update(clArg)
            description1=f"*Канал {clArg} был успешно добавлен в игнорируемые*"


        elif arg == 'remove_ignorechannel':
            if not(clArg):
                raise commands.BadArgument(f"*Использование:* {prefix}settings remove_IgnoreChannel (название класса)*")
            
            if not(clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']):
                raise commands.BadArgument(f"*Канала {clArg} нет в игнорируемых*")
            
            data[str(ctx.author.guild.id)]['IgnoreChannels'].pop(clArg)
            description1=f"*Канал {clArg} был успешно удалён*"


        elif arg == 'add_IgnoreRole':
            if not(clArg):
                raise commands.BadArgument(f"*Использование: {prefix}settings add_IgnoreRole (id роли)*")
            if clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']:
                raise commands.BadArgument(f"*Роль {clArg} уже добавленf*")
            data[str(ctx.author.guild.id)]['IgnoreRoles'].update(clArg)
            description1=f"*Роль {clArg} была успешно добавлена в игнорируемые*"


        elif arg == 'remove_IgnoreRole':
            if not(clArg):
                raise commands.BadArgument(f"*Использование:* {prefix}settings remove_IgnoreRole (id роли)*")
            if not(clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']):
                raise commands.BadArgument(f"*Роли {clArg} нет в игнорируемых*")
            data[str(ctx.author.guild.id)]['IgnoreRoles'].pop(clArg)
            description1=f"*Роль {clArg} была успешно удалёна из игнорируемых*"


        elif arg == 'IgnoreRoles':
            IGRL =data[str(ctx.author.guild.id)]['IgnoreRoles']
            title="*Игнориеумые роли:*"
            for i in IGRL:
                embb.add_field(name=ctx.guild.get_channel(i), value=''.join(i), inline=True)
            await ctx.send(embed=embb)


        elif arg == 'Modrole':
            if not(str(clArg) in [str(i.id) for i in ctx.author.guild.roles]):
                raise commands.BadArgument(f'Роли с id {str(clArg)} не существует!')
            data[str(ctx.author.guild.id)]['ModRoles'].update({
                str(clArg): {
                    'Kick': 'True', 
                    'Bans': {'Ban': 'True', 'UnBan': 'True', 'TempBan': 'True'},
                    'Warns': {
                        'Warn': 'True',
                        'TempWarn': 'True',
                        'UnWarn': 'True',
                        'ClearWarns': 'Ture'
                    },
                    'Settings': 'True',
                    'Clear': 'True',
                    'Rate': {
                        'Score': 'True',
                        'ClearScore': 'True',
                        'SetLvl': 'True',
                        'ClearRank': 'True',

                    },
                    'Roles': {'TempRole': 'True', 'GiveRole': 'True'}
                }
            })
                
            description1=f'Мод роль {[i for i in ctx.author.guild.roles if str(i.id) == str(clArg)]} добавлена!'


        elif arg == 'set_mods':
            try:
                if clArg == 'Kick':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Kick'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Kick'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Ban':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['Ban'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['Ban'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Unban':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['UnBan'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['UnBan'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Tempban':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['TempBan'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['TempBan'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Warn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['Warn'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['Warn'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Unwarn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['UnWarn'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['UnWarn'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Tempwarn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['TempWarn'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['TempWarn'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clearwarn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['ClearWarn'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['ClearWarn'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Settings':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Settings'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Settings'] = 'False' 
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clear':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Clear'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Clear'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Score':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['Score'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['Score'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clearscore':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearScore'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearScore'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Set_lvl':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['SetLvl'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['SetLvl'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clear_rank':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearRank'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearRank'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Temprole':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['TempRole'] = 'True' 
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['TempRole'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Giverole':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['GiveRole'] = 'True'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['GiveRole'] = 'False'
                            await embpy(ctx, comp='s', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
            except:
                await embpy(ctx, comp='e', des=f'')                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                

        else:
            embb = discord.Embed(title=f'Ошибка',
                            description="***Все доступные настройки:*** \n\
                                add_class (название класса): Добавить класс с ролей\n\
                                remove_class (название класса): Удалить класс с ролями\n\
                                add_role (id роли) (название класса): Добавить роль в класс\n\
                                remove_role (id роли) (название класса): Удалить роль из класса\n\
                                color: Цвет обычных сообщений бота \n\
                                ercolor: Цвет сообщений с ошибками бота \n\
                                IDА: ID Админ канала \n\
                                nCaps: Максимальное число капсов для предупреждения \n\
                                nWarns: Максимальное число варнов до бана \n\
                                add_badword (слово)\n\
                                remove_badword (слово котороe нужно исключить из списка плохих слов) \n\
                                selfroom (Id воис канала): Сделать комнату для создания личных каналов\n\
                                selftitle (Текст): Текст, который будет указан при выборе ролей \n\
                                join_message (Текмт): Изменить текст отправляемый учаснику при присоединении \n\
                                add_join_role (Id роли): Добавить роль в автовыдачу\n\
                                remove_join_role (id роли): Убрать роль из автовыдачи \n\
                                join_roles: Список всех ролей в автовыдаче",
                            )
            
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        if description1:
            await embpy(ctx, comp='s', des=description1)
        if description2:
            await embpy(ctx, comp='e', des=description2)
        if title:
            await embpy(ctx, comp='n', des=title)