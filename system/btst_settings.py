import discord
from discord.ext import commands
from email.errors import InvalidMultipartContentTransferEncodingDefect
import json
from BTSET import BD


class CheckMesBTST:
    def __init__(self, interaction):
        self.interaction: discord_components.Interaction = interaction

    def check(self, mes: discord.Message):
        return self.interaction.author == mes.author and self.interaction.channel == mes.channel


class SetForBTST():
    def __init__(self, bot, interaction, old_emb, arg):
        self.bot = bot
        self.interaction: discord_components.Interaction = interaction
        self.old_emb = old_emb
        self.arg = arg
        self.check = CheckMesBTST(interaction)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)

        self.data = data
        self.roles = data[str(interaction.guild.id)]['JoinRoles']
        self.COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
        self.Classes = data[str(interaction.guild.id)]['ROLES']
        self.chlens = []
        self.serverRoles = []


        for i in range(0, len(interaction.guild.roles),
                       24):
            self.serverRoles.append(interaction.guild.roles[
                               i:i + 24])

        for i in range(0, len([chlen for chlen in interaction.guild.text_channels]),
                       24):
            self.chlens.append([chlen for chlen in interaction.guild.text_channels][
                          i:i + 24])


    async def music(self):
        if [i for i in self.interaction.guild.categories if i.name == 'music']:
            for category in self.interaction.guild.categories:
                [await chnl.delete() for chnl in category.channels if category.name == 'music']
            [await i.delete() for i in self.interaction.guild.categories if i.name == 'music']
        else:

            with open('music.json', 'r') as file:
                data_mus: dict = json.load(file)
            if not (str(self.interaction.guild.id) in [i for i in data_mus.keys()]):
                data_mus.update(
                    {
                        self.interaction.guild.id: {
                            'songs': [],
                            'pl_id': None,
                            'chl_id': None
                        }
                    }
                )

            with open('music.json', 'w') as file:
                json.dump(data_mus, file, indent=4)

            ctg = await self.interaction.guild.create_category(name='music')
            txt_cnlen = await ctg.create_text_channel(name='великий дон ягон')
            vc_clen = await ctg.create_voice_channel(name='music')
            embd = discord.Embed(
                title='***                               wave player***',
                description=f'=================================',
                colour=0x00FFFF
            )
            embd.add_field(name='сейчас играет:', value='ничего')

            comp = [
                [
                    Button(emoji='◀', style=2),
                    Button(emoji='⏯', style=2),
                    Button(emoji='▶', style=2),
                    Button(emoji='🔀', style=2)
                ],
                [
                    Button(emoji='➕', style=2),
                    Button(emoji='🔊', style=2),
                    Button(emoji='🔈', style=2),
                    Button(emoji='🔇', style=2)
                ]
            ]

            msc_player = await txt_cnlen.send(embed=embd, components=comp)

            await vc_clen.connect()

            with open('music.json', 'r') as file:
                data_mus = json.load(file)
                data_mus[str(self.interaction.guild.id)]['pl_id'] = msc_player.id
                data_mus[str(self.interaction.guild.id)]['chl_id'] = txt_cnlen.id
            with open('music.json', 'w') as file:
                json.dump(data_mus, file, indent=4)

    async def role_set(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='Укажите классы в которые вы хотите добавить роли', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb,
               components=[
                   Select(
                       placeholder='Укажите классы в которые вы хотите добавить роли',
                       max_values=len(self.data[str(self.interaction.guild.id)]['ROLES']),
                       min_values=1,
                       options=[SelectOption(label=str(i), value=str(i)) for i in
                                [k for k in self.Classes.keys()]]
                   ),
                   [
                       Button(label='модерация'),
                       Button(label='настройка бота'),
                       Button(label='настройка рейтинга')
                   ],
                   [
                       Button(label='<---'),
                       Button(label='OK'),
                       Button(label='--->')
                   ]
               ])

    async def add_roleclass(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с названием класса', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not (ms.content in data[str(self.interaction.guild.id)]['ROLES']):
            with open(f'{BD}users.json', 'w') as file:
                data[str(self.interaction.guild.id)]['ROLES'].update({ms.content: [[], []]})
                json.dump(data, file, indent=4)

        await ms.delete()

    async def color_choice(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)
        await self.interaction.edit_origin()

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        with open(f'{BD}users.json', 'w') as file:
            data[str(self.interaction.guild.id)]['COLOR'] = '0x' + ms.content
            json.dump(data, file, indent=4)
        await ms.delete()

    async def er_col_choice(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)
        await self.interaction.edit_origin()

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        with open(f'{BD}users.json', 'w') as file:
            data[str(self.interaction.guild.id)]['ErCOLOR'] = '0x' + ms.content
            json.dump(data, file, indent=4)
        await ms.delete()

    async def admin_clen(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.old_emb.description,
            color=self.old_emb.color
        )
        emb.add_field(name='выберете канал который хотите сделать каналом администратора',
                      value=f'страница 1 из {len(self.chlens)}')

        await self.interaction.message.edit(embed=emb, components=[
            Select(
                placeholder='выберете канал который хотите сделать каналом администратора',
                options=[SelectOption(label=i.name, value=str(i.id)) for i in self.chlens[0]]
            ),
            [
                Button(label='модерация'),
                Button(label='настройка бота'),
                Button(label='настройка рейтинга')
            ],
            [
                Button(label='<---'),
                Button(label='OK'),
                Button(label='--->')
            ]
        ])
        await self.interaction.edit_origin()

    async def ncaps(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        with open(f'{BD}users.json', 'w') as file:
            data[str(self.interaction.guild.id)]['nCaps'] = ms.content
            json.dump(data, file, indent=4)
        await ms.delete()

    async def nwarns(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с nwarns', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        with open(f'{BD}users.json', 'w') as file:
            data[str(self.interaction.guild.id)]['nWarns'] = ms.content
            json.dump(data, file, indent=4)
        await ms.delete()

    async def add_bad_word(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        with open(f'{BD}users.json', 'w') as file:
            data[str(self.interaction.guild.id)]['BADWORDS'].append(ms.content)
            json.dump(data, file, indent=4)
        await ms.delete()

    async def remove_bod_word(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с словом которое Вы хотите исключить из списка badwords', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if ms.channel in data[str(self.interaction.guild.id)]['BADWORDS']:
            with open(f'{BD}users.json', 'w') as file:
                data[str(self.interaction.guild.id)]['BADWORDS'].pop(
                    data[str(self.interaction.guild.id)]['BADWORDS'].index(ms.content))
                json.dump(data, file, indent=4)
        else:
            await self.interaction.send('слова нет')
        await ms.delete()

    async def selfrooms(self):
        ctx = [i for i in self.bot.guilds if i.id == self.interaction.guild_id][0]
        chlen_krokodila = [i for i in ctx.text_channels if i.id == self.interaction.channel_id][0]

        if self.data[str(ctx.id)]['selfRoom'] != '0':
            for category in ctx.categories:
                [await chnl.delete() for chnl in category.channels if str(category.id) == self.data[str(ctx.id)]['selfRoom']["ct"]]
            [await i.delete() for i in ctx.categories if str(i.id) == self.data[str(ctx.id)]['selfRoom']["ct"] or str(i.id) == self.data[str(ctx.id)]['selfRoom']["ctp"]]
            self.data[str(ctx.id)]['selfRoom'] = '0'
            await chlen_krokodila.send(embed=discord.Embed(title='***Успешно***',
            description='Канал для создания комнат удалён',
            color=self.COLOR))
        else:

            ct = await ctx.create_category(name='ССК', position=1)
            vcch = await ctx.create_voice_channel(name=f'Создать комнату', category=ct)
            chn = await ctx.create_text_channel(name=f'Настройка комнаты', category=ct)
            ctp = await ctx.create_category(name='Свои румы', position=2)
            stb_gld: discord.Guild = self.bot.get_guild(id=981511419042361344)
            emb = discord.Embed(title='***⚙️ Управление приватными комнатами***',
                                    description=f'<:corona1:1020971032309403758> - назначить нового создателя комнаты \n\
                        <:notebook1:1020971040416993280> - ограничить/выдать доступ к комнате \n\
                        <:meet1:1020971037741043713> - задать новый лимит участников \n\
                        <:locker1:1020971036252053524> - закрыть/открыть комнату \n\
                        <:pencil1:1020971043856330782> - изменить название комнаты \n\
                        <:eye1:1020971035014746162> - скрыть/открыть комнату \n\
                        <:door1:1020971033756450866> - выгнать участника из комнаты \n\
                        <:microphone1:1020971039141920819> - ограничить/выдать право говорить',
                                    color=self.COLOR)
            await chn.send(embed=emb,
                        components=[
                            [
                                       Button(emoji=await stb_gld.fetch_emoji(1020971032309403758)),
                                       Button(emoji=await stb_gld.fetch_emoji(1020971040416993280)),
                                       Button(emoji=await stb_gld.fetch_emoji(1020971037741043713)),
                                       Button(emoji=await stb_gld.fetch_emoji(1020971036252053524))
                                   ],
                                   [
                                       Button(emoji=await stb_gld.fetch_emoji(1020971043856330782)),
                                       Button(emoji=await stb_gld.fetch_emoji(1020971035014746162)),
                                       Button(emoji=await stb_gld.fetch_emoji(1020971033756450866)),
                                       Button(emoji=await stb_gld.fetch_emoji(1020971039141920819))
                                   ]
                        ]
                        )
            self.data[str(ctx.id)]['selfRoom'] = {"ct": str(ct.id), "ctp": str(ctp.id), "vc": str(vcch.id), "tc": str(chn.id)}
            await chlen_krokodila.send(embed=discord.Embed(title='***Успешно***',
            description='Канал для создания комнат создан',
            color=self.COLOR))
            with open(f'{BD}users.json', 'w') as file:
                json.dump(self.data, file, indent=4)

    async def prefix(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        with open(f'{BD}users.json', 'w') as file:
            data[str(self.interaction.guild.id)]['PREFIX'] = ms.content
            json.dump(data, file, indent=4)
        await ms.delete()

    async def selftitle(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.arg,
            color=self.COLOR
        )
        emb.add_field(name='отправьте сообщение с цветом в hex', value='страница 1 из 1')
        await self.interaction.message.edit(embed=emb)

        ms: discord.Message = await self.bot.wait_for('message', check=self.check.check)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        with open(f'{BD}users.json', 'w') as file:
            data[str(self.interaction.guild.id)]['SelfTitle'] = ms.content
            json.dump(data, file, indent=4)
        await ms.delete()

    async def join_roles(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.old_emb.description,
            color=self.old_emb.color
        )
        emb.add_field(name=f'Укажите роли которые будут выдоваться участникам при входе на сервер',
                      value=f'страница 1 из {len(self.serverRoles)}')

        await self.interaction.message.edit(components=[
            Select(
                placeholder=f'Укажите роли которые будут выдоваться участникам при входе на сервер',
                max_values=len(self.serverRoles[0]),
                min_values=0,
                options=[SelectOption(label=i.name, value=str(i.id)) for i in self.serverRoles[0]]
            ),
            [
                Button(label='модерация'),
                Button(label='настройка бота'),
                Button(label='настройка рейтинга')
            ],
            [
                Button(label='<---'),
                Button(label='OK'),
                Button(label='--->')
            ]
        ])

    async def info_clen(self):
        with open('glb_vote.json', 'r') as file:
            vt_data = json.load(file)

        if not (str(self.interaction.guild.id) in [k for k in vt_data.keys()]):

            ct = await self.interaction.guild.create_category(name='ссссссс', position=1)
            chn = await self.interaction.guild.create_text_channel(name=f'Голосование от wave', category=ct)
            chn1 = await self.interaction.guild.create_text_channel(name=f'Информация от wave', category=ct)

            vt_data.update({
                self.interaction.guild.id: {
                    'vote_id': chn.id,
                    'info_id': chn1.id
                }
            })
        else:
            await self.interaction.guild.get_channel(vt_data[str(self.interaction.guild.id)]['vote_id']).category.delete()
            await self.interaction.guild.get_channel(vt_data[str(self.interaction.guild.id)]['vote_id']).delete()
            await self.interaction.guild.get_channel(vt_data[str(self.interaction.guild.id)]['info_id']).delete()
            del vt_data[str(self.interaction.guild.id)]

        with open('glb_vote.json', 'w') as file:
            json.dump(vt_data, file, indent=4)


class SecSetForBTST():
    def __init__(self, bot, interaction, old_emb):
        self.bot = bot
        self.interaction: discord_components.Interaction = interaction
        self.old_emb = old_emb
        self.check = CheckMesBTST(interaction)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)

        self.data = data
        self.roles = data[str(interaction.guild.id)]['JoinRoles']
        self.COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
        self.Classes = data[str(interaction.guild.id)]['ROLES']
        self.chlens = []
        self.serverRoles = []

        for i in range(0, len(interaction.guild.roles),
                       24):
            self.serverRoles.append(interaction.guild.roles[
                                    i:i + 24])

        for i in range(0, len([chlen for chlen in interaction.guild.text_channels]),
                       24):
            self.chlens.append([chlen for chlen in interaction.guild.text_channels][
                               i:i + 24])


    async def rolecass_choice(self):
        emb = discord.Embed(
            title=self.old_emb.title,
            description=self.old_emb.description,
            color=self.old_emb.color
        )
        emb.add_field(name=f'Укажите роли которые вы хотите добавить в класс {self.interaction.values[0]}',
                      value=f'страница 1 из {len(self.serverRoles)}')
        await self.interaction.message.edit(embed=emb,
           components=[
               Select(
                   placeholder=f'Укажите роли которые вы хотите добавить в класс *{self.interaction.values[0]}',
                   max_values=len(self.serverRoles[0]),
                   min_values=0,
                   options=[SelectOption(label=i.name, value=i.id) for i in
                            self.serverRoles[0]]
               ),
               [
                   Button(label='модерация'),
                   Button(label='настройка бота'),
                   Button(label='настройка рейтинга')
               ],
               [
                   Button(label='<---'),
                   Button(label='OK'),
                   Button(label='--->')
               ]
           ])

    async def role_choice(self):
        self.data[str(self.interaction.author.guild.id)]['ROLES'][self.interaction.component.placeholder.split('*')[1]][
            0] = self.interaction.values
        self.data[str(self.interaction.author.guild.id)]['ROLES'][self.interaction.component.placeholder.split('*')[1]][1] = [0 for
                                                                                                               i in
                                                                                                               self.interaction.values]
        await self.interaction.send(embed=discord.Embed(
            title=f'Роли выбранны',
            color=self.COLOR
        ))

        with open(f'{BD}users.json', 'w') as file:
            json.dump(self.data, file, indent=4)

    async def admin_clen(self):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        data[str(self.interaction.guild.id)]['idAdminchennel'] = self.interaction.values[0]
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        await self.interaction.send(embed=discord.Embed(
            title="Успешно",
            description=f"*Канал администратора изменен на {self.interaction.values[0]}*",
        ))

    async def join_roles(self):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        data[str(self.interaction.guild.id)]['JoinRoles'] = self.interaction.values
        await self.interaction.send('роли выбранны')
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)


class ScrollSet():
    def __init__(self, bot, interaction, old_emb):
        self.bot = bot
        self.interaction: discord_components.Interaction = interaction
        self.old_emb = old_emb
        self.check = CheckMesBTST(interaction)

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)

        self.data = data
        self.roles = data[str(interaction.guild.id)]['JoinRoles']
        self.COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
        self.Classes = data[str(interaction.guild.id)]['ROLES']
        self.chlens = []
        self.serverRoles = []

        for i in range(0, len(interaction.guild.roles),
                       24):
            self.serverRoles.append(interaction.guild.roles[
                                    i:i + 24])

        for i in range(0, len([chlen for chlen in interaction.guild.text_channels]),
                       24):
            self.chlens.append([chlen for chlen in interaction.guild.text_channels][
                               i:i + 24])


    async def scroll_right(self):
        if self.interaction.message.embeds[0].fields[0].name\
                .startswith('Укажите роли которые вы хотите добавить в класс')\
            and int(self.interaction.message.embeds[0].fields[0].value.split()[1]) < len(self.serverRoles):
            emb = discord.Embed(
                title=self.old_emb.title,
                description=self.old_emb.description,
                color=self.old_emb.color
            )

            emb.add_field(name=self.interaction.message.embeds[0].fields[0].name,
                          value=f'страница {int(self.interaction.message.embeds[0].fields[0].value.split()[1]) + 1 if int(self.interaction.message.embeds[0].fields[0].value.split()[1]) < len(self.serverRoles) else self.interaction.message.embeds[0].fields[0].value.split()[1]} из {str(len(self.serverRoles))}')

            await self.interaction.message.edit(embed=emb,
                components=[
                    Select(
                        placeholder=self.interaction.message.embeds[0].fields[0].name,
                        max_values=len(self.serverRoles[int(self.interaction.message.embeds[0].fields[0].value.split()[1])]),
                        min_values=0,
                        options=[SelectOption(label=i.name, value=i.id) for i in
                                 self.serverRoles[int(self.interaction.message.embeds[0].fields[0].value.split()[1])]]
                    ),
                    [
                        Button(label='модерация'),
                        Button(label='настройка бота'),
                        Button(label='настройка рейтинга')
                    ],
                    [
                        Button(label='<---'),
                        Button(label='OK'),
                        Button(label='--->')
                    ]
                ])

        elif self.interaction.message.embeds[0].fields[0].name\
                .startswith('выберете канал который хотите сделать каналом администратора')\
                    and int(self.interaction.message.embeds[0].fields[0].value.split()[1]) < len(self.serverRoles):

            emb = discord.Embed(
                title=self.old_emb.title,
                description=self.old_emb.description,
                color=self.old_emb.color
            )
            emb.add_field(name=self.interaction.message.embeds[0].fields[0].name,
                          value=f'страница {int(self.interaction.message.embeds[0].fields[0].value.split()[1]) + 1 if int(self.interaction.message.embeds[0].fields[0].value.split()[1]) < len(self.chlens) else self.interaction.message.embeds[0].fields[0].value.split()[1]} из {str(len(self.chlens))}')


            await self.interaction.message.edit(embed=emb, components=[
                Select(
                    placeholder='выберете канал который хотите сделать каналом администратора',
                    options=[SelectOption(label=i.name, value=i.id) for i in
                                 self.chlens[int(self.interaction.message.embeds[0].fields[0].value.split()[1])]]
                ),
                [
                    Button(label='модерация'),
                    Button(label='настройка бота'),
                    Button(label='настройка рейтинга')
                ],
                [
                    Button(label='<---'),
                    Button(label='OK'),
                    Button(label='--->')
                ]
            ])
            await self.interaction.edit_origin()

    async def scroll_left(self):
        if self.interaction.message.embeds[0].fields[0].name \
                .startswith('Укажите роли которые вы хотите добавить в класс') \
                and int(self.interaction.message.embeds[0].fields[0].value.split()[1]) > 1:
            emb = discord.Embed(
                title=self.old_emb.title,
                description=self.old_emb.description,
                color=self.old_emb.color
            )

            emb.add_field(name=self.interaction.message.embeds[0].fields[0].name,
                          value=f'страница {int(self.interaction.message.embeds[0].fields[0].value.split()[1]) - 1} из {str(len(self.serverRoles))}')

            await self.interaction.message.edit(embed=emb,
                    components=[
                        Select(
                            placeholder=self.interaction.message.embeds[0].fields[0].name,
                            max_values=len(self.serverRoles[int(
                                self.interaction.message.embeds[0].fields[0].value.split()[
                                    1])-2]),
                            min_values=0,
                            options=[SelectOption(label=i.name, value=i.id) for i in
                                     self.serverRoles[int(
                                         self.interaction.message.embeds[0].fields[
                                             0].value.split()[1])-2]]
                        ),
                        [
                            Button(label='модерация'),
                            Button(label='настройка бота'),
                            Button(label='настройка рейтинга')
                        ],
                        [
                            Button(label='<---'),
                            Button(label='OK'),
                            Button(label='--->')
                        ]
                    ])

        elif self.interaction.message.embeds[0].fields[0].name\
                .startswith('выберете канал который хотите сделать каналом администратора')\
                    and int(self.interaction.message.embeds[0].fields[0].value.split()[1]) > 1:
                emb = discord.Embed(
                title=self.old_emb.title,
                description=self.old_emb.description,
                color=self.old_emb.color
                )

                emb.add_field(name=self.interaction.message.embeds[0].fields[0].name,
                            value=f'страница {int(self.interaction.message.embeds[0].fields[0].value.split()[1]) - 1} из {str(len(self.chlens))}')


                await self.interaction.message.edit(embed=emb, components=[
                    Select(
                        placeholder='выберете канал который хотите сделать каналом администратора',
                        options=[SelectOption(label=i.name, value=i.id) for i in
                                     self.chlens[int(
                                         self.interaction.message.embeds[0].fields[
                                             0].value.split()[1])-2]]
                    ),
                    [
                        Button(label='модерация'),
                        Button(label='настройка бота'),
                        Button(label='настройка рейтинга')
                    ],
                    [
                        Button(label='<---'),
                        Button(label='OK'),
                        Button(label='--->')
                    ]
                ])
                await self.interaction.edit_origin()

class SettingsPanel():
    def __init__(self, bot, interaction):
        self.bot = bot
        self.interaction: discord_components.Interaction = interaction

        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)

        self.COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)

    settings_for_btst = {
        'модерация': {
            'настроить роли': 'выбрать роли которые может выдавать бот',
            'добавить класс ролей': 'добавить класс ролей',
            'настроить аудит': 'этой штуки нет',
            'канал администратора': 'канал администратора',
            'кол-во капсов для предупреждения': 'количество сообщений написанное пользователем капсом до получения им предупреждения',
            'кол-во варнов для бана': 'количество предупреждений которое может получить пользователь до бана',
            'добавить плохое слово': 'добавить слово за использование которого пользователь получит предупреждение',
            'префикс': 'выбрать префикс на который реагирует бот',
            'указать свой текст при выборе ролей': 'текст при выборе роли (у каждого класса разный)',
            'убрать плохое слово': 'убрать слово за использование которого пользователь получит предупреждение'
        },
        'настройка бота': {
            'настроить цвет': 'цвет сообщений бота',
            'настроить цвет ошибок': 'цвет сообщений бота при ошибке',
            'музыка': 'создать категорию с каналами для музаки',
            'создать "свои комнаты"': '-',
            'добавить канал с инфорацией': 'канал с информацией от WaveBot',
            'роли для новых участников': 'выбрать роли которые будут выдаваться людям при заходе на сервер',

        },
        'настройка рейтинга': {}
    }

    async def btst_set_def(self, f=0):
        preference_set_for_best = ['канал администратора', 'настроить цвет', 'префикс']

        emb = discord.Embed(
            title='―――――――――*Wave Settings*―――――――――――',
            description='.',
            color=self.COLOR
        )
        emb.add_field(name='это настройки WaveBot',
                      value='Вы можете выбрать раздел или сразу открыть рекомендуемые настройки')

        comp = [
            Select(placeholder='рекомендуем настроить', options=[SelectOption(label=i, value=i) for i in preference_set_for_best], max_values=1),
            [
                Button(label='модерация'),
                Button(label='настройка бота'),
                Button(label='настройка рейтинга')
            ],
            [
                Button(label='<---'),
                Button(label='OK'),
                Button(label='--->')
            ]]

        if f:
            await self.interaction.send(embed=emb, components=comp)
        else:
            await self.interaction.message.edit(embed=emb, components=comp)

    async def tabs_choice(self):
        keys = []
        items = []

        for key in SettingsPanel.settings_for_btst[f'{self.interaction.component.label}']:
            keys.append(key)
            items.append(SettingsPanel.settings_for_btst[f'{self.interaction.component.label}'][key])

        emb = discord.Embed(
            title=self.interaction.message.embeds[0].title,
            description=f'**{self.interaction.component.label}**',
            color=self.COLOR
        )
        emb.add_field(name=f'{keys[0]}', value=f'{items[0]}')
        emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
        await self.interaction.message.edit(embed=emb, components=self.interaction.message.components)

    async def settings_choice_right(self):
        old_emb: discord.Embed = self.interaction.message.embeds[0].description.replace('*', '')

        keys = []
        keys.append(self.interaction.message.embeds[0].fields[0].name)
        keys.extend(self.interaction.message.embeds[0].fields[1].value.replace('.', '').replace('*', '').split('\n'))

        keys.append(keys.pop(0))

        emb = discord.Embed(
            title=self.interaction.message.embeds[0].title,
            description=f'**{old_emb}**',
            color=self.COLOR
        )
        emb.add_field(name=f'{keys[0]}', value=f'{SettingsPanel.settings_for_btst[old_emb][keys[0]]}')
        emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
        await self.interaction.message.edit(embed=emb)

    async def settings_choice_left(self):
        old_emb: discord.Embed = self.interaction.message.embeds[0].description.replace('*', '')

        keys = []
        keys.append(self.interaction.message.embeds[0].fields[0].name)
        keys.extend(self.interaction.message.embeds[0].fields[1].value.replace('.', '').replace('*', '').split('\n'))

        keys.insert(0, keys.pop(-1))
        emb = discord.Embed(
            title=self.interaction.message.embeds[0].title,
            description=f'**{old_emb}**',
            color=self.COLOR
        )
        emb.add_field(name=f'{keys[0]}', value=f'{SettingsPanel.settings_for_btst[old_emb][keys[0]]}')
        emb.add_field(name='.', value='**' + "\n".join(keys[1:]) + '**', inline=False)
        await self.interaction.message.edit(embed=emb)

