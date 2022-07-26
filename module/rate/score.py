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