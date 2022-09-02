import discord
from BTSET import BOTVERSION
from discord.ext import commands
from BD import bdpy
class Infopy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases =['Инфо', 'инфо', 'ИНФО'])
    async def info(self, ctx): #и кста я сегодня пиццу ел!!! #молодец что пиццу ел а теперь мафию пиши
        COLOR = bdpy(ctx)['COLOR']
        emb = discord.Embed(title = f'{self.bot.user.name} BOT',
        description=f'Вас приветствует {self.bot.user.name} bot.', #Степа пиши свою хуйню сам
        color = COLOR)
        emb.set_thumbnail(url=self.bot.user.avatar_url)
        emb.add_field(name = 'Версия', value = str(BOTVERSION))
        emb.add_field(name = 'Создатели бота', value = '$DoNaT$#6442\n stёbo#6694\n ALT_F_400#1604')
        emb.set_footer(text='devepoled by the Wave team', icon_url = self.bot.user.avatar_url)
        '''добавить инфу по обратной связи'''
        await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Infopy(bot))