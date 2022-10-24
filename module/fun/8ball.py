import discord
import random
from discord.ext import commands
from BTSET import bdpy
class Ballpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Волшебный_шар', '8ball', 'MagicBall', '8Ball'])
    async def Magicball(self, ctx):
        COLOR = bdpy(ctx)['COLOR']
        randball = random.randint(1, 3)
        if randball == 1:
            await ctx.send(embed=discord.Embed(
                title="Шар судьбы говорит: ",
                description="*Да!*",
                color=COLOR
            ))
        elif randball == 2:
            await ctx.send(embed=discord.Embed(
                title="Шар судьбы говорит: ",
                description="*Может быть.*",
                color=COLOR
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="Шар судьбы говорит: ",
                description="*Нет!*",
                color=COLOR
            ))

def setup(bot):
    bot.add_cog(Ballpy(bot))