import time
import asyncio
import multiprocessing
import os
import subprocess
from discord.ext import commands
import datetime
from system import JSONwriter

def res_copy():
    if not int(datetime.datetime.now().time().hour) and int(datetime.datetime.now().minute) <= 1:
        for i in os.listdir('.'):
            if i.endswith('.json'):
                subprocess.call(fr'copy {i} system\rezerv\{i[:-5]}_rez.json', shell=True, stdout=subprocess.DEVNULL)

def prnt():
    while 1:
        res_copy()

        time.sleep(60)

class Wile_on(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        JSONwriter.Json_write(self.bot).jsonwrite()  # эту строчку смыть в унитаз
        pr = multiprocessing.Process(target=prnt)
        pr.start()


async def setup(bot):
    await bot.add_cog(Wile_on(bot))
    pass
