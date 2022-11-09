import discord
import random
from discord.ext import commands
from BTSET import bdpy

class Coinpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['монетка', 'Монетка', 'МОНЕТКА'])
    async def coin(self, ctx, *arg):
        COLOR = bdpy(ctx)['COLOR']
        await ctx.send(embed=discord.Embed(
            title="Выпал: ",
            description="*Орел*" if random.randint(1, 2) == 1 else "*Решка*",
            color=COLOR
        ))

def setup(bot):
    bot.add_cog(Coinpy(bot))

