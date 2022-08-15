import discord
import json
from discord.ext import commands
from typing import Optional
from distutils.log import error
import re
import interactions
from BD import bdint
class Scoreint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="score",
        description="Взаимодействие с очками",
    )
    async def score(self, ctx: interactions.context, mr: Optional[interactions.Member], arg: Optional[str]):
        try:
            mrr = mr or ctx.author
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            COLOR = bdint(ctx)['COLOR']
            ErCOLOR = bdint(ctx)['ErCOLOR']
            pref = bdint(ctx)['PREFIX']
            SCR = bdint(ctx)['USERS'][str(mrr.id)]['SCR']
            LVL = bdint(ctx)['USERS'][str(mrr.id)]['LvL']

            if not(arg):
                await ctx.send(embeds=interactions.Embed(
                    title=f'Количество очков {mrr.name}',
                    description=f'{SCR}',
                    color=COLOR
                ))
        #F
            elif arg.startswith('+'): #1 лвл не такой как все 0-199 200-299 разряд x2 на 1 лвл
                argg = arg.replace('+', '')
                if int(argg) < 10001 and arg != None:
                    if LVL == 1:
                        pass
                    else:
                        dermo = int(SCR) + int(argg)
                        newLvl = ((LVL*100)+dermo)-(LVL+1)*100
                        xp = ((LVL*100)+dermo) - (newLvl//100+LVL)*100
                        if newLvl > LVL*100:
                            with open('users.json', 'w') as file:
                                bdint(ctx)['USERS'][str(mrr.id)]['SCR'] = xp
                                bdint(ctx)['USERS'][str(mrr.id)]['LvL'] = newLvl//100
                                json.dump(dataServerID, file, indent=4)
                            await ctx.send(embeds=interactions.Embed(
                                title='Успешно',
                                description=f'{mrr.name} получил {argg} очков!',
                                color=COLOR
                            ))
                        else:
                            with open('users.json', 'w') as file:
                                bdint(ctx)[str(mrr.id)]['SCR'] = int(dermo) 
                                json.dump(dataServerID, file, indent=4)
                                
                            await ctx.send(embeds=interactions.Embed(
                                title='Успешно',
                                description=f'{mrr.name} получил {argg} очков!',
                                color=COLOR
                            ))
                else:
                    await ctx.send(embeds=interactions.Embed(
                        title='Ошибка',
                        description=f'Максимально количество выданого опыта не может привешать 10000!',
                        color=ErCOLOR
                    ))

            elif arg.startswith('-'):
                argg = arg.replace('-', '')
                if int(argg) < 10001 and arg != None:
                    dermo = int(SCR) - int(argg)
                    if dermo<0:
                        newLvl = ((LVL*100)+dermo)//100
                        xp = ((LVL*100)+dermo) - newLvl*100
                        with open('users.json', 'w') as file:
                            bdint(ctx)['USERS'][str(mrr.id)]['SCR'] = xp
                            bdint(ctx)['USERS'][str(mrr.id)]['LvL'] = newLvl
                            json.dump(dataServerID, file, indent=4)
                    else:
                        with open('users.json', 'w') as file:
                            bdint(ctx)['USERS'][str(mrr.id)]['SCR'] = int(dermo) 
                            json.dump(dataServerID, file, indent=4)
                    await ctx.send(embeds=interactions.Embed(
                        title='Успешно',
                        description=f'{mrr.name} потерял {argg} очков!',
                        color=COLOR
                    ))
                else:
                    await ctx.send(embeds=interactions.Embed(
                            title='Ошибка',
                            description=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)',
                            color=ErCOLOR
                        ))

            elif not(arg.startswith('-') or arg.startswith('+')):
                a = int(arg) + 0
                if arg>= (LVL+1)*100:
                    newLvl = ((LVL*100)+arg)//100
                    xp = ((LVL*100)+arg) - newLvl*100
                    with open('users.json', 'w') as file:
                        bdint(ctx)['USERS'][str(mrr.id)]['SCR'] = int(xp)
                        bdint(ctx)['USERS'][str(mrr.id)]['LvL'] = int(newLvl)
                        json.dump(dataServerID, file, indent=4)
                    await ctx.send(embeds=interactions.Embed(
                            title='Успешно',
                            description=f'Участнику {mrr.name} было установлено {int(a)} опыта!',
                            color=COLOR
                        ))
                else:
                    with open('users.json', 'w') as file:
                        bdint(ctx)['USERS'][str(mrr.id)]['SCR'] = int(a)
                        json.dump(dataServerID, file, indent=4)
                    await ctx.send(embeds=interactions.Embed(
                            title='Успешно',
                            description=f'Участнику {mrr.name} было установлено {int(a)} опыта!',
                            color=COLOR
                        ))

            else:
                await ctx.send(embeds=interactions.Embed(
                    title='Ошибка',
                    description=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)',
                    color=ErCOLOR
                ))
        except:
            await ctx.send(embeds=interactions.Embed(
                    title='Ошибка',
                    description=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)',
                    color=ErCOLOR
                ))
    @interactions.extension_command(
        name="clear score",
        description="Очистить очки",
    )
    async def clear_score(self, ctx: interactions.context, mr: Optional[interactions.Member]):
        mrr = mr or ctx.author
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
        COLOR = bdint(ctx)['COLOR']
        with open('users.json', 'w') as file:
            bdint(ctx)['USERS'][str(mrr.id)]['SCR'] = int(0)
            json.dump(dataServerID, file, indent=4)
        await ctx.send(embeds=interactions.Embed(
            title='Успешно',
            description=f'{mrr.name} потерял все очки!',
            color=COLOR
        ))
    @interactions.extension_command(
        name="Set lvl",
        description="Установить лвл",
    )
    async def set_lvl(self, ctx: interactions.context, mr: Optional[interactions.Member], arg = None):
        try:
            mrr = mr or ctx.author
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            COLOR = bdint(ctx)['COLOR']
            ErCOLOR = bdint(ctx)['ErCOLOR']
            if not(int(arg)<0):
                with open('users.json', 'w') as file:
                    bdint(ctx)['USERS'][str(mrr.id)]['LvL'] = int(arg)
                    json.dump(dataServerID, file, indent=4)
                await ctx.send(embeds=interactions.Embed(
                    title=f'Успешно',
                    description=f'Участнику {mrr.name} был выдан {arg} уровень!',
                    color=COLOR
                ))
            else:
                await ctx.send(embeds=interactions.Embed(
                    title=f'Ошибка',
                    description='Нельзя поставить лвл меньше или равный 0 ',
                    color=ErCOLOR
                ))
        except:
            pass
    @interactions.extension_command(
        name="clear rank",
        description="Отчистить ранк",
    )
    async def clear_rank(self, ctx: interactions.context, mr: Optional[interactions.Member]):
        try:
            mrr = mr or ctx.author
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
            COLOR = bdint(ctx)['COLOR']
            with open('users.json', 'w') as file:
                bdint(ctx)['USERS'][str(mrr.id)]['LvL'] = 1
                bdint(ctx)['USERS'][str(mrr.id)]['SCR'] = 0
                json.dump(dataServerID, file, indent=4)
            await ctx.send(embeds=interactions.Embed(
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
            COLOR = bdint(ctx)['COLOR']
            ErCOLOR = bdint(ctx)['ErCOLOR']
            
        if isinstance(error, commands.errors.MemberNotFound):
            found = re.findall(r'Member \s*"([^\"]*)"', str(error))
            if found == ["all"]:
                for member in ctx.guild.members:
                        with open('users.json', 'w') as file:
                            bdint(ctx)[str(member.id)]['LvL'] = 1
                            bdint(ctx)['USERS'][str(member.id)]['SCR'] = 0
                            json.dump(dataServerID, file, indent=4)
                await ctx.send(embeds=interactions.Embed(
                    title=f'Успешно',
                    description=f'Все участники этого сервера потерял свой ранк!',
                    color=COLOR
                ))
            else:
                await ctx.send(embeds=interactions.Embed(
            title="Ошибка",
            description=f"*Участник `{''.join(found)}` не найден*",
            color = ErCOLOR
        ))
def setup(client):
    Scoreint(client)