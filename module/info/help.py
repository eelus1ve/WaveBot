def setup(bot):

    import discord
    import json
    from discord.ext import commands
    from BTSET import BOTVERSION

    config = {
    'prefix': '~' #поиграться с префиксами
    }   
    
    @bot.command(aliases = ['хелп', 'Хелп', 'ХЕЛП'])
    async def help(ctx, *arg):
        with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if arg:
            if arg[0] == 'rand':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]}\n\
                        Генерирует случайное число*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------------
            elif arg[0] == 'info':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} \n\
                        Информация о боте*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------------
            elif arg[0] == 'warn':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])}{arg[0]} (@Учасник) (Причина) \n\
                        Выдать предупреждение пользователю",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------------
            elif arg[0] == 'coin':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} \n\
                        Подбросить монетку*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
                #------------------------------------------------------------------
            elif arg[0] == 'ban':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} (@Учасник)\n\
                        Забанить человека*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'clear':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} (кол-во сообщений от 1 до 1000)\n\
                        Отчистить чат на какое-то количество сообщений*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'kick':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} (@Учасник)\n\
                        Кикнуть пользователя*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #---------------------------------------------------------------------
            elif arg[0] == 'select':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} (класс) \n\
                        Выдача ролей \n\
                            Настраивать через {str(config['prefix'])}settings*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #--------------------------------------------------------------------
            elif arg[0] == 'join':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} ||Временно бессмысленно|| \n\
                        Бот присоединяется к вашему воис чату*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-------------------------------------------------------------------
            elif arg[0] == 'spotify':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} (@Участник) \n\
                        Показывает что слушает пользователь*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #------------------------------------------------------------------
            elif arg[0] == 'user':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} (@Учасник) \n\
                        Информация об учснике*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-----------------------------------------------------------------
            elif arg[0] == 'MagicBall':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} \n\
                        Магический шар ответит на ваш вопрос (возможные ответы: да, нет, может быть)*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #-------------------------------------------------------------------
            elif arg[0] == 'server_info':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} \n\
                        Информация о сервере*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'mafia':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} \n\
                        Запускает мафию*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'mafia':
                await ctx.author.send(embed=discord.Embed(
                    title=f'***{arg[0]}***',
                    description=f"*Использование: {str(config['prefix'])} {arg[0]} \n\
                        Запускает мафию*",
                    color=COLOR
                ))
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            #----------------------------------------------------------------------
            elif arg[0] == 'settings':
                emb = discord.Embed(title=f'Настройка сервера ***{str(ctx.message.guild)}***',
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
                await ctx.author.send(embed=emb)
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Информация о комманде {arg[0]} отправлена вам в личные сообщения!',
                    color=COLOR
                ))
            else:
                emb = discord.Embed(title='*Список доступных команд:*', 
                description ='***{}rand***'.format(config['prefix']) + ' — рандомайзер \n\
                ***{}info***'.format(config['prefix']) + ' — Информация о боте \n\
                ***{}warn***'.format(config['prefix']) + ' — Выдать предупреждение \n\
                ***{}unwarn***'.format(config['prefix']) + ' — Убрать предупреждение \n\
                ***{}clear_warns***'.format(config['prefix']) + ' — Очистка предупреждений \n\
                ***{}coin***'.format(config['prefix']) + ' — Кинуть монетку \n\
                ***{}ban***'.format(config['prefix']) + ' — Забанить пользователя\n\
                ***{}clear***'.format(config['prefix']) + ' — Очистка чата \n\
                ***{}kick***'.format(config['prefix']) + ' — Кикнуть пользователя \n\
                ***{}select***'.format(config['prefix']) + ' — Выдача ролей \n\
                ***{}join***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
                ***{}play***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
                ***{}start***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
                ***{}stop***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
                ***{}pause***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
                ***{}spotify***'.format(config['prefix']) + ' — Информация юзера о прослушивании spotify \n\
                ***{}user***'.format(config['prefix']) + ' — Информация о юзере \n\
                ***{}MagicBall***'.format(config['prefix']) + ' — Магический шар \n\
                ***{}server_info***'.format(config['prefix']) + ' — Информация о сервере \n\
                ***{}mafia***'.format(config['prefix']) + ' — Запустить мафию \n\
                ***{}score***'.format(config['prefix']) + 'Посмотреть счет учасника \n\
                ***{}add_score***'.format(config['prefix']) + ' \n\
                ***{}remove_score***'.format(config['prefix']) + ' \n\
                ***{}clear_score***'.format(config['prefix']) + ' \n\
                ***{}tr***'.format(config['prefix']) + ' —  Перевести текст \n\
                ***{}vote***'.format(config['prefix']) + ' —  Вызвать голосование \n\
                ***{}rank***'.format(config['prefix']) + ' — Показать ваш ранк на сервере \n\
                ***{}settings***'.format(config['prefix']) + ' — Информация о настройке сервера',
                color=COLOR)
                await ctx.author.send(embed=emb)
                await ctx.send(embed=discord.Embed(
                    title='Ошибка',
                    description=f'Список доступных комманд отправлен вам в личные сообщения!',
                    color=COLOR
                ))
        #---------------------------------------------------------------------
        else:
            emb = discord.Embed(title = str(BOTVERSION) + ' | Навигация по командам',
            description = 'Команды: \n\
            ***{}rand***'.format(config['prefix']) + ' — рандомайзер \n\
            ***{}info***'.format(config['prefix']) + ' — Информация о боте \n\
            ***{}warn***'.format(config['prefix']) + ' — Выдать предупреждение \n\
            ***{}unwarn***'.format(config['prefix']) + ' — Убрать предупреждение \n\
            ***{}clear_warns***'.format(config['prefix']) + ' — Очистка предупреждений \n\
            ***{}coin***'.format(config['prefix']) + ' — Кинуть монетку \n\
            ***{}ban***'.format(config['prefix']) + ' — Забанить пользователя\n\
            ***{}clear***'.format(config['prefix']) + ' — Очистка чата \n\
            ***{}kick***'.format(config['prefix']) + ' — Кикнуть пользователя \n\
            ***{}select***'.format(config['prefix']) + ' — Выдача ролей \n\
            ***{}join***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
            ***{}play***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
            ***{}start***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
            ***{}stop***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
            ***{}pause***'.format(config['prefix']) + ' — Присоединение бота к голосовому чату \n\
            ***{}spotify***'.format(config['prefix']) + ' — Информация юзера о прослушивании spotify \n\
            ***{}user***'.format(config['prefix']) + ' — Информация о юзере \n\
            ***{}MagicBall***'.format(config['prefix']) + ' — Магический шар \n\
            ***{}server_info***'.format(config['prefix']) + ' — Информация о сервере \n\
            ***{}mafia***'.format(config['prefix']) + ' — Запустить мафию \n\
            ***{}score***'.format(config['prefix']) + 'Посмотреть счет учасника \n\
            ***{}add_score***'.format(config['prefix']) + ' \n\
            ***{}remove_score***'.format(config['prefix']) + ' \n\
            ***{}clear_score***'.format(config['prefix']) + ' \n\
            ***{}tr***'.format(config['prefix']) + ' —  Перевести текст \n\
            ***{}vote***'.format(config['prefix']) + ' —  Вызвать голосование \n\
            ***{}rank***'.format(config['prefix']) + ' — Показать ваш ранк на сервере \n\
            ***{}settings***'.format(config['prefix']) + ' — Информация о настройке сервера \n\
                \n\
            что бы узнать как работает команда по подробнее напишите ***{}help***'.format(config['prefix']) + '(название команды)',
            color = COLOR)
            emb.set_thumbnail(url=bot.user.avatar_url)
            await ctx.author.send(embed = emb)
            await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'Навигация по командам отправлена вам в личные сообщения!',
                    color=COLOR
                ))