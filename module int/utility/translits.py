import discord
import json
from discord.ext import commands
import interactions
from BD import bdint
lst = [' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
lst1 = [' ', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.',]
class Transint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="translit",
        description="Перевести текст на русский",
    )
    async def tr(self, ctx, *arg):
        COLOR = bdint(ctx)['COLOR']

        if arg:
            bf = []
            for ii in arg:
                bf.extend([ii[i] for i in range(len(ii))] + [' '])

            await ctx.send(embeds=interactions.Embed(
                title="Перевод: ",
                description=''.join([lst1[lst.index(i)] for i in bf]),
                color = COLOR
            ))
        
def setup(client):
    Transint(client)