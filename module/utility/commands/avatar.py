import discord
from discord.ext import commands
from typing import Optional
from BTSET import Utility
class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_avatar(self, ctx: commands.Context, member: discord.Member):
        emb = discord.Embed(title=f'Аватар {member.name}', color=Utility(ctx).color)
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)