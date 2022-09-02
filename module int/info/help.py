from BTSET import BOTVERSION
import interactions
from BD import bdint

class Helpint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="help",
        description="Отправит все команды и информацию по использованию их",
    )
    async def help(self, ctx, *arg):
        COLOR = bdint(ctx)['COLOR']
        pref = bdint(ctx)['PREFIX']
        if arg:
            if arg[0] == 'rand':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]}\n\
                        Генерирует случайное число*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------------
            elif arg[0] == 'info':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} \n\
                        Информация о боте*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------------
            elif arg[0] == 'warn':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref}{arg[0]} (@Учасник) (Причина) \n\
                        Выдать предупреждение пользователю",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------------
            elif arg[0] == 'coin':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} \n\
                        Подбросить монетку*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
                #------------------------------------------------------------------
            elif arg[0] == 'ban':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} (@Учасник)\n\
                        Забанить человека*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'clear':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} (кол-во сообщений от 1 до 1000)\n\
                        Отчистить чат на какое-то количество сообщений*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'kick':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} (@Учасник)\n\
                        Кикнуть пользователя*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #---------------------------------------------------------------------
            elif arg[0] == 'select':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} (класс) \n\
                        Выдача ролей \n\
                            Настраивать через {pref}settings*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #--------------------------------------------------------------------
            elif arg[0] == 'join':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} ||Временно бессмысленно|| \n\
                        Бот присоединяется к вашему воис чату*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-------------------------------------------------------------------
            elif arg[0] == 'spotify':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} (@Участник) \n\
                        Показывает что слушает пользователь*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #------------------------------------------------------------------
            elif arg[0] == 'user':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} (@Учасник) \n\
                        Информация об учснике*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------
            elif arg[0] == 'MagicBall':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} \n\
                        Магический шар ответит на ваш вопрос (возможные ответы: да, нет, может быть)*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-------------------------------------------------------------------
            elif arg[0] == 'server_info':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} \n\
                        Информация о сервере*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'mafia':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} \n\
                        Запускает мафию*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'mafia':
                await ctx.author.send(embeds=interactions.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {pref} {arg[0]} \n\
                        Запускает мафию*",
                    color=COLOR
                ))
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'settings':
                emb = interactions.Embed(title=f'Настройка сервера ***{str(ctx.message.guild)}***',
                                description="***Параметры:*** \n\
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
                                    join_message (Текмт): Изменить текст отправляемый учаснику при присоединении",
                                color=COLOR
                                )
                await ctx.author.send(embeds=emb)
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            else:
                emb = interactions.Embed(title='*Список доступных команд:*', 
                description =f'***{pref}rand*** — рандомайзер \n\
                ***{pref}info*** — Информация о боте \n\
                ***{pref}warn*** — Выдать предупреждение \n\
                ***{pref}unwarn*** — Убрать предупреждение \n\
                ***{pref}clear_warns*** — Очистка предупреждений \n\
                ***{pref}coin*** — Кинуть монетку \n\
                ***{pref}ban*** — Забанить пользователя\n\
                ***{pref}clear*** — Очистка чата \n\
                ***{pref}kick*** — Кикнуть пользователя \n\
                ***{pref}select*** — Выдача ролей \n\
                ***{pref}join*** — Присоединение бота к голосовому чату \n\
                ***{pref}play*** — Присоединение бота к голосовому чату \n\
                ***{pref}start*** — Присоединение бота к голосовому чату \n\
                ***{pref}stop*** — Присоединение бота к голосовому чату \n\
                ***{pref}pause*** — Присоединение бота к голосовому чату \n\
                ***{pref}spotify*** — Информация юзера о прослушивании spotify \n\
                ***{pref}user*** — Информация о юзере \n\
                ***{pref}MagicBall*** — Магический шар \n\
                ***{pref}server_info*** — Информация о сервере \n\
                ***{pref}mafia*** — Запустить мафию \n\
                ***{pref}score*** Посмотреть счет учасника \n\
                ***{pref}add_score*** \n\
                ***{pref}remove_score*** \n\
                ***{pref}clear_score*** \n\
                ***{pref}tr*** —  Перевести текст \n\
                ***{pref}vote*** —  Вызвать голосование \n\
                ***{pref}rank*** — Показать ваш ранк на сервере \n\
                ***{pref}settings*** — Информация о настройке сервера',
                color=COLOR)
                await ctx.author.send(embeds=emb)
                await ctx.send(embeds=interactions.Embed(
                    title='Ошибка',
                    description=f'Список доступных комманд отправлен вам в личные сообщения!',
                    color=COLOR
                ))
        #---------------------------------------------------------------------
        else:
            emb = interactions.Embed(title = str(BOTVERSION) + ' | Навигация по командам',
            description = f'Команды: \n\
            ***{pref}rand*** — рандомайзер \n\
            ***{pref}info*** — Информация о боте \n\
            ***{pref}warn*** — Выдать предупреждение \n\
            ***{pref}unwarn*** — Убрать предупреждение \n\
            ***{pref}clear_warns*** — Очистка предупреждений \n\
            ***{pref}coin*** — Кинуть монетку \n\
            ***{pref}ban*** — Забанить пользователя\n\
            ***{pref}clear*** — Очистка чата \n\
            ***{pref}kick*** — Кикнуть пользователя \n\
            ***{pref}select*** — Выдача ролей \n\
            ***{pref}join*** — Присоединение бота к голосовому чату \n\
            ***{pref}play*** — Присоединение бота к голосовому чату \n\
            ***{pref}start*** — Присоединение бота к голосовому чату \n\
            ***{pref}stop*** — Присоединение бота к голосовому чату \n\
            ***{pref}pause*** — Присоединение бота к голосовому чату \n\
            ***{pref}spotify*** — Информация юзера о прослушивании spotify \n\
            ***{pref}user*** — Информация о юзере \n\
            ***{pref}MagicBall*** — Магический шар \n\
            ***{pref}server_info*** — Информация о сервере \n\
            ***{pref}mafia*** — Запустить мафию \n\
            ***{pref}score***Посмотреть счет учасника \n\
            ***{pref}add_score*** \n\
            ***{pref}remove_score*** \n\
            ***{pref}clear_score*** \n\
            ***{pref}tr*** —  Перевести текст \n\
            ***{pref}vote*** —  Вызвать голосование \n\
            ***{pref}rank*** — Показать ваш ранк на сервере \n\
            ***{pref}settings*** — Информация о настройке сервера \n\
                \n\
            что бы узнать как работает команда по подробнее напишите ***{pref}help*** (название команды)',
            color = COLOR)
            emb.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.author.send(embeds = emb)
            await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Навигация по командам отправлена вам в личные сообщения!',
                    color=COLOR
                ))
def setup(client):
    Helpint(client)
    
    