def setup(bot):

    import discord
    import json
    from discord.ext import commands
    from discord.utils import get

    config = {
    'prefix': '~' #поиграться с префиксами
    }

    @bot.event
    async def on_message(message):
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
        await bot.process_commands(message)
    # Выдача варнов
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def warn(ctx, member: discord.Member, reason: str):
        with open('users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            idAdminchennel = int(data[str(ctx.author.guild.id)]['idAdminchennel'])
            nWarns = int(data[str(ctx.guild.id)]['nWarns'])
            nCaps = int(data[str(ctx.author.guild.id)]['nCaps'])
            BADWORDS = data[str(ctx.author.guild.id)]['BADWORDS']
            LINKS = data[str(ctx.author.guild.id)]['LINKS']
            WARN = []
            WARN.extend(BADWORDS); WARN.extend(LINKS)
            with open('users.json', 'w') as file:
                data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] += 1
                json.dump(data, file, indent=4)
            emb = discord.Embed(
                title='Нарушение',
                description=f"*Ранее, у нарушителя было уже {data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
                timestamp=ctx.message.created_at,
                color=COLOR
            )
            emb.add_field(name='Канал:', value='Не определён', inline=True)
            emb.add_field(name='Нарушитель:', value=member.mention, inline=True)
            emb.add_field(name='Причина:', value=f'{reason}', inline=True)
            await get(ctx.guild.text_channels, id=int(data[str(ctx.author.guild.id)]['idAdminchennel'])).send(embed=emb)
            if data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] >= nWarns:
                await member.ban(reason='Вы привысили допустимое количество нарушений')
            await ctx.message.reply(embed=discord.Embed(
                title="Успешно",
                description="*Предупреждение выдано*",
                timestamp=ctx.message.created_at,
                color=COLOR
            ))


    @warn.error
    async def error(ctx, error):
        with open('users.json', 'r') as file:
            data = json.load(file) 
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            idAdminchennel = int(data[str(ctx.author.guild.id)]['idAdminchennel'])
            nWarns = int(data[str(ctx.guild.id)]['nWarns'])
            nCaps = int(data[str(ctx.author.guild.id)]['nCaps'])
            BADWORDS = data[str(ctx.author.guild.id)]['BADWORDS']
            LINKS = data[str(ctx.author.guild.id)]['LINKS']
            WARN = []
            WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: " + str(config['prefix']) + "warn (@Участник) (Причина)",
                color=ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))


    @bot.command()
    @commands.has_permissions(administrator=True)
    async def unwarn(ctx, member: discord.Member):
        with open('users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            idAdminchennel = int(data[str(ctx.author.guild.id)]['idAdminchennel'])
            nWarns = int(data[str(ctx.guild.id)]['nWarns'])
            nCaps = int(data[str(ctx.author.guild.id)]['nCaps'])
            BADWORDS = data[str(ctx.author.guild.id)]['BADWORDS']
            LINKS = data[str(ctx.author.guild.id)]['LINKS']
            WARN = []
            WARN.extend(BADWORDS); WARN.extend(LINKS)
            
        with open('users.json', 'w') as file:
            data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] -= 1
            json.dump(data, file, indent=4)

            
        await ctx.send(embed=discord.Embed(
            title="Успешно",
            description="Предупреждение снято!",
            timestamp=ctx.message.created_at,
            color=COLOR
        ))


    @unwarn.error
    async def error(ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            idAdminchennel = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'])
            nWarns = int(dataServerID[str(ctx.guild.id)]['nWarns'])
            nCaps = int(dataServerID[str(ctx.author.guild.id)]['nCaps'])
            BADWORDS = dataServerID[str(ctx.author.guild.id)]['BADWORDS']
            LINKS = dataServerID[str(ctx.author.guild.id)]['LINKS']
            WARN = []
            WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: " + str(config['prefix']) + "unwarn (@Участник)",
                color=ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))


    @bot.command()
    @commands.has_permissions(administrator=True)
    async def clear_warns(ctx, member: discord.Member):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            idAdminchennel = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'])
            nWarns = int(dataServerID[str(ctx.guild.id)]['nWarns'])
            nCaps = int(dataServerID[str(ctx.author.guild.id)]['nCaps'])
            BADWORDS = dataServerID[str(ctx.author.guild.id)]['BADWORDS']
            LINKS = dataServerID[str(ctx.author.guild.id)]['LINKS']
            WARN = []
            WARN.extend(BADWORDS); WARN.extend(LINKS)
        with open('users.json', 'r') as file:
            data = json.load(file)
            

        with open('users.json', 'w') as file:
            data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] = 0
            json.dump(data, file, indent=4)

            
        await ctx.send(embed=discord.Embed(
            title="Успешно",
            description="Предупреждения сняты!",
            timestamp=ctx.message.created_at,
            color=COLOR
        ))


    @clear_warns.error
    async def error(ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            idAdminchennel = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'])
            nWarns = int(dataServerID[str(ctx.guild.id)]['nWarns'])
            nCaps = int(dataServerID[str(ctx.author.guild.id)]['nCaps'])
            BADWORDS = dataServerID[str(ctx.author.guild.id)]['BADWORDS']
            LINKS = dataServerID[str(ctx.author.guild.id)]['LINKS']
            WARN = []
            WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование: " + str(config['prefix']) + "clear_warns (@Участник)",
                color=ErCOLOR

            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))