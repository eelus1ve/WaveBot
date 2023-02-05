import discord
from BTSET import BOTVERSION, ADMINS, BETATESTERS, Info
from discord.ext import commands
 
class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_info(self, ctx: commands.Context): #и кста я сегодня пиццу ел!!! #молодец что пиццу ел а теперь мафию пиши
        emb = discord.Embed(title = f'{self.bot.user.name} BOT',
        description=f'Вас приветствует {self.bot.user.name} bot.', #Степа пиши свою хуйню сам
        color = Info(ctx).color)
        emb.set_thumbnail(url=self.bot.user.avatar_url)
        emb.add_field(name='Версия', value=str(BOTVERSION))
        emb.add_field(name='Создатели бота', value='\n'.join([f'{self.bot.get_user(int(i)).name}#{self.bot.get_user(int(i)).discriminator}' for i in ADMINS]))
        emb.add_field(name='Бета тестеры', value='\n'.join([f'{self.bot.get_user(int(i)).name}#{self.bot.get_user(int(i)).discriminator}' for i in BETATESTERS]))
        emb.set_footer(text='devepoled by the Wave team', icon_url = self.bot.user.avatar_url)
        #добавить информацию про бетотестреов и остальных юзеров бота до релиза + инфу про ботф (можно позаимствовать из dox файла или презентации)
        await ctx.send(embed = emb)