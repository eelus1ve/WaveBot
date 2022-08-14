def setup(bot):
    
    import discord
    from operator import index
    from discord.ext import commands
    from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
    from discord.utils import get
    from email.errors import InvalidMultipartContentTransferEncodingDefect
    import asyncio
    import json

    @bot.command()
    async def btst(ctx):
        with open('users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
        settings_names = ['add_role', 'add_class', 'remove_role', 'remove_class', 'color', 'ercolor',
                          'IDA', 'ncaps', 'nwarns', 'add_badword', 'remove_badword', 'prefix', 'selftitle',
                          'add_join_role', 'remove_join_role', 'join_roles', 'class', 'add_IgnoreChannel',
                          'remove_IgnoreChannel', 'IgnoreRoles', 'selfroom']

        await ctx.send(embed=discord.Embed(
                    title='Выберете настройки',
                    color=COLOR
                ),
                    components=[
                        Select(
                            placeholder='Выберете настройки',
                            max_values=1, #len(settings_names),
                            min_values=1,
                            options=[SelectOption(label=i, value=i) for i in settings_names]
                        )
                    ]
                )


    @bot.listen('on_select_option')
    async def sel_opt(interaction):
        try:
            settings_names = ['add_role', 'add_class', 'remove_role', 'remove_class', 'color', 'ercolor',
                            'IDA', 'ncaps', 'nwarns', 'add_badword', 'remove_badword', 'prefix', 'selftitle',
                            'add_join_role', 'remove_join_role', 'join_roles', 'class', 'add_IgnoreChannel',
                            'remove_IgnoreChannel', 'IgnoreRoles', 'selfroom']

            with open('users.json', 'r') as file:
                    data = json.load(file)
                    roles =  data[str(interaction.guild.id)]['JoinRoles']
                    COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
                    ErCOLOR = int(data[str(interaction.guild.id)]['ErCOLOR'], 16)
                    Classes = data[str(interaction.guild.id)]['ROLES']
                    IGCH = data[str(interaction.guild.id)]['IgnoreChannels']
                    IGRL = data[str(interaction.guild.id)]['IgnoreRoles']
                    SelfRoom = int(data[str(interaction.guild.id)]['selfRoom'])
                    serverRoles = []
                    for i in range(0, len(interaction.guild.roles), 24):# первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        serverRoles.append(interaction.guild.roles[i:i + 24])# второй важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


            if interaction.component.placeholder == 'Выберете настройки':
                for arg in interaction.values:
                    if arg == 'add_role':
                        await interaction.send(embed=discord.Embed(
                        title='Укажите классы в которые вы хотите добавить роли',
                        color=COLOR
                    ),
                        components=[
                            Select(
                                placeholder='Укажите классы в которые вы хотите добавить роли',
                                max_values=len(data[str(interaction.author.guild.id)]['ROLES']),
                                min_values=1,
                                options=[SelectOption(label=i, value=i) for i in [k for k in Classes.keys()]]
                            )
                        ]
                    )
                    elif arg == 'add_class':
                        pass
                    elif arg == 'color':
                        pass
                    elif arg == 'ercolor':
                        pass
                    elif arg == 'IDA':
                        await interaction.send(embed=discord.Embed(
                        title='Укажите админ канал',
                        color=COLOR
                    ),
                        components=[
                            Select(
                                placeholder='Укажите админ канал',
                                max_values=1,
                                min_values=1,
                                options=[SelectOption(label=i.name, value=i.id) for i in interaction.guild.text_channels]
                            )
                        ]
                    )
                    elif arg == 'ncaps':
                        pass
                    elif arg == 'nwarns':
                        pass
                    elif arg == 'add_badword':
                        pass
                    elif arg == 'remove_badword':
                        pass
                    elif arg == 'selfroom':
        
                        if data[str(interaction.guild.id)]['selfRoom'] != '0':
                            [[ii for ii in i.channels] for i in interaction.guild.categories if i.name == 'Дон Ягон']
                            [await i.delete() for i in interaction.guild.categories if i.name == 'Дон Ягон']
                            data[str(interaction.guild.id)]['selfRoom'] = '0'
                            await interaction.send(discord.Embed(title='***Успешно***',
                                description='Канал для создания комнат удалён',
                                color = COLOR))
                        else:
                            ct = await interaction.guild.create_category(name='Дон Ягон', position=1)
                            vcch = await interaction.guild.create_voice_channel(name=f'Дон Ягон', category=ct)
                            chn = await interaction.guild.create_text_channel(name=f'Дон Ягон', category=ct)
                            emb = discord.Embed(title='***⚙️ Управление приватными комнатами***',
                                description='👑 - назначить нового создателя комнаты \n\
                                🗒 - ограничить/выдать доступ к комнате \n\
                                👥 - задать новый лимит участников \n\
                                🔒 - закрыть/открыть комнату \n\
                                ✏️ - изменить название комнаты \n\
                                👁‍🗨 - скрыть/открыть комнату \n\
                                🚪 - выгнать участника из комнаты \n\
                                🎙 - ограничить/выдать право говорить',
                                color = COLOR)
                            await chn.send(embed=emb,
                            components = [
                                [
                                    Button(emoji = '👑', style=1),
                                    Button(emoji = '🗒', style=1),
                                    Button(emoji = '👥', style=1),
                                    Button(emoji = '🔒', style=1)
                                ],
                                [
                                    Button(emoji = '✏️', style=1),
                                    Button(emoji = '👁‍🗨', style=1),
                                    Button(emoji = '🚪', style=1),
                                    Button(emoji = '🎙', style=1)
                                ]
                            ]
                            )
                            data[str(interaction.guild.id)]['selfRoom'] = str(vcch.id)
                            await interaction.send(discord.Embed(title='***Успешно***',
                                description='Канал для создания комнат создан',
                                color = COLOR))
                    elif arg == 'prefix':
                        pass
                    elif arg == 'selftitle':
                        pass
                    elif arg == 'add_join_role':
                        pass
                    elif arg == 'remove_join_role':
                        pass
                    elif arg == 'join_roles':
                        pass
                    elif arg == 'class':
                        pass
                    elif arg == 'classes':
                        pass
                    elif arg == 'add_IgnoreChannel':
                        pass
                    elif arg == 'remove_IgnoreChannel':
                        pass
                    elif arg == 'add_IgnoreRole':
                        pass
                    elif arg == 'remove_IgnoreRole':
                        pass
                    elif arg == 'IgnoreRoles':
                        pass
            elif interaction.component.placeholder == 'Укажите классы в которые вы хотите добавить роли':
                for i in interaction.values:
                    for rls in serverRoles:
                        await interaction.send(embed=discord.Embed(
                            title=f'Укажите роли которые вы хотите добавить в класс {i}',
                            color=COLOR
                        ),
                            components=[
                                Select(
                                    placeholder=f'Укажите роли которые вы хотите добавить в класс *{i}',
                                    max_values=len(rls),
                                    min_values=0,
                                    options=[SelectOption(label=i.name, value=i.id) for i in rls]
                                )
                            ]
                        )

            

            elif interaction.component.placeholder.startswith('Укажите роли которые вы хотите добавить в класс'):
                data[str(interaction.author.guild.id)]['ROLES'][interaction.placeholder.split('*')[1][0]] = interaction.values
                data[str(interaction.author.guild.id)]['ROLES'][interaction.placeholder.split('*')[1][1]] = [0 for i in interaction.values]
                with open('users.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    


            elif interaction.component.placeholder.startswith('Укажите админ канал'):
                with open('users.json', 'w') as file:
                        data[str(interaction.guild.id)]['idAdminchennel'] = str(interaction.values[0])
                        json.dump(data, file, indent=4)
                await interaction.send(embed=discord.Embed(
                title="Успешно",
                description=f"*Канал администратора изменен*",
                color=COLOR
                ))


            elif interaction.component.placeholder.startswith('Укажите канал для создании комнат'):
                with open('users.json', 'w') as file:
                        data[str(interaction.guild.id)]['selfRoom'] = str(interaction.values[0])
                        json.dump(data, file, indent=4)
                        await interaction.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"*Канал для создания своей комнаты назначен*",
                        color=COLOR
                        ))
            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)
        except InvalidMultipartContentTransferEncodingDefect:
            pass