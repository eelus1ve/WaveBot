import random
import discord
from discord.ext import commands
from BTSET import Fun

class MagicBall(commands.Cog):

    async def command_Magicball(self, ctx: commands.Context):
        randball = random.randint(1, 3)
        await ctx.send(embed=discord.Embed(
            title="Шар судьбы говорит: ",
            description="*Да!*" if randball == 1 else False or "*Может быть.*" if randball == 2 else False or "*Нет!*" if randball == 3 else False,
            color=Fun(ctx).color
        ))
