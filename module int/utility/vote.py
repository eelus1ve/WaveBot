from discord.ext import commands
import interactions
from BD import bdint
class Voteint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="vote",
        description="Начать голосование",
    )
    async def vote(self, ctx, *arg):
        COLOR = bdint(ctx)['COLOR']

        em = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣⃣', '7️⃣', '8️⃣', '9️⃣', '0️⃣']
        arg = ''.join(arg)
        arg = arg.split(';')
        title = []
        title.append(arg.pop(0))
        e = 0
        for i in arg:
            title.append('\n' + str(em[e]) + ' ' + str(i))
            e += 1
        ms = await ctx.send(embeds=interactions.Embed(title=title.pop(0), description=''.join(title), color = COLOR))
        
        for i in range(len(title)):
            await ms.add_reaction(em[i])

def setup(client):
        Voteint(client)