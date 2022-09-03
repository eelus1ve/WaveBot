import time
import asyncio
import multiprocessing
import os
import subprocess
import discord_components
from discord.ext import commands
from discord_components import ComponentsBot
import datetime

def res_copy():
    if not int(datetime.datetime.now().time().hour):
        for i in os.listdir('.'):
            if i.endswith('.json'):
                subprocess.call(fr'copy {i} system\rezerv\{i[:-5]}_rez.json', shell=True, stdout=subprocess.DEVNULL)

def prnt():
    while 1:
        res_copy()
        time.sleep(60)

class Wile_on(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

        pr = multiprocessing.Process(target=prnt)
        pr.start()




def setup(bot):
    bot.add_cog(Wile_on(bot))