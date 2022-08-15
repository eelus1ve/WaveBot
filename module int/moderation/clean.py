from BTSET import ADMINS
import discord
import asyncio
from discord.ext import commands
import interactions
from BD import bdint
class Cleanint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name='clear',
        description='Очистить чат'
    )
    async def clear(self, ctx, amount: int):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']
        if amount <= 1000:
            await ctx.channel.purge(limit=int(amount))
            msg = await ctx.send(embeds=interactions.Embed(
                title="Очистка прошла успешно",
                description="*Очищено* " + str(amount) + " *сообщений*",
                color=COLOR
            ))
            
        else:
            msg = await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*clear (количество до 1000 за 1 раз)*",
                color=ErCOLOR
            ))
        await asyncio.sleep(5)
        await msg.delete()
    @clear.error
    async def error(self, ctx, error):
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']
            
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*clear (количество до 1000 за 1 раз)*",
                color=ErCOLOR
            ))
        elif isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))
        await asyncio.sleep(2)
        await msg.delete()

    @interactions.extension_command(
        name='clear channels',
        description='Удалить все чаты'
    )
    async def clear_channels(self, ctx):
        if ctx.author.id == ctx.guild.owner.id or ctx.author.id in ADMINS:
            guild = ctx.guild
            for channel in guild.channels:
                await channel.delete()
        else:
            ErCOLOR = bdint(ctx)['ErCOLOR']
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*Пошел нахуй!*",
                color=ErCOLOR
            ))
def setup(client):
    Cleanint(client)