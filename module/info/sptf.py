import discord
from discord import Spotify
import json
from discord.ext import commands

class sptf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
        with open('users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            
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
                    embed.set_footer(text="Песня началась в {}".format(activity.created_at.strftime("%H:%M")))
                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(sptf(bot))

    