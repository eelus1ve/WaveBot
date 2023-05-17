import os
import discord
from discord.ext import commands
from BTSET import embpy
from dotenv import load_dotenv, find_dotenv
from system.Bot import WaveBot
from system.DBwriter import SQL_write

load_dotenv(find_dotenv())

intents = discord.Intents.all()


def get_prefix(bot: WaveBot, message: discord.Message):
    try:
        prefix = bot.read_sql("servers", guild=str(message.guild.id), key="PREFIX")
    except AttributeError:
        bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="PREFIX", value="~")
        raise commands.BadArgument() #сюда текст
    return commands.when_mentioned(bot, message) + list(prefix)


bot = WaveBot(command_prefix=get_prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Portal 2'))
    await bot.load_extension('module.loader')
    print("modules connected")
    await bot.load_extension('system.while')
    print("module while connected")
    SQL_write(bot).createsqltabel()
    print(f'{bot.user.name} connected')

@bot.command()
async def a(ctx: commands.Context):
    await embpy(ctx, comp='s', des=f'Степа все плохо')


def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()