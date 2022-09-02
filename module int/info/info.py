from BTSET import BOTVERSION
import interactions
from BD import bdint

class Infoint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="info",
        description="Узнать информацию о боте",
    )
    async def info(self, ctx): #и кста я сегодня пиццу ел!!! #молодец что пиццу ел а теперь мафию пиши
        COLOR = bdint(ctx)['COLOR']
        emb = interactions.Embed(title = f'{self.bot.user.name} BOT',
        description=f'Вас приветствует {self.bot.user.name} bot.', #Степа пиши свою хуйню сам
        color = COLOR)
        emb.set_thumbnail(url=self.bot.user.avatar_url)
        emb.add_field(name = 'Версия', value = str(BOTVERSION))
        emb.add_field(name = 'Создатели бота', value = '$DoNaT$#6442\n stёbo#6694\n ALT_F_400#1604')
        emb.set_footer(text='devepoled by the Wave team', icon_url = self.bot.user.avatar_url)
        '''добавить инфу по обратной связи'''
        await ctx.send(embeds = emb)

def setup(client):
    Infoint(client)