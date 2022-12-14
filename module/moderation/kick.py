import discord
from discord.ext import commands
from distutils.log import error
from BTSET import embpy, bdpy
from discord.utils import get
import datetime
import pytz
moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
class Kickpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['кик', 'Кик', 'КИК'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason, amount=1):
        if bdpy(ctx)['ModRoles'] != {}:
            quest = bdpy(ctx)['ModRoles'][[str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0]]['Kick'] == "True" or ctx.author.guild_permissions.administrator
        else:
            quest = ctx.author.guild_permissions.administrator
        if quest:
            COLOR = bdpy(ctx)['COLOR']
            idAdminchennel = bdpy(ctx)['idAdminchennel']
            #====================================================================
            #audit
            #====================================================================
            if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
                emb=discord.Embed(
                    title='Исключение участника',
                    description=f'Учасник {member.name}#{member.discriminator} был исключен!\nПричина: {reason}',
                    timestamp=moscow_time,
                    color=COLOR
                )
                emb.set_footer(text=f'Модератор исключивший участника {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                await get(ctx.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)
            #====================================================================
            #rep
            #====================================================================
            await embpy(ctx, comp='s', des=f"*{member.mention} был кикнут!*", time=10.00)
                    
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
        else:
            await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
    @kick.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
            
        if isinstance(error, commands.MissingRequiredArgument):
            await embpy(ctx, comp='e', des=f"*Использование:* {pref}*kick (@Участник)*", time=10.00)
def setup(bot):
    bot.add_cog(Kickpy(bot))