import discord
import json
from discord.ext import commands
from typing import Optional
from distutils.log import error
import re
from discord.utils import get
import datetime
import pytz
import time
from BTSET import Score_presets, Rool, embpy, bdpy, BD

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

    #ПЕРЕПИСАТЬ ПОЛНОСТЬЮ!!!!!!!!!!!!!!!!!!!!!!!!
    async def command_score(self, ctx: commands.Context, mrr: discord.Member, arg: Optional[str]):
        try:
            with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
            moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d:%H:%M') 
            pref =  bdpy(ctx)['PREFIX']

            if not(arg):
                    await ctx.send(embed=discord.Embed(
                        title=f'Количество очков {mrr.name}',
                        description=f'{Score_presets(member=mrr).score}',
                        color=Score_presets(ctx).color
                    ))
            elif Rool(ctx).score:
                if arg.startswith('+'): #1 лвл не такой как все 0-199 200-299 разряд x2 на 1 лвл
                    argg = arg.replace('+', '')
                    if int(argg) < 10001 and arg != None:
                        
                        dermo = int(Score_presets(member=mrr).score) + int(argg)
                        Lvl1 = Score_presets(member=mrr).lvl-1
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
                            color=Score_presets(ctx).color
                        )
                        emb.set_footer(text=f'Модератор выдавший очки опыта участнику {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                        await get(ctx.guild.text_channels, id=int(Score_presets(member=mrr).idadminchannel)).send(embed=emb)
                        #====================================================================
                        #rep
                        #====================================================================
                        await ctx.send(embed=discord.Embed(
                            title='Успешно',
                            description=f'{mrr.name} получил {Score_commands.mes(argg)}!',
                            color=Score_presets(ctx).color
                        ))
                    else:
                        await ctx.send(embed=discord.Embed(
                            title='Ошибка',
                            description=f'Максимально количество выданого опыта не может привешать 10000!',
                            color=self.ercolor
                        ))

                elif arg.startswith('-'):
                    argg = arg.replace('-', '')
                    if int(argg) < 10001 and arg != None:
                        dermo = int(Score_presets(member=mrr).score) - int(argg)
                        Lvl1 = Score_presets(member=mrr).lvl-1
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
                                color=Score_presets(ctx).color
                            )
                            emb.set_footer(text=f'Модератор удаливший очки опыта участнику {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                            await get(ctx.guild.text_channels, id=int(Score_presets(member=mrr).idadminchannel)).send(embed=emb)
                            #====================================================================
                            #rep
                            #====================================================================
                            await ctx.send(embed=discord.Embed(
                                    title='Успешно',
                                    description=f'{mrr.name} потерял {Score_commands.mes(argg)}',
                                    color=Score_presets(ctx).color
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
                                color=Score_presets(ctx).color
                            )
                            emb.set_footer(text=f'Модератор удаливший очки опыта участнику {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                            await get(ctx.guild.text_channels, id=int(Score_presets(member=mrr).idadminchannel)).send(embed=emb)
                            #====================================================================
                            #rep
                            #====================================================================
                            await ctx.send(embed=discord.Embed(
                                    title='Успешно',
                                    description=f'{mrr.name} потерял {Score_commands.mes(argg)}!',
                                    color=Score_presets(ctx).color
                            ))
                            #====================================================================
                            #ls
                            #====================================================================
                    else:
                        await ctx.send(embed=discord.Embed(
                            title='Ошибка',
                            description=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)',
                            color=self.ercolor
                        ))

                elif not(arg.startswith('-') or arg.startswith('+')):
                    a = int(arg) + 0
                    newLvl = ((Score_presets(member=mrr).lvl*100)+arg)//100
                    xp = ((Score_presets(member=mrr).lvl*100)+arg) - newLvl*100
                    
                    data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(xp)
                    data[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(newLvl)
                        
                    #====================================================================
                    #audit
                    #====================================================================
                    emb=discord.Embed(
                        title='Установление очков опыта',
                        description=f'Учаснику {mrr.mention} было установлено {Score_commands.mes(argg)}',
                        timestamp=moscow_time,
                        color=Score_presets(ctx).color
                    )
                    emb.set_footer(text=f'Модератор исключивший участника {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
                    await get(ctx.guild.text_channels, id=int(Score_presets(member=mrr).idadminchannel)).send(embed=emb)
                    #====================================================================
                    #rep
                    #====================================================================
                    await ctx.send(embed=discord.Embed(
                        title='Успешно',
                        description=f'Участнику {mrr.name} было установлено {Score_commands.mes(argg)}!',
                        color=Score_presets(ctx).color
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
                
    async def command_clear_score(self, ctx: commands.Context, member: discord.Member):
        if Rool(ctx).setlvl:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            
            data[str(member.guild.id)]['USERS'][str(member.id)]['SCR'] = int(0)
            await embpy(ctx, comp='s', des=f'{member.name} потерял все очки!', time=10.00)
            with open(f'{BD}users.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            await embpy(ctx, comp='e', des=f'У вас недостаточно прав!', time=10.00)

    async def command_set_lvl(self, ctx: commands.Context, member: discord.Member, arg = None):
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            if not(int(arg)<0):
                data[str(member.guild.id)]['USERS'][str(member.id)]['LvL'] = int(arg)
                await ctx.send(embed=discord.Embed(
                    title=f'Успешно',
                    description=f'Участнику {member.name} был выдан {arg} уровень!',
                    color=Score_presets(ctx).color
                ))
            else:
                await ctx.send(embed=discord.Embed(
                    title=f'Ошибка',
                    description='Нельзя поставить лвл меньше или равный 0 ',
                    color=self.ercolor
                ))
            with open(f'{BD}users.json', 'w') as file:
                json.dump(data, file, indent=4)


    async def command_clear_rank(self, ctx: commands.Context, member: discord.Member):
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            
            data[str(member.guild.id)]['USERS'][str(member.id)]['LvL'] = 1
            data[str(member.guild.id)]['USERS'][str(member.id)]['SCR'] = 0
            await ctx.send(embed=discord.Embed(
                title=f'Успешно',
                description=f'Участник {member.name} отчистил свой ранк!',
                color=Score_presets(ctx).color
            ))
            with open(f'{BD}users.json', 'w') as file:
                json.dump(data, file, indent=4)


    # @clear_rank.error
    # async def error(self, ctx, error):
    #     with open(f'{BD}users.json', 'r') as file:
    #         data = json.load(file)
    #     if isinstance(error, commands.errors.MemberNotFound):
    #         found = re.findall(r'Member \s*"([^\"]*)"', str(error))
    #         if found == ["all"]:
    #             for member in ctx.guild.members:
    #                 data[str(member.guild.id)]['USERS'][str(member.id)]['LvL'] = 1
    #                 data[str(member.guild.id)]['USERS'][str(member.id)]['SCR'] = 0
    #             await ctx.send(embed=discord.Embed(
    #                 title=f'Успешно',
    #                 description=f'Все участники этого сервера потерял свой ранк!',
    #                 color=Score_presets(ctx).color
    #             ))
    #             with open(f'{BD}users.json', 'w') as file:
    #                 json.dump(data, file, indent=4)
    #         else:
    #             await ctx.send(embed=discord.Embed(
    #                 title="Ошибка",
    #                 description=f"*Участник `{''.join(found)}` не найден*",
    #                 color = self.ercolor
    #             ))

    async def command_voice_time(self, ctx: commands.Context, member: discord.Member):
        sec = bdpy(ctx)['USERS'][str(member.id)]['TIME']
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        emb = discord.Embed(
            title=f'Voice {member.name}',
            description=f'{int(hours)}:{int(mins)}:{sec}',
            color=Score_presets(ctx).color
        )
        await ctx.send(embed=emb)


class Score_listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def mbtime(member):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        endTime = time.time()
        sec = endTime - beforeTime[member.id]
        sec = round(sec, 2)
        data[str(member.guild.id)]['USERS'][str(member.id)]['TIME'] += sec
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)


    async def listener_score_on_voice_state_update(self, member: discord.Member, before, after):
        try:
            if before.channel and after.channel:
                if str(before.channel.id) != str(after.channel.id):
                    Score_listener.mbtime(member)
                    startTime = time.time()
                    beforeTime.update({member.id: startTime})
            elif before.channel and not(after.channel):
                Score_listener.mbtime(member)
            elif after.channel and not(before.channel):
                startTime = time.time()
                beforeTime.update({member.id: startTime})
        except Exception as ex:
            print(f'error eblan:\n{ex}')