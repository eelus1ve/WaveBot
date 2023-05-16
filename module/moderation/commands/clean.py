import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_clear(self, ctx: commands.Context, amount: int):
        max_amount = 1000
        if amount > max_amount:
            raise commands.BadArgument('{} {}'.format(Lang(ctx).language['clear_er_mess'], max_amount))
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(
            title=Lang(ctx).language['clear_title'],
            description="{} {} {}".format(Lang(ctx).language['clear_des_1'], amount, Lang(ctx).language['clear_des_2']),
            color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="MODERATIONCOLOR")
        ))