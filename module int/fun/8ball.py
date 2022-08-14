import random
import json
import interactions
from bd import bdpy
class ballint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="Magicball",
        description="Бросить кости",
    )
    async def ball(self, ctx, *arg):
        COLOR = bdint(ctx)['COLOR']
        randball = random.randint(1, 3)
        if randball == 1:
            await ctx.send(embeds=interactions.Embed(
                title="Шар судьбы говорит: ",
                description="*Да!*",
                color=COLOR
            ))
        elif randball == 2:
            await ctx.send(embeds=interactions.Embed(
                title="Шар судьбы говорит: ",
                description="*Может быть.*",
                color=COLOR
            ))
        else:
            await ctx.send(embeds=interactions.Embed(
                title="Шар судьбы говорит: ",
                description="*Нет!*",
                color=COLOR
            ))

def setup(client):
    ballint(client)