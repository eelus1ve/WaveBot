def setup(bot):
    import discord
    import json
    from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption, Interaction
    from discord.ext import commands
    from easy_pil import Editor, load_image_async, Font
    from typing import Optional
    from discord import File
    import asyncio
    import random
    import os
    import json
    COLOR = 0x0000FF
    ErCOLOR = 0x8B0000
    ques = ['Вопрос по использованую команды', 'Проблемы в роботе бота', 'Общий вопрос']
    @bot.command()
    async def question(ctx):
        try:
            print(ctx.author.guild.id)
        except AttributeError:
            await ctx.send(embed=discord.Embed(
                    title='Выберите тип запроса',
                    color=COLOR
                ),
                    components=[
                        Select(
                            placeholder='Выберите тип',
                            max_values=1,
                            min_values=1,
                            options=[SelectOption(label=i, value=i) for i in ques]
                        )
                    ]
                )
    @bot.listen('on_select_option')
    async def que(interaction):
        ques = ['Вопрос по использованую команды', 'Проблемы в роботе бота', 'Общий вопрос']

        if interaction.component.placeholder == 'Выберите тип':
            try:
                for q1 in interaction.values:
                    if q1 == 'Вопрос по использованую команды':
                        await interaction.send(embed=discord.Embed(
                        title='Опишите ваш вопрос',
                        color=COLOR
                        ))
                        ms = await bot.wait_for(event='message')
                        await interaction.send(embed=discord.Embed(
                        title='Отправить запрос?',
                        description=f'Ваш запрос: \n\
                        Тип вопроса: {interaction.component.placeholder} \n\
                        Ваш вопрос: {ms}',
                        color=COLOR
                        ),
                        components = [
                            Button(label='Да', style=1),
                            Button(label='Нет', style=1)
                        ])
            except:
                pass
    @bot.event
    async def on_button_click(interaction):
        if str(interaction.component.label) == 'Да':
            with open('quest.json', 'r') as file:
                data = json.load(file)
            with open('quest.json', 'w') as file:
                data.update({
                    1
                })

