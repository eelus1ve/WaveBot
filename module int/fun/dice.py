import random
import interactions
from BD import bdint

class Diceint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="dice",
        description="Бросить кости",
    )
    async def dice(self, ctx):
        COLOR = bdint(ctx)['COLOR']
            
        msg = await ctx.send(embeds=interactions.Embed(
                title="Игральная кость говорит:",
                description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                color = COLOR
            )
        )
        for i in range(5):
            await msg.edit(embeds=interactions.Embed(
                    title="Игральная кость говорит: ",
                    description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                    color=COLOR
                )
            )
def setup(client):
    Diceint(client)