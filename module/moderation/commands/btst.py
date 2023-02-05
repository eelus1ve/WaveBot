import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from email.errors import InvalidMultipartContentTransferEncodingDefect
import json
import discord_components
from BTSET import BD
from system.btst_settings import SetForBTST, SecSetForBTST, ScrollSet, SettingsPanel

def setup(bot: discord_components.ComponentsBot):
    preference_set_for_best = ['канал администратора', 'настроить цвет', 'префикс']

    @bot.command()
    async def btst(ctx):
        await SettingsPanel(bot, ctx).btst_set_def(1)

    @bot.listen('on_button_click')
    async def tabs_choice(interaction: discord_components.Interaction):
        if interaction.component.label in ['модерация', 'настройка бота', 'настройка рейтинга', '--->', '<---']: await interaction.edit_origin()
        if interaction.component.label in ['модерация', 'настройка бота', 'настройка рейтинга']:
            await SettingsPanel(bot, interaction).tabs_choice()



    @bot.listen('on_button_click')
    async def settings_choice(interaction: discord_components.Interaction):
        try:
            set_panel = SettingsPanel(bot, interaction)
            if interaction.component.label == '--->':
                await set_panel.settings_choice_right()

            if interaction.component.label == '<---':
                await set_panel.settings_choice_left()
        except:
            pass

    @bot.listen('on_button_click')
    async def settings(interaction: discord_components.Interaction):
        if interaction.component.label == 'OK':
            old_emb = interaction.message.embeds[0]
            arg = old_emb.fields[0].name

            set_btst = SetForBTST(bot, interaction, old_emb, arg)
            set_pan = SettingsPanel(bot, interaction)

            await interaction.message.edit(components=[
                Select(placeholder='рекомендуем настроить',
                       options=[SelectOption(label=' '*i, value='zxc'*i) for i in range(len(preference_set_for_best))], max_values=1),
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
                await set_pan.btst_set_def()

            if arg == 'настроить роли':
                await set_btst.role_set()
                await interaction.edit_origin()

            if arg == 'добавить класс ролей':
                await set_btst.add_roleclass()
                await set_pan.btst_set_def()

            elif arg == 'настроить цвет':
                await set_btst.color_choice()
                await set_pan.btst_set_def()

            elif arg == 'настроить цвет ошибок':
                await set_btst.er_col_choice()
                await set_pan.btst_set_def()

            elif arg == 'канал администратора':
                await set_btst.admin_clen()

            elif arg == 'ncaps':
                await set_btst.ncaps()
                await set_pan.btst_set_def()

            elif arg == 'nwarns':
                await set_btst.nwarns()
                await set_pan.btst_set_def()

            elif arg == 'добавить плохое слово':
                await set_btst.add_bad_word()
                await set_pan.btst_set_def()

            elif arg == 'убрать плохое слово':
                await set_btst.remove_bod_word()
                await set_pan.btst_set_def()

            elif arg == 'создать "свои комнаты"':
                await set_btst.selfrooms()
                await set_pan.btst_set_def()

            elif arg == 'префикс':
                await set_btst.prefix()
                await set_pan.btst_set_def()

            elif arg == 'Указать свой текст при выборе ролей':
                await set_btst.selftitle()
                await set_pan.btst_set_def()

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
            set_pan = SettingsPanel(bot, interaction)

            if interaction.component.placeholder == 'Укажите классы в которые вы хотите добавить роли':
                await sec_set.rolecass_choice()
                await interaction.edit_origin()

            elif interaction.component.placeholder.startswith('Укажите роли которые вы хотите добавить в класс'):
                await sec_set.role_choice()
                await set_pan.btst_set_def()

            if interaction.component.placeholder.startswith('выберете канал который хотите сделать каналом администратора'):
                await sec_set.admin_clen()
                await set_pan.btst_set_def()

            if interaction.component.placeholder.startswith(
                    'Укажите роли которые будут выдоваться участникам при входе на сервер'):
                await sec_set.join_roles()
                await set_pan.btst_set_def()

        except:
            pass

    @bot.listen('on_select_option')
    async def preference_options(interaction):
        old_emb = interaction.message.embeds[0]
        arg = old_emb.fields[0].name

        set_btst = SetForBTST(bot, interaction, old_emb, arg)
        set_pan = SettingsPanel(bot, interaction)

        if interaction.values[0] == 'канал администратора':
            await set_btst.admin_clen()
            await set_pan.btst_set_def()

        elif interaction.values[0] == 'настроить цвет':
            await set_btst.color_choice()
            await set_pan.btst_set_def()

        elif interaction.values[0] == 'префикс':
            await set_btst.prefix()
            await set_pan.btst_set_def()

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



