import random
import discord
from discord.ext import commands
from BTSET import Fun

class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_coin(self, ctx: commands.Context):
        result = "Орел" if random.randint(1, 2) == 1 else "Решка"
        await ctx.send(embed=discord.Embed(
            title="Выпал: " if result == "Орел" else "Выпала: ",
            description=result,
            color=Fun(ctx).color
        ))
