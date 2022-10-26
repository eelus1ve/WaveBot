from time import sleep
import discord
from discord.ext import commands
import json
from BTSET import embpy, bdmpy, bdpy, BD
import asyncio

class Stngspy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['settings'])
    @commands.has_permissions(administrator=True)
    async def set(self, ctx: commands.Context, arg=None, clArg=None, roleClass=None, emo=None):
        
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        roles = data[str(ctx.author.guild.id)]['JoinRoles']
        COLOR = data[str(ctx.author.guild.id)]['COLOR']
        ErCOLOR = data[str(ctx.author.guild.id)]['ErCOLOR']
        prefix = data[str(ctx.author.guild.id)]['PREFIX']
        description1 = 0
        description2 = 0
        title = 0

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
        elif arg == 'add_role':
            if clArg and roleClass:
                if roleClass in data[str(ctx.author.guild.id)]['ROLES']:
                    if len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26 and not(clArg in data[str(ctx.author.guild.id)]['ROLES'][roleClass]):
                        
                        data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].append(str(clArg))
                        if emo:
                            data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(str(emo))
                        else:
                            data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(' ')
                            description1=f"*В класс {roleClass} была добавленна роль {clArg}*"
                    elif not(len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26):
                            description2="Вы привысели число ролей в данном классе! (максимально число в классе 25)"
                    else:
                            description2=f"Роль {clArg} уже есть в этом классе!"
                else:
                        description2=f"*Класса {roleClass} не существует!*"
            else:   
                description2=f"*Использование:* {prefix}settings add_role (id роли) (название класса)"
        elif arg == 'add_class':
            if clArg:
                if not(clArg in data[str(ctx.author.guild.id)]['ROLES']):
                    data[str(ctx.author.guild.id)]['ROLES'].update({clArg: [[],[]]})
                    description1=f"*Класс {clArg} был успешно создан*"
                else:
                    description2=f"*Класс {clArg} уже существует*"
            else:
                description2=f"*Использование: {prefix}settings add_class (название класса)*",
        elif arg == 'remove_role':
            if clArg and roleClass:
                if roleClass in data[str(ctx.author.guild.id)]['ROLES']:
                    if clArg in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]:
                        data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(clArg)))
                        data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(clArg)))
                        description1=f"*Из класса {roleClass} была удалена роль {clArg}*"
                    else:
                        description2=f"*Роли с id {clArg} нету в классе {roleClass}!*"
                else:
                        description2=f"*Класса {roleClass} не существует!*"
            else:
                description2=f"*Использование: {prefix}settings remove_role (id роли) (название класса)*"

        elif arg == 'remove_class':
            if clArg:
                if clArg in data[str(ctx.author.guild.id)]['ROLES']:
                    data[str(ctx.author.guild.id)]['ROLES'].pop(clArg)
                    description1=f"*Класс {clArg} был успешно удалён*"
                else:
                    description2=f"*Класса {clArg} не существует*",
            else:
                description2=f"*Использование:* {prefix}settings remove_class (название класса)*"

        elif arg == 'color':       
            if not([i for i in [clArg[ii] for ii in range(len(clArg))] if not(i in ['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'])]):
                if [clArg[i] for i in range(len(clArg))][0] != '#':
                    if len(clArg) == 6:
                        data[str(ctx.author.guild.id)]['COLOR'] ='0x' + str(clArg)
                        description1=f"*Цвет сообщений бота изменен на {clArg}*"
                    else:
                        description2=f"*Использование:* {prefix}settings color (ваш цвет в hex)"
                elif [clArg[i] for i in range(len(clArg))][0] == '#':
                    if len(clArg) == 7:
                        data[str(ctx.author.guild.id)]['COLOR'] ='0x' + str(''.join([clArg[i] for i in range(len(clArg))][1:])) 
                        description1=f"*Цвет сообщений бота изменен на {clArg}*"
                    else:
                        description2=f"*Использование:* {prefix}settings color (ваш цвет в hex)"
            else:
                description2=f"*Цвета {clArg} не существует!*"
            

        elif arg == 'ercolor':
                if not([i for i in [clArg[ii] for ii in range(len(clArg))] if not(i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'])]):
                    if [clArg[i] for i in range(len(clArg))][0] != '#':
                        if len(clArg) == 6:
                            data[str(ctx.author.guild.id)]['ErCOLOR'] ='0x' + str(clArg) 
                            description1=f"*Цвет ошибок изменен на {clArg}*"
                        else:
                            description2=f"*Использование:* {prefix}settings color (ваш цвет в hex)"
                    elif [clArg[i] for i in range(len(clArg))][0] == '#':
                        if len(clArg) == 7:
                            data[str(ctx.author.guild.id)]['COLOR'] ='0x' + str(''.join([clArg[i] for i in range(len(clArg))][1:]))
                            description1=f"*Цвет ошибок изменен на {clArg}*"
                        else:
                            description2=f"*Использование:* {prefix}settings color (ваш цвет в hex)"
                else:
                    description2=f"*Цвета {clArg} не существует!*"
        
        elif arg == 'IDA':
            if clArg:
                data[str(ctx.author.guild.id)]['idAdminchennel'] = str(clArg)
                description1=f"*Канал администратора изменен на {clArg}*"
            else:
                description2=f"*Использование: {prefix}settings IDA (id канала для администраторов)*"
        
        elif arg == 'ncaps':
            if clArg:
                data[str(ctx.author.guild.id)]['nCaps'] = str(clArg) 
                description1=f"*Количество капса изменино на {clArg}*",
            else:
                description2=f"*Использование: {prefix}settings ncaps (количество капса до выдачи 1 предупреждения)*"

        elif arg == 'nwarns':
            if clArg:
                data[str(ctx.author.guild.id)]['nWarns'] = str(clArg) 
                description1=f"*Количество варнов изменино на {clArg}*"
            else:
                description2=f"*Использование: {prefix}settings nwarns (количество предупреждений до выдачи бана)*"
        elif arg == 'add_badword':
            if clArg:
                if not(clArg in data[str(ctx.author.guild.id)]['BADWORDS']):
                    data[str(ctx.author.guild.id)]['BADWORDS'].append(str(clArg))
                    description1=f"*В список badwords добавленно слово ||{clArg}||*"
                else:
                    description2=f"*Слово ||{clArg}|| уже добавлено в список плохих слов*"
            else:
                    description2=f"*Использование: {prefix}settings add_badword (слово за использование которого участнику сервера будет выданно предупреждение)*"
        elif arg == 'remove_badword':
            if clArg:
                if clArg in data[str(ctx.author.guild.id)]['BADWORDS']:
                    data[str(ctx.author.guild.id)]['BADWORDS'].pop(data[str(ctx.author.guild.id)]['BADWORDS'].index(str(clArg)))
                    description1=f"*Слово ||{clArg}|| в списке плохих слов*"
                else:
                    description2=f"*Слово ||{clArg}|| нету в списке плохих слов!*"
            else:
                description2=f'*Использование: {prefix}settings remove_badword (слово котороe нужно исключить из списка плохих слов)*'
        elif arg == 'prefix':
            if clArg:
                data[str(ctx.author.guild.id)]['PREFIX'] = str(clArg)
                description1=f"*Ваш префикс изменен на {clArg}*"
            else:
                description2=f"Для смены префикса напишите {prefix}settings prefix ваш_префикс"

        elif arg == 'selfroom':
            if clArg:
                data[str(ctx.author.guild.id)]['selfRoom'] = str(clArg)
                description1=f"*Канал для создания своей комнаты успешно назначен (Id назначеного канала {clArg})*"
            else:
                description2=f"*Использование:* {prefix}settings selfroom (id канала)"
        
        elif arg == 'selftitle':
            if clArg:
                data[str(ctx.author.guild.id)]['SelfTitle'] = str(clArg)
                description1=f"*Текст выбора ролей успешно изменён на {clArg}*",
            else:
                description2=f"*Использование:* {prefix}settings selftitle (Текст)",

        elif arg == 'join_message':
            if clArg:
                msg = await ctx.channel.fetch_message(clArg)
                data[str(ctx.author.guild.id)]['JNMSG'] = str(msg.content)
                description1=f"*Текст отправляемый пользователю при присоединении успешно изменён на:* \n\
                {msg.content}"
            else:
                description2=f"*Использование:* {prefix}settings join_message (Id сообщения с текстом)",
        elif arg == 'add_join_role':
            if clArg:
                if not(clArg in data[str(ctx.author.guild.id)]['JoinRoles']):
                    data[str(ctx.author.guild.id)]['JoinRoles'].append(str(clArg))
                    rl1 = ctx.guild.get_role(int(clArg))
                    description1=f"Роль {rl1} успешно добавлена!"
                else:
                    description2=f"Роль {rl1} уже была добавлена!"
            else:
                description2=f"Использование: {prefix}settings add_join_role (ID роли)"

        elif arg == 'remove_join_role':
            if clArg in data[str(ctx.author.guild.id)]['JoinRoles']:
                data[str(ctx.author.guild.id)]['JoinRoles'].pop(data[str(ctx.author.guild.id)]['JoinRoles'].index(str(clArg)))
                rl2 = ctx.guild.get_role(int(clArg))
                description1=f"Роль {rl2} успешно добавлена"
            else:
                description2=f"Такого ID не существует!"
        elif arg == 'join_roles':
            embb = discord.Embed(title = f'Успешно',
            description1=f'*Роли:*',
            color = COLOR)
            n = 0
            while len(roles) != n:
                embb.add_field(name = f'{ctx.guild.get_role(int(roles[n]))}', value =f'{roles[n]}', inline=True)
                n += 1
            await ctx.send(embed = embb)
        elif arg == 'class':
            if clArg in data[str(ctx.author.guild.id)]['ROLES']:
                SelRoles = data[str(ctx.author.guild.id)]['ROLES'][str(clArg)]
                embb = discord.Embed(title = f'Успешно',
                    description2=f'*Роли:*',
                    color = COLOR)
                n = 0
                while len(SelRoles) != n:
                    embb.add_field(name = f'{ctx.guild.get_role(int(SelRoles[n]))}', value =f'{SelRoles[n]}', inline=True)
                    n += 1
                await ctx.send(embed = embb)
            else:
                description2=f"Класса {clArg} не существует!"
        elif arg == 'classes':
            Classes = data[str(ctx.author.guild.id)]['ROLES']
            description1=f'*Роли:*'
            n = 0
            while len(Classes) != n:
                ClassesRoles = data[str(ctx.author.guild.id)]['ROLES'][str(Classes[n])][0]
                embb.add_field(name = f'{str(Classes[n])}', value =''.join(ClassesRoles), inline=True)
                n += 1
            await ctx.send(embed = embb)
        elif arg == 'add_IgnoreChannel':
            if clArg:
                if not(clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']):
                    data[str(ctx.author.guild.id)]['IgnoreChannels'].update(clArg)
                    description1=f"*Канал {clArg} был успешно добавлен в игнорируемые*"
                else:
                    description2=f"*Канал {clArg} уже добавлен*"
            else:
                description2=f"*Использование: {prefix}settings add_IgnoreChannel (название канала)*"
        elif arg == 'remove_IgnoreChannel':
            if clArg:
                if clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']:
                    data[str(ctx.author.guild.id)]['IgnoreChannels'].pop(clArg)
                    description1=f"*Канал {clArg} был успешно удалён*"
                else:
                    description2=f"*Канала {clArg} нет в игнорируемых*"
            else:
                description2=f"*Использование:* {prefix}settings remove_IgnoreChannel (название класса)*"
        elif arg == 'IgnoreChannels':
            IGCH =data[str(ctx.author.guild.id)]['IgnoreChannels']

            embb = discord.Embed(title="*Игнориеумые каналы:*",
                color=COLOR)
            n = 0
            while n != len(IGCH):
                embb.add_field(name=ctx.guild.get_channel(IGCH[n]), value=''.join(IGCH[n]), inline=True)
                n += 1
            await ctx.send(embed=embb)
        elif arg == 'add_IgnoreRole':
            if clArg:
                if not(clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']):
                    data[str(ctx.author.guild.id)]['IgnoreRoles'].update(clArg)
                    description1=f"*Роль {clArg} была успешно добавлена в игнорируемые*"
                else:
                    description2=f"*Роль {clArg} уже добавленf*",
            else:
                description2=f"*Использование: {prefix}settings add_IgnoreRole (id роли)*"
        elif arg == 'remove_IgnoreRole':
            if clArg:
                if clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']:
                    data[str(ctx.author.guild.id)]['IgnoreRoles'].pop(clArg)
                    description1=f"*Роль {clArg} была успешно удалёна из игнорируемых*"
                else:
                    description2=f"*Роли {clArg} нет в игнорируемых*",
            else:
                description2=f"*Использование:* {prefix}settings remove_IgnoreRole (id роли)*"

        elif arg == 'IgnoreRoles':
            IGRL =data[str(ctx.author.guild.id)]['IgnoreRoles']
            title="*Игнориеумые роли:*"
            n = 0
            while n != len(IGRL):
                embb.add_field(name=ctx.guild.get_channel(IGRL[n]), value=''.join(IGRL[n]), inline=True)
                n += 1
            await ctx.send(embed=embb)
        elif arg == 'Modrole':
            if str(clArg) in [str(i.id) for i in ctx.author.guild.roles]:
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
            else:
                description2=f'Роли с id {str(clArg)} не существует!'
        elif arg == 'set_mods':
            try:
                if clArg == 'Kick':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Kick'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Kick'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Ban':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['Ban'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['Ban'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Unban':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['UnBan'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['UnBan'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Tempban':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['TempBan'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Bans']['TempBan'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Warn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['Warn'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['Warn'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Unwarn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['UnWarn'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['UnWarn'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Tempwarn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['TempWarn'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['TempWarn'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clearwarn':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['ClearWarn'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Warns']['ClearWarn'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Settings':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Settings'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Settings'] = 'False' 
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clear':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Clear'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Clear'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Score':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['Score'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['Score'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clearscore':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearScore'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearScore'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Set_lvl':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['SetLvl'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['SetLvl'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Clear_rank':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearRank'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Rate']['ClearRank'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Temprole':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['TempRole'] = 'True' 
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['TempRole'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                elif clArg == 'Giverole':
                    if str(roleClass) == 'True':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['GiveRole'] = 'True'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    elif str(roleClass) == 'False':
                        if str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)]['Roles']['GiveRole'] = 'False'
                            await ctx.send(embed = embpy(ctx, comp='s', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                    else:
                        await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
            except:
                await ctx.send(embed = embpy(ctx, comp='e', des=f''))                                                       #НАПИСАТЬ ХОТЬ ЧТО ТО
                

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
            await ctx.send(embed=embpy(ctx, comp='s', des=description1))
        if description2:
            await ctx.send(embed=embpy(ctx, comp='e', des=description2))
        if title:
            await ctx.send(embed=embpy(ctx, comp='n', des=title))
        
def setup(bot):
    bot.add_cog(Stngspy(bot))