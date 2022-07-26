def setup(bot):

    import discord
    import json
    from BTSET import BOTVERSION
    from discord.ext import commands
    
    
    @bot.command(aliases =['Инфо', 'инфо', 'ИНФО'])
    async def info(ctx): #и кста я сегодня пиццу ел!!! #молодец что пиццу ел а теперь мафию пиши
        with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
        emb = discord.Embed(title = f'{bot.user.name} BOT',
        description=f'Вас приветствует {bot.user.name} bot.', #Степа пиши свою хуйню сам
        color = COLOR)
        emb.set_thumbnail(url=bot.user.avatar_url)
        emb.add_field(name = 'Версия', value = str(BOTVERSION))
        emb.add_field(name = 'Создатели бота', value = '$DoNaT$#6442 \n stёbo#6694')
        emb.set_footer(text='devepoled by the Wave team', icon_url = bot.user.avatar_url)
        '''добавить инфу по обратной связи'''
        await ctx.send(embed = emb)