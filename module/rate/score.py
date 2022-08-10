import discord
import json
from discord.ext import commands
from typing import Optional
from distutils.log import error
import re
class Score(commands.Cog):
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

            elif arg.startswith('+'):
                argg = arg.replace('+', '')
                if int(argg) < 10001 and arg != None:
                    dermo = int(SCR) + int(argg)
                    if int(dermo+SCR) >= ((int(LVL)+1)*100):
                        print((LVL*100+dermo)//100)#дописать формулу
                        with open('users.json', 'w') as file:
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = 1#подставиить переменую
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] = 1#подставиить переменую
                            json.dump(dataServerID, file, indent=4)
                            
                        await ctx.send(embed=discord.Embed(
                            title='Успешно',
                            description=f'{mrr.name} получил {argg} очков!',
                            color=COLOR
                        ))
                    else:
                        with open('users.json', 'w') as file:
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(dermo) 
                            json.dump(dataServerID, file, indent=4)
                            
                        await ctx.send(embed=discord.Embed(
                            title='Успешно',
                            description=f'{mrr.name} получил {argg} очков!',
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
                    if dermo<0:
                        res = ((int(LVL)+1)*100) - dermo
                        with open('users.json', 'w') as file:
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = res
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['LvL'] -= 1
                            json.dump(dataServerID, file, indent=4)
                    else:
                        with open('users.json', 'w') as file:
                            dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(dermo) 
                            json.dump(dataServerID, file, indent=4)
                    await ctx.send(embed=discord.Embed(
                        title='Успешно',
                        description=f'{mrr.name} потерял {argg} очков!',
                        color=COLOR
                    ))
                else:
                    await ctx.send(embed=discord.Embed(
                            title='Ошибка',
                            description=f'Использование: {pref}remove_score (@Учасник) +/-(кол-во опыта)',
                            color=ErCOLOR
                        ))

            elif not(arg.startswith('-') or arg.startswith('+')):
                a = int(arg) + 0
                with open('users.json', 'w') as file:
                    dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(a)
                    json.dump(dataServerID, file, indent=4)
                await ctx.send(embed=discord.Embed(
                        title='Успешно',
                        description=f'Участнику {mrr.name} было установлено {int(a)} опыта!',
                        color=COLOR
                    ))

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
def setup(bot):
    bot.add_cog(Score(bot))