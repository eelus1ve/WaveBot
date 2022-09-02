import random
import interactions
from BD import bdint

class Randdint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="rand",
        description="Получить случайное число",
    )
    async def rand(self, ctx: interactions.CommandContext, arg = None, arg2 = None):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']

        if arg and not(arg2):
            des=random.randint(0, int(arg))
        elif arg and arg2:
            des=random.randint(int(arg), int(arg2))
        elif not(arg):
            des=random.randint(0, 100)
        else:
            await ctx.send(embeds=interactions.Embed(
                    title="Ошибка",
                    description=f'Использование {pref}rand (число1) [число2]\n\n\
                        Пример с одним числом: {pref}rand 100\n\
                            ┗Выведет рандомное число в пределах 100 \n\
                        Пример с двумя числами: {pref}rand 100 200\n\
                            ┗Выведет рандомное число от 100 до 200',
                    color = ErCOLOR,
                ))
        await ctx.send(embeds=interactions.Embed(
                    title="Ваше рандомное число: ",
                    description=des,
                    color = COLOR,
                ))
def setup(bot):
    Randdint(bot)

    