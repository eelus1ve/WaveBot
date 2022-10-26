import json
from BTSET import bdpy, BD
from discord.ext import commands

class mrate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener('on_message')
    async def my_message(self, message):
        try:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
                IgnoreChannels = bdpy(ctx=message)['IgnoreChannels']
                IgnoreRoles = bdpy(ctx=message)['IgnoreRoles']
                pref = str(data[str(message.author.guild.id)]['PREFIX'])
            if not(message.content.startswith(pref) or str(message.channel.id) in IgnoreChannels or True in [str(ii) in IgnoreRoles for ii in [i.id for i in message.author.roles]] or message.author.bot):

                xp = bdpy(ctx=message)['USERS'][str(message.author.id)]['SCR']
                lvl = bdpy(ctx=message)['USERS'][str(message.author.id)]['LvL']
    
                if len(message.content) < 100:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//10
                elif len(message.content) >= 100 and len(message.content) < 200:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//40
                elif len(message.content) >= 200 and len(message.content) < 500:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//50
                elif len(message.content) >= 500 and len(message.content) < 1000:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//100
                elif len(message.content) >= 1000 and len(message.content) < 1500:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//200
                elif len(message.content) >= 1500 and len(message.content) < 2000:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//1000
                elif len(message.content) >= 2000:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 1
                        
                increased_xp = xp+15
                new_level = int(increased_xp/100)
                if new_level > lvl:
                    await message.channel.send(f"{message.author.mention} получил новый уровень {new_level}!")
                
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR']=0 #написать формулу + переменая
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['LvL']=new_level
                with open(f'{BD}users.json', 'w') as f:
                    json.dump(data, f, indent=4)
        except:
            pass
def setup(bot):
    bot.add_cog(mrate(bot))