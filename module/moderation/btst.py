import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from email.errors import InvalidMultipartContentTransferEncodingDefect
import json
import discord_components

def setup(bot: discord_components.ComponentsBot):

    settings_for_btst = {
        'модерация': {
            'настроить роли': 'выбрать роли которые может выдавать бот',
            'добавить класс ролей': 'добавить класс ролей',
            'настроить аудит': 'этой штуки нет',
            'канал администратора': 'канал администратора',
            'кол-во капсов для предупреждения': 'количество сообщений написанное пользователем капсом до получения им предупреждения',
            'кол-во варнов для бана': 'количество предупреждений которое может получить пользователь до бана',
            'добавить плохое слово': 'добавить слово за использование которого пользователь получит предупреждение',
            'префикс': 'выбрать префикс на который реагирует бот',
            'указать свой текст при выборе ролей': 'текст при выборе роли (у каждого класса разный)',
            'убрать плохое слово': 'убрать слово за использование которого пользователь получит предупреждение'
        },
        'настройка бота': {
            'настроить цвет': 'цвет сообщений бота',
            'настроить цвет ошибок': 'цвет сообщений бота при ошибке',
            'музыка': 'создать категорию с каналами для музаки',
            'создать "свои комнаты"': '-',
            'добавить канал с инфорацией': 'канал с информацией от WaveBot',
            'роли для новых участников': 'выбрать роли которые будут выдаваться людям при заходе на сервер',

        },
        'настройка рейтинга': {}
    }

    async def btst_set_def(interaction, f=0):
        with open('users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)

        emb = discord.Embed(
            title='―――――――――*Wave Settings*―――――――――――',
            description='\n',
            color=COLOR
        )
        emb.add_field(name='это настройки WaveBot',
                      value='Вы можете выбрать раздел или сразу открыть рекомендуемые настройки')
        if f:
            await interaction.send(embed=emb, components=[
            Select(placeholder='рекомендуем настроить', options=[SelectOption(label='f', value='qwertyu')]),
            [
                Button(label='модерация'),
                Button(label='настройка бота'),
                Button(label='настройка рейтинга')
            ],
            [
                Button(label='<---'),
                Button(label='OK'),
                Button(label='--->')
            ]
            ])
        else:
            await interaction.message.edit(embed=emb, components=[
                Select(placeholder='рекомендуем настроить', options=[SelectOption(label='f', value='qwertyu')]),
                [
                    Button(label='модерация'),
                    Button(label='настройка бота'),
                    Button(label='настройка рейтинга')
                ],
                [
                    Button(label='<---'),
                    Button(label='OK'),
                    Button(label='--->')
                ]
            ])

    @bot.command()
    async def btst(interaction):
        gld: discord.Guild = interaction.guild
        channels = gld.channels

        with open('users.json', 'r') as file:
            data = json.load(file)
            roles = data[str(interaction.guild.id)]['JoinRoles']
            COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
            Classes = data[str(interaction.guild.id)]['ROLES']

            serverRoles = []
            for i in range(0, len(gld.roles),
                           24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                serverRoles.append(gld.roles[
                                   i:i + 24])  # второй важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            chlens = []
            for i in range(0, len([chlen for chlen in channels if str(chlen.type) == 'ChannelType.GUILD_TEXT']),
                           24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                chlens.append([chlen for chlen in channels if str(chlen.type) == 'ChannelType.GUILD_TEXT'][
                              i:i + 24])  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        await btst_set_def(interaction, 1)

    @bot.listen('on_button_click')
    async def animation(interaction: discord_components.Interaction):
        gld: discord.Guild = interaction.guild
        channels = gld.channels

        with open('users.json', 'r') as file:
            data = json.load(file)
            roles = data[str(interaction.guild.id)]['JoinRoles']
            COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
            Classes = data[str(interaction.guild.id)]['ROLES']

            serverRoles = []
            for i in range(0, len(gld.roles),
                           24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                serverRoles.append(gld.roles[
                                   i:i + 24])  # второй важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            chlens = []
            for i in range(0, len([chlen for chlen in interaction.guild.text_channels]),
                           24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                chlens.append([chlen for chlen in interaction.guild.text_channels][
                              i:i + 24])  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        if interaction.component.label in ['модерация', 'настройка бота', 'настройка рейтинга', '--->', '<---']: await interaction.edit_origin()
        if interaction.component.label in ['модерация', 'настройка бота', 'настройка рейтинга']:

            keys = []
            items = []

            for key in settings_for_btst[f'{interaction.component.label}']:
                keys.append(key)
                items.append(settings_for_btst[f'{interaction.component.label}'][key])

            emb = discord.Embed(
                title=interaction.message.embeds[0].title,
                description=f'**{interaction.component.label}**',
                color=COLOR
            )
            emb.add_field(name=f'{keys[0]}', value=f'{items[0]}')
            emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
            await interaction.message.edit(embed=emb, components=[
                Select(placeholder='рекомендуем настроить', options=[SelectOption(label='f', value='qwertyu')]),
                [
                    Button(label='модерация'),
                    Button(label='настройка бота'),
                    Button(label='настройка рейтинга')
                ],
                [
                    Button(label='<---'),
                    Button(label='OK'),
                    Button(label='--->')
                ]
            ])

        if interaction.component.label == '--->':
            old_emb: discord.Embed = interaction.message.embeds[0].description.replace('*', '')

            keys = list(settings_for_btst[old_emb].keys())
            itm = settings_for_btst[old_emb][keys[0]]
            del settings_for_btst[old_emb][keys[0]]
            settings_for_btst[old_emb].update({keys[0]: itm})

            keys = []
            items = []
            for key in settings_for_btst[f'{old_emb}']:
                keys.append(key)
                items.append(settings_for_btst[f'{old_emb}'][key])
            emb = discord.Embed(
                title=interaction.message.embeds[0].title,
                description=f'**{old_emb}**',
                color=COLOR
            )
            emb.add_field(name=f'{keys[0]}', value=f'{items[0]}')
            emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
            await interaction.message.edit(embed=emb)

        if interaction.component.label == '<---':
            old_emb: discord.Embed = interaction.message.embeds[0].description.replace('*', '')

            e = 0
            while len(settings_for_btst[old_emb]) - 1 != e:
                keys = list(settings_for_btst[old_emb].keys())
                itm = settings_for_btst[old_emb][keys[0]]
                del settings_for_btst[old_emb][keys[0]]
                settings_for_btst[old_emb].update({keys[0]: itm})
                e += 1

            keys = []
            items = []
            for key in settings_for_btst[f'{old_emb}']:
                keys.append(key)
                items.append(settings_for_btst[f'{old_emb}'][key])
            emb = discord.Embed(
                title=interaction.message.embeds[0].title,
                description=f'**{old_emb}**',
                color=COLOR
            )
            emb.add_field(name=f'{keys[0]}', value=f'{items[0]}')
            emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
            await interaction.message.edit(embed=emb)

        if interaction.component.label == 'OK':  #                                                                                               Вынести в отдельный класс
            old_emb = interaction.message.embeds[0]
            arg = old_emb.fields[0].name

            def check(mes: discord.Message):
                return interaction.author == mes.author and interaction.channel == mes.channel

            if arg == 'музыка':
                if [i for i in interaction.guild.categories if i.name == 'music']:
                    for category in interaction.guild.categories:
                        [await chnl.delete() for chnl in category.channels if category.name == 'music']
                    [await i.delete() for i in interaction.guild.categories if i.name == 'music']
                else:

                    with open('music.json', 'r') as file:
                        data_mus: dict = json.load(file)
                    if not (str(interaction.guild.id) in [i for i in data_mus.keys()]):
                        data_mus.update(
                            {
                                interaction.guild.id: {
                                    'songs': [],
                                    'pl_id': None,
                                    'chl_id': None
                                }
                            }
                        )

                    with open('music.json', 'w') as file:
                        json.dump(data_mus, file, indent=4)

                    ctg = await interaction.guild.create_category(name='music')
                    txt_cnlen = await ctg.create_text_channel(name='великий дон ягон')
                    vc_clen = await ctg.create_voice_channel(name='music')
                    embd = discord.Embed(
                        title='***                               wave player***',
                        description=f'=================================',
                        colour=0x00FFFF
                    )
                    embd.add_field(name='сейчас играет:', value='ничего')

                    comp = [
                        [
                            Button(emoji='◀', style=2),
                            Button(emoji='⏯', style=2),
                            Button(emoji='▶', style=2),
                            Button(emoji='🔀', style=2)
                        ],
                        [
                            Button(emoji='➕', style=2),
                            Button(emoji='🔊', style=2),
                            Button(emoji='🔈', style=2),
                            Button(emoji='🔇', style=2)
                        ]
                    ]

                    msc_player = await txt_cnlen.send(embed=embd, components=comp)

                    await vc_clen.connect()
                    await btst_set_def(interaction)

                    with open('music.json', 'r') as file:
                        data_mus = json.load(file)
                        data_mus[str(interaction.guild.id)]['pl_id'] = msc_player.id
                        data_mus[str(interaction.guild.id)]['chl_id'] = txt_cnlen.id
                    with open('music.json', 'w') as file:
                        json.dump(data_mus, file, indent=4)

            if arg == 'настроить роли':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='Укажите классы в которые вы хотите добавить роли', value='страница 1 из 1')
                await interaction.message.edit(embed=emb,
                   components=[
                       Select(
                           placeholder='Укажите классы в которые вы хотите добавить роли',
                           max_values=len(data[str(interaction.guild.id)]['ROLES']),
                           min_values=1,
                           options=[SelectOption(label=str(i), value=str(i)) for i in
                                    [k for k in Classes.keys()]]
                       ),
                       [
                           Button(label='модерация'),
                           Button(label='настройка бота'),
                           Button(label='настройка рейтинга')
                       ],
                       [
                           Button(label='<---'),
                           Button(label='OK'),
                           Button(label='--->')
                       ]
                   ])

                await interaction.edit_origin()

            if arg == 'добавить класс ролей':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с названием класса', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)


                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                if not (ms.content in data[str(interaction.guild.id)]['ROLES']):
                    with open('users.json', 'w') as file:
                        data[str(interaction.guild.id)]['ROLES'].update({ms.content: [[], []]})
                        json.dump(data, file, indent=4)

                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'настроить цвет':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)
                await interaction.edit_origin()

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['COLOR'] = '0x' + ms.content
                    json.dump(data, file, indent=4)
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'настроить цвет ошибок':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)
                await interaction.edit_origin()

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['ErCOLOR'] = '0x' + ms.content
                    json.dump(data, file, indent=4)
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'канал администратора':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=old_emb.description,
                    color=old_emb.color
                )
                emb.add_field(name='выберете канал который хотите сделать каналом администратора',
                              value=f'страница 1 из {len(chlens)}')

                await interaction.message.edit(embed=emb, components=[
                    Select(
                        placeholder='выберете канал который хотите сделать каналом администратора',
                        options=[SelectOption(label=i.name, value=str(i.id)) for i in chlens[0]]
                    ),
                    [
                        Button(label='модерация'),
                        Button(label='настройка бота'),
                        Button(label='настройка рейтинга')
                    ],
                    [
                        Button(label='<---'),
                        Button(label='OK'),
                        Button(label='--->')
                    ]
                ])
                await interaction.edit_origin()

            elif arg == 'ncaps':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['nCaps'] = ms.content
                    json.dump(data, file, indent=4)
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'nwarns':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с nwarns', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['nWarns'] = ms.content
                    json.dump(data, file, indent=4)
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'добавить плохое слово':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['BADWORDS'].append(ms.content)
                    json.dump(data, file, indent=4)
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'убрать плохое слово':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                if ms.channel in data[str(interaction.guild.id)]['BADWORDS']:
                    with open('users.json', 'w') as file:
                        data[str(interaction.guild.id)]['BADWORDS'].pop(
                            data[str(interaction.guild.id)]['BADWORDS'].index(ms.content))
                        json.dump(data, file, indent=4)
                else:
                    await interaction.send('слова нет')
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'создать "свои комнаты"':
                chlen_krokodila = interaction.channel

                if data[str(interaction.guild.id)]['selfRoom'] != '0':
                    for category in interaction.guild.categories:
                        [await chnl.delete() for chnl in category.channels if
                         str(category.id) == data[str(interaction.guild.id)]['selfRoom']["ct"]]
                    [await i.delete() for i in interaction.guild.categories if
                     str(i.id) == data[str(interaction.guild.id)]['selfRoom']["ct"] or str(i.id) == data[str(interaction.guild.id)]['selfRoom']["ctp"]]
                    data[str(interaction.guild.id)]['selfRoom'] = '0'
                    await chlen_krokodila.send(embed=discord.Embed(title='***Успешно***',
                                                                   description='Канал для создания комнат удалён',
                                                                   color=COLOR))
                    await btst_set_def(interaction)
                else:
                    ct = await interaction.guild.create_category(name='ССК', position=1)
                    vcch = await interaction.guild.create_voice_channel(name=f'Создать комнату', category=ct)
                    chn = await interaction.guild.create_text_channel(name=f'Настройка комнаты', category=ct)
                    ctp = await interaction.guild.create_category(name='Свои румы', position=2)
                    emb = discord.Embed(title='***⚙️ Управление приватными комнатами***',
                                        description=f'<:corona1:1020971032309403758> - назначить нового создателя комнаты \n\
                            <:notebook1:1020971040416993280> - ограничить/выдать доступ к комнате \n\
                            <:meet1:1020971037741043713> - задать новый лимит участников \n\
                            <:locker1:1020971036252053524> - закрыть/открыть комнату \n\
                            <:pencil1:1020971043856330782> - изменить название комнаты \n\
                            <:eye1:1020971035014746162> - скрыть/открыть комнату \n\
                            <:door1:1020971033756450866> - выгнать участника из комнаты \n\
                            <:microphone1:1020971039141920819> - ограничить/выдать право говорить',
                                        color=COLOR)
                    stb_gld: discord.Guild = bot.get_guild(id=981511419042361344)
                    await chn.send(embed=emb,
                                   components=[
                                       [
                                           Button(emoji=await stb_gld.fetch_emoji(1020971032309403758)),
                                           Button(emoji=await stb_gld.fetch_emoji(1020971040416993280)),
                                           Button(emoji=await stb_gld.fetch_emoji(1020971037741043713)),
                                           Button(emoji=await stb_gld.fetch_emoji(1020971036252053524))
                                       ],
                                       [
                                           Button(emoji=await stb_gld.fetch_emoji(1020971043856330782)),
                                           Button(emoji=await stb_gld.fetch_emoji(1020971035014746162)),
                                           Button(emoji=await stb_gld.fetch_emoji(1020971033756450866)),
                                           Button(emoji=await stb_gld.fetch_emoji(1020971039141920819))
                                       ]
                                   ]
                                   )
                    data[str(interaction.guild.id)]['selfRoom'] = {"ct": str(ct.id), "ctp": str(ctp.id),
                                                                   "vc": str(vcch.id),
                                                                   "tc": str(chn.id)}
                    ow2 = discord.PermissionOverwrite()
                    ow2.send_messages = False
                    await chn.set_permissions(target=interaction.guild.roles[0], overwrite=ow2) 
                    await chlen_krokodila.send(embed=discord.Embed(title='***Успешно***',
                                                                   description='Канал для создания комнат создан',
                                                                   color=COLOR))
                    with open('users.json', 'w') as file:
                        json.dump(data, file, indent=4)

                    await btst_set_def(interaction)

            elif arg == 'префикс':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['PREFIX'] = ms.content
                    json.dump(data, file, indent=4)
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'Указать свой текст при выборе ролей':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=arg,
                    color=COLOR
                )
                emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
                await interaction.message.edit(embed=emb)

                ms: discord.Message = await bot.wait_for('message', check=check)

                with open('users.json', 'r') as file:
                    data = json.load(file)
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['SelfTitle'] = ms.content
                    json.dump(data, file, indent=4)
                await ms.delete()
                await btst_set_def(interaction)

            elif arg == 'настроить роли при входе на сервер':
                emb = discord.Embed(
                    title=old_emb.title,
                    description=old_emb.description,
                    color=old_emb.color
                )
                emb.add_field(name=f'Укажите роли которые будут выдоваться участникам при входе на сервер',
                              value=f'страница 1 из {len(serverRoles)}')

                await interaction.message.edit(components=[
                    Select(
                        placeholder=f'Укажите роли которые будут выдоваться участникам при входе на сервер',
                        max_values=len(serverRoles[0]),
                        min_values=0,
                        options=[SelectOption(label=i.name, value=str(i.id)) for i in serverRoles[0]]
                    ),
                    [
                        Button(label='модерация'),
                        Button(label='настройка бота'),
                        Button(label='настройка рейтинга')
                    ],
                    [
                        Button(label='<---'),
                        Button(label='OK'),
                        Button(label='--->')
                    ]
                ])
            elif arg == 'список join ролей':
                pass

            elif arg == 'classes':
                pass
                '''with open('users.json', 'r') as file:
                    data = json.load(file)
                    Classes = data[str(interaction.guild.id)]['ROLES']
                emb = discord.Embed(title=f'Успешно',
                    escription=f'*Роли:*',
                    color=COLOR)
                n = 0
                while len(Classes) != n:
                    with open('users.json', 'r') as file:
                        ClassesRoles = data[str(interaction.guild.id)]['ROLES'][str(Classes[n])][0]
                    emb.add_field(name=f'{str(Classes[n])}', value=''.join(ClassesRoles), inline=True)
                    n += 1
                await [i for i in bot.get_all_channels() if i.id == interaction.channel_id][0].send(embed=emb)'''
            elif arg == 'add_IgnoreChannel':
                pass
            elif arg == 'add_IgnoreRole':
                pass
            elif arg == 'IgnoreRoles':
                pass
            elif arg == 'добавить канал с инфорацией':  # переимовать

                with open('glb_vote.json', 'r') as file:
                    vt_data = json.load(file)

                if not (str(interaction.guild.id) in [k for k in vt_data.keys()]):

                    ct = await interaction.guild.create_category(name='ссссссс', position=1)
                    chn = await interaction.guild.create_text_channel(name=f'Голосование от wave', category=ct)
                    chn1 = await interaction.guild.create_text_channel(name=f'Информация от wave', category=ct)

                    vt_data.update({
                        interaction.guild.id: {
                            'vote_id': chn.id,
                            'info_id': chn1.id
                        }
                    })
                else:
                    await interaction.guild.get_channel(vt_data[str(interaction.guild.id)]['vote_id']).category.delete()
                    await interaction.guild.get_channel(vt_data[str(interaction.guild.id)]['vote_id']).delete()
                    await interaction.guild.get_channel(vt_data[str(interaction.guild.id)]['info_id']).delete()
                    del vt_data[str(interaction.guild.id)]

                with open('glb_vote.json', 'w') as file:
                    json.dump(vt_data, file, indent=4)

            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)

            await btst_set_def(interaction)

    @bot.event
    async def on_select_option(interaction: discord_components.Interaction):
        try:
            old_emb = interaction.message.embeds[0]
            with open('users.json', 'r') as file:
                data = json.load(file)
                COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)

            serverRoles: list = []
            for i in range(0, len(interaction.guild.roles),
                           24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                serverRoles.append(interaction.guild.roles[
                                   i:i + 24])  # второй важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        except:
            pass

        if interaction.component.placeholder == 'Укажите классы в которые вы хотите добавить роли':
            emb = discord.Embed(
                title=old_emb.title,
                description=old_emb.description,
                color=old_emb.color
            )
            emb.add_field(name=f'Укажите роли которые вы хотите добавить в класс {interaction.values[0]}',
                          value=f'страница 1 из {len(interaction.values)}')
            await interaction.message.edit(embed=emb,
               components=[
                   Select(
                       placeholder=f'Укажите роли которые вы хотите добавить в класс *{interaction.values[0]}',
                       max_values=len(serverRoles[0]),
                       min_values=0,
                       options=[SelectOption(label=i.name, value=i.id) for i in
                                serverRoles[0]]
                   ),
                   [
                       Button(label='модерация'),
                       Button(label='настройка бота'),
                       Button(label='настройка рейтинга')
                   ],
                   [
                       Button(label='<---'),
                       Button(label='OK'),
                       Button(label='--->')
                   ]
               ])

            await interaction.edit_origin()

        elif interaction.component.placeholder.startswith('Укажите роли которые вы хотите добавить в класс'):
            data[str(interaction.author.guild.id)]['ROLES'][interaction.component.placeholder.split('*')[1]][
                0] = interaction.values
            data[str(interaction.author.guild.id)]['ROLES'][interaction.component.placeholder.split('*')[1]][1] = [0 for
                                                                                                                   i in
                                                                                                                   interaction.values]
            await interaction.send(embed=discord.Embed(
                title=f'Роли выбранны',
                color=COLOR
            ))

        with open('users.json', 'w') as file:
            json.dump(data, file, indent=4)

        await btst_set_def(interaction)

            # ==========================================================================================================================   IDA
        if interaction.component.placeholder.startswith('выберете канал который хотите сделать каналом администратора'):
            with open('users.json', 'r') as file:
                data = json.load(file)
            data[str(interaction.guild.id)]['idAdminchennel'] = interaction.values[0]
            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)
            await interaction.send(embed=discord.Embed(
                title="Успешно",
                description=f"*Канал администратора изменен на {interaction.values[0]}*",
            ))
            await btst_set_def(interaction)

        # # =======================================================================================================================    join roles
        if interaction.component.placeholder.startswith(
                'Укажите роли которые будут выдоваться участникам при входе на сервер'):
            with open('users.json', 'r') as file:
                data = json.load(file)
            data[str(interaction.guild.id)]['JoinRoles'] = interaction.values
            await interaction.send('роли выбранны')
            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)

            await btst_set_def(interaction)
