import discord
from discord.ext import commands
from system.Bot import WaveBot

lst = [' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
lst1 = [' ', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.',]


class Translits(commands.Cog):
    def __init__(self, bot: WaveBot, color):
        self.bot = bot
        self.color = color

    async def command_tr(self, ctx: commands.Context, arg):
        if arg:
            bf = []
            for ii in arg:
                bf.extend([ii[i] for i in range(len(ii))] + [' '])

            await ctx.send(embed=discord.Embed(
                title="Перевод: ",
                description=''.join([lst1[lst.index(i)] for i in bf]),
                color=self.color
            ))