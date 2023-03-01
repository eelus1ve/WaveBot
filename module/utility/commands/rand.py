import discord
import random
from discord.ext import commands
from BTSET import Utility

class Rand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def command_rand(self, ctx: commands.Context, arg: int, arg2: int):
        if arg and not(arg2):
            des=random.randint(0, arg)
        elif arg and arg2:
            des=random.randint(arg, arg2)
        elif not(arg):
            des=random.randint(0, 100)
        await ctx.send(embed=discord.Embed(
                    title="Ваше рандомное число: ",
                    description=des,
                    color = Utility(ctx).color,
                ))
