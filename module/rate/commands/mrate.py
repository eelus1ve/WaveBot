import json
from BTSET import Score_presets, bdpy, BD, IGNORE_SIMV, Lang
from discord.ext import commands
import discord
from system.Bot import WaveBot


class Mrate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_my_message(self, message: discord.Message):
        try:
            if not(message.content.startswith(Score_presets(message.author).prefix) or (str(self.bot.user.mention) in message.content) or str(message.channel.id) in Score_presets(message.author).ignorechannels or True in [str(ii) in Score_presets(message.author).ignoreroles for ii in [i.id for i in message.author.roles]] or message.author.bot or [True for i in IGNORE_SIMV if i in message.content][0]):

                xp = Score_presets(message.author).score
                lvl = Score_presets(message.author).lvl

                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)

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
                    await message.channel.send(f"{message.author.mention} {Lang(message).language['mrate_command_my_message_text']} {new_level}!")
                
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR']=0 #написать формулу + переменая
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['LvL']=new_level
                with open(f'{BD}users.json', 'w') as f:
                    json.dump(data, f, indent=4)
        except:
            pass