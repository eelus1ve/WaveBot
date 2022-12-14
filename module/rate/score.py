import discord
import json
from discord.ext import commands
from typing import Optional
from distutils.log import error
import re
from discord.utils import get
import interactions
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption
import datetime
import pytz
from BTSET import embint, embpy, bdint, bdpy, BD

memberInfo = {}
beforeTime = {}

class Score_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def mes(argg):
        if int(str(argg)[-1]) == 1:
            reason = f'{argg} очко опыта'
        elif int(str(argg)[-1]) > 1 and int(str(argg)[-1]) < 5:
            reason = f'{argg} очка опыта'
        if int(str(argg)[-1]) == 0  or int(str(argg)[-1]) > 4:
            reason = f'{argg} очков опыта'
        return reason

    @commands.command() #ПЕРЕПИСАТЬ ПОЛНОСТЬЮ!!!!!!!!!!!!!!!!!!!!!!!!
    async def score(self, ctx: commands.Context, mr: Optional[discord.Member], arg: Optional[str]):
        try:
            if bdpy(ctx)['ModRoles'] != {}:
                quest = bdpy(ctx)['ModRoles'][str([str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0])]['Rate']['Score'] == "True" or ctx.author.guild_permissions.administrator
            else:
                quest = ctx.author.guild_permissions.administrator
            if quest:
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                mrr = mr or ctx.author
                moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d:%H:%M')
                COLOR = bdpy(ctx)['COLOR']
                ErCOLOR =  bdpy(ctx)['ErCOLOR']
                pref =  bdpy(ctx)['PREFIX']
                SCR =  bdpy(ctx)['USERS'][str(mrr.id)]['SCR']
                LVL =  bdpy(ctx)['USERS'][str(mrr.id)]['LvL']
                idAdminchennel = bdpy(ctx)['idAdminchennel']

                if not(arg):
                    await ctx.send(embed=discord.Embed(
                        title=f'Количество очков {mrr.name}',
                        description=f'{SCR}',
                        color=COLOR
                    ))
                elif arg.startswith('+'): #1 лвл не такой как все 0-199 200-299 разряд x2 на 1 лвл
                    argg = arg.replace('+', '')
                    if int(argg) < 10001 and arg != None:
                        
                        dermo = int(SCR) + int(argg)
                        Lvl1 = LVL-1
                        xp = (400+100*(Lvl1-1))/2*Lvl1 + dermo
                        d = (3**2+4*2*xp/100)**0.5
                        if (-3-d)/2 > (-3+d)/2:
                            level = (-3-d)/2
                        else:
                            level = (-3+d)/2
                        xpp = xp - (400+100*(int(level-1)))/2*int(level)
                        data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(xpp)
                        data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(level+1)
                        #====================================================================
                        #audit
                        #====================================================================
                        emb=discord.Embed(
                            title='Добавление очков опыта',
                            description=f'Учаснику {mrr.mention} было добавлено {Score_commands.mes(argg)}!',
                            timestamp=moscow_time,
                            color=COLOR
                        )
                        emb.set_footer(text=f'Модератор выдавший очки опыта участнику {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                        await get(ctx.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)
                        #====================================================================
                        #rep
                        #====================================================================
                        await ctx.send(embed=discord.Embed(
                            title='Успешно',
                            description=f'{mrr.name} получил {Score_commands.mes(argg)}!',
                            color=COLOR
                        ))
                    else:
                        await ctx.send(embed=discord.Embed(
                            title='Ошибка',
                            description=f'Максимально количество выданого опыта не может привешать 10000!',
                            color=ErCOLOR
                        ))

                elif arg.startswith('-'):
                    argg = arg.replace('-', '')
                    if int(argg) < 10001 and arg != None:
                        dermo = int(SCR) - int(argg)
                        Lvl1 = LVL-1
                        xp = (400+100*(Lvl1-1))/2*Lvl1 + dermo
                        d = (3**2+4*2*xp/100)**0.5
                        if (-3-d)/2 > (-3+d)/2:
                            level = (-3-d)/2
                        else:
                            level = (-3+d)/2
                        xpp = xp - (400+100*(int(level-1)))/2*int(level)
                        if str(level).startswith('-') or str(xpp).startswith('-'):
                            data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = 0
                            data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = 1
                            #====================================================================
                            #audit
                            #====================================================================
                            emb=discord.Embed(
                                title='Уадение очков опыта',
                                description=f'Учаснику {mrr.mention} было удалено {Score_commands.mes(argg)}',
                                timestamp=moscow_time,
                                color=COLOR
                            )
                            emb.set_footer(text=f'Модератор удаливший очки опыта участнику {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                            await get(ctx.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)
                            #====================================================================
                            #rep
                            #====================================================================
                            await ctx.send(embed=discord.Embed(
                                    title='Успешно',
                                    description=f'{mrr.name} потерял {Score_commands.mes(argg)}',
                                    color=COLOR
                            ))
                            #====================================================================
                            #ls
                            #====================================================================
                        else:
                            
                            data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(xpp)
                            data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(level+1)
                                
                            #====================================================================
                            #audit
                            #====================================================================
                            emb=discord.Embed(
                                title='Уадение очков опыта',
                                description=f'Учаснику {mrr.mention} было удалено {Score_commands.mes(argg)}',
                                timestamp=moscow_time,
                                color=COLOR
                            )
                            emb.set_footer(text=f'Модератор удаливший очки опыта участнику {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                            await get(ctx.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)
                            #====================================================================
                            #rep
                            #====================================================================
                            await ctx.send(embed=discord.Embed(
                                    title='Успешно',
                                    description=f'{mrr.name} потерял {Score_commands.mes(argg)}!',
                                    color=COLOR
                            ))
                            #====================================================================
                            #ls
                            #====================================================================
                    else:
                        await ctx.send(embed=discord.Embed(
                            title='Ошибка',
                            description=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)',
                            color=ErCOLOR
                        ))

                elif not(arg.startswith('-') or arg.startswith('+')):
                    a = int(arg) + 0
                    newLvl = ((LVL*100)+arg)//100
                    xp = ((LVL*100)+arg) - newLvl*100
                    
                    data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(xp)
                    data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(newLvl)
                        
                    #====================================================================
                    #audit
                    #====================================================================
                    emb=discord.Embed(
                        title='Установление очков опыта',
                        description=f'Учаснику {mrr.mention} было установлено {Score_commands.mes(argg)}',
                        timestamp=moscow_time,
                        color=COLOR
                    )
                    emb.set_footer(text=f'Модератор исключивший участника {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                    await get(ctx.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)
                    #====================================================================
                    #rep
                    #====================================================================
                    await ctx.send(embed=discord.Embed(
                        title='Успешно',
                        description=f'Участнику {mrr.name} было установлено {Score_commands.mes(argg)}!',
                        color=COLOR
                    ))
                    #====================================================================
                    #ls
                    #====================================================================

                else:
                    await embpy(ctx, comp='e', des=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)', time=10.00)
                        
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
        except:
            await embpy(ctx, comp='e', des=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)', time=10.00)
                
    @commands.command()
    async def clear_score(self, ctx: commands.Context, mr: Optional[discord.Member]):
        if bdpy(ctx)['ModRoles'] != {}:
            quest = bdpy(ctx)['ModRoles'][str([str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0])]['Rate']['ClearScore'] == "True" or ctx.author.guild_permissions.administrator
        else:
            quest = ctx.author.guild_permissions.administrator
        if quest:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            mrr = mr or ctx.author
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
            data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(0)
            await embpy(ctx, comp='s', des=f'{mrr.name} потерял все очки!', time=10.00)
            with open(f'{BD}users.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
    @commands.command()
    async def set_lvl(self, ctx: commands.Context, mr: Optional[discord.Member], arg = None):
        try:
            if bdpy(ctx)['ModRoles'] != {}:
                quest = bdpy(ctx)['ModRoles'][str([str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0])]['Rate']['SetLvl'] == "True" or ctx.author.guild_permissions.administrator
            else:
                quest = ctx.author.guild_permissions.administrator
            if quest:
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                mrr = mr or ctx.author
                
                COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
                if not(int(arg)<0):
                    data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(arg)
                    await ctx.send(embed=discord.Embed(
                        title=f'Успешно',
                        description=f'Участнику {mrr.name} был выдан {arg} уровень!',
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                        title=f'Ошибка',
                        description='Нельзя поставить лвл меньше или равный 0 ',
                        color=ErCOLOR
                    ))
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
        except:
            pass
    @commands.command()
    async def clear_rank(self, ctx: commands.Context, mr: Optional[discord.Member]):
        try:
            if bdpy(ctx)['ModRoles'] != {}:
                quest = bdpy(ctx)['ModRoles'][str([str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0])]['Rate']['CLearRank'] == "True" or ctx.author.guild_permissions.administrator
            else:
                quest = ctx.author.guild_permissions.administrator
            if quest:
                mrr = mr or ctx.author
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
                data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = 1
                data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = 0
                await ctx.send(embed=discord.Embed(
                    title=f'Успешно',
                    description=f'Участник {mrr.name} отчистил свой ранк!',
                    color=COLOR
                ))
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)
        except:
            pass
    @clear_rank.error
    async def error(self, ctx, error):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
        ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            
        if isinstance(error, commands.errors.MemberNotFound):
            found = re.findall(r'Member \s*"([^\"]*)"', str(error))
            if found == ["all"]:
                for member in ctx.guild.members:
                    data[str(member.guild.id)]['USERS'][str(member.id)]['LvL'] = 1
                    data[str(member.guild.id)]['USERS'][str(member.id)]['SCR'] = 0
                await ctx.send(embed=discord.Embed(
                    title=f'Успешно',
                    description=f'Все участники этого сервера потерял свой ранк!',
                    color=COLOR
                ))
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Участник `{''.join(found)}` не найден*",
                    color = ErCOLOR
                ))

    @commands.Cog.listener('on_voice_state_update')
    async def score_on_voice_state_update(self, member, before, after):
        try:
            moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d:%H:%M')
            guild = member.guild
            if after.channel.guild.id != before.channel.guild.id:
                
                reversed_beforeTime = str(beforeTime[str(member.id)]).split(':')
                reversed_NowTime = str(moscow_time).split(':')


                cum = 0

                for i in reversed_beforeTime:
                    if i == reversed_beforeTime[2]:
                       cum += int(i)/60
                    elif i == reversed_beforeTime[1]:
                        cum += int(i)
                    elif i == reversed_beforeTime[0]:
                        cum += int(i)*24

                for i in reversed_NowTime:
                    if i == reversed_NowTime[2]:
                       cum -= int(i)/60
                    elif i == reversed_NowTime[1]:
                        cum -= int(i)
                    elif i == reversed_NowTime[0]:
                        cum -= int(i)*24


                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                data[str(before.channel.guild.id)]['USERS'][str(member.id)]['TIME'] += cum
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
                
                beforeTime.pop(str(member.id))
                
                beforeTime.update({str(member.id): str(moscow_time)})
            
            elif str(after.channel.guild.id) == str(guild.id) and str(before.channel.guild.id) == str(guild.id):
                pass
                

            else:
                beforeTime.update({str(member.id): str(moscow_time)})
        
        except AttributeError:
            if after.channel == None:
                guild = member.guild
                reversed_beforeTime = str(beforeTime[str(member.id)]).split(':')
                reversed_NowTime = str(moscow_time).split(':')
                
                cum = 0
                for i in reversed_beforeTime:
                    if i == reversed_beforeTime[2]:
                        cum += int(i)/60
                    elif i == reversed_beforeTime[1]:
                        cum += int(i)
                    elif i == reversed_beforeTime[0]:
                        cum += int(i)*24
                
                for i in reversed_NowTime:
                    if i == reversed_NowTime[2]:
                        cum -= int(i)/60
                    elif i == reversed_NowTime[1]:
                        cum -= int(i)
                    elif i == reversed_NowTime[0]:
                        cum -= int(i)*24
                        
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                data[str(before.channel.guild.id)]['USERS'][str(member.id)]['TIME'] += cum
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
            else:
                print(f'HELLO ERROR || {member} || {before.channel} || {after.channel} || {member.guild}')
                beforeTime.update({str(member.id): str(moscow_time)})
                
def setup(bot):
        bot.add_cog(Score_commands(bot))
