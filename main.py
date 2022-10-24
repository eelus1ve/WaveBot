#=============================================================================================импорты
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       --> token стёпы <---             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      #нахуя?       #нужно было!     #нахуя?    #чтобы токен поменять!5
import multiprocessing
from discord_components import SelectOption as Sel
import discord_components
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import interactions
from discord_components import ComponentsBot, Button, Select
from pydoc import cli
import discord
import json
import os
import asyncio
from BTSET import bdpy, embpy
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption, error
import re


load_dotenv(find_dotenv())

#=======================================================================================================================
intents=discord.Intents.all()
def get_prefix(bot, message):
    with open('users.json', 'r') as file:
        data = json.load(file)
    try:
        prefix = data[str(message.guild.id)]['PREFIX']
    except AttributeError:
        prefix = '~'
    return prefix
client = interactions.Client(token=os.getenv('TOKEN'))
bot =ComponentsBot(command_prefix = get_prefix, intents=intents)
bot.remove_command('help')
#=======================================================================================================================

#=======================================================================================================================
@bot.event
async def on_ready():
    bot.load_extension('loaderpy')
    bot.load_extension('JSONwriter')
    # client.load('module.rate.score')
    # client.reload('module.rate.score')
    client.load('module.voice.vcbot')
    client.reload('module.voice.vcbot')
    bot.load_extension('system.while')
    
    
    print(f'{bot.user.name} connected')


    await bot.change_presence(activity=discord.Game('Portal 2'))
#=======================================================================================================================

#=======================================================================================================================
@bot.command()
async def a(ctx: commands.Context):
    # client.load('module.moderation.warns')
    await ctx.send(embed=embpy(ctx, comp='s', des=f'хуй'))

#===================================================================================================
# @client.command(
#     name='settigs',
#     description='stgngs',
# )
# async def btst_start(ctx):
#     settings_names = ['настроить роли', 'добавить класс ролей', 'настроить цвет', 'настроить цвет ошибок',
#                       'канал администратора', 'кол-во капсов для предупреждения', 'кол-во варнов для бана', 'добавить плохое слово', 'префикс', 'указать свой текст при выборе ролей',
#                       'настроить роли при входе на сервер', 'список join ролей', 'убрать плохое слово',
#                       'создать "свои комнаты"', 'музыка', 'добавить канал с инфорацией']

#     await ctx.send(components=SelectMenu(
#         custom_id='btst1',
#         options=[SelectOption(label=i, value=i) for i in settings_names],
#         placeholder='выберете настройки',
#         max_values=1,
#         min_values=1
#     ))

# @client.component('btst1')
# async def sel_opt(interaction: interactions.ComponentContext, int_val):
#     gld = await interaction.get_guild()
#     channels = await gld.get_all_channels()

#     with open('users.json', 'r') as file:
#         data = json.load(file)
#         roles = data[str(interaction.guild_id)]['JoinRoles']
#         COLOR = int(data[str(interaction.guild_id)]['COLOR'], 16)
#         Classes = data[str(interaction.guild_id)]['ROLES']

#         serverRoles = []
#         for i in range(0, len(gld.roles),
#                        24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             serverRoles.append(gld.roles[
#                                i:i + 24])  # второй важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#         chlens = []
#         for i in range(0, len([chlen for chlen in channels if str(chlen.type) == 'ChannelType.GUILD_TEXT']),
#                        24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             chlens.append([chlen for chlen in channels if str(chlen.type) == 'ChannelType.GUILD_TEXT'][
#                           i:i + 24])  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#     for arg in int_val:
#         if arg == 'музыка':
#             ctx: discord.Guild = [i for i in bot.guilds if i.id == interaction.guild_id][0]
#             chlen_dinozavra = [i for i in ctx.text_channels if i.id == interaction.channel_id][0]
#             if [i for i in ctx.categories if i.name == 'music']:
#                 await interaction.send('успешно', ephemeral=True)
#                 for category in ctx.categories:
#                     [await chnl.delete() for chnl in category.channels if category.name == 'music']
#                 [await i.delete() for i in ctx.categories if i.name == 'music']
#             else:

#                 with open('music.json', 'r') as file:
#                     data_mus: dict = json.load(file)
#                 if not(str(ctx.id) in [i for i in data_mus.keys()]):
#                     data_mus.update(
#                         {
#                             ctx.id: {
#                                 'songs': [],
#                                 'pl_id': None,
#                                 'chl_id': None
#                             }
#                         }
#                     )

#                 with open('music.json', 'w') as file:
#                     json.dump(data_mus, file, indent=4)

#                 await interaction.send('успешно', ephemeral=True)
#                 ctg = await ctx.create_category(name='music')
#                 txt_cnlen = await ctg.create_text_channel(name='великий дон ягон')
#                 vc_clen = await ctg.create_voice_channel(name='music')
#                 embd = discord.Embed(
#                     title='***                               wave player***',
#                     description=f'=================================',
#                     colour=0x00FFFF
#                 )
#                 embd.add_field(name='сейчас играет:', value='ничего')

#                 comp = [
#                     [
#                         Button(emoji='◀', style=2),
#                         Button(emoji='⏯', style=2),
#                         Button(emoji='▶', style=2),
#                         Button(emoji='🔀', style=2)
#                     ],
#                     [
#                         Button(emoji='🔁', style=2),
#                         Button(emoji='🔊', style=2),
#                         Button(emoji='🔈', style=2),
#                         Button(emoji='🔇', style=2)
#                     ]
#                 ]

#                 msc_player = await txt_cnlen.send(embed=embd, components=comp)

#                 await vc_clen.connect()


#                 with open('music.json', 'r') as file:
#                     data_mus = json.load(file)
#                     data_mus[str(ctx.id)]['pl_id'] = msc_player.id
#                     data_mus[str(ctx.id)]['chl_id'] = txt_cnlen.id
#                 with open('music.json', 'w') as file:
#                     json.dump(data_mus, file, indent=4)

#         if arg == 'настроить роли':
#             ctxx = [i for i in bot.get_all_channels() if i.id == interaction.channel_id][0]
#             await ctxx.send(embed=discord.Embed(
#                 title='Укажите классы в которые вы хотите добавить роли',
#                 color=COLOR
#             ),
#             components=[
#                 Select(
#                     placeholder='Укажите классы в которые вы хотите добавить роли',
#                     max_values=len(data[str(interaction.guild_id)]['ROLES']),
#                     min_values=1,
#                     options=[Sel(label=str(i), value=str(i)) for i in [k for k in Classes.keys()]]
#                 )
#             ]
#             )

#         if arg == 'добавить класс ролей':
#             await interaction.popup(Modal(
#                 custom_id='Add_class',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите название класса'
#                     )
#                 ]
#             ))
#         elif arg == 'настроить цвет':
#             await interaction.popup(Modal(
#                 custom_id='Color',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите цвет в hex без #',
#                         min_length=6,
#                         max_length=6
#                     )
#                 ]
#             ))
#         elif arg == 'настроить цвет ошибок':
#             await interaction.popup(Modal(
#                 custom_id='ErColor',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите цвет в hex без #',
#                         min_length=6,
#                         max_length=6
#                     )
#                 ]
#             ))
#         elif arg == 'канал администратора':
#             for chlen_begemota in chlens:
#                 SM = SelectMenu(
#                     custom_id='IDA1',
#                     options=[
#                         SelectOption(label=i.name, value=str(i.id)) for i in chlen_begemota
#                     ],
#                     placeholder='выберете канал который хотите сделать каналом администратора'
#                 )
#                 await interaction.send(components=SM)
#         elif arg == 'ncaps':
#             await interaction.popup(Modal(
#                 custom_id='Ncaps',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите максимальное кол-во капсов'
#                     )
#                 ]
#             ))
#         elif arg == 'nwarns':
#             await interaction.popup(Modal(
#                 custom_id='Nwarns',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите максимальное кол-во варнов'
#                     )
#                 ]
#             ))
#         elif arg == 'добавить плохое слово':
#             await interaction.popup(Modal(
#                 custom_id='Add_badword',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите слово которое будет запрещено использовать на этом сервере'
#                     )
#                 ]
#             ))
#         elif arg == 'убрать плохое слово':
#             await interaction.popup(Modal(
#                 custom_id='Remove_badword',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите слово которое Вы хотите убрать из списка слов запрещённых на этом сервере'
#                     )
#                 ]
#             ))
#         elif arg == 'создать "свои комнаты"':

#             ctx = [i for i in bot.guilds if i.id == interaction.guild_id][0]
#             chlen_krokodila = [i for i in ctx.text_channels if i.id == interaction.channel_id][0]

#             if data[str(ctx.id)]['selfRoom'] != '0':
#                 for category in ctx.categories:
#                     [await chnl.delete() for chnl in category.channels if str(category.id) == data[str(ctx.id)]['selfRoom']["ct"]]
#                 [await i.delete() for i in ctx.categories if str(i.id) == data[str(ctx.id)]['selfRoom']["ct"] or str(i.id) == data[str(ctx.id)]['selfRoom']["ctp"]]
#                 data[str(ctx.id)]['selfRoom'] = '0'
#                 await chlen_krokodila.send(embed=discord.Embed(title='***Успешно***',
#                 description='Канал для создания комнат удалён',
#                 color=COLOR))
#             else:
                
#                 ct = await ctx.create_category(name='ССК', position=1)
#                 vcch = await ctx.create_voice_channel(name=f'Создать комнату', category=ct)
#                 chn = await ctx.create_text_channel(name=f'Настройка комнаты', category=ct)
#                 ctp = await ctx.create_category(name='Свои румы', position=2)
#                 stb_gld: discord.Guild = bot.get_guild(id=981511419042361344)
#                 emb = discord.Embed(title='***⚙️ Управление приватными комнатами***',
#                                         description=f'<:corona1:1020971032309403758> - назначить нового создателя комнаты \n\
#                             <:notebook1:1020971040416993280> - ограничить/выдать доступ к комнате \n\
#                             <:meet1:1020971037741043713> - задать новый лимит участников \n\
#                             <:locker1:1020971036252053524> - закрыть/открыть комнату \n\
#                             <:pencil1:1020971043856330782> - изменить название комнаты \n\
#                             <:eye1:1020971035014746162> - скрыть/открыть комнату \n\
#                             <:door1:1020971033756450866> - выгнать участника из комнаты \n\
#                             <:microphone1:1020971039141920819> - ограничить/выдать право говорить',
#                                         color=COLOR)
#                 await chn.send(embed=emb,
#                             components=[
#                                 [
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971032309403758)),
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971040416993280)),
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971037741043713)),
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971036252053524))
#                                        ],
#                                        [
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971043856330782)),
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971035014746162)),
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971033756450866)),
#                                            Button(emoji=await stb_gld.fetch_emoji(1020971039141920819))
#                                        ]
#                             ]
#                             )
#                 data[str(ctx.id)]['selfRoom'] = {"ct": str(ct.id), "ctp": str(ctp.id), "vc": str(vcch.id), "tc": str(chn.id)}
#                 await chlen_krokodila.send(embed=discord.Embed(title='***Успешно***',
#                 description='Канал для создания комнат создан',
#                 color=COLOR))
#                 with open('users.json', 'w') as file:
#                     json.dump(data, file, indent=4)

#         elif arg == 'префикс':
#             await interaction.popup(Modal(
#                 custom_id='Prefix',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите prefix'
#                     )
#                 ]
#             ))
#         elif arg == 'Указать свой текст при выборе ролей':
#             await interaction.popup(Modal(
#                 custom_id='Selftitle',
#                 title=' ',
#                 components=[
#                     TextInput(
#                         style=TextStyleType.SHORT,
#                         custom_id='qwertyuiop',
#                         label='Введите selftitle'
#                     )
#                 ]
#             ))
#         elif arg == 'настроить роли при входе на сервер':
#             for rls in serverRoles:
#                 await interaction.send(components=SelectMenu(
#                     custom_id='jnrl1',
#                     placeholder=f'Укажите роли которые будут выдоваться участникам при входе на сервер',
#                     max_values=len(rls),
#                     min_values=0,
#                     options=[SelectOption(label=i.name, value=str(i.id)) for i in rls]
#                 ))
#         elif arg == 'список join ролей':
#             emb = discord.Embed(title=f'Успешно',
#                                 description=f'*Роли:*',
#                                 color=COLOR)
#             n = 0
#             while len(roles) != n:
#                 emb.add_field(name=f'{(await interaction.guild.get_role(int(roles[n]))).name}', value=f'{roles[n]}',
#                               inline=True)
#                 n += 1

#             await [i for i in bot.get_all_channels() if i.id == interaction.channel_id][0].send(embed=emb)

#         elif arg == 'classes':
#             pass
#             '''with open('users.json', 'r') as file:
#                 data = json.load(file)
#                 Classes = data[str(interaction.guild_id)]['ROLES']
#             emb = discord.Embed(title=f'Успешно',
#                 escription=f'*Роли:*',
#                 color=COLOR)
#             n = 0
#             while len(Classes) != n:
#                 with open('users.json', 'r') as file:
#                     ClassesRoles = data[str(interaction.guild_id)]['ROLES'][str(Classes[n])][0]
#                 emb.add_field(name=f'{str(Classes[n])}', value=''.join(ClassesRoles), inline=True)
#                 n += 1
#             await [i for i in bot.get_all_channels() if i.id == interaction.channel_id][0].send(embed=emb)'''
#         elif arg == 'add_IgnoreChannel':
#             pass
#         elif arg == 'add_IgnoreRole':
#             pass
#         elif arg == 'IgnoreRoles':
#             pass
#         elif arg == 'добавить канал с инфорацией': #переимовать
#             ctx = [i for i in bot.guilds if i.id == interaction.guild_id][0]

#             with open('glb_vote.json', 'r') as file:
#                 vt_data = json.load(file)

#             if not(str(ctx.id) in [k for k in vt_data.keys()]):

#                 ct = await ctx.create_category(name='ссссссс', position=1)
#                 chn = await ctx.create_text_channel(name=f'Голосование от wave', category=ct)
#                 chn1 = await ctx.create_text_channel(name=f'Информация от wave', category=ct)

#                 vt_data.update({
#                     ctx.id: {
#                         'vote_id': chn.id,
#                         'info_id': chn1.id
#                     }
#                 })
#             else:
#                 await ctx.get_channel(vt_data[str(ctx.id)]['vote_id']).category.delete()
#                 await ctx.get_channel(vt_data[str(ctx.id)]['vote_id']).delete()
#                 await ctx.get_channel(vt_data[str(ctx.id)]['info_id']).delete()
#                 del vt_data[str(ctx.id)]

#             with open('glb_vote.json', 'w') as file:
#                 json.dump(vt_data, file, indent=4)




#         with open('users.json', 'w') as file:
#             json.dump(data, file, indent=4)
        
            

            


# # =======================================================================================================================================   roles
# @bot.event
# async def on_select_option(interaction):
#     try:
#         with open('users.json', 'r') as file:
#             data = json.load(file)
#             COLOR = int(data[str(interaction.guild_id)]['COLOR'], 16)

#         serverRoles = []
#         for i in range(0, len(interaction.guild.roles),
#                        24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             serverRoles.append(interaction.guild.roles[
#                                i:i + 24])  # второй важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     except:
#         pass

#     if interaction.component.placeholder == 'Укажите классы в которые вы хотите добавить роли':
#         for i in interaction.values:
#             for rls in serverRoles:
#                 await interaction.send(embed=discord.Embed(
#                     title=f'Укажите роли которые вы хотите добавить в класс {i}',
#                     color=COLOR
#                 ),
#                 components=[
#                     Select(
#                         placeholder=f'Укажите роли которые вы хотите добавить в класс *{i}',
#                         max_values=len(rls),
#                         min_values=0,
#                         options=[Sel(label=i.name, value=i.id) for i in rls]
#                     )
#                     ]
#                 )

#     elif interaction.component.placeholder.startswith('Укажите роли которые вы хотите добавить в класс'):
#         data[str(interaction.author.guild.id)]['ROLES'][interaction.component.placeholder.split('*')[1]][0] = interaction.values
#         data[str(interaction.author.guild.id)]['ROLES'][interaction.component.placeholder.split('*')[1]][1] = [0 for i in interaction.values]
#         await interaction.send(embed=discord.Embed(
#             title=f'Роли выбранны',
#             color=COLOR
#         ))

#     with open('users.json', 'w') as file:
#         json.dump(data, file, indent=4)

#         # ==========================================================================================================================   IDA
# @client.component('IDA1')
# async def vgf(interaction, int_val):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(interaction.guild_id)]['idAdminchennel'] = ''.join(int_val)
#         json.dump(data, file, indent=4)
#     await interaction.send('+')
#     with open('users.json', 'w') as file:
#         json.dump(data, file, indent=4)
#     await interaction.send(embeds=discord.Embed(
#         title="Успешно",
#         description=f"*Канал администратора изменен на {int_val}*",
#     ), ephemeral=True)
# # =======================================================================================================================    join roles
# @client.component('jnrl1')
# async def jf(interaction, int_val):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     data[str(interaction.guild_id)]['JoinRoles'] = int_val
#     await interaction.send('роли выбранны')
#     with open('users.json', 'w') as file:
#         json.dump(data, file, indent=4)
# #===============================================================================================     addclass
# @client.modal('Add_class')
# async def vvb(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     if not (shrt in data[str(ctx.guild_id)]['ROLES']):
#         with open('users.json', 'w') as file:
#             data[str(ctx.guild_id)]['ROLES'].update({shrt: [[], []]})
#             json.dump(data, file, indent=4)
#     await ctx.send(f'Класс {shrt} создан', ephemeral=True)
# #============================================================================== color

# @client.modal('Color')
# async def bbdbkn(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(ctx.guild_id)]['COLOR'] = '0x' + shrt
#         json.dump(data, file, indent=4)
#     await ctx.send('успешно', ephemeral=True)

# #=========================================================================    ercolor

# @client.modal('ErColor')
# async def sgdhj(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(ctx.guild_id)]['ErCOLOR'] = '0x' + shrt
#         json.dump(data, file, indent=4)
#     await ctx.send('успешно', ephemeral=True)

# #======================================================================      ncaps
# @client.modal('Ncaps')
# async def opkijn(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(ctx.guild_id)]['nCaps'] = shrt
#         json.dump(data, file, indent=4)
#     await ctx.send('Успешно', ephemeral=True)

# #=========================================================================    nwarns
# @client.modal('Nwarns')
# async def opkin(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(ctx.guild_id)]['nWarns'] = shrt
#         json.dump(data, file, indent=4)
#     await ctx.send('Успешно', ephemeral=True)

# #========================================================================     addbadword
# @client.modal('Add_badword')
# async def opkvijn(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(ctx.guild_id)]['BADWORDS'].append(shrt)
#         json.dump(data, file, indent=4)
#     await ctx.send(f"*В список badwords добавленно слово ||{shrt}||*", ephemeral=True)


# #======================================================================    rem badword
# @client.modal('Remove_badword')
# async def opeijn(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     if shrt in data[str(ctx.guild_id)]['BADWORDS']:
#         with open('users.json', 'w') as file:
#             data[str(ctx.guild_id)]['BADWORDS'].pop(data[str(ctx.guild_id)]['BADWORDS'].index(shrt))
#             json.dump(data, file, indent=4)
#         await ctx.send(f"*Слово ||{shrt}|| больше нет в списке плохих слов*")
#     else:
#         await ctx.send('слова нет', ephemeral=True)


# #=====================================================================    prefix
# @client.modal('Prefix')
# async def oskijn(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(ctx.guild_id)]['PREFIX'] = shrt
#         json.dump(data, file, indent=4)
#     await ctx.send(f"*Ваш префикс изменен на {shrt}*", ephemeral=True)


# #======================================================================   selftitle
# @client.modal('Selftitle')
# async def opasn(ctx, shrt):
#     with open('users.json', 'r') as file:
#         data = json.load(file)
#     with open('users.json', 'w') as file:
#         data[str(ctx.guild_id)]['SelfTitle'] = shrt
#         json.dump(data, file, indent=4)
#     await ctx.send(f"*Текст выбора ролей успешно изменён на {shrt}*", ephemeral=True)


#=======================================================================================================================
# @bot.event
# async def on_command_error(ctx, error):
#     with open('users.json', 'r') as file:
#         dataServerID = json.load(file)
#         ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
#         pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
    # if isinstance(error, commands.errors.CommandNotFound):
    #     print(error)
    #     found = re.findall(r'Command \s*"([^\"]*)"', str(error))
    #     await ctx.send(embed=discord.Embed(
    #         title="Ошибка",
    #         description=f"*Команды `{''.join(found)}` не существует*",
    #         color = ErCOLOR
    #     ))
    # elif isinstance(error, commands.errors.MemberNotFound):
    #     found = re.findall(r'Member \s*"([^\"]*)"', str(error))
    #     await ctx.send(embed=discord.Embed(
    #         title="Ошибка",
    #         description=f"*Участник `{''.join(found)}` не найден*",
    #         color = ErCOLOR
    #     ))
    # elif isinstance(error, commands.errors.CommandInvokeError):
    #     pass

#=======================================================================================================================


# @bot.event
# async def on_error(ctx, err):
#     print('ошибка', ':', ctx)
#     print(err)


def main():

    loop = asyncio.get_event_loop()

    task2 = loop.create_task(bot.start(os.getenv('TOKEN')))
    task1 = loop.create_task(client._ready())

    gathered = asyncio.gather(task1, task2, loop=loop)
    loop.run_until_complete(gathered)


if __name__ == '__main__':
    main()
