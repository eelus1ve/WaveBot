#=============================================================================================импорты
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       --> token стёпы <---             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      #нахуя?       #нужно было!     #нахуя?    #чтобы токен поменять!5
import multiprocessing
from discord_components import SelectOption as Sel
import discord_components
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import interactions
from discord_components import ComponentsBot, Button, Select
from pydoc import cli
import discord
import os
import asyncio
from BTSET import bdpy, embpy
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption, error
import re


load_dotenv(find_dotenv())


#=======================================================================================================================
intents=discord.Intents.all()
def get_prefix(bot, message):
    try:
        prefix = bdpy(ctx=message)['PREFIX']
    except AttributeError:
        prefix = '~'
    return prefix
client = interactions.Client(token=os.getenv('TOKEN'))
bot =ComponentsBot(command_prefix = get_prefix, intents=intents)
bot.remove_command('help')
#=======================================================================================================================

#=======================================================================================================================
@bot.event
async def on_ready():
    bot.load_extension('module.loader')
    bot.load_extension('system.JSONwriter')
    # client.load('module.rate.score')
    # client.reload('module.rate.score')
    client.load('module.moderation.warns')
    client.reload('module.moderation.warns')
    bot.load_extension('system.while')
    
    
    print(f'{bot.user.name} connected')


    await bot.change_presence(activity=discord.Game('Portal 2'))
#=======================================================================================================================

#=======================================================================================================================
@bot.command()
async def a(ctx: commands.Context):
    client.load('module.moderation.warns')
    await embpy(ctx, comp='s', des=f'Степа все плохо')

#===================================================================================================


#=======================================================================================================================
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

#=======================================================================================================================


# @bot.event
# async def on_error(ctx, err):
#     print('ошибка', ':', ctx)
#     print(err)


def main():

    loop = asyncio.get_event_loop()

    task2 = loop.create_task(bot.start(os.getenv('TOKEN')))
    task1 = loop.create_task(client._ready())

    gathered = asyncio.gather(task1, task2, loop=loop)
    loop.run_until_complete(gathered)


if __name__ == '__main__':
    main()
