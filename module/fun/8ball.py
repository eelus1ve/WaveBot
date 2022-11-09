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
        await ctx.send(embed=discord.Embed(
            title="Шар судьбы говорит: ",
            description="*Да!*" if randball == 1 else False or "*Может быть.*" if randball == 2 else False or "*Нет!*" if randball == 3 else False,
            color=COLOR
        ))
            

def setup(bot):
    bot.add_cog(Ballpy(bot))