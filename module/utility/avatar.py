import discord
from discord.ext import commands
from typing import Optional
from BTSET import bdpy

class Avatarpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def avatar(self, ctx: commands.Context, user: Optional[discord.Member]):
        COLOR = bdpy(ctx)['COLOR']
        userr = user or ctx.author
        emb = discord.Embed(title=f'Аватар {userr.name}',
                            color=COLOR
                            )
        emb.set_image(url=userr.avatar_url)
        await ctx.send(embed=emb)
def setup(bot):
    bot.add_cog(Avatarpy(bot))