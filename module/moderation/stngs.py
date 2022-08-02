import discord
from operator import index
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from discord.utils import get
import asyncio
import json
class stngs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def settings(self, ctx, arg=None, clArg=None, roleClass=None, emo=None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            roles =  dataServerID[str(ctx.author.guild.id)]['JoinRoles']
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            prefix = dataServerID[str(ctx.author.guild.id)]['PREFIX']
        #print([SelectOption(label=i, value=i) for i in ctx.author.guild.roles])
        emb = discord.Embed(title=f'Настройка сервера ***{str(ctx.message.guild)}***',      #ПЕРЕДЕЛАТЬ
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
                            color=COLOR
                            )
        if arg==None:   
            await ctx.send(embed=emb)
        elif arg == 'add_role':
            if clArg and roleClass:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if roleClass in data[str(ctx.author.guild.id)]['ROLES']:
                    if len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26 and not(clArg in data[str(ctx.author.guild.id)]['ROLES'][roleClass]):
                        with open('users.json', 'w') as file:
                            data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].append(str(clArg))
                            if emo:
                                data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(str(emo))
                            else:
                                data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(' ')
                            json.dump(data, file, indent=4)
                        await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*В класс {roleClass} была добавленна роль {clArg}*",
                            color=COLOR
                        ))
                    elif not(len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26):
                        await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description="Вы привысели число ролей в данном классе! (максимально число в классе 25)",
                            color=ErCOLOR
                        ))
                    else:
                        await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description=f"Роль {clArg} уже есть в этом классе!",
                            color=ErCOLOR
                        ))
                else:
                    await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Класса {roleClass} не существует!*",
                        color=ErCOLOR
                        ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* !settings add_role (id роли) (название класса)",
                color=ErCOLOR
                ))
        elif arg == 'add_class':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if not(clArg in data[str(ctx.author.guild.id)]['ROLES']):
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['ROLES'].update({clArg: [[],[]]})
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Класс {clArg} был успешно создан*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Класс {clArg} уже существует*",
                color=ErCOLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: !settings add_class (название класса)*",
                color=ErCOLOR
                ))
        elif arg == 'remove_role':
            if clArg and roleClass:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if roleClass in data[str(ctx.author.guild.id)]['ROLES']:
                    if clArg in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]:
                        with open('users.json', 'w') as file:
                            data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(clArg)))
                            data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(clArg)))
                            json.dump(data, file, indent=4)
                        await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*Из класса {roleClass} была удалена роль {clArg}*",
                            color=COLOR
                        ))
                    else:
                        await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Роли с id {clArg} нету в классе {roleClass}!*",
                        color=ErCOLOR
                        ))
                else:
                    await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Класса {roleClass} не существует!*",
                        color=ErCOLOR
                        ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: !settings remove_role (id роли) (название класса)*",
                color=ErCOLOR
                ))
        elif arg == 'remove_class':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if clArg in data[str(ctx.author.guild.id)]['ROLES']:
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['ROLES'].pop(clArg)
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Класс {clArg} был успешно удалён*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Класса {clArg} не существует*",
                    color=ErCOLOR
                    ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* !settings remove_class (название класса)*",
                color=ErCOLOR
                ))

        elif arg == 'color':          
                if not([i for i in [clArg[ii] for ii in range(len(clArg))] if not(i in ['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'])]):
                    if [clArg[i] for i in range(len(clArg))][0] != '#':
                        if len(clArg) == 6:
                            with open('users.json', 'r') as file:
                                    data = json.load(file)
                            with open('users.json', 'w') as file:
                                data[str(ctx.author.guild.id)]['COLOR'] ='0x' + str(clArg) 
                                json.dump(data, file, indent=4)
                            await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*Цвет сообщений бота изменен на {clArg}*",
                            color=COLOR
                            ))
                        else:
                            await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description="*Использование:* !settings color (ваш цвет в hex)",
                            color=ErCOLOR
                            ))
                    elif [clArg[i] for i in range(len(clArg))][0] == '#':
                        if len(clArg) == 7:
                            with open('users.json', 'r') as file:
                                    data = json.load(file)
                            with open('users.json', 'w') as file:
                                data[str(ctx.author.guild.id)]['COLOR'] ='0x' + str(''.join([clArg[i] for i in range(len(clArg))][1:])) 
                                json.dump(data, file, indent=4)
                            await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*Цвет сообщений бота изменен на {clArg}*",
                            color=COLOR
                            ))
                        else:
                            await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description="*Использование:* !settings color (ваш цвет в hex)",
                            color=ErCOLOR
                            ))
                else:
                    print(2)
                    await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Цвета {clArg} не существует!*",
                    color=ErCOLOR
                    )) 
            

        elif arg == 'ercolor':
                if not([i for i in [clArg[ii] for ii in range(len(clArg))] if not(i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'])]):
                    if [clArg[i] for i in range(len(clArg))][0] != '#':
                        if len(clArg) == 6:
                            with open('users.json', 'r') as file:
                                    data = json.load(file)
                            with open('users.json', 'w') as file:
                                data[str(ctx.author.guild.id)]['ErCOLOR'] ='0x' + str(clArg) 
                                json.dump(data, file, indent=4)
                            await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*Цвет ошибок изменен на {clArg}*",
                            color=COLOR
                            ))
                        else:
                            await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description="*Использование:* !settings color (ваш цвет в hex)",
                            color=ErCOLOR
                            ))
                    elif [clArg[i] for i in range(len(clArg))][0] == '#':
                        if len(clArg) == 7:
                            with open('users.json', 'r') as file:
                                    data = json.load(file)
                            with open('users.json', 'w') as file:
                                data[str(ctx.author.guild.id)]['COLOR'] ='0x' + str(''.join([clArg[i] for i in range(len(clArg))][1:]))
                                json.dump(data, file, indent=4)
                            await ctx.send(embed=discord.Embed(
                            title="Успешно",
                            description=f"*Цвет ошибок изменен на {clArg}*",
                            color=COLOR
                            ))
                        else:
                            await ctx.send(embed=discord.Embed(
                            title="Ошибка",
                            description="*Использование:* !settings color (ваш цвет в hex)",
                            color=ErCOLOR
                            ))
                else:
                    await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Цвета {clArg} не существует!*",
                    color=ErCOLOR
                    ))
        
        elif arg == 'IDA':
            if clArg:
                with open('users.json', 'r') as file:
                        data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(ctx.author.guild.id)]['idAdminchennel'] = str(clArg)
                    json.dump(data, file, indent=4)
                await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*Канал администратора изменен на {clArg}*",
                color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: !settings IDA (id канала для администраторов)*",
                color=ErCOLOR
                ))
        
        elif arg == 'ncaps':
            if clArg:
                with open('users.json', 'r') as file:
                        data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(ctx.author.guild.id)]['nCaps'] = str(clArg) 
                    json.dump(data, file, indent=4)
                await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*Количество капса изменино на {clArg}*",
                color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: !settings ncaps (количество капса до выдачи 1 предупреждения)*",
                color=ErCOLOR
                ))

        elif arg == 'nwarns':
            if clArg:
                with open('users.json', 'r') as file:
                        data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(ctx.author.guild.id)]['nWarns'] = str(clArg) 
                    json.dump(data, file, indent=4)
                await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*Количество варнов изменино на {clArg}*",
                color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: !settings nwarns (количество предупреждений до выдачи бана)*",
                color=ErCOLOR
                ))
        elif arg == 'add_badword':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if not(clArg in data[str(ctx.author.guild.id)]['BADWORDS']):
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['BADWORDS'].append(str(clArg))
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*В список badwords добавленно слово ||{clArg}||*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Слово ||{clArg}|| уже добавлено в список плохих слов*",
                    color=ErCOLOR
                    ))
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description="*Использование: !settings add_badword (слово за использование которого участнику сервера будет выданно предупреждение)*",
                    color=ErCOLOR
                ))

        elif arg == 'remove_badword':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if clArg in data[str(ctx.author.guild.id)]['BADWORDS']:
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['BADWORDS'].pop(data[str(ctx.author.guild.id)]['BADWORDS'].index(str(clArg)))
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Слово ||{clArg}|| в списке плохих слов*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"*Слово ||{clArg}|| нету в списке плохих слов!*",
                        color=COLOR
                    ))
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description='*Использование: !settings remove_badword (слово котороe нужно исключить из списка плохих слов)*',
                    color=ErCOLOR
                ))


        elif arg == 'prefix':
            if clArg:
                with open('users.json', 'r') as file:
                        data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(ctx.author.guild.id)]['PREFIX'] = str(clArg)
                    json.dump(data, file, indent=4)
                await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*Ваш префикс изменен на {clArg}*",
                color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title=f"Префикс установленный на сервере: ***{prefix}***",
                description=f"Для смены префикса напишите {prefix}settings prefix ваш_префикс",
                color=COLOR
                ))

        elif arg == 'selfroom':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(ctx.author.guild.id)]['selfRoom'] = str(clArg)
                    json.dump(data, file, indent=4)
                await ctx.send(embed=discord.Embed(
                    title="Успешно",
                    description=f"*Канал для создания своей комнаты успешно назначен (Id назначеного канала {clArg})*",
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* !settings selfroom (id канала)",
                color=ErCOLOR
                ))
        
        elif arg == 'selftitle':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(ctx.author.guild.id)]['SelfTitle'] = str(clArg)
                    json.dump(data, file, indent=4)
                await ctx.send(embed=discord.Embed(
                    title="Успешно",
                    description=f"*Текст выбора ролей успешно изменён на {clArg}*",
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* !settings selftitle (Текст)",
                color=ErCOLOR
                ))

        elif arg == 'join_message':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                msg = await ctx.channel.fetch_message(clArg)
                with open('users.json', 'w') as file:
                    data[str(ctx.author.guild.id)]['JNMSG'] = str(msg.content)
                    json.dump(data, file, indent=4)

                await ctx.send(embed=discord.Embed(
                    title="Успешно",
                    description=f"*Текст отправляемый пользователю при присоединении успешно изменён на:* \n\
                        {msg.content}",
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* !settings join_message (Id сообщения с текстом)",
                color=ErCOLOR
                ))
        elif arg == 'add_join_role':
            if clArg:
                if not(clArg in dataServerID[str(ctx.author.guild.id)]['JoinRoles']):
                    with open('users.json', 'w') as file:
                        dataServerID[str(ctx.author.guild.id)]['JoinRoles'].append(str(clArg))
                        json.dump(dataServerID, file, indent=4)

                    rl1 = ctx.guild.get_role(int(clArg))
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"Роль {rl1} успешно добавлена!",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                        title="Ошибка",
                        description=f"Роль {rl1} уже была добавлена!",
                        color=COLOR
                    ))
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"Использование: ~settings add_join_role (ID роли)",
                    color=COLOR
                ))

        elif arg == 'remove_join_role':
            if clArg in dataServerID[str(ctx.author.guild.id)]['JoinRoles']:
                with open('users.json', 'w') as file:
                    dataServerID[str(ctx.author.guild.id)]['JoinRoles'].pop(dataServerID[str(ctx.author.guild.id)]['JoinRoles'].index(str(clArg)))
                    json.dump(dataServerID, file, indent=4)
                rl2 = ctx.guild.get_role(int(clArg))
                await ctx.send(embed=discord.Embed(
                    title="Успешно",
                    description=f"Роль {rl2} успешно добавлена",
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"Такого ID не существует!",
                    color=COLOR
                ))
        elif arg == 'join_roles':
            emb = discord.Embed(title = f'Успешно',
            description=f'*Роли:*',
            color = COLOR)
            n = 0
            while len(roles) != n:
                emb.add_field(name = f'{ctx.guild.get_role(int(roles[n]))}', value =f'{roles[n]}', inline=True)
                n += 1
            await ctx.send(embed = emb)
        elif arg == 'class':
            if clArg in dataServerID[str(ctx.author.guild.id)]['ROLES']:
                with open('users.json', 'r') as file:
                    SelRoles = dataServerID[str(ctx.author.guild.id)]['ROLES'][str(clArg)]
                emb = discord.Embed(title = f'Успешно',
                    escription=f'*Роли:*',
                    color = COLOR)
                n = 0
                while len(SelRoles) != n:
                    emb.add_field(name = f'{ctx.guild.get_role(int(SelRoles[n]))}', value =f'{SelRoles[n]}', inline=True)
                    n += 1
                await ctx.send(embed = emb)
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"Класса {clArg} не существует!",
                    color=COLOR
                ))
        elif arg == 'classes':
            with open('users.json', 'r') as file:
                Classes = dataServerID[str(ctx.author.guild.id)]['ROLES']
            emb = discord.Embed(title = f'Успешно',
                    escription=f'*Роли:*',
                    color = COLOR)
            n = 0
            while len(Classes) != n:
                with open('users.json', 'r') as file:
                    ClassesRoles = dataServerID[str(ctx.author.guild.id)]['ROLES'][str(Classes[n])][0]
                emb.add_field(name = f'{str(Classes[n])}', value =''.join(ClassesRoles), inline=True)
                n += 1
            await ctx.send(embed = emb)
        elif arg == 'add_IgnoreChannel':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if not(clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']):
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['IgnoreChannels'].update(clArg)
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Канал {clArg} был успешно добавлен в игнорируемые*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Канал {clArg} уже добавлен*",
                color=ErCOLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: !settings add_IgnoreChannel (название канала)*",
                color=ErCOLOR
                ))
        elif arg == 'remove_IgnoreChannel':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']:
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['IgnoreChannels'].pop(clArg)
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Канал {clArg} был успешно удалён*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Канала {clArg} нет в игнорируемых*",
                    color=ErCOLOR
                    ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* !settings remove_IgnoreChannel (название класса)*",
                color=ErCOLOR
                ))
        elif arg == 'IgnoreChannels':
            with open('users.json', 'r') as file:
                    data = json.load(file)
                    IGCH = data[str(ctx.author.guild.id)]['IgnoreChannels']

            emb = discord.Embed(title="*Игнориеумые каналы:*",
                color=COLOR)
            n = 0
            while n != len(IGCH):
                emb.add_field(name=ctx.guild.get_channel(IGCH[n]), value=''.join(IGCH[n]), inline=True)
                n += 1
            await ctx.send(embed=emb)
        elif arg == 'add_IgnoreRole':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if not(clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']):
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['IgnoreRoles'].update(clArg)
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Роль {clArg} была успешно добавлена в игнорируемые*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Роль {clArg} уже добавленf*",
                color=ErCOLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: !settings add_IgnoreRole (id роли)*",
                color=ErCOLOR
                ))
        elif arg == 'remove_IgnoreRole':
            if clArg:
                with open('users.json', 'r') as file:
                    data = json.load(file)
                if clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']:
                    with open('users.json', 'w') as file:
                        data[str(ctx.author.guild.id)]['IgnoreRoles'].pop(clArg)
                        json.dump(data, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Роль {clArg} была успешно удалёна из игнорируемых*",
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Роли {clArg} нет в игнорируемых*",
                    color=ErCOLOR
                    ))
            else:
                await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* !settings remove_IgnoreRole (id роли)*",
                color=ErCOLOR
                ))
        elif arg == 'IgnoreRoles':
            with open('users.json', 'r') as file:
                    data = json.load(file)
                    IGRL = data[str(ctx.author.guild.id)]['IgnoreRoles']

            emb = discord.Embed(title="*Игнориеумые роли:*",
                color=COLOR)
            n = 0
            while n != len(IGRL):
                emb.add_field(name=ctx.guild.get_channel(IGRL[n]), value=''.join(IGRL[n]), inline=True)
                n += 1
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f'Ошибка',
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
                            color=COLOR
                            )
            await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(stngs(bot))