import discord
from operator import index
import discord_components
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select
from discord_components import SelectOption
from discord.utils import get
from email.errors import InvalidMultipartContentTransferEncodingDefect
import asyncio
import json
import StringProgressBar#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from discord_components import ComponentsBot
import interactions
#from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption, Option
from youtube_dl import YoutubeDL
import os
import time


client = interactions.Client('OTgxNTExNjgyOTYwNTQ3ODYw.GpV6bM.XIGASOaT6YPnhU2Q0sAPOqRwBrFfWzcRsvkv6E')
bot: ComponentsBot = ComponentsBot(command_prefix='~')
loop = asyncio.get_event_loop()

def support_json_writer(member: discord.Member, reason: str, text: str):
    with open('../../../кусок бота/support.json', 'r') as file:
        sup_data = json.load(file)

    sup_data[reason].update({
        member.id: text
    })

    with open('../../../кусок бота/support.json', 'w') as file:
        json.dump(sup_data, file, indent=4)




class Suppot(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

        if not os.path.exists('../../../кусок бота/support.json'):
            with open('../../../кусок бота/support.json', 'w') as file:
                json.dump({
                    'idea': {},
                    'que': {},
                    'err': {},
                    'message': {}
                }, file, indent=4)
        else:
            with open('../../../кусок бота/support.json', 'r') as file:
                if not file.read():
                    with open('../../../кусок бота/support.json', 'w') as file:
                        json.dump({
                            'idea': {},
                            'que': {},
                            'err': {},
                            'message': {}
                        }, file, indent=4)
                    print("Пока json(support)")

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
                        SelectOption(label='Cooбщение для разработчиков', value='aboba3')
                    ]
                )
            ])
    @commands.Cog.listener('on_select_option')
    async def main_support_select(self, interaction: discord_components.Interaction):

        def check(message: discord.Message):
            return msg.author == interaction.author and not message.guild

        if interaction.values[0] == 'idea':
            await interaction.send(embed=discord.Embed(
                title='Напишите Вашу идею'
            ))

            ms: discord.Message = await self.bot.wait_for('message', check=check)

            support_json_writer(member=interaction.author, reason='idea', text=ms.content)
        elif interaction.component.label == 'que':
            await interaction.send(embed=discord.Embed(
                title='Напишите Ваш вопрос'
            ))

            ms: discord.Message = await self.bot.wait_for('message', check=check)

            support_json_writer(member=interaction.author, reason='que', text=ms.content)
        elif interaction.component.label == 'err':
            await interaction.send(embed=discord.Embed(
                title='Напишите найденную вами ошибку'
            ))

            ms: discord.Message = await self.bot.wait_for('message', check=check)

            support_json_writer(member=interaction.author, reason='err', text=ms.content)
        elif interaction.component.label == 'message':
            ms: discord.Message = await self.bot.wait_for('message', check=check)

            support_json_writer(member=interaction.author, reason='message', text=ms.content)

bot.add_cog(Suppot(bot))



task2 = loop.create_task(bot.start("OTgxNTExNjgyOTYwNTQ3ODYw.GpV6bM.XIGASOaT6YPnhU2Q0sAPOqRwBrFfWzcRsvkv6E"))
task1 = loop.create_task(client._ready())

gathered = asyncio.gather(task1, task2, loop=loop)
loop.run_until_complete(gathered)