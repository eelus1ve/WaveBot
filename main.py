import os
import discord
from discord.ext import commands
from BTSET import bdpy, embpy
from dotenv import load_dotenv, find_dotenv
from discord_components import ComponentsBot


load_dotenv(find_dotenv())


intents=discord.Intents.all()
def get_prefix(bot, message):
    try:
        prefix = bdpy(ctx=message)['PREFIX']
    except AttributeError:
        prefix = '~'
    return commands.when_mentioned(bot, msg=message) + list(prefix)
        
bot = ComponentsBot(command_prefix = get_prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    bot.load_extension('system.JSONwriter')
    bot.load_extension('module.loader')
    bot.load_extension('system.while')
    await bot.change_presence(activity=discord.Game('Portal 2'))
    print(f'{bot.user.name} connected')

@bot.command()
async def a(ctx: commands.Context):
    await embpy(ctx, comp='s', des=f'Степа все плохо')


def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()