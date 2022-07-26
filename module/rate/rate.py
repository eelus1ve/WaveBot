def setup(bot):
    import discord
    import json
    import asyncio
    import random
    import os
    from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption, Interaction
    from discord.ext import commands
    from easy_pil import Editor, load_image_async, Font
    from typing import Optional
    from discord import File

    @bot.command()
    async def score(ctx, mr: discord.Member = None, arg = None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if mr != None:
            with open('users.json', 'r') as file:
                SCR = dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR']
            await ctx.send(embed=discord.Embed(
                title=f'Количество очков {mr}',
                description=f'{SCR}',
                color=COLOR
            ))
        else:
            with open('users.json', 'r') as file:
                SCR = dataServerID[str(ctx.author.guild.id)]['USERS'][str(ctx.author.id)]['SCR']
            await ctx.send(embed=discord.Embed(
                title=f'Количество очков {ctx.author}',
                description=f'{SCR}',
                color=COLOR
            ))
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def add_score(ctx, mr: discord.Member = None, arg = None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if mr != None:
            if int(arg) < 10001:
                with open('users.json', 'r') as file:
                    SCR = dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR']
                dermo = int(SCR) + int(arg)
                with open('users.json', 'w') as file:
                    dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR'] = int(dermo) 
                    json.dump(dataServerID, file, indent=4)
                    
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'{mr} получил {arg} очков!',
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                        title='Ошибка',
                        description=f'Использование: ~add_score (@Учасник) (кол-во опыта)',
                        color=ErCOLOR
                    ))
        else:
            if int(arg) < 10001:
                with open('users.json', 'r') as file:
                    SCR = dataServerID[str(ctx.author.guild.id)]['USERS'][str(ctx.author.id)]['SCR']
                dermo = int(SCR) + int(arg)
                with open('users.json', 'w') as file:
                    dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR'] = int(dermo) 
                    json.dump(dataServerID, file, indent=4)
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'{ctx.author} получил {arg} очков!',
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                        title='Ошибка',
                        description=f'Использование: ~add_score (@Учасник) (кол-во опыта)',
                        color=ErCOLOR
                    ))
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def remove_score(ctx, mr: discord.Member = None, arg = None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if mr != None:
            if int(arg) < 10001:
                with open('users.json', 'r') as file:
                    SCR = dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR']
                dermo = int(SCR) - int(arg)
                with open('users.json', 'w') as file:
                    dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR'] = int(dermo) 
                    json.dump(dataServerID, file, indent=4)
                    
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'{mr} потерял {arg} очков!',
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                        title='Ошибка',
                        description=f'Использование: ~remove_score (@Учасник) (кол-во опыта)',
                        color=ErCOLOR
                    ))
        else:
            if int(arg) < 10001:
                with open('users.json', 'r') as file:
                    SCR = dataServerID[str(ctx.author.guild.id)]['USERS'][str(ctx.author.id)]['SCR']
                dermo = int(SCR) - int(arg)
                with open('users.json', 'w') as file:
                    dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR'] = int(dermo) 
                    json.dump(dataServerID, file, indent=4)
                await ctx.send(embed=discord.Embed(
                    title='Успешно',
                    description=f'{ctx.author} потерял {arg} очков!',
                    color=COLOR
                ))
            else:
                await ctx.send(embed=discord.Embed(
                        title='Ошибка',
                        description=f'Использование: ~remove_score (@Учасник) (кол-во опыта)',
                        color=ErCOLOR
                    ))
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def clear_score(ctx, mr: discord.Member = None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            SCR = dataServerID[str(ctx.author.guild.id)]['USERS'][str(ctx.author.id)]['SCR']
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if mr != None:
            with open('users.json', 'w') as file:
                dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR'] = int(0)
                json.dump(dataServerID, file, indent=4)
            await ctx.send(embed=discord.Embed(
                title='Успешно',
                description=f'{mr} потерял все очки!',
                color=COLOR
            ))
        else:
            with open('users.json', 'w') as file:
                dataServerID[str(ctx.author.guild.id)]['USERS'][str(ctx.author.id)]['SCR'] = int(0)
                json.dump(dataServerID, file, indent=4)
            await ctx.send(embed=discord.Embed(
                title='Успешно',
                description=f'{ctx.author} потерял все очки!',
                color=COLOR
            ))
    @bot.command()
    async def set_lvl(ctx, user = discord.Member, arg = None):
        userr = user or ctx.author
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if arg:
            with open('users.json', 'w') as file:
                dataServerID[str(userr.guild.id)]['USERS'][str(userr.id)]['LvL'] = arg
                json.dump(dataServerID, file, indent=4)
            await ctx.send(embed=discord.Embed(
                title=f'Успешно',
                description='',
                color=COLOR
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title=f'Ошибка',
                description='',
                color=ErCOLOR
            ))


    @bot.command()
    async def leaders(ctx, range_num=10):
        with open("users.json", "r") as f:
            data = json.load(f)
        COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
        l = {}
        total_xp = []
        for userid in data[str(ctx.guild.id)]['USERS']:
            xp = int(data[str(ctx.guild.id)]['USERS'][str(userid)]['SCR'])+(sum([i for i in range((int(data[str(ctx.guild.id)]['USERS'][str(userid)]['LvL']) + 1))])*100)

            l[xp] = f"{userid};{data[str(ctx.guild.id)]['USERS'][str(userid)]['LvL']};{data[str(ctx.guild.id)]['USERS'][str(userid)]['SCR']}"
            total_xp.append(xp)

        total_xp = sorted(total_xp, reverse=True)
        index=1
        
        mbed = discord.Embed(
        title="Доска лидеров",
        color=COLOR
        )

        for amt in total_xp:
            print(total_xp)
            print(l)
            print(amt)
            id_ = int(str(l[amt]).split(";")[0])
            level = int(str(l[amt]).split(";")[1])
            xp = int(str(l[amt]).split(";")[2])

            member = await ctx.bot.fetch_user(id_)
            if member is not None:
                name = member.name
                mbed.add_field(name=f"{index}. {name}",
                value=f"**Level: {level} | XP: {xp}**", 
                inline=False)
                
                if index == range_num:
                    break
                else:
                    index += 1

        await ctx.send(embed = mbed)
    
    @bot.command()
    async def rank(ctx: commands.Context, user: Optional[discord.Member]):
        userr = user or ctx.author
        with open("users.json", "r") as f:
            data = json.load(f)
        xp = data[str(ctx.guild.id)]['USERS'][str(userr.id)]["SCR"]
        lvl = data[str(ctx.guild.id)]['USERS'][str(userr.id)]["LvL"]
        next_level_xp = (lvl+1) * 100
        xp_need = next_level_xp
        xp_have = data[str(ctx.guild.id)]['USERS'][str(userr.id)]["SCR"]
        setcard = str(data[str(ctx.guild.id)]['card'])
        text_color = str(data[str(ctx.guild.id)]['text_color'])
        bar_color = str(data[str(ctx.guild.id)]['bar_color'])
        blend = int(data[str(ctx.guild.id)]['blend'])

        percentage = int(((xp_have * 100)/ xp_need))

        if percentage < 1:
            percentage = 0
        
        background = Editor(f"D:/Windows/Рабочий стол/wave1/module/rate/img/{setcard}")
    
        profile = await load_image_async(str(userr.avatar_url))

        profile = Editor(profile).resize((150, 150)).circle_image()
        
        FONT = Font.caveat(size=60)
        FONT_small = Font.caveat(size=50)

        
        if blend == 1:
            ima = Editor("D:/Windows/Рабочий стол/wave1/module/rate/set/zBLACK.png")
            background.blend(image=ima, alpha=.5, on_top=False)

        background.paste(profile.image, (30, 30))

        background.rectangle((30, 220), width=650, height=40, fill="#fff", radius=20)
        background.bar(
            (30, 220),
            max_width=650,
            height=40,
            percentage=percentage,
            fill=bar_color,
            radius=20,
        )
        background.text((200, 40), str(userr.name), font=FONT, color=text_color)

        background.rectangle((200, 100), width=350, height=2, fill=bar_color)
        background.text(
            (200, 130),
            f"Level : {lvl}   "
            + f" XP : {xp} / {(lvl+1) * 100}",
            font=FONT_small,
            color=text_color,
        )

        card = File(fp=background.image_bytes, filename="D:/Windows/Рабочий стол/wave1/module/rate/set/zCARD.png")
        await ctx.send(file=card)
    
    @bot.listen('on_message')
    async def my_message(message):
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                IgnoreChannels = data[str(message.guild.id)]['IgnoreChannels']
                IgnoreRoles = data[str(message.guild.id)]['IgnoreRoles']
            if not(message.content.startswith("~") or str(message.channel.id) in IgnoreChannels or True in [str(ii) in IgnoreRoles for ii in [i.id for i in message.author.roles]] or message.author.bot):

                    xp = data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR']
                    lvl = data[str(message.guild.id)]['USERS'][str(message.author.id)]['LvL']
        
                    if len(message.content) < 100:
                        with open('users.json', 'w') as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//10
                            json.dump(data, f, indent=4)
                    elif len(message.content) >= 100 and len(message.content) < 200:
                        with open('users.json', 'w') as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//40
                            json.dump(data, f, indent=4)
                    elif len(message.content) >= 200 and len(message.content) < 500:
                        with open('users.json', 'w') as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//50
                            json.dump(data, f, indent=4)
                    elif len(message.content) >= 500 and len(message.content) < 1000:
                        with open('users.json', 'w') as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//100
                            json.dump(data, f, indent=4)
                    elif len(message.content) >= 1000 and len(message.content) < 1500:
                        with open('users.json', 'w') as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//200
                            json.dump(data, f, indent=4)
                    elif len(message.content) >= 1500 and len(message.content) < 2000:
                        with open('users.json', 'w') as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 5 + (len(message.content))//1000
                            json.dump(data, f, indent=4)
                    elif len(message.content) >= 2000:
                        with open('users.json', 'w') as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR'] = xp + 1
                            json.dump(data, f, indent=4)

                    increased_xp = xp+15
                    new_level = int(increased_xp/100)
                    if new_level > lvl:
                        await message.channel.send(f"{message.author.mention} получил новый уровень {new_level}!")
                        
                        with open("users.json", "w") as f:
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['SCR']=0
                            data[str(message.guild.id)]['USERS'][str(message.author.id)]['LvL']=new_level
                            json.dump(data, f, indent=4)
        except:
            pass
        
        
    #Global rate = жопа