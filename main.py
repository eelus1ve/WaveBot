import os
import discord
from discord.ext import commands
from BTSET import embpy, Lang
from dotenv import load_dotenv, find_dotenv
from system.Bot import WaveBot
from system.DBwriter import SQL_write
from discord import app_commands

from BTSET import BD
import sqlite3

def db_get_prefix(guild_id):
    conn = sqlite3.connect(f'{BD}WaveDateBase.db')
    cursor = conn.cursor()
    cursor.execute(f'''SELECT PREFIX FROM servers WHERE ID = {guild_id}''')
    records = cursor.fetchone()[0]
    conn.close()
    return records


load_dotenv(find_dotenv())

intents = discord.Intents.all()


def get_prefix(bot: WaveBot, message: discord.Message):
    # try:
    print(message.guild.id, type(message.guild.id), sep='\n')
    prefix = db_get_prefix(message.guild.id)
    # except AttributeError:
    #     bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="PREFIX", value="~")
    #     prefix = bot.read_sql("servers", guild=str(message.guild.id), key="PREFIX")
    #     raise commands.BadArgument(Lang(message).language['get_prefix_error'])
    return commands.when_mentioned(bot, message) + list(prefix)


bot = WaveBot(command_prefix=get_prefix, intents=intents)
bot.remove_command('help')

# from system.db_.sqledit import SQLeditor
# import random
# import sqlite3

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Portal 2'))
    # await bot.load_extension('module.loader')
    # print("modules connected")
    # await bot.load_extension('system.while')
    # print("module while connected")
    SQL_write(bot).write_db()
    print(f'{bot.user.name} connected')
    # print('1128082554751291552', len('1128082554751291552'), sep="\n")
    # for guild in bot.guilds:
    #     for _ in range(10):
    #         name = ''.join(random.choices("qwertyuiopasdfghjklzxcvbnm", k=6))
    #         SQLeditor.add_class(guild_id=guild.id, name=name)
    #         for __ in range(10):
    #             SQLeditor.add_role(guild_id=guild.id, name=name, role_id=random.randint(1000000000, 1000000000000))
    # conn = sqlite3.connect(f'{BD}WaveDateBase.db')
    # conn.execute("""PRAGMA foreign_keys=on""")
    # conn.execute('''UPDATE servers SET ID = 1234567890 WHERE ID = 547782677793734656''')
    # conn.execute('''DELETE FROM servers WHERE ID = 1234567890''')
    # conn.commit()
    # conn.close()
@bot.command()
async def a(ctx: commands.Context):
    await embpy(ctx, comp='s', des=f'Степа все плохо')

def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
