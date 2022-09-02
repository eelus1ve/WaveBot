from sqlite3 import Time
from time import time
from tkinter.tix import INTEGER
import discord
from discord.ext import commands
from distutils.log import error
from BD import bdpy
from typing import Optional
import datetime
import pytz
moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
class Banpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['бан', 'Бан', 'БАН'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, reason = None):
        COLOR = bdpy(ctx)['COLOR']
        await member.ban(reason=reason)
        
        #====================================================================
        #audit
        #====================================================================
        emb=discord.Embed(
            title='Блокировка участника',
            description=f'Учасник {member.name}#{memebr.discriminator} был заблокирован!\nПричина: {reason}',
            timestamp=moscow_time,
            color=COLOR
        )
        emb.set_footer(text=f'Модератор заблокировавший участника {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
        await get(message.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)
        #====================================================================
        #rep
        #====================================================================
        await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*{member.mention} был забанен !*",
                timestamp=moscow_time,
                color=COLOR
            ))
        #====================================================================
        #ls
        #====================================================================
        emb=discord.Embed(
            title='Вас заблокировали',
            description=f'Вы были заблокированы на сервере {ctx.guild.name}!\nПричина: {reason}',
            timestamp=moscow_time,
            color=COLOR
        )
        emb.set_footer(text=f'Модератор исключивший вас {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
        await member.send(embed=emb)
        #====================================================================


    # @commands.command(aliases=['бан', 'Бан', 'БАН'])
    # @commands.has_permissions(administrator=True)
    # async def ban(self, ctx, member: discord.Member, *reason):
    #     COLOR = bdpy(ctx)['COLOR']
    #     # await member.ban(reason=reason)
    #     await ctx.send(embed=discord.Embed(
    #             title="Успешно",
    #             description=f"*{member.mention} был забанен !*",
    #             color=COLOR
    #         ))
    #     if 'д' in str(reason[0]) or 'd' in str(reason[0]):
    #         [i for i in reason[0] if i.type == int]
        







    '''@ban.error
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
            ))'''
            
def setup(bot):
    bot.add_cog(Banpy(bot))