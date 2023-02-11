import discord
from discord.ext import commands
from BTSET import Moderation, Lang

class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_clear(self, ctx: commands.Context, amount: int):
        max_amount = 1000
        if amount > max_amount:
            raise commands.BadArgument('{} {}'.format(Lang(ctx).language['clear_er_mess'], max_amount))
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(
            title=Lang(ctx).language['clear_title'],
            description="{} {} {}".format(Lang(ctx).language['clear_des_1'], amount, Lang(ctx).language['clear_des_2']),
            color=Moderation(ctx.author).color
        ))