import random
import discord
from discord.ext import commands
from BTSET import Fun, Lang

class MagicBall(commands.Cog):

    async def command_Magicball(self, ctx: commands.Context):
        language = Lang.words(Lang.set_lang(ctx))
        randball = random.randint(1, 3)
        await ctx.send(embed=discord.Embed(
            title=language['magicball_title'],
            description=language[f'magicball_des_{randball}'],
            color=Fun(ctx).color
        ))
