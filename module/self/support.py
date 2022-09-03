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

        if not os.path.exists('support.json'):
            with open('support.json', 'w') as file:
                json.dump({
                    'idea': {},
                    'que': {},
                    'err': {},
                    'message': {}
                }, file, indent=4)
        else:
            with open('support.json', 'r') as file:
                if not file.read():
                    with open('support.json', 'w') as file:
                        json.dump({
                            'idea': {},
                            'que': {},
                            'err': {},
                            'message': {}
                        }, file, indent=4)
                    print("Пока json(support)")

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

        def check(message: discord.Message):
            return message.author == interaction.author and not message.guild

        if interaction.values[0] == 'idea':
            await interaction.send(embed=discord.Embed(
                title='Напишите Вашу идею'
            ))

            ms: discord.Message = await self.bot.wait_for('message', check=check)

            Suppot.support_json_writer(member=interaction.author, reason='idea', text=ms.content)

        elif interaction.values[0] == 'que':
            await interaction.send(embed=discord.Embed(
                title='Напишите Ваш вопрос'
            ))

            ms: discord.Message = await self.bot.wait_for('message', check=check)

            Suppot.support_json_writer(member=interaction.author, reason='que', text=ms.content)

        elif interaction.values[0] == 'err':
            await interaction.send(embed=discord.Embed(
                title='Напишите найденную вами ошибку'
            ))

            ms: discord.Message = await self.bot.wait_for('message', check=check)

            Suppot.support_json_writer(member=interaction.author, reason='err', text=ms.content)

        elif interaction.values[0] == 'message':
            ms: discord.Message = await self.bot.wait_for('message', check=check)

            Suppot.support_json_writer(member=interaction.author, reason='message', text=ms.content)

def serup(bot):
    bot.add_cog(Suppot(bot))

