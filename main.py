import os
import discord
from discord.ext import commands
from BTSET import bdpy, embpy
from dotenv import load_dotenv, find_dotenv
from system.Bot import WaveBot

load_dotenv(find_dotenv())

intents = discord.Intents.all()


def get_prefix(bot, message):
    try:
        prefix = bdpy(ctx=message)['PREFIX']
    except AttributeError:
        prefix = '~'
    return commands.when_mentioned(bot, message) + list(prefix)


bot = WaveBot(command_prefix=get_prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Portal 2'))
    print(f'{bot.user.name} connected')


@bot.command()
async def a(ctx: commands.Context):
    await embpy(ctx, comp='s', des=f'Степа все плохо')
    bot.db_wrt_utilitycolor(ctx, '0x8B0000')


def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
