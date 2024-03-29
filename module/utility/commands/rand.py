import discord
import random
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class Rand(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_rand(self, ctx: commands.Context, arg: int = None, arg2: int = None):
        if arg and not(arg2):
            des = random.randint(0, arg)
        elif arg and arg2:
            des = random.randint(arg, arg2)
        elif not arg:
            des = random.randint(0, 100)
        await ctx.send(embed=discord.Embed(
                    title=Lang(ctx).language['rand_title'],
                    description=des,
                    color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="UTILITYCOLOR")
                ))
