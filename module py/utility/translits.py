import discord
from discord.ext import commands
from BD import bdpy

lst = [' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
lst1 = [' ', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.',]
class Translitspy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def tr(self, ctx, *arg):
        COLOR = bdpy(ctx)['COLOR']

        if arg:
            bf = []
            for ii in arg:
                bf.extend([ii[i] for i in range(len(ii))] + [' '])

            await ctx.send(embed=discord.Embed(
                title="Перевод: ",
                description=''.join([lst1[lst.index(i)] for i in bf]),
                color = COLOR
            ))
        
def setup(bot):
    bot.add_cog(Translitspy(bot))