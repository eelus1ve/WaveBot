import discord
from discord.ext import commands
from typing import Optional
import interactions
from BD import bdint
class Avatarint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="avatar",
        description="Показать аватар пользователя",
    )
    async def avatar(self, ctx: commands.Context, user: Optional[discord.Member]):
        COLOR = bdint(ctx)['COLOR']
        userr = user or ctx.author
        emb = interactions.Embed(title=f'Аватар {userr.name}',
                            color=COLOR
                            )
        emb.set_image(url=userr.avatar_url)
        await ctx.send(embeds=emb)
def setup(client):
    Avatarint(client)