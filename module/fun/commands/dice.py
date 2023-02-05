import random
import discord
from discord.ext import commands
from BTSET import Fun

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def command_dice(self, ctx: commands.Context):
        msg = await ctx.send(embed=discord.Embed(
                title="Игральная кость говорит:",
                description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                color = Fun(ctx).color
            )
        )
        for _ in range(5):
            await msg.edit(
                embed=discord.Embed(
                    title="Игральная кость говорит: ",
                    description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                    color=Fun(ctx).color
                )
            )