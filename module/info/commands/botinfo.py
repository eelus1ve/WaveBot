import discord
from BTSET import BOTVERSION, ADMINS, BETATESTERS, Lang
from discord.ext import commands
from system.Bot import WaveBot


import json
from BTSET import BD



class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_info(self, ctx: commands.Context): #и кста я сегодня пиццу ел!!! #молодец что пиццу ел а теперь мафию пиши
        emb = discord.Embed(title='{} {}'.format(self.bot.user.name, Lang(ctx).language['botinfo_title']),
                            description='{} {} {}'.format(Lang(ctx).language['botinfo_des_1'], self.bot.user.name, Lang(ctx).language['botinfo_des_2']), #Степа пиши свою хуйню сам
                            color=self.bot.read_sql(table="colors", guild=ctx.guild.id, key="INFOCOLOR"))
        emb.set_thumbnail(url=self.bot.user.display_avatar)
        emb.add_field(name=Lang(ctx).language['botinfo_ver'], value=str(BOTVERSION))
        emb.add_field(name=Lang(ctx).language['botinfo_dev'], value='\n'.join([f'{self.bot.get_user(int(i)).name}#{self.bot.get_user(int(i)).discriminator}' for i in ADMINS]))
        emb.add_field(name=Lang(ctx).language['botinfo_beta-testers'], value='\n'.join([f'{self.bot.get_user(int(i)).name}#{self.bot.get_user(int(i)).discriminator}' for i in BETATESTERS]))
        emb.set_footer(text=Lang(ctx).language['botinfo_footer'], icon_url = self.bot.user.display_avatar)
        #добавить информацию про бетотестреов и остальных юзеров бота до релиза + инфу про ботф (можно позаимствовать из dox файла или презентации)
        await ctx.send(embed = emb)
    

    #удалить эту часть кода перед релизом
    
    async def command_new_betatesters(self, ctx: commands.Context):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        print([i for i in data["981257625696075896"]["USERS"].keys()])
 

