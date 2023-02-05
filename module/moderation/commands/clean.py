import discord
from discord.ext import commands
from BTSET import Moderation

class Clean(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_clear(self, ctx: commands.Context, amount: int):
        if amount > 1000:
            raise commands.BadArgument(f'Количество удаленных сообщений не может превышать 1000')
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(
            title='Успешно',
            description=f"Очищено {amount} сообщений",
            color=Moderation(ctx.author).color
        ))