from email.errors import InvalidMultipartContentTransferEncodingDefect
from turtle import title
from typing import Optional
import discord
import json
from discord.ext import commands
from discord.utils import get
from typing import Optional
import interactions
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption
import datetime
import pytz
from BTSET import embint, embpy, bdpy, bdint, BD
n = {}
class Warnspy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def warn(self, ctx: commands.Context, memberr: discord.Member, reason: str):
        try:
            if bdpy(ctx)['ModRoles'] != {}:
                quest = bdpy(ctx)['ModRoles'][[str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0]]['Warns']['Warn'] == "True" or ctx.author.guild_permissions.administrator
            else:
                quest = ctx.author.guild_permissions.administrator
            if quest:
                COLOR = bdpy(ctx)['COLOR']
                BADWORDS = bdpy(ctx)['BADWORDS']
                LINKS = bdpy(ctx)['LINKS']
                WARN = []
                WARN.extend(BADWORDS); WARN.extend(LINKS)
                warns = bdpy(ctx)['USERS'][str(memberr.id)]['WARNS']
                nWarns = bdpy(ctx)['nWarns']
                member = memberr
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] += 1
                #====================================================================
                #audit
                #====================================================================
                if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
                    emb = discord.Embed(
                        title='Нарушение',
                        description=f"*Ранее, у нарушителя было уже {data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
                        timestamp=ctx.message.created_at,
                        color=COLOR
                    )
                    emb.add_field(name='Канал:', value='Не определён', inline=True)
                    emb.add_field(name='Нарушитель:', value=member.mention, inline=True)
                    emb.add_field(name='Причина:', value=f'{reason}', inline=True)
                    emb.set_footer(text=f'Предупреждение выдано {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
                    await get(ctx.guild.text_channels, id=int(data[str(ctx.author.guild.id)]['idAdminchennel'])).send(embed=emb)
                #====================================================================
                #rep
                #====================================================================
                await ctx.message.reply(embed=discord.Embed(
                    title="Успешно",
                    description="*Предупреждение выдано*",
                    timestamp=ctx.message.created_at,
                    color=COLOR
                ), delete_after=10.0) 
                #====================================================================
                #ls
                #====================================================================
                emb=discord.Embed(
                    title='Нарушение',
                    description=f'Вы получили нарушение на сервере ***{ctx.guild.name}***\nПричина: {reason}',
                    timestamp=ctx.message.created_at,
                    color = COLOR
                )
                emb.add_field(name='Текущее кол-во нарушений', value=f'{warns}/{nWarns}', inline=True)
                emb.set_footer(text=f'Нарушение выдано {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
                await memberr.send(embed=emb)
                #====================================================================
                if data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] >= nWarns:
                    await member.ban(reason='Вы привысили допустимое количество нарушений')
                #====================================================================
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
        except:
            await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)


    #======================ERROR=======================================
    @warn.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await embpy(ctx, comp='e', des=f"*Использование: {pref}warn (@Участник) (Причина)", time=10.00)
                
    #======================ERROR=======================================

    @commands.command()
    async def unwarn(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        try:
            if bdpy(ctx)['ModRoles'] != {}:
                quest = bdpy(ctx)['ModRoles'][[str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0]]['Warns']['UnWarn'] == "True" or ctx.author.guild_permissions.administrator
            else:
                quest = ctx.author.guild_permissions.administrator
            if quest:
                member = memberr or ctx.author
                COLOR = bdpy(ctx)['COLOR']
                BADWORDS = bdpy(ctx)['BADWORDS']
                LINKS = bdpy(ctx)['LINKS']
                WARN = []
                WARN.extend(BADWORDS); WARN.extend(LINKS)
                nWarns = bdpy(ctx)['nWarns']
                warns = bdpy(ctx)['USERS'][str(memberr.id)]['WARNS']
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] -= 1
                #====================================================================
                #audit
                #====================================================================
                if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
                    emb = discord.Embed(
                        title='Нарушение снято!',
                        description=f"*Ранее, у участника было уже {data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
                        timestamp=ctx.message.created_at,
                        color=COLOR
                    )                                                                                                                   #переписать под unwarn
                    emb.add_field(name='Канал:', value='Не определён', inline=True)
                    emb.add_field(name='Участник:', value=member.mention, inline=True)
                    emb.set_footer(text=f'Предупреждение снято участником {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
                    await get(ctx.guild.text_channels, id=int(data[str(ctx.author.guild.id)]['idAdminchennel'])).send(embed=emb)
                #====================================================================
                #rep
                #==================================================================== 
                await embpy(ctx, comp='s', des="Предупреждение снято!", time=10.00)
                    
                #====================================================================
                #ls
                #====================================================================
                emb=discord.Embed(
                    title='Нарушение',
                    description=f'Вам было прощено нарушение!',
                    timestamp=ctx.message.created_at,
                    color = COLOR
                )
                emb.add_field(name='Текущее кол-во нарушений', value=f'{warns}/{nWarns}', inline=True)
                emb.set_footer(text=f'Нарушение снято учасником{ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
                await memberr.send(embed=emb)
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
        except:
            await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
        #====================================================================

    #======================ERROR=======================================
    @unwarn.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await embpy(ctx, comp='e', des=f"*Использование: {pref}unwarn (@Участник)", time=10.00)
                

    #======================ERROR=======================================

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear_warns(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        try:
            if bdpy(ctx)['ModRoles'] != {}:
                quest = bdpy(ctx)['ModRoles'][[str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0]]['Warns']['ClearWarn'] == "True" or ctx.author.guild_permissions.administrator
            else:
                quest = ctx.author.guild_permissions.administrator
            if quest:
                member = memberr or ctx.author
                COLOR = bdpy(ctx)['COLOR']
                BADWORDS = bdpy(ctx)['BADWORDS']
                LINKS = bdpy(ctx)['LINKS']
                WARN = []
                WARN.extend(BADWORDS); WARN.extend(LINKS)
                warns = bdpy(ctx)['USERS'][str(memberr.id)]['WARNS']
                nWarns = bdpy(ctx)['nWarns']
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] = 0
                #====================================================================
                #audit
                #====================================================================
                if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
                    emb = discord.Embed(
                        title='Нарушения очищены',
                        description=f"*Ранее, у нарушителя было уже {data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
                        timestamp=ctx.message.created_at,
                        color=COLOR
                    )                                                                                                               #переписать под clear_warn
                    emb.add_field(name='Канал:', value='Не определён', inline=True)
                    emb.add_field(name='Участник:', value=member.mention, inline=True)
                    emb.set_footer(text=f'Нарушения очищены учасником{ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
                    await get(ctx.guild.text_channels, id=int(data[str(ctx.author.guild.id)]['idAdminchennel'])).send(embed=emb)
                #====================================================================
                #rep
                #====================================================================
                await embpy(ctx, comp='s', des="Предупреждения сняты!", time=10.00)
                #====================================================================
                #ls
                #====================================================================
                emb=discord.Embed(
                    title='Нарушение',
                    description=f'С вас сняли все предупреждения!',
                    timestamp=ctx.message.created_at,
                    color = COLOR
                )
                emb.add_field(name='Текущее кол-во нарушений', value=f'{warns}/{nWarns}', inline=True)
                emb.set_footer(text=f'Нарушения сняты участником{ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
                await memberr.send(embed=emb)
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
        except:
            await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
            #====================================================================


    #======================ERROR=======================================
    @clear_warns.error
    async def error(self, ctx: commands.Context, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
        BADWORDS = bdpy(ctx)['BADWORDS']
        LINKS = bdpy(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await embpy(ctx, comp='e', des=f"*Использование: {pref}clear_warns (@Участник)", time=10.00)
                
            
    #======================ERROR=======================================

def setup(bot):
        bot.add_cog(Warnspy(bot))