import discord
import json
from discord.ext import commands
from discord.utils import get
from BTSET import BD
from system.Bot import WaveBot


class Mwarns(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def listener_on_message_mwarns(self, message: discord.Message):
        try:
            if message.guild:
                with open(f'{BD}users.json', 'r') as file:
                    data = json.load(file)
                WARN = []
                WARN.extend(self.bot.db_get_badwords(message))
                WARN.extend(self.bot.db_get_links(message))
                if self.bot.db_get_modroles(message) != {}:
                    Modroot = self.bot.db_get_modroles(message)[[str(i.id) for i in message.author.roles if str(i.id) in self.bot.db_get_modroles(message)][0]]['Warns']['Warn'] == "True" or message.author.guild_permissions.administrator
                else:
                    Modroot = message.author.guild_permissions.administrator
                for i in range(0, len(WARN)):
                    #badwords + links==============================================================
                    if WARN[i] in message.content.lower():
                        if str(message.content) == f'~set add_badword {WARN[i]}' and Modroot:
                            await message.delete()
                        else:
                            data[str(message.guild.id)]["USERS"][str(message.author.id)]["WARNS"] +=1


                            #====================================================================
                            #audit
                            #====================================================================
                            if self.bot.db_get_adminchannel(message) in [str(i.id) for i in message.guild.channels]:
                                emb = discord.Embed(
                                    title='Нарушение',
                                    description=f"*Ранее, у нарушителя было уже {self.bot.db_get_user_warns(message.author) - 1} нарушений, после {self.bot.db_get_nwarns(message)} он будет забанен!*",
                                    timestamp=message.created_at,
                                    color=self.bot.db_get_modercolor(message)
                                )
                                emb.add_field(name='Сообщение нарушителя:', value=message.content, inline=False)
                                emb.add_field(name='Канал:', value=message.channel.mention, inline=True)
                                emb.add_field(name='Нарушитель:', value=message.author.mention, inline=True)
                                emb.add_field(name='Тип нарушения:', value='Ругательства/ссылки', inline=True)
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
                            
                            await message.author.send(embed=emb)
                        #================================================================================================================================================================================


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