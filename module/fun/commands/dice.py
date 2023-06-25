import random
import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class Dice(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot
        
    async def command_dice(self, ctx: commands.Context):
        msg = await ctx.send(embed=discord.Embed(
                title=Lang(ctx).language['dice_title'],
                description='{} {} {}'.format(random.randint(1, 6), Lang(ctx).language['dice_des'], random.randint(1, 6)),
                color=self.bot.read_sql(table="colors", key="FUNCOLOR")
            )
        )
        for _ in range(5):
            await msg.edit(
                embed=discord.Embed(
                    title=Lang(ctx).language['dice_title'],
                    description='{} {} {}'.format(random.randint(1, 6), Lang(ctx).language['dice_des'], random.randint(1, 6)),
                    color=self.bot.read_sql(table="colors", key="FUNCOLOR")
                )
            )
