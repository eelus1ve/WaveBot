import discord
from BTSET import BOTVERSION, ADMINS, BETATESTERS, Info, Lang
from discord.ext import commands
 
class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_info(self, ctx: commands.Context): #и кста я сегодня пиццу ел!!! #молодец что пиццу ел а теперь мафию пиши
        language = Lang.words(Lang.set_lang(ctx))
        emb = discord.Embed(title = '{} {}'.format(self.bot.user.name, language['botinfo_title']),
        description='{} {} {}'.format(language['botinfo_des_1'], self.bot.user.name, language['botinfo_des_2']), #Степа пиши свою хуйню сам
        color = Info(ctx).color)
        emb.set_thumbnail(url=self.bot.user.avatar_url)
        emb.add_field(name=language['botinfo_ver'], value=str(BOTVERSION))
        emb.add_field(name=language['botinfo_dev'], value='\n'.join([f'{self.bot.get_user(int(i)).name}#{self.bot.get_user(int(i)).discriminator}' for i in ADMINS]))
        emb.add_field(name=language['botinfo_beta-testers'], value='\n'.join([f'{self.bot.get_user(int(i)).name}#{self.bot.get_user(int(i)).discriminator}' for i in BETATESTERS]))
        emb.set_footer(text=language['botinfo_footer'], icon_url = self.bot.user.avatar_url)
        #добавить информацию про бетотестреов и остальных юзеров бота до релиза + инфу про ботф (можно позаимствовать из dox файла или презентации)
        await ctx.send(embed = emb)