import discord
import json
from discord.ext import commands
from typing import Optional
from distutils.log import error
import re
import interactions
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption
import datetime
import pytz
moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
from BD import bdint
from BTSET import embint
n = {}
class Score_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def score(self, ctx: commands.Context, mr: Optional[discord.Member], arg: Optional[str]):
        try:
            mrr = mr or ctx.author
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
            SCR = dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR']
            LVL = dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL']

            if not(arg):
                await ctx.send(embed=discord.Embed(
                    title=f'Количество очков {mrr.name}',
                    description=f'{SCR}',
                    color=COLOR
                ))
        #F
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
                    with open('users.json', 'w') as file:
                        dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(xpp)
                        dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(level+1)
                        json.dump(dataServerID, file, indent=4)
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
                        title='Успешно',
                        description=f'{mrr.name} получил {argg} очков!',
                        color=COLOR
                    ))
                    #====================================================================
                    #ls
                    #====================================================================
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
                        with open('users.json', 'w') as file:
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = 0
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = 1
                            json.dump(dataServerID, file, indent=4)
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
                                title='Успешно',
                                description=f'{mrr.name} потерял {argg} очков!',
                                color=COLOR
                        ))
                        #====================================================================
                        #ls
                        #====================================================================
                    else:
                        with open('users.json', 'w') as file:
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(xpp)
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(level+1)
                            json.dump(dataServerID, file, indent=4)
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
                                title='Успешно',
                                description=f'{mrr.name} потерял {argg} очков!',
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
                with open('users.json', 'w') as file:
                    dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(xp)
                    dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(newLvl)
                    json.dump(dataServerID, file, indent=4)
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
                    title='Успешно',
                    description=f'Участнику {mrr.name} было установлено {int(a)} опыта!',
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
        except:
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)',
                color=ErCOLOR
            ))
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear_score(self, ctx: commands.Context, mr: Optional[discord.Member]):
        mrr = mr or ctx.author
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
        COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
        with open('users.json', 'w') as file:
            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(0)
            json.dump(dataServerID, file, indent=4)
        await ctx.send(embed=discord.Embed(
            title='Успешно',
            description=f'{mrr.name} потерял все очки!',
            color=COLOR
        ))
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def set_lvl(self, ctx: commands.Context, mr: Optional[discord.Member], arg = None):
        try:
            mrr = mr or ctx.author
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            if not(int(arg)<0):
                with open('users.json', 'w') as file:
                    dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = int(arg)
                    json.dump(dataServerID, file, indent=4)
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
        except:
            pass
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear_rank(self, ctx: commands.Context, mr: Optional[discord.Member]):
        try:
            mrr = mr or ctx.author
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            with open('users.json', 'w') as file:
                dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = 1
                dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = 0
                json.dump(dataServerID, file, indent=4)
            await ctx.send(embed=discord.Embed(
                title=f'Успешно',
                description=f'Участник {mrr.name} отчистил свой ранк!',
                color=COLOR
            ))
        except:
            pass
    @clear_rank.error
    async def error(self, ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            
        if isinstance(error, commands.errors.MemberNotFound):
            found = re.findall(r'Member \s*"([^\"]*)"', str(error))
            if found == ["all"]:
                for member in ctx.guild.members:
                        with open('users.json', 'w') as file:
                            dataServerID[str(member.guild.id)]['USERS'][str(member.id)]['LvL'] = 1
                            dataServerID[str(member.guild.id)]['USERS'][str(member.id)]['SCR'] = 0
                            json.dump(dataServerID, file, indent=4)
                await ctx.send(embed=discord.Embed(
                    title=f'Успешно',
                    description=f'Все участники этого сервера потерял свой ранк!',
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f"*Участник `{''.join(found)}` не найден*",
                    color = ErCOLOR
                ))


class Score_interactions(interactions.Extension):
    def __init__(self, client):
        self.client = client
    
    @interactions.extension_user_command(
        name='score'
    )
    async def score_int(self, ctx: interactions.CommandContext):
        n.update({str(ctx.author.id): [str(ctx.target.user.id), str(ctx.target.name)]})
        await ctx.popup(Modal(
                custom_id='Score',
                title=' ',
                components=[
                    TextInput(
                        style=TextStyleType.SHORT,
                        custom_id='qwertyuiop',
                        label='укажите знак(+/-) и кол-во очков',
                        min_length=2,
                        max_length=5
                    )
                ]
            ))
    
    @interactions.extension_modal('Score')
    async def scrya(self, ctx: interactions.CommandContext, shrt):
        print(ctx.author.avatar)
        with open('users.json', 'r') as file:
            data = json.load(file)
        SCR = bdint(ctx)['USERS'][str(n[str(ctx.author.id)][0])]['SCR']
        LVL = bdint(ctx)['USERS'][str(n[str(ctx.author.id)][0])]['LvL']
        if str(shrt).startswith('+'):
            argg = str(shrt).replace('+', '')
            dermo = int(SCR) + int(argg)
            Lvl1 = LVL-1
            xp = (400+100*(Lvl1-1))/2*Lvl1 + dermo
            d = (3**2+4*2*xp/100)**0.5
            if (-3-d)/2 > (-3+d)/2:
                level = (-3-d)/2
            else:
                level = (-3+d)/2
            xpp = xp - (400+100*(int(level-1)))/2*int(level)
            with open('users.json', 'w') as file:
                data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['SCR'] = int(xpp)
                data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['LvL'] = int(level+1)
                json.dump(data, file, indent=4)
            await ctx.send(embeds = embint(ctx, comp='s', des=f'Участник {str(n[str(ctx.author.id)][1])} получил {argg}'))
        elif str(shrt).startswith('-'):
            argg = str(shrt).replace('-', '')
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
                with open('users.json', 'w') as file:
                    data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['SCR'] = 0
                    data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['LvL'] = 1
                    json.dump(data, file, indent=4)
            else:
                with open('users.json', 'w') as file:
                    data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['SCR'] = int(xpp)
                    data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['LvL'] = int(level+1)
                    json.dump(data, file, indent=4)
            await ctx.send(embeds = embint(ctx, comp='s', des=f'Участник {str(n[str(ctx.author.id)][1])} получил {argg}'), ephemeral=True)
        else:
            await ctx.send(embeds = embint(ctx, comp='e', des=f'укажите знак(+/-) и кол-во очков'), ephemeral=True)
        for i in [k for k in n.keys()]:
            if i == str(ctx.author.id):
                n.pop(i)
def setup(bot):
    if str(bot).startswith('<d'):
        bot.add_cog(Score_commands(bot))
    elif str(bot).startswith('<i'):
        Score_interactions(bot)
