import discord
from discord.ext import commands
from distutils.log import error
from BD import bdpy

class Kickpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['кик', 'Кик', 'КИК'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None, amount=1):
        COLOR = bdpy(ctx)['COLOR']
        await ctx.channel.purge(limit=int(amount))
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*{member.mention} был кикнут!*",
                color=COLOR
            ))
    @kick.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']

            
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*kick (@Участник)*",
                color = ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color = ErCOLOR
            ))
def setup(bot):
    bot.add_cog(Kickpy(bot))