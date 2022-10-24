import discord
import random
from discord.ext import commands
from BTSET import bdpy

class Randpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases = ['ранд', 'РАНД', 'Ранд'])
    async def rand(self, ctx, arg = None, arg2 = None):
        COLOR = bdpy(ctx)['COLOR']
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']

        if arg and not(arg2):
            des=random.randint(0, int(arg))
        elif arg and arg2:
            des=random.randint(int(arg), int(arg2))
        elif not(arg):
            des=random.randint(0, 100)
        else:
            await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description=f'Использование {pref}rand (число1) [число2]\n\n\
                        Пример с одним числом: {pref}rand 100\n\
                            ┗Выведет рандомное число в пределах 100 \n\
                        Пример с двумя числами: {pref}rand 100 200\n\
                            ┗Выведет рандомное число от 100 до 200',
                    color = ErCOLOR,
                ))
        await ctx.send(embed=discord.Embed(
                    title="Ваше рандомное число: ",
                    description=des,
                    color = COLOR,
                ))

def setup(bot):
    bot.add_cog(Randpy(bot))

    