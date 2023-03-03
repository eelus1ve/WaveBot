import random
import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class MagicBall(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    async def command_Magicball(self, ctx: commands.Context):
        randball = random.randint(1, 3)
        await ctx.send(embed=discord.Embed(
            title=Lang(ctx).language['magicball_title'],
            description=Lang(ctx).language[f'magicball_des_{randball}'],
            color=self.bot.db_get_funcolor(ctx)
        ))