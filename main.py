import os
import discord
from discord.ext import commands
from BTSET import embpy, Lang
from dotenv import load_dotenv, find_dotenv
from system.Bot import WaveBot
from system.DBwriter import SQL_write


import sqlite3
from BTSET import BD

load_dotenv(find_dotenv())

intents = discord.Intents.all()


def get_prefix(bot: WaveBot, message: discord.Message):
    try:
        prefix = bot.read_sql(table="prefix", guild_id=message.guild.id, key="VALUE")
    except AttributeError:
        bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="PREFIX", value="~")
        prefix = bot.read_sql(table="prefix", guild=str(message.guild.id), key="PREFIX")
        raise commands.BadArgument(Lang(message).language['get_prefix_error'])
    return commands.when_mentioned(bot, message) + list(prefix)


bot: WaveBot = WaveBot(command_prefix=get_prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Portal 2'))
    await bot.load_extension('module.loader')
    print("modules connected")
    await bot.load_extension('system.while')
    print("module while connected")
    SQL_write(bot).write_db()
    print(f'{bot.user.name} connected')


@bot.command()
async def a(ctx: commands.Context):
    await embpy(ctx, comp='s', des=f'Степа все плохо')

    print(bot.read_sql(table='colors', key='COLOR'))


def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
