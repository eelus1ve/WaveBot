import interactions
from BD import bdint
from discord import Spotify
from typing import Optional
import pytz
class Spotifyint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="spotify",
        description="Узнать что слушает пользователь",
    )
    async def spotify(self, ctx: interactions.Context, user: Optional[interactions.Member]):
        COLOR = bdint(ctx)['COLOR']
        userr = user or ctx
        if userr.activities:
            for activity in userr.activities:
                if isinstance(activity, Spotify):
                    embed = interactions.Embed(
                        title=f"{userr.name}'s Spotify",
                        description="Слушает {}".format(activity.title),
                        color=COLOR)#0x008000)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Исполнитель", value=activity.artist)
                    embed.add_field(name="Альбом", value=activity.album)
                    embed.set_footer(text=f"Песня началась в {activity.created_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%H:%M')}")
                    await ctx.send(embeds=embed)
def setup(client):
    Spotifyint(client)