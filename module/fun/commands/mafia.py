def setup(bot):
    
    import discord
    import json
    import asyncio
    import random
    from discord.ext import commands
    from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption, Interaction
    
    @bot.command()
    async def mafia(ctx):
        ctg = await ctx.guild.create_category('мафия')
        mnchn = await ctx.guild.create_text_channel('настройки', category=ctg)
        await ctx.guild.create_text_channel('Город', category=ctg)
        await ctx.guild.create_voice_channel('город', category=ctg)

        with open('users.json', 'r') as file:
            dat = json.load(file)
        if not(str(mnchn.guild.id) in [str(k) for k in dat[str(mnchn.guild.id)]['Mafrooms'].keys()]):
            dat[str(mnchn.guild.id)]['Mafrooms'].update({
                str(mnchn.id): {
                    'Settings': {
                        'actRoles': [],
                        'mafs': 1,
                    },
                    'ownMaf': ctx.author.id,
                    "MEMBERS": {}
                }})
        with open('users.json', 'w') as file:
            json.dump(dat, file, indent=4)

        mfRoles = ['доктор', 'шериф', 'любовница', 'дон-мафии', 'маньяк', 'комиссар', 'лунатик', 'адвокат', 'оборотень', 'студент', 'зеркало', 'журналист']

        await mnchn.send(embed=discord.Embed(
            title='***Добро пожаловать в игру мафия***',
            description=f'***Настройте пожалуйста игру*** \n\
                        👤 - кол-во игроков \n\
                        🔪 - кол-во мафий\n\
                        👞 - выгнать человека\n\
        '),
        components=[
            [
                Button(emoji='👤', style=1),
                Button(emoji='🔪', style=1),
                Button(emoji='👞', style=1)
            ],
            Select(
                placeholder="выберете доп. персонажей",
                max_values=len(mfRoles),
                min_values=0,
                options=[SelectOption(label=i, value=i) for i in mfRoles]
            ),
            [
                Button(label='Старт!', style=1)
            ]
        ])



    @bot.listen('on_select_option')
    async def my_select_option(interaction):
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
                ErCOLOR = int(data[str(interaction.guild.id)]['ErCOLOR'], 16)
                AdminchennelID = data[str(interaction.guild.id)]['idAdminchennel']
                roles = data[str(interaction.guild.id)]['ROLES']
            if interaction.component.placeholder == 'выберете доп. персонажей':
                await interaction.send(embed=discord.Embed(
                title='***Успешно***',
                description=f'Доп персонажи успешно выбраны!',
                color=COLOR
                ))
                [await interaction.guild.create_text_channel(str(i), category=interaction.channel.category) for i in interaction.values]
                with open('users.json', 'w') as file:
                    data[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['actRoles'] = interaction.values
                    json.dump(data, file, indent=4)
                with open('users.json', 'r') as file:
                    data = json.load(file)
                    
                    [await i.delete() for i in interaction.channel.category.channels if not(i.name in data[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['actRoles']) and not(i.name in ['город', 'настройки'])]
        except:
            pass


    @bot.event
    async def on_button_click(interaction):
        if interaction.channel.name == 'настройки':
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                ownMaf = int(dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['ownMaf'])
            if str(interaction.component.emoji) == '👤':
                await interaction.send('напишите число участников')
                ms = await bot.wait_for(event='message')

                if ms.author == interaction.guild.get_member(ownMaf):
                    [await i.edit(user_limit=int(ms.content)) for i in interaction.channel.category.channels if i.name == 'город']
                else:
                    while ms.author != interaction.guild.get_member(ownMaf):
                        if ms.author != interaction.guild.get_member(ownMaf): continue
                        ms = await bot.wait_for(event='message')
                        try:
                            [await i.edit(user_limit=int(ms.content)) for i in interaction.channel.category.channels if i.name == 'город']
                        except:
                            pass
            elif str(interaction.component.emoji) == '👞':
                await interaction.send('напишите @участник  которого хотите выгнать')
                ms = await bot.wait_for(event='message')
                if ms.author == interaction.guild.get_member(ownMaf):
                    [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                else:
                    while ms.author != interaction.guild.get_member(ownMaf):
                        if ms.author != interaction.guild.get_member(ownMaf): continue
                        ms = await bot.wait_for(event='message')
                        try:
                            [await i.move_to(None) for i in ms.author.voice.channel.members if ms.content == i.mention]
                        except:
                            pass
            elif str(interaction.component.emoji) == '🔪':
                await interaction.send('напишите число мафий')
                ms = await bot.wait_for(event='message', channel=interaction.channel)
                if ms.author == interaction.guild.get_member(ownMaf):
                    with open('users.json', 'w') as file:
                        dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['mafs'] = int(ms.content)
                        json.dump(dataServerID, file, indent=4)
                else:
                    while ms.author != interaction.guild.get_member(ownMaf):
                        if ms.author != interaction.guild.get_member(ownMaf): continue
                        ms = await bot.wait_for(event='message')
                        try:
                            with open('users.json', 'w') as file:
                                dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)][
                                    'Settings']['mafs'] = int(ms.content)
                                json.dump(dataServerID, file, indent=4)
                        except:
                            pass






            elif interaction.component.label == 'Старт!':


                with open('users.json', 'w') as file:
                    for i in interaction.channel.category.channels:
                        if i.name == 'Город':
                            for ii in ii.members:
                                if dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['mafs']:
                                    dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['MEMBERS'].update({
                                        ii.id: 'мафия'
                                    })
                                    dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['mafs'] -= 1

                                elif dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['actRoles']:
                                    dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['MEMBERS'].update({
                                        ii.id: dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['actRoles'].pop(random.randrange(len(dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)])))
                                    })
                                else:
                                    dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['MEMBERS'].update({
                                        ii.id: None
                                    })
                    json.dump(dataServerID, file, indent=4)

                pr = discord.PermissionOverwrite()
                pr.view_channel = False
                await interaction.channel.category.set_permissions(overwrite=pr, target=interaction.guild.roles[0])

                pr.view_channel = True
                for i in [k for k in dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['MEMBERS'].keys()]:
                    await interaction.channel.category.channels[interaction.channel.category.channels.index('Город')].set_permissions(overwrite=pr, target=interaction.guild.get_member(i))
                    [await e.set_permissions(overwrite=pr, target=interaction.guild.get_member(i)) for e in interaction.channel.category.channels if dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['MEMBERS'][i] == e.name]
                    [await e.send(embed=discord.Embed(title=f'{interaction.guild.get_member(i).mention}', description=f'вам досталась роль {e.name}')) for e in interaction.channel.category.channels if dataServerID[str(interaction.guild.id)]['Mafrooms'][str(interaction.channel.id)]['Settings']['MEMBERS'][i] == e.name]

