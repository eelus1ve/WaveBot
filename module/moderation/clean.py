from BTSET import ADMINS, embpy, bdpy
import discord
import asyncio
from discord.ext import commands
class Cleanpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['очистить', 'Очистить', 'ОЧИСТИТЬ'])
    async def clear(self, ctx, amount: int):
        if bdpy(ctx)['ModRoles'] != {}:
            quest = bdpy(ctx)['ModRoles'][[str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0]]['Clear'] == "True" or ctx.author.guild_permissions.administrator
        else:
            quest = ctx.author.guild_permissions.administrator
        if quest:
            COLOR = bdpy(ctx)['COLOR']
            ErCOLOR = bdpy(ctx)['ErCOLOR']
            pref = bdpy(ctx)['PREFIX']
            if amount <= 1000:
                await ctx.channel.purge(limit=int(amount))
                await ctx.send(embed=discord.Embed(
                    title="Очистка прошла успешно",
                    description="*Очищено* " + str(amount) + " *сообщений*",
                    color=COLOR
                ), delete_after=10.0)
                
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Использование:* {pref}*clear (количество до 1000 за 1 раз)*",
                    color=ErCOLOR
                ), delete_after=10.0)
        else:
            await ctx.send(embpy(ctx, comp='e', des=f'У вас недостаточно прав!'), delete_after=10.0)
    @clear.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
            
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*clear (количество до 1000 за 1 раз)*",
                color=ErCOLOR
            ), delete_after=10.0)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ), delete_after=10.0)

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
                description="*Айай вводить такие команды!*",
                color=ErCOLOR
            ), delete_after=10.0)
def setup(bot):
    bot.add_cog(Cleanpy(bot))