def setup(bot):
    import discord
    from discord import Spotify
    from discord.ext import commands
    import json
    

    @bot.command()
    async def server_info(ctx):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            
        emb = discord.Embed(title=f'Информация о сервере ***{str(ctx.message.guild)}***',
                            description="Основная информация",
                            color=COLOR
                            )
        emb.set_thumbnail(url=ctx.author.guild.icon_url) 
        emb.add_field(name='Количество участников: ', value=ctx.message.guild.member_count)
        emb.add_field(name='Владелец: ', value=ctx.message.guild.owner)
        emb.add_field(name='Дата создания: ', value=ctx.message.guild.created_at.strftime("%d.%m.%y"))
        await ctx.send(embed=emb)

    @bot.command() #Доделать. Знаю что доделать делаю делаю и думаю о том что ты пидр ведь мог бы и сам сделать а ты что-то другое делаешь а мне ещё документацию писать я тут сдохну 
    async def server_info_channel(ctx, arg=None):
        if arg == 'on':
            if not('📊Info📊' in [i.name for i in ctx.guild.categories]):
                ct = await ctx.guild.create_category(name='📊Info📊', position=0)
                await ctx.guild.create_voice_channel(name=f'👥Members: {len(ctx.guild.members)}👥', category=ct)
                await ctx.guild.create_voice_channel(name=f'🤖Bots: {len([i for i in ctx.guild.members if i.bot])}🤖', category=ct)
                await ctx.guild.create_voice_channel(name=f'👤Humans: {len(ctx.guild.members) - len([i for i in ctx.guild.members if i.bot])}👤', category=ct)
                pr = discord.PermissionOverwrite()
                pr.connect = False
                [await chlen.set_permissions(target=ctx.guild.roles[0], overwrite=pr) for chlen in ct.channels]
        if arg == 'off':
            if '📊Info📊' in [i.name for i in ctx.guild.categories]:
                [await i.delete() for i in [ii.channels for ii in ctx.guild.categories if ii.name == '📊Info📊'][0]]
                [await ii.delete() for ii in ctx.guild.categories if ii.name == '📊Info📊']

                
    @bot.listen('on_member_join')
    async def srinfo(member):
        roomNames=[f'👥Members: {len(member.guild.members)}👥', f'🤖Bots: {len([i for i in member.guild.members if i.bot])}🤖', f'👤Humans: {len(member.guild.members) - len([i for i in member.guild.members if i.bot])}👤']
        if '📊Info📊' in [i.name for i in member.guild.categories]:
                [await i.edit(name=roomNames.pop(0)) for i in [ii.channels for ii in member.guild.categories if ii.name == '📊Info📊'][0]]


    @bot.event
    async def on_member_remove(member):
        roomNames=[f'👥Members: {len(member.guild.members)}👥', f'🤖Bots: {len([i for i in member.guild.members if i.bot])}🤖', f'👤Humans: {len(member.guild.members) - len([i for i in member.guild.members if i.bot])}👤']
        if '📊Info📊' in [i.name for i in member.guild.categories]:
                [await i.edit(name=roomNames.pop(0)) for i in [ii.channels for ii in member.guild.categories if ii.name == '📊Info📊'][0]]
