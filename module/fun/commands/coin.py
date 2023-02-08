import random
import discord
from discord.ext import commands
from BTSET import Fun, Lang

class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_coin(self, ctx: commands.Context):
        language = Lang.words(Lang.set_lang(ctx))
        result = language['coin_result_1'] if random.randint(1, 2) == 1 else Lang.words(language)['coin_result_2']
        await ctx.send(embed=discord.Embed(
            title=language['coin_title_1'] if result == language['coin_result_1'] else language['coin_title_2'],
            description=result,
            color=Fun(ctx).color
        ))