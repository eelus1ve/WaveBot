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

                xp = self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP")
                lvl = self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") #формула

                if len(message.content) < 100:
                    self.bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP", value=self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") + 5 + (len(message.content))//10)
                elif len(message.content) >= 100 and len(message.content) < 200:
                    self.bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP", value=self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") + 5 + (len(message.content))//40)
                elif len(message.content) >= 200 and len(message.content) < 500:
                    self.bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP", value=self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") + 5 + (len(message.content))//50)
                elif len(message.content) >= 500 and len(message.content) < 1000:
                    self.bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP", value=self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") + 5 + (len(message.content))//100)
                elif len(message.content) >= 1000 and len(message.content) < 1500:
                    self.bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP", value=self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") + 5 + (len(message.content))//200)
                elif len(message.content) >= 1500 and len(message.content) < 2000:
                    self.bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP", value=self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") + 5 + (len(message.content))//1000)
                elif len(message.content) >= 2000:
                    self.bot.write_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP", value=self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP") + 1)
                        
                increased_xp = xp+15
                new_level = int(increased_xp/100)
                if new_level > lvl:
                    await message.channel.send(f"{message.author.mention} {Lang(message).language['mrate_command_my_message_text']} {new_level}!")
        except:
            pass