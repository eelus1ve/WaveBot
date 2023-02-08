import random
import discord
from discord.ext import commands
from BTSET import Fun, Lang

class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_coin(self, ctx: commands.Context):
        language = Lang.words(Lang.set_lang(ctx))
        result = random.randint(1, 2)
        await ctx.send(embed=discord.Embed(
            title=language[f'coin_title_{result}'],
            description=language[f'coin_result_{result}'],
            color=Fun(ctx).color
        ))
