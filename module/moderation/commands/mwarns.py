import discord
import json
from discord.ext import commands
from discord.utils import get
from BTSET import Moderation, bdpy, BD

class Mwarns(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    async def listener_on_message_mwarns(self, message: discord.Message):
        try:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            WARN = []
            WARN.extend(Moderation(message.author).badwords); WARN.extend(Moderation(message.author).links)
            if bdpy(ctx=message)['ModRoles'] != {}:
                Modroot = bdpy(ctx=message)['ModRoles'][[str(i.id) for i in message.author.roles if str(i.id) in bdpy(ctx=message)['ModRoles']][0]]['Warns']['Warn'] == "True" or message.author.guild_permissions.administrator
            else:
                Modroot = message.author.guild_permissions.administrator
            for i in range(0, len(WARN)):
                #badwords + links==============================================================
                if WARN[i] in message.content.lower():
                    if str(message.content) == f'~set add_badword {WARN[i]}' and Modroot:
                        await message.delete()
                    else:
                        data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] +=1


                        #====================================================================
                        #audit
                        #====================================================================
                        if Moderation(message) in [str(i.id) for i in message.guild.channels]:
                            emb = discord.Embed(
                                title='Нарушение',
                                description=f"*Ранее, у нарушителя было уже {data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] - 1} нарушений, после {Moderation(message).nWarns} он будет забанен!*",
                                timestamp=message.created_at,
                                color=Moderation(message).color
                            )
                            emb.add_field(name='Сообщение нарушителя:', value=message.content, inline=False)
                            emb.add_field(name='Канал:', value=message.channel.mention, inline=True)
                            emb.add_field(name='Нарушитель:', value=message.author.mention, inline=True)
                            emb.add_field(name='Тип нарушения:', value='Ругательства/ссылки', inline=True)
                            emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')
                            await get(message.guild.text_channels, id=Moderation(message).idadminchannel).send(embed=emb)


                        #====================================================================
                        #ls
                        #====================================================================
                        emb = discord.Embed(
                            title='Нарушение',
                            description=f'Вам выдали предупреждение на сервере {message.guild.name}\nСообщение с нарушением: {message.content}',
                            timestamp=message.created_at,
                            color=Moderation(message).color
                        )
                        emb.add_field(name='Канал', value=message.channel.mention, inline=True)
                        emb.add_field(name='Тип нарушения:', value=f'Ругательства/ссылки', inline=True)
                        emb.add_field(name='Кол-во нарушений', value=f'{Moderation(message).warns}/{Moderation(message).nWarns}', inline=True)
                        emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')
                        
                        await message.author.send(embed=emb)
                    #================================================================================================================================================================================


                        #====================================================================
                        #ban
                        #====================================================================
                        if data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] >= Moderation(message.aithor).nWarns:
                            ReasoN = 'Вы привысили допустимое количество нарушений'
                            emb = discord.Embed(
                            title=f'Вас забанили на сервере {message.guild.name}',
                            description=f'{ReasoN}',
                            timestamp=message.created_at,
                            color=Moderation(message).color
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
                if data[str(message.guild.id)]['USERS'][str(message.author.id)]['CAPS'] >= Moderation(message).nCaps:
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['CAPS'] = 0
                    data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] += 1
                    #====================================================================
                    #audit
                    #====================================================================
                    if bdpy(ctx=message)['idAdminchennel'] in [str(i.id) for i in message.guild.channels]:
                        emb = discord.Embed(
                            title='Нарушение',
                            description=f"*Ранее, у нарушителя было уже {data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS' - 1]} нарушений, после {Moderation(message).nWarns} он будет забанен!*",
                            timestamp=message.created_at,
                            color=Moderation(message).color
                        )
                        emb.add_field(name='Канал:', value=message.channel.mention, inline=True)
                        emb.add_field(name='Нарушитель:', value=message.author.mention, inline=True)
                        emb.add_field(name='Тип нарушения:', value='Капс', inline=True)
                        emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')
                        
                        await get(message.guild.text_channels, id=int(data[str(message.author.guild.id)]['idAdminchennel'])).send(embed=emb)
                    #====================================================================
                    #ls
                    #====================================================================
                    emb = discord.Embed(
                        title='Нарушение',
                        description=f'Вам выдали предупреждение на сервере {message.guild.name}\nСообщение с нарушением: {message.content}',
                        timestamp=message.created_at,
                        color=Moderation(message).color
                    )
                    emb.add_field(name='Канал', value=message.channel.mention, inline=True)
                    emb.add_field(name='Тип нарушения:', value=f'Ругательства/ссылки', inline=True)
                    emb.add_field(name='Кол-во нарушений', value=f'{Moderation(message).warns}/{Moderation(message).nWarns}', inline=True)
                    emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')

                    await message.author.end(embed=emb)
                    #===========================================================================================================================================================================================

                    #====================================================================
                    #ban
                    #====================================================================
                    if data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] >= Moderation(message).nWarns:
                        ReasoN = 'Вы привысили допустимое количество нарушений'
                        emb = discord.Embed(
                        title=f'Вас забанили на сервере {message.guild.name}',
                        description=f'{ReasoN}',
                        timestamp=message.created_at,
                        color=Moderation(message).color
                        )
                        await message.author.send(embed=emb)
                        await message.author.ban(reason=ReasoN)
                    #=====================================================================================
                    
                    #message_delete=======
                    await message.delete()
                    #=====================
            with open(f'{BD}users.json', 'w') as file:
                json.dump(data, file, indent=4)
        except:
            pass