import random
import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot

class Coin(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    async def command_coin(self, ctx: commands.Context):
        result = random.randint(1, 2)
        await ctx.send(embed=discord.Embed(
            title=Lang(ctx).language[f'coin_title_{result}'],
            description=Lang(ctx).language[f'coin_result_{result}'],
            color=self.bot.db_get_funcolor(ctx)
        ))
