from BTSET import ADMINS
import discord
import asyncio
from discord.ext import commands
from BD import bdpy
class Cleanpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['очистить', 'Очистить', 'ОЧИСТИТЬ'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        COLOR = bdpy(ctx)['COLOR']
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
        if amount <= 1000:
            await ctx.channel.purge(limit=int(amount))
            msg = await ctx.send(embed=discord.Embed(
                title="Очистка прошла успешно",
                description="*Очищено* " + str(amount) + " *сообщений*",
                color=COLOR
            ))
            
        else:
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*clear (количество до 1000 за 1 раз)*",
                color=ErCOLOR
            ))
        await asyncio.sleep(5)
        await msg.delete()
    @clear.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
            
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*clear (количество до 1000 за 1 раз)*",
                color=ErCOLOR
            ))
        elif isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))
        await asyncio.sleep(2)
        await msg.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear_channels(self, ctx):
        if ctx.author.id == ctx.guild.owner.id or ctx.author.id in ADMINS:
            guild = ctx.guild
            for channel in guild.channels:
                await channel.delete()
        else:
            ErCOLOR = bdpy(ctx)['ErCOLOR']
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Пошел нахуй!*",
                color=ErCOLOR
            ))
def setup(bot):
    bot.add_cog(Cleanpy(bot))