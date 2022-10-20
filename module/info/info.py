import discord
from BTSET import BOTVERSION, ADMINS
from discord.ext import commands
from BD import bdpy
class Infopy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases =['Инфо', 'инфо', 'ИНФО'])
    async def info(self, ctx): #и кста я сегодня пиццу ел!!! #молодец что пиццу ел а теперь мафию пиши
        COLOR = bdpy(ctx)['COLOR']
        devlist = []
        for i in ADMINS:
            devlist.append(f'{self.bot.get_user(int(i)).name}#{self.bot.get_user(int(i)).discriminator}')
        emb = discord.Embed(title = f'{self.bot.user.name} BOT',
        description=f'Вас приветствует {self.bot.user.name} bot.', #Степа пиши свою хуйню сам
        color = COLOR)
        emb.set_thumbnail(url=self.bot.user.avatar_url)
        emb.add_field(name = 'Версия', value = str(BOTVERSION))
        emb.add_field(name = 'Создатели бота', value = '\n'.join(devlist))
        emb.set_footer(text='devepoled by the Wave team', icon_url = self.bot.user.avatar_url)
        '''добавить инфу по обратной связи'''
        await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Infopy(bot))