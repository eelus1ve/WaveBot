import discord
from discord.ext import commands
from distutils.log import error
from BD import bdpy
import datetime
import pytz
moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
class Kickpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['кик', 'Кик', 'КИК'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None, amount=1):
        COLOR = bdpy(ctx)['COLOR']
        #====================================================================
        #audit
        #====================================================================
        emb=discord.Embed(
            title='Исключение участника',
            description=f'Учасник {member.name}#{memebr.discriminator} был исключен!\nПричина: {reason}',
            timestamp=moscow_time,
            color=COLOR
        )
        emb.set_footer(text=f'Модератор исключивший участника {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
        await get(message.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)
        #====================================================================
        #rep
        #====================================================================
        await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*{member.mention} был кикнут!*",
                timestamp=moscow_time,
                color=COLOR
            ))
        #====================================================================
        #ls
        #====================================================================
        emb=discord.Embed(
            title='Вас исключили',
            description=f'Вы были исключены с сервера {ctx.guild.name}!\nПричина: {reason}',
            timestamp=moscow_time,
            color=COLOR
        )
        emb.set_footer(text=f'Модератор исключивший вас {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
        await member.send(embed=emb)
        #====================================================================
        await ctx.channel.purge(limit=int(amount))
        await member.kick(reason=reason)
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