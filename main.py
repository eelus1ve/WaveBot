#=============================================================================================импорты
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       --> token стёпы <---             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      #нахуя?       #нужно было!     #нахуя?    #чтобы токен поменять! #ещё комент кста
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from discord_components import ComponentsBot
import discord
import os
from BTSET import bdpy, embpy

load_dotenv(find_dotenv())

intents = discord.Intents.all()


def get_prefix(message):
    try:
        prefix = bdpy(ctx=message)['PREFIX']
    except AttributeError:
        prefix = '~'
    return prefix


def mention_and_prefix(bot, message):
    return commands.when_mentioned(bot, msg=message) + list(get_prefix(message))


bot =ComponentsBot(command_prefix=mention_and_prefix, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    bot.load_extension('module.loader')
    bot.load_extension('system.JSONwriter')
    bot.load_extension('system.while')
    await bot.change_presence(activity=discord.Game('Portal 2'))
    print(f'{bot.user.name} connected')


@bot.command()
async def a(ctx: commands.Context):
    await embpy(ctx, comp='s', des=f'Степа все плохо')
    

# @bot.event
# async def on_command_error(ctx, error):
#     ErCOLOR = bdpy(ctx)['ErCOLOR']
#     pref = bdpy(ctx)['PREFIX']
#     if isinstance(error, commands.errors.CommandNotFound):
#         print(error)
#         found = re.findall(r'Command \s*"([^\"]*)"', str(error))
#         await ctx.send(embed=discord.Embed(
#             title="Ошибка",
#             description=f"*Команды `{''.join(found)}` не существует*",
#             color = ErCOLOR
#         ))
    # elif isinstance(error, commands.errors.MemberNotFound):
    #     found = re.findall(r'Member \s*"([^\"]*)"', str(error))
    #     await ctx.send(embed=discord.Embed(
    #         title="Ошибка",
    #         description=f"*Участник `{''.join(found)}` не найден*",
    #         color = ErCOLOR
    #     ))
    # elif isinstance(error, commands.errors.CommandInvokeError):
    #     pass


def main():
    bot.run(os.getenv('TOKEN'))


if __name__ == '__main__':
    main()
