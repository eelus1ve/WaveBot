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
            description=language['magicball_des_1'] if randball == 1 else False or language['magicball_des_2'] if randball == 2 else False or language['magicball_des_3'] if randball == 3 else False,
            color=Fun(ctx).color
        ))
