import discord
from discord.ext import commands
from BTSET import Utility, Lang
class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_avatar(self, ctx: commands.Context, member: discord.Member):
        emb = discord.Embed(title=f"{Lang(ctx).language['avatar_title']} {member.name}", color=Utility(ctx).color)
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)