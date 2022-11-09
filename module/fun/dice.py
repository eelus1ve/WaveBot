import discord
import random
from discord.ext import commands
from BTSET import bdpy

class Dicepy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        COLOR = bdpy(ctx)['COLOR']
            
        msg = await ctx.send(embed=discord.Embed(
                title="Игральная кость говорит:",
                description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                color = COLOR
            )
        )
        for _ in range(5):
            await msg.edit(
                embed=discord.Embed(
                    title="Игральная кость говорит: ",
                    description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                    color=COLOR
                )
            )
def setup(bot):
    bot.add_cog(Dicepy(bot))