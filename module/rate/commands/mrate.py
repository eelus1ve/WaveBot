from system.Bot import WaveBot
from module.rate.commands.rank import Rank
from BTSET import IGNORE_SIMV, Lang
from discord.ext import commands
import discord


class Mrate(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    async def command_my_message(self, message: discord.Message):
        try: #подправить логику в if-ке под sql
            if not(message.content.startswith(self.bot.read_sql(db="servers", guild=message.guild.id, key="PREFIX")) or (str(self.bot.user.mention) in message.content) or str(message.channel.id) in self.bot.read_sql(db="servers", guild=message.guild.id, key="IGNORECHANNELS") or True in [str(ii) in self.bot.read_sql(db="servers", guild=message.guild.id, key="IGNOREROLES") for ii in [i.id for i in message.author.roles]] or message.author.bot or [True for i in IGNORE_SIMV if i in message.content][0]):

                xp = self.bot.read_sql(db=f"server{message.guild.id}", guild=str(message.author.id), key="XP")
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

                if Rank.xpFunction(Rank.levelFunction(xp)) > xp:
                    await message.channel.send(f"{message.author.mention} {Lang(message).language['mrate_command_my_message_text']} {Rank.levelFunction(xp)}!")
        except:
            pass