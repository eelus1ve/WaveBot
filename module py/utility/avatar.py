import discord
import json
from discord.ext import commands
from typing import Optional
class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def avatar(self, ctx: commands.Context, user: Optional[discord.Member]):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
        COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
        userr = user or ctx.author
        emb = discord.Embed(title=f'Аватар {userr.name}',
                            color=COLOR
                            )
        emb.set_image(url=userr.avatar_url)
        await ctx.send(embed=emb)
def setup(bot):
    bot.add_cog(Avatar(bot))