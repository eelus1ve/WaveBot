import time
import asyncio
import multiprocessing
import os

import discord_components
from discord.ext import commands
from discord_components import ComponentsBot


class Wile():
    def __init__(self, bot):
        self.bot = bot

    def res_copy(self):
        #os.popen(f'copy {} ')
        pass

    def while_true(self):
        while 1:
            time.sleep(60)

            Wile.res_copy()


class Wile_on(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot



def setup(bot):
    bot.add_cog(Wile_on(bot))