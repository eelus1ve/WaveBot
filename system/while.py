import time
import asyncio
import multiprocessing

import discord_components
from discord.ext import commands
from discord_components import ComponentsBot


class Wile_on(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

