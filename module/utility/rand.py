def setup(bot):

    import discord
    import random
    import json
    from discord.ext import commands

    config = {
    'prefix': '~' #поиграться с префиксами
}

    @bot.command(aliases = ['ранд', 'РАНД', 'Ранд'])
    async def rand(ctx, arg = None, arg2 = None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)

        if arg and not(arg2):
            des=random.randint(0, int(arg))
        elif arg and arg2:
            des=random.randint(int(arg), int(arg2))
        elif not(arg):
            des=random.randint(0, 100)
        else:
            await ctx.send(embed=discord.Embed(
                    title="Ошибка",
                    description='Использование {}rand'.format(config['prefix']) + ' (число1) [число2]\n\n\
                        Пример с одним числом: {}rand'.format(config['prefix']) + ' 100\n\
                            ┗Выведет рандомное число в пределах 100 \n\
                        Пример с двумя числами: {}rand'.format(config['prefix']) + ' 100 200\n\
                            ┗Выведет рандомное число от 100 до 200',
                    color = ErCOLOR,
                ))
        await ctx.send(embed=discord.Embed(
                    title="Ваше рандомное число: ",
                    description=des,
                    color = COLOR,
                ))