import discord
import json
from discord.ext import commands
from discord.utils import get
class mwarns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener('on_message')
    async def ion_message(self, message):
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                COLOR = int(data[str(message.author.guild.id)]['COLOR'], 16)
                idAdminchennel = int(data[str(message.author.guild.id)]['idAdminchennel'])
                nWarns = int(data[str(message.author.guild.id)]['nWarns'])
                nCaps = int(data[str(message.author.guild.id)]['nCaps'])
                BADWORDS = data[str(message.author.guild.id)]['BADWORDS']
                LINKS = data[str(message.author.guild.id)]['LINKS']
                WARN = []
                WARN.extend(BADWORDS); WARN.extend(LINKS)
            for i in range(0, len(WARN)):
                if WARN[i] in message.content.lower():
                    
                    with open('users.json', 'w') as file:
                        data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] +=1
                        json.dump(data, file, indent=4)
                        
                    emb = discord.Embed(
                        title='Нарушение',
                        description=f"*Ранее, у нарушителя было уже {data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
                        timestamp=message.created_at,
                        color=COLOR
                    )
                    emb.add_field(name='Канал:', value=message.channel.mention, inline=True)
                    emb.add_field(name='Нарушитель:', value=message.author.mention, inline=True)
                    emb.add_field(name='Тип нарушения:', value='Ругательства/ссылки', inline=True)

                    await get(message.guild.text_channels, id=int(idAdminchennel)).send(embed=emb)

                    if data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] >= nWarns:
                        await message.author.ban(reason='Вы привысили допустимое количество нарушений')

            if message.content.isupper():
                with open('users.json', 'r') as file:
                    data = json.load(file)
                    

                with open('users.json', 'w') as file:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['CAPS'] += 1
                    json.dump(data, file, indent=4)
                if data[str(message.guild.id)]['USERS'][str(message.author.id)]['CAPS'] >= int(nCaps):
                    with open('users.json', 'w') as file:
                        data[str(message.guild.id)]['USERS'][str(message.author.id)]['CAPS'] = 0
                        data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] += 1

                        json.dump(data, file, indent=4)
                        
                        emb = discord.Embed(
                            title='Нарушение',
                            description=f"*Ранее, у нарушителя было уже {data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS' - 1]} нарушений, после {nWarns} он будет забанен!*",
                            timestamp=message.created_at,
                            color=COLOR
                        )
                    emb.add_field(name='Канал:', value=message.channel.mention, inline=True)
                    emb.add_field(name='Нарушитель:', value=message.author.mention, inline=True)
                    emb.add_field(name='Тип нарушения:', value='Капс', inline=True)

                    await get(message.guild.text_channels, id=int(data[str(message.author.guild.id)]['idAdminchennel'])).send(embed=emb)

                    if data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] >= nWarns:
                        await message.author.ban(reason='Вы привысили допустимое количество нарушений')

        except:
            pass
def setup(bot):
    bot.add_cog(mwarns(bot))