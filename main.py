#=============================================================================================импорты
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       --> token стёпы <---             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      #нахуя?       #нужно было!     #нахуя?    #чтобы токен поменять!5
import multiprocessing

import discord
import json
import os
import asyncio
import discord_components
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import interactions
from BD import bdpy, bdint
from interactions import TextInput, Modal, TextStyleType, SelectMenu#, SelectOption, error
from discord_components import ComponentsBot, Button, Select
from discord_components import SelectOption
load_dotenv(find_dotenv())

#=======================================================================================================================
intents=discord.Intents.all()
def get_prefix(bot, message):
    with open('users.json', 'r') as file:
        data = json.load(file)
    try:
        prefix = data[str(message.guild.id)]['PREFIX']
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
    bot.load_extension('loaderpy')
    bot.load_extension('JSONwriter')
    # client.load('module.rate.score')
    # client.reload('module.rate.score')
    client.load('module.voice.vcbot')
    client.reload('module.voice.vcbot')
    bot.load_extension('system.while')
    
    
    print(f'{bot.user.name} connected')


    await bot.change_presence(activity=discord.Game('Portal 2'))
#=======================================================================================================================

#=======================================================================================================================
@bot.command()
async def a(ctx: commands.Context):
    # client.load('module.moderation.warns')
    gld: discord.Guild = ctx.guild
    for em in gld.emojis:
        print(em)
    await ctx.send(embed=discord.Embed(
        title="Степ не волнуйся все плохо)",
        color=bdpy(ctx)['COLOR']
        ))

@client.command(
    name='a',
    description='b'
)
async def a(ctx):
    
    await ctx.send(embeds=interactions.Embed(
        title="Степ не волнуйся все очень плохо)",
        color=bdint(ctx)['COLOR']
        ))
#=======================================================================================================================
# @bot.event
# async def on_command_error(ctx, error):
#     with open('users.json', 'r') as file:
#         dataServerID = json.load(file)
#         ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
#         pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
    # if isinstance(error, commands.errors.CommandNotFound):
    #     print(error)
    #     found = re.findall(r'Command \s*"([^\"]*)"', str(error))
    #     await ctx.send(embed=discord.Embed(
    #         title="Ошибка",
    #         description=f"*Команды `{''.join(found)}` не существует*",
    #         color = ErCOLOR
    #     ))
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
