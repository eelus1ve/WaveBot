import discord
import json
from discord.ext import commands
from discord.utils import get
from BTSET import BD
from system.Bot import WaveBot
from BTSET import Lang


class Mwarns_audit(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def audit1(self, message: discord.Message):
        COLOR = self.bot.read_sql(db="servers", guild=message.guild.id, key="MODERATIONCOLOR")
        #====================================================================
        #audit
        #====================================================================
        if self.bot.read_sql(db="servers", guild=str(message.guild.id), key="ADMINCHANNEL"):
            emb = discord.Embed(
                title=Lang(message).language['mwarns_audit1_title'],
                description=f"*{Lang(message).language['mwarns_audit1_des_1']} {self.bot.db_get_user_warns(message.author) - 1} {Lang(message).language['mwarns_audit1_des_2']} {self.bot.db_get_nwarns(message)} {Lang(message).language['mwarns_audit1_des_3']}*",
                timestamp=message.created_at,
                color=COLOR
            )
            emb.add_field(name=Lang(message).language['mwarns_audit1_field_1'], value=message.content, inline=False)
            emb.add_field(name=Lang(message).language['mwarns_audit1_field_2'], value=message.channel.mention, inline=True)
            emb.add_field(name=Lang(message).language['mwarns_audit1_field_3'], value=message.author.mention, inline=True)
            emb.add_field(name=Lang(message).language['mwarns_audit1_field_4_name'], value=Lang(message).language['mwarns_audit1_field_4_value'], inline=True)
            emb.set_footer(text=Lang(message).language['mwarns_audit1_footer'])
            await get(message.guild.text_channels, id=int(self.bot.read_sql(db="servers", guild=str(message.guild.id), key="ADMINCHANNEL"))).send(embed=emb)

        #====================================================================
        #ls
        #====================================================================
        emb = discord.Embed(
            title='Нарушение',
            description=f'Вам выдали предупреждение на сервере {message.guild.name}\nСообщение с нарушением: {message.content}',
            timestamp=message.created_at,
            color=COLOR
        )
        emb.add_field(name='Канал', value=message.channel.mention, inline=True)
        emb.add_field(name='Тип нарушения:', value=f'Ругательства/ссылки', inline=True)
        emb.add_field(name='Кол-во нарушений', value=f'{self.bot.db_get_user_warns(message.author)}/{self.bot.db_get_nwarns(message)}', inline=True)
        emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')
        
        await message.author.send(embed=emb)
    #================================================================================================================================================================================









class NewMwarns(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot: WaveBot = bot


    async def cheack_mess(self, message: discord.Message):
        badlist = self.bot.read_sql(db="servers", guild=message.guild.id, key="BADWORDS, LINKS")
        for i in badlist:
            modroles = self.bot.read_sql(db="servers", guild=message.guild.id, key="MODROLES")
            if modroles != {}:
                Modroot = modroles[[str(i.id) for i in message.author.roles if str(i.id) in modroles][0]]['Warns']['Warn'] == "True" or message.author.guild_permissions.administrator
            else:
                Modroot = message.author.guild_permissions.administrator


            if str(message.content) == f'~set add_badword {i}' and Modroot:
                await message.delete()

            else:
                warn = self.bot.read_sql(db=f"server{message.guild.id}", guild=message.author.id, key="WARNS")
                messagelist = list(str(message.content.lower()).split(" "))
                if "**" in i:
                    leni = len(i)
                    if "**" == i[:-(leni-2)] and "**" == i[leni-2] and i in message.content.lower():
                        self.bot.write_sql(db=f"server{message.guild.id}", guild=message.author.id, key="WARNS", value=warn+1)
                        return warn+1
                    if "**" == i[:-(leni-2)] and True in [i[2:] == ii[len(ii)-leni:] in ii for ii in messagelist]:
                        self.bot.write_sql(db=f"server{message.guild.id}", guild=message.author.id, key="WARNS", value=warn+1)
                        return warn+1
                    if "**" == i[leni-2] and True in [i[2:] == ii[:-(len(ii)-leni)] in ii for ii in messagelist]:
                        self.bot.write_sql(db=f"server{message.guild.id}", guild=message.author.id, key="WARNS", value=warn+1)
                        return warn+1
                    
                elif " " in message.content.lower():
                    for ii in messagelist:
                        if i == ii:
                            self.bot.write_sql(db=f"server{message.guild.id}", guild=message.author.id, key="WARNS", value=warn+1)
                            return warn+1
                    if "*" in i:
                        if "*" == i[0] and True in [i[1:] == ii[1:] for ii in messagelist]:
                            self.bot.write_sql(db=f"server{message.guild.id}", guild=message.author.id, key="WARNS", value=warn+1)
                            return warn+1
                        if "*" == i[-1] and True in [i[:-1] == ii[:-1] for ii in messagelist]:
                            self.bot.write_sql(db=f"server{message.guild.id}", guild=message.author.id, key="WARNS", value=warn+1)
                            return warn+1
        return 0




class Mwarns(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot: WaveBot = bot
    
    async def listener_on_message_mwarns(self, message: discord.Message):
        try:
            if message.guild:
                userWarn = NewMwarns(self.bot).cheack_mess(message)
                if userWarn:
                    pass
                else:
                    #====================================================================
                    #ban
                    #====================================================================
                    if userWarn >= self.bot.read_sql(db="servers", guild=message.guild.id, key="NWARNS"):
                        ReasoN = 'Вы привысили допустимое количество нарушений'
                        emb = discord.Embed(
                        title=f'Вас забанили на сервере {message.guild.name}',
                        description=f'{ReasoN}',
                        timestamp=message.created_at,
                        color=self.bot.read_sql(db="servers", guild=message.guild.id, key="MODERATIONCOLOR")
                        )
                        await message.author.send(embed=emb)
                        await message.author.ban(reason=ReasoN)
                    #========================================================================================

                    #message_delete=======
                    await message.delete()
                    #=====================



                #Caps===================================================================
                if message.content.isupper():
                    with open(f'{BD}users.json', 'r') as file:
                        data = json.load(file)
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['CAPS'] += 1
                    if self.bot.db_get_user_caps(message.author) - 1 >= self.bot.db_get_ncaps(message):
                        data[str(message.guild.id)]['USERS'][str(message.author.id)]['CAPS'] = 0
                        data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] += 1
                        #====================================================================
                        #audit
                        #====================================================================
                        if self.bot.db_get_adminchannel(message) in [str(i.id) for i in message.guild.channels]:
                            emb = discord.Embed(
                                title='Нарушение',
                                description=f"*Ранее, у нарушителя было уже {[self.bot.db_get_user_warns(message.author) - 1]} нарушений, после {self.bot.db_get_nwarns(message)} он будет забанен!*",
                                timestamp=message.created_at,
                                color=self.bot.db_get_modercolor(message)
                            )
                            emb.add_field(name='Канал:', value=message.channel.mention, inline=True)
                            emb.add_field(name='Нарушитель:', value=message.author.mention, inline=True)
                            emb.add_field(name='Тип нарушения:', value='Капс', inline=True)
                            emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')
                            
                            await get(message.guild.text_channels, id=int(self.bot.db_get_adminchannel(message))).send(embed=emb)
                        #====================================================================
                        #ls
                        #====================================================================
                        emb = discord.Embed(
                            title='Нарушение',
                            description=f'Вам выдали предупреждение на сервере {message.guild.name}\nСообщение с нарушением: {message.content}',
                            timestamp=message.created_at,
                            color=self.bot.db_get_modercolor(message)
                        )
                        emb.add_field(name='Канал', value=message.channel.mention, inline=True)
                        emb.add_field(name='Тип нарушения:', value=f'Ругательства/ссылки', inline=True)
                        emb.add_field(name='Кол-во нарушений', value=f'{self.bot.db_get_user_warns(message.author)}/{self.bot.db_get_nwarns(message)}', inline=True)
                        emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')

                        await message.author.end(embed=emb)
                        #===========================================================================================================================================================================================

                        #====================================================================
                        #ban
                        #====================================================================
                        if data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] >= self.bot.db_get_nwarns(message):
                            ReasoN = 'Вы привысили допустимое количество нарушений'
                            emb = discord.Embed(
                            title=f'Вас забанили на сервере {message.guild.name}',
                            description=f'{ReasoN}',
                            timestamp=message.created_at,
                            color=self.bot.db_get_modercolor(message)
                            )
                            await message.author.send(embed=emb)
                            await message.author.ban(reason=ReasoN)
                        #=====================================================================================
                        
                        #message_delete=======
                        await message.delete()
                        #=====================
                with open(f'{BD}users.json', 'w') as file:
                    json.dump(data, file, indent=4)
        except InterruptedError:
            pass