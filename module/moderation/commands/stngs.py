from time import sleep
import discord
from discord.ext import commands
import json
from BTSET import embpy, bdpy, BD, Lang, DEFGUILD, DEFMODROLE
import asyncio
from system.Bot import WaveBot

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
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        # roles = self.bot.db_get_joinroles(ctx)
        COLOR = self.bot.db_get_modercolor(ctx)
        prefix = self.bot.db_get_prefix(ctx)
        description1 = 0
        description2 = 0
        title = 0
        command_name = 'setting'




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
        embb = discord.Embed(title=f'Настройка сервера ***{str(ctx.message.guild)}***',      #ПЕРЕДЕЛАТЬ
                description=some_des,
                color=COLOR)
        if arg==None:
            print(30)
            await ctx.send(embed=embb)


        elif arg == 'add_role' or arg == 'remove_role':
            if not(clArg and roleClass):
                raise commands.MissingRequiredArgument("*{}* {}{} {} {}".format(Lang(ctx).language[f'settings_command_set_role_{arg}_error_1'], self.bot.db_get_prefix(ctx)), command_name, arg, Lang(ctx).language[f'settings_command_set_role_{arg}_error_2'])
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
                raise commands.MissingRequiredArgument("*{} {}{} {} {}*".format(Lang(ctx).language[f'settings_command_set_class_{arg}_error_1'], self.bot.db_get_prefix(ctx), command_name, arg, Lang(ctx).language[f'settings_command_set_class_{arg}_error_2']))
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


        elif arg in [i.lower() for i in DEFGUILD.keys() if "COLOR" in i]:
            if not(clArg):
                raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_color_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_color_{arg}_not_ex_2']))
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
                raise commands.BadArgument("*{} {}{} {}*".format(Lang(ctx).language[f'settings_command_set_{arg}_error_1'], self.bot.db_get_prefix(ctx), command_name, Lang(ctx).language[f'settings_command_set_{arg}_error_2']))
            data[str(ctx.author.guild.id)][arg.upper()] = str(clArg)
            description1="*{} {}*".format(Lang(ctx).language[f'settings_command_set_{arg}'], clArg)

        elif arg == 'join_message':
            if not(clArg):
                raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_{arg}_error_1']} {prefix}{command_name} {arg} {Lang(ctx).language[f'settings_command_set_{arg}_error_2']}")
            msg: discord.Message = await ctx.channel.fetch_message(clArg)
            data[str(ctx.author.guild.id)]['JNMSG'] = str(msg.content)
            description1=f"{Lang(ctx).language[f'settings_command_set_{arg}']} \n\
            {msg.content}"


        elif arg in ['add_badword', 'remove_badword']:
            if not(clArg):
                raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_badword_{arg}_error_1']} {prefix}{command_name} {arg} {Lang(ctx).language[f'settings_command_set_badword_{arg}_error_2']}*")
            if arg == 'add_badword':
                if clArg in data[str(ctx.author.guild.id)]['BADWORDS']:
                    raise commands.BadArgument("*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_2']))
                data[str(ctx.author.guild.id)]['BADWORDS'].append(str(clArg))
            else:
                if not(clArg in data[str(ctx.author.guild.id)]['BADWORDS']):
                    raise commands.BadArgument("*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_badword_{arg}_not_ex_2']))
                data[str(ctx.author.guild.id)]['BADWORDS'].pop(data[str(ctx.author.guild.id)]['BADWORDS'].index(str(clArg)))
            description1=="*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{arg}_1'], clArg, Lang(ctx).language[f'settings_command_set_badword_{arg}_2'])

        elif arg in ['add_join_role', 'remove_join_role']:
            if not(clArg):
                raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_join_roles_{arg}_eroor_1']} {prefix}{command_name} {arg} {Lang(ctx).language[f'settings_command_set_join_roles_{arg}_eroor_2']}")
            if arg == 'add_join_role':
                if clArg in data[str(ctx.author.guild.id)]['JoinRoles']:
                    raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_join_roles_{arg}_ex_1']} {rl1} {Lang(ctx).language[f'settings_command_set_join_roles_{arg}_ex_2']}")
                data[str(ctx.author.guild.id)]['JoinRoles'].append(str(clArg))
                rl1 = ctx.guild.get_role(int(clArg))
            else:
                if not(clArg in data[str(ctx.author.guild.id)]['JoinRoles']):
                    raise commands.BadArgument(Lang(ctx).language[f'settings_command_set_join_roles_{arg}not_ex_1'])
                data[str(ctx.author.guild.id)]['JoinRoles'].pop(data[str(ctx.author.guild.id)]['JoinRoles'].index(str(clArg)))
                rl1 = ctx.guild.get_role(int(clArg))
            description1=f"{Lang(ctx).language[f'settings_command_set_join_roles_{arg}_1']} {rl1} {Lang(ctx).language[f'settings_command_set_join_roles_{arg}_2']}"

        # elif arg == 'join_roles':
        #     description1=f'*Роли:*',
        #     for i in roles:
        #         emb.add_field(name = f'{ctx.guild.get_role(int(i))}', value =f'{i}', inline=True)
        #     await ctx.send(embed=embb)

        # #? что за class и classes
        # elif arg == 'class':
        #     if not(clArg):
        #         raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_class_{arg}_error_1']} {prefix}{command_name} {arg} {Lang(ctx).language[f'settings_command_set_class_{arg}_error_2']}")
        #     if not(clArg in data[str(ctx.author.guild.id)]['ROLES']):
        #         raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_class_{arg}_not_ex_1']} {clArg} {Lang(ctx).language[f'settings_command_set_class_{arg}_not_ex_2']}")
        #     SelRoles = data[str(ctx.author.guild.id)]['ROLES'][str(clArg)]
        #     for i in SelRoles:
        #         emb.add_field(name = f'{ctx.guild.get_role(int(i))}', value =f'{i}', inline=True)
        #     await ctx.send(embed = embb)
        #     description1=Lang(ctx).language[f'settings_command_set_class_{arg}'],


        elif arg == 'IgnoreRoles':
            IGRL =data[str(ctx.author.guild.id)]['IgnoreRoles']
            description1=Lang(ctx).language[f'settings_command_set_ignoreRole_{arg}']
            for i in IGRL:
                embb.add_field(name=ctx.guild.get_channel(i), value=''.join(i), inline=True)
            await ctx.send(embed=embb)
            
        #? что за class и classes
        elif arg == 'classes':
            Classes = data[str(ctx.author.guild.id)]['ROLES']
            description1=Lang(ctx).language[f'settings_command_set_class_{arg}']
            for i in Classes:
                ClassesRoles = data[str(ctx.author.guild.id)]['ROLES'][str(i)][0]
                embb.add_field(name = f'{str(i)}', value =''.join(ClassesRoles), inline=True)
            await ctx.send(embed = embb)

        elif arg == 'ignorechannels':
            IGCH =data[str(ctx.author.guild.id)]['IgnoreChannels']
            description1=Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}']
            for i in IGCH:
                embb.add_field(name=ctx.guild.get_channel(i), value=''.join(i), inline=True)
            await ctx.send(embed=embb)


        elif arg in ['add_ignorechannel', 'remove_ignorechannel']:
            if not(clArg):
                raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_error_1']} {prefix}{command_name} {arg} {Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_error_2']}*")
            if arg == 'add_ignorechannel':
                if clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']:
                    raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_ex_1']} {clArg} {Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_ex_2']}*")
                data[str(ctx.author.guild.id)]['IgnoreChannels'].update(clArg)
            else:
                if not(clArg in data[str(ctx.author.guild.id)]['IgnoreChannels']):
                    raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_not_ex_1']} {clArg} {Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_not_ex_2']}*")
                data[str(ctx.author.guild.id)]['IgnoreChannels'].pop(clArg)
                
            description1=f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_1']} {clArg} {Lang(ctx).language[f'settings_command_set_ignorechannel_{arg}_2']}*"


        elif arg in ['add_IgnoreRole', 'remove_IgnoreRole']:
            if not(clArg):
                raise commands.BadArgument("*{} {}{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_1'], prefix, command_name, arg, Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_2']))
            if arg == 'add_IgnoreRole':
                if clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']:
                    raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_ex_2']) )
                data[str(ctx.author.guild.id)]['IgnoreRoles'].update(clArg)
            else:
                if not(clArg in data[str(ctx.author.guild.id)]['IgnoreRoles']):
                    raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_not_ex_1'], clArg, Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_not_ex_2']) )
                data[str(ctx.author.guild.id)]['IgnoreRoles'].pop(clArg)
            description1="*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_1'], clArg, Lang(ctx).language[f'settings_command_set_ignorerole_{arg}_2'])

        elif arg == 'modrole':
            if not(str(clArg) in [str(i.id) for i in ctx.author.guild.roles]):
                raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_modrole_{arg}_error_1']} {str(clArg)} {Lang(ctx).language[f'settings_command_set_modrole_{arg}_error_2']}")
            data[str(ctx.guild.id)]['ModRoles'].update({
                clArg: DEFMODROLE
            })

            description1=f"{Lang(ctx).language[f'settings_command_set_modrole_{arg}_1']} {[i for i in ctx.author.guild.roles if str(i.id) == str(clArg)]} {Lang(ctx).language[f'settings_command_set_modrole_{arg}_2']}"


        elif arg == 'set_mods':
            if not(clArg):
                raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_modrole_{arg}_error_1']} {clArg} {Lang(ctx).language[f'settings_command_set_modrole_{arg}_error_2']}")
            if not str(emo) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
                raise commands.BadArgument(Lang(ctx).language[f'settings_command_set_modrole_{arg}_not_ex_1'])
            data[str(ctx.author.guild.id)]['ModRoles'][str(emo)][clArg] = 'True' in roleClass
            description1 = Lang(ctx).language[f'settings_command_set_modrole_{arg}']

        else:
            embb = discord.Embed(title=f'Ошибка',
                            description=some_des,
                            )

        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        if description1:
            await ctx.send(embed=discord.Embed(title="Успешно", description=description1, color=COLOR))
        if description2:
            await embpy(ctx, comp='e', des=description2)
        if title:
            await embpy(ctx, comp='n', des=title)