import asyncio

import discord
import discord_components
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select
from discord_components import SelectOption
import json
import os


class Suppot(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

    def support_json_writer(member: discord.Member, reason: str, text: str):
        with open('support.json', 'r') as file:
            sup_data = json.load(file)

        sup_data[reason].update({
            member.id: text
        })

        with open('support.json', 'w') as file:
            json.dump(sup_data, file, indent=4)

    @commands.command()
    async def main_support(self, ctx):
        if not ctx.guild:
            await ctx.send(components=[
                Select(
                    max_values=1,
                    min_values=0,
                    placeholder='Выберете что Вам нужно',
                    options=[
                        SelectOption(label='Предложить идею', value='idea'),
                        SelectOption(label='Вопрос о команде', value='que'),
                        SelectOption(label='Рассказать про ошибку', value='err'),
                        SelectOption(label='Cooбщение для разработчиков', value='message')
                    ]
                )
            ])
    @commands.Cog.listener('on_select_option')
    async def main_support_select(self, interaction: discord_components.Interaction):
        if interaction.component.placeholder == 'Выберете что Вам нужно':
            try:
                def check(message: discord.Message):
                    return message.author == interaction.author and not message.guild

                if interaction.values[0] == 'idea':
                    await interaction.send(embed=discord.Embed(
                        title='Напишите Вашу идею'
                    ))

                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    Suppot.support_json_writer(member=interaction.author, reason='idea', text=ms.content)

                    await ms.author.send('спасибо за идею она будет рассмотренни в течении недели')
                    adm_user = await self.bot.fetch_user(466609421863354388)
                    await adm_user.send('ОТВЕТЬ МРАЗЬ ТЕБЕ ВОПРОС ЗАДАЛИ')

                elif interaction.values[0] == 'que':
                    await interaction.send(embed=discord.Embed(
                        title='Напишите Ваш вопрос'
                    ))

                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    Suppot.support_json_writer(member=interaction.author, reason='que', text=ms.content)

                    await ms.author.send('ответ будет дан в течении двух дней')
                    adm_user = await self.bot.fetch_user(466609421863354388)
                    await adm_user.send('ОТВЕТЬ МРАЗЬ ТЕБЕ ВОПРОС ЗАДАЛИ')

                elif interaction.values[0] == 'err':
                    await interaction.send(embed=discord.Embed(
                        title='Напишите найденную вами ошибку'
                    ))

                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    Suppot.support_json_writer(member=interaction.author, reason='err', text=ms.content)

                    await ms.author.send('спасибо за помощь в поисках ошибок бота')
                    adm_user = await self.bot.fetch_user(466609421863354388)
                    await adm_user.send('ОТВЕТЬ МРАЗЬ ТЕБЕ ВОПРОС ЗАДАЛИ')

                elif interaction.values[0] == 'message':
                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    Suppot.support_json_writer(member=interaction.author, reason='message', text=ms.content)

                    await ms.author.send('ожидайте ответа в течении' + '999999'*1000 + 'дней')
                    adm_user = await self.bot.fetch_user(466609421863354388)
                    await adm_user.send('ОТВЕТЬ МРАЗЬ ТЕБЕ ВОПРОС ЗАДАЛИ')
            except IndexError:
                pass

class SupportAnswer(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

    @commands.command()
    async def admin_request(self, ctx):
        with open('support.json', 'r') as file:
            sup_data = json.load(file)
        await ctx.send(components=[
            Select(
                max_values=1,
                min_values=1,
                placeholder='чё смотреть хочешь?',
                options=[
                    SelectOption(label=f'{key}', value=key) for key in sup_data if sup_data[key]
                ]
            )
        ])

    @commands.Cog.listener('on_select_option')
    async def vbhyfd(self, interaction):
        if interaction.component.placeholder == 'чё смотреть хочешь?':
            with open('support.json', 'r') as file:
                sup_data = json.load(file)

            int_val = sup_data[interaction.values[0]]

            await interaction.send(components=[
                Select(
                    max_values=1,
                    min_values=1,
                    placeholder='кого смотреть хочешь?',
                    options=[
                        SelectOption(label=f'{await self.bot.fetch_user(int(key))}', value=f'{interaction.values[0]}/*/*/{key}') for key in int_val if int_val[key]
                    ]
                )
            ])

    @commands.Cog.listener('on_select_option')
    async def vbhyffdd(self, interaction):
        if interaction.component.placeholder == 'кого смотреть хочешь?':
            with open('support.json', 'r') as file:
                sup_data = json.load(file)

            int_val = interaction.values[0].split('/*/*/')
            in_mess = sup_data[int_val[0]][int_val[1]]
            member = await self.bot.fetch_user(int(int_val[1]))

            await interaction.send(f'{in_mess} \n\nпиши ответ')
            await asyncio.sleep(3)
            await interaction.send()

            def check(message: discord.Message):
                return message.author == interaction.author and not message.guild

            ms: discord.Message = await self.bot.wait_for('message', check=check)

            await member.send(ms.content)





def setup(bot):
    bot.add_cog(Suppot(bot))
    bot.add_cog(SupportAnswer(bot))

