import discord
from discord import Spotify
from typing import Optional
from discord.ext import commands
from BD import bdpy
import pytz
class Sptfpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def spotify(self, ctx: commands.Context, user: Optional[discord.Member]):
        COLOR = bdpy(ctx)['COLOR']
        userr = user or ctx.author
        if userr.activities:
            for activity in userr.activities:
                if isinstance(activity, Spotify):
                    embed = discord.Embed(
                        title=f"{userr.name}'s Spotify",
                        description="Слушает {}".format(activity.title),
                        color=COLOR)#0x008000)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Исполнитель", value=activity.artist)
                    embed.add_field(name="Альбом", value=activity.album)
                    embed.set_footer(text=f"Песня началась в {activity.created_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%H:%M')}")
                    await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Sptfpy(bot))