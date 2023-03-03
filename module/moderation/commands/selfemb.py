import discord
from discord.ext import commands
# from BTSET import embpy
import json
import datetime
import pytz
from system.Bot import WaveBot

class Selfemb(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot
    
    @commands.command()
    async def create_emb(self, ctx: commands.Context):
        # await embpy(ctx, comp='n', des=f'some text')

        moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d:%H:%M')

        content = 0
        title = 0
        des = 0
        color = 0

        def checkemb(a):
            if a:
                return a
            else:
                pass
            
        def check(msg: discord.Message):
            return msg.author == ctx.author and ('<WaveEmb>' in msg.content)

        # ms: str = await self.bot.wait_for(event='message', check=check)

        ms = '''<WaveEmb>{
            "title": "123", 
            "description": "321",
            "color": "000000",
            "add_field": {
                "0": ["123", "321"]
                "1": ["222", "111"]
            }
            "set_footer": "some",
            }'''


        ms = ms.replace('<WaveEmb>', '')

        if '<moscowTime>' in ms:
            ms = ms.replace('<moscowTime>', f'{moscow_time}')
        msemb = json.loads(ms)
        mskeys = [k for k in msemb.keys()]


        if 'content' in mskeys:
            content = msemb['content']
        if 'title' in mskeys:
            title = msemb['title']
        if 'description' in mskeys:
            des = msemb['description']
        if 'color' in mskeys:
            color = msemb['color']

        try: #чекнуть по поводу указания времени
            emb = discord.Embed(checkemb(title), checkemb(des), int(checkemb(color), 16))
        except: #узнать какая будет ошибка и отлавливать её
            emb = discord.Embed(checkemb(title), checkemb(des))
        
        if 'add_field' in mskeys:
            for i in msemb['add_field'].keys():
                emb.add_field(name=msemb['add_field'][i][0], value=msemb['add_field'][i][1])
        
        if 'set_footer' in mskeys:
            emb.set_footer(text=msemb['set_footer'])

        try:
            if 'set_thumbnail' in mskeys:
                emb.set_thumbnail(url=msemb['set_thumbnail'])
                
            if 'set_image' in mskeys:
                emb.set_image(url=msemb['set_image'])
        except: #узнать какая будет ошибка и отлавливать её
            pass #тут написать про ошибку!!!!!!!!!

        #ещё пару пунктов по поводу emb.set и готово


        
        # await ctx.send(embed=emb, components = Comp)













# ms = '''<Wavemb>
# {
#     "title": "",
#     "des": "",
#     "color": "",
#     "add_field": {
#         "name": "", "value": "",
#         ...
#     }
#     "set_footer": ""
# }        
# '''




def setup(bot):
    bot.add_cog(Selfemb(bot))
