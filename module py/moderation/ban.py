import discord
from discord.ext import commands
from distutils.log import error
from BD import bdpy
class Banpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['бан', 'Бан', 'БАН'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, reason = None):
        COLOR = bdpy(ctx)['COLOR']
        await member.ban(reason=reason)
        await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*{member.mention} был забанен !*",
                color=COLOR
            ))

    @ban.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*ban (@Участник)*",
                color = ErCOLOR
            ))
            
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color = ErCOLOR
            ))
            
def setup(bot):
    bot.add_cog(Banpy(bot))