import os
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from system.Bot import WaveBot
from system.DBwriter import SQL_write
from discord import app_commands

from BTSET import BD


load_dotenv(find_dotenv())

intents = discord.Intents.all()


def get_prefix(bot: WaveBot, message: discord.Message):
    prefix = db_get_prefix(message.guild.id)
    return commands.when_mentioned(bot, message) + list(prefix)


bot = WaveBot(command_prefix=get_prefix, intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Portal 2'))
    SQL_write(bot).write_db()
    await bot.load_extension('module.loader')
    print(f'{bot.user.name} connected')

@bot.command()
async def a(ctx: commands.Context):
    await embpy(ctx, comp='s', des=f'Степа все плохо')

def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
