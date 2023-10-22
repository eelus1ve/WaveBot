import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class Avatar(commands.Cog):
    def __init__(self, bot: WaveBot, color):
        self.bot = bot
        self.color = color

    async def command_avatar(self, ctx: commands.Context, member: discord.Member):
        emb = discord.Embed(title=f"{Lang(ctx).language['avatar_title']} {member.name}",
                            color=self.color)
        emb.set_image(url=member.avatar)
        await ctx.send(embed=emb)
