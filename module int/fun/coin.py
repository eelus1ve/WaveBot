import random
import interactions
from BD import bdint
class Coinint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="coin",
        description="Подбросить монетку",
    )
    async def coin(self, ctx, *arg):
        COLOR = bdint(ctx)['COLOR']
        if random.randint(1, 2) == 1:
            await ctx.send(embeds=interactions.Embed(
                title="Выпал: ",
                description="*Орел*",
                color=COLOR
            ))
        else:
            await ctx.send(embeds=interactions.Embed(
                title="Выпала: ",
                description="*Решка*",
                color=COLOR
            ))

def setup(client):
    Coinint(client)

