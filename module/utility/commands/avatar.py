import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_avatar(self, ctx: commands.Context, member: discord.Member):
        emb = discord.Embed(title=f"{Lang(ctx).language['avatar_title']} {member.name}",
                            color=self.bot.db_get_utilitycolor(ctx))
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)
