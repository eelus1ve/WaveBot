import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from email.errors import InvalidMultipartContentTransferEncodingDefect
import json
import discord_components
from BTSET import BD
from system.btst_settings import SetForBTST, SecSetForBTST, ScrollSet

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

    preference_set_for_best = ['канал администратора', 'настроить цвет', 'префикс']

    async def btst_set_def(interaction, f=0):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)

        emb = discord.Embed(
            title='―――――――――*Wave Settings*―――――――――――',
            description='.',
            color=COLOR
        )
        emb.add_field(name='это настройки WaveBot',
                      value='Вы можете выбрать раздел или сразу открыть рекомендуемые настройки')

        if f:
            await interaction.send(embed=emb, components=[
            Select(placeholder='рекомендуем настроить', options=[SelectOption(label=i, value=i) for i in preference_set_for_best], max_values=1),
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
                Select(placeholder='рекомендуем настроить', options=[SelectOption(label=i, value=i) for i in preference_set_for_best], max_values=1),
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
        await btst_set_def(interaction, 1)

    @bot.listen('on_button_click')
    async def tabs_choice(interaction: discord_components.Interaction):
        gld: discord.Guild = interaction.guild

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)

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
            await interaction.message.edit(embed=emb, components=interaction.message.components)

    @bot.listen('on_button_click')
    async def settings_choice(interaction: discord_components.Interaction):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)

        try:
            if interaction.component.label == '--->':
                old_emb: discord.Embed = interaction.message.embeds[0].description.replace('*', '')

                keys = []
                keys.append(interaction.message.embeds[0].fields[0].name)
                keys.extend(interaction.message.embeds[0].fields[1].value.replace('.', '').replace('*', '').split('\n'))

                keys.append(keys.pop(0))

                emb = discord.Embed(
                    title=interaction.message.embeds[0].title,
                    description=f'**{old_emb}**',
                    color=COLOR
                )
                emb.add_field(name=f'{keys[0]}', value=f'{settings_for_btst[old_emb][keys[0]]}')
                emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
                await interaction.message.edit(embed=emb)

            if interaction.component.label == '<---':
                old_emb: discord.Embed = interaction.message.embeds[0].description.replace('*', '')

                keys = []
                keys.append(interaction.message.embeds[0].fields[0].name)
                keys.extend(interaction.message.embeds[0].fields[1].value.replace('.', '').replace('*', '').split('\n'))

                keys.insert(0, keys.pop(-1))
                emb = discord.Embed(
                    title=interaction.message.embeds[0].title,
                    description=f'**{old_emb}**',
                    color=COLOR
                )
                emb.add_field(name=f'{keys[0]}', value=f'{settings_for_btst[old_emb][keys[0]]}')
                emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
                await interaction.message.edit(embed=emb)
        except:
            pass

    @bot.listen('on_button_click')
    async def settings(interaction: discord_components.Interaction):
        if interaction.component.label == 'OK':
            old_emb = interaction.message.embeds[0]
            arg = old_emb.fields[0].name

            set_btst = SetForBTST(bot, interaction, old_emb, arg)

            await interaction.message.edit(components=[
                Select(placeholder='рекомендуем настроить',
                       options=[SelectOption(label=i, value=i) for i in preference_set_for_best], max_values=1),
                [
                    Button(label='модерация', disabled=True),
                    Button(label='настройка бота', disabled=True),
                    Button(label='настройка рейтинга', disabled=True)
                ],
                [
                    Button(label='<---'),
                    Button(label='OK'),
                    Button(label='--->')
                ]
            ])

            if arg == 'музыка':
                await set_btst.music()
                await btst_set_def(interaction)

            if arg == 'настроить роли':
                await set_btst.role_set()
                await interaction.edit_origin()

            if arg == 'добавить класс ролей':
                await set_btst.add_roleclass()
                await btst_set_def(interaction)

            elif arg == 'настроить цвет':
                await set_btst.color_choice()
                await btst_set_def(interaction)

            elif arg == 'настроить цвет ошибок':
                await set_btst.er_col_choice()
                await btst_set_def(interaction)

            elif arg == 'канал администратора':
                await set_btst.admin_clen()

            elif arg == 'ncaps':
                await set_btst.ncaps()
                await btst_set_def(interaction)

            elif arg == 'nwarns':
                await set_btst.nwarns()
                await btst_set_def(interaction)

            elif arg == 'добавить плохое слово':
                await set_btst.add_bad_word()
                await btst_set_def(interaction)

            elif arg == 'убрать плохое слово':
                await set_btst.remove_bod_word()
                await btst_set_def(interaction)

            elif arg == 'создать "свои комнаты"':
                await set_btst.selfrooms()
                await btst_set_def(interaction)

            elif arg == 'префикс':
                await set_btst.prefix()
                await btst_set_def(interaction)

            elif arg == 'Указать свой текст при выборе ролей':
                await set_btst.selftitle()
                await btst_set_def(interaction)

            elif arg == 'настроить роли при входе на сервер':
                await set_btst.join_roles()

            elif arg == 'список join ролей':
                pass

            elif arg == 'classes':
                pass

            elif arg == 'add_IgnoreChannel':
                pass

            elif arg == 'add_IgnoreRole':
                pass

            elif arg == 'IgnoreRoles':
                pass

            elif arg == 'добавить канал с инфорацией':  # переимовать
                pass

    @bot.listen('on_select_option')
    async def second_set(interaction: discord_components.Interaction):
        try:
            old_emb = interaction.message.embeds[0]

            sec_set = SecSetForBTST(bot, interaction, old_emb)

            if interaction.component.placeholder == 'Укажите классы в которые вы хотите добавить роли':
                await sec_set.rolecass_choice()
                await interaction.edit_origin()

            elif interaction.component.placeholder.startswith('Укажите роли которые вы хотите добавить в класс'):
                await sec_set.role_choice()
                await btst_set_def(interaction)

            if interaction.component.placeholder.startswith('выберете канал который хотите сделать каналом администратора'):
                await sec_set.admin_clen()
                await btst_set_def(interaction)

            if interaction.component.placeholder.startswith(
                    'Укажите роли которые будут выдоваться участникам при входе на сервер'):
                await sec_set.join_roles()
                await btst_set_def(interaction)

        except:
            pass

    @bot.listen('on_select_option')
    async def preference_options(interaction):
        old_emb = interaction.message.embeds[0]
        arg = old_emb.fields[0].name

        set_btst = SetForBTST(bot, interaction, old_emb, arg)

        if interaction.values[0] == 'канал администратора':
            await set_btst.admin_clen()
            await btst_set_def(interaction)
        elif interaction.values[0] == 'настроить цвет':
            await set_btst.color_choice()
            await btst_set_def(interaction)
        elif interaction.values[0] == 'префикс':
            await set_btst.prefix()
            await btst_set_def(interaction)

    @bot.listen('on_button_click')
    async def scroll_set(interaction):
        try:
            old_emb = interaction.message.embeds[0]

            scr_set = ScrollSet(bot, interaction, old_emb)

            if interaction.component.label == '--->':
                await scr_set.scroll_right()

            if interaction.component.label == '<---':
                await scr_set.scroll_left()

        except InvalidMultipartContentTransferEncodingDefect:
            pass



