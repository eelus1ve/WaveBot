import discord
from discord.ext import commands
from BTSET import BOTVERSION
from BD import bdpy
class Helppy(commands.Cog):

    help_dict = {
                'rand': 'рандомайзер',
                'info': 'Информация о боте',
                'warn': 'Выдать предупреждение',
                'unwarn': 'Убрать предупреждение',
                'clear_warns': 'Очистка предупреждений',
                'coin': 'Кинуть монетку',
                'ban': 'Забанить пользователя',
                'clear': 'Очистка чата',
                'kick': 'Кикнуть пользователя',
                'select': 'Выдача ролей',
                'join': 'Присоединение бота к голосовому чату',
                'play': 'Присоединение бота к голосовому чату',
                'start': 'Присоединение бота к голосовому чату',
                'stop': 'Присоединение бота к голосовому чату',
                'pause': 'Присоединение бота к голосовому чату',
                'spotify': 'Информация юзера о прослушивании spotify',
                'user': 'Информация о юзере',
                'MagicBall': 'Магический шар',
                'server_info': 'Информация о сервере',
                'mafia': 'Запустить мафию',
                'score': 'осмотреть счет учасника',
                'add_score': '',
                'remove_score': '',
                'clear_score': '',
                'tr': 'Перевести текст',
                'vote': 'Вызвать голосование',
                'rank': 'Показать ваш ранк на сервере',
                'settings': '***Параметры:*** \n\
                                add_class (название класса): Добавить класс с ролей\n\
                                remove_class (название класса): Удалить класс с ролями\n\
                                add_role (id роли) (название класса): Добавить роль в класс\n\
                                remove_role (id роли) (название класса): Удалить роль из класса\n\
                                color (Ваш цвет в HEX): Цвет обычных сообщений бота \n\
                                ercolor (Ваш цвет в HEX): Цвет сообщений с ошибками бота \n\
                                IDА (ID Админ чата): Добавляет ID Админ чата \n\
                                nCaps: Максимальное число капсов для предупреждения \n\
                                nWarns: Максимальное число варнов до бана \n\
                                add_badword (слово)\n\
                                remove_badword (слово котороe нужно исключить из списка плохих слов) \n\
                                selfroom (Id воис канала): Сделать комнату для создания личных каналов\n\
                                selftitle (Текст): Текст, который будет указан при выборе ролей \n\
                                join_message (Текмт): Изменить текст отправляемый учаснику при присоединении'
    }

    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases = ['хелп', 'Хелп', 'ХЕЛП'])
    async def help(self, ctx, *arg):
        COLOR = bdpy(ctx)['COLOR']
        pref = bdpy(ctx)['PREFIX']
        if (arg[0] if arg else False):
            await ctx.author.send(embed=discord.Embed(
                title=f'***{arg[0]}***',
                description=f"*Использование: {pref} {arg[0]}\n\
                    {Helppy.help_dict[arg[0]]}*",
                color=COLOR
            ))
            await ctx.send(embed=discord.Embed(
                title='Успешно',
                description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                color=COLOR
            ))

        else:
            emb = discord.Embed(title='*Список доступных команд:*',
            description = f'\n'.join([str(i) + ' - ' + str(Helppy.help_dict[i]) for i in Helppy.help_dict]),
            color=COLOR)
            await ctx.author.send(embed=emb)
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f'Список доступных комманд отправлен вам в личные сообщения!',
                color=COLOR
            ))

def setup(bot):
    bot.add_cog(Helppy(bot))
