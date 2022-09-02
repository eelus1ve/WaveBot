from discord import Spotify
from typing import Optional
from BTSET import ADMINS
import pytz
import interactions
from BD import bdint
import discord

class Userint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="user",
        description="abrakodabra",
        options= [
        {
            "name": "user",
            "description": "Serch animal",
            "type": 6,
            "required": True
        }]
    )
    async def user(self, ctx, user: interactions.Member):
        
        await ctx.send(embeds=emb)

def setup(client):
    Userint(client) 