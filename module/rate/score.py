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
from distutils.log import error
class Score(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def score(self, ctx, mr: discord.Member = None, arg = None):
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
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_score(self, ctx, mr: discord.Member, arg = None):
        try:
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
                pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
            if mr:
                if int(arg) < 10001 and arg != None:
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
                        description=f'Максимально количество выданого опыта не может привешать 10000!',
                        color=ErCOLOR
                    ))
            else:
                    await ctx.send(embed=discord.Embed(
                        title='Ошибка',
                        description=f'Использование: {pref}add_score (@Учасник) (кол-во опыта)',
                        color=ErCOLOR
                    ))
        except:
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f'Использование: {pref}add_score (@Учасник) (кол-во опыта)',
                color=ErCOLOR
            ))
    @add_score.error
    async def error(self, ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)
            pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
            
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f'Использование: {pref}add_score (@Учасник) (кол-во опыта)',
                color=ErCOLOR
            ))
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_score(self, ctx, mr: discord.Member = None, arg = None):
        try:
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
                pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
            if mr:
                if int(arg) < 10001 and arg != None:
                    with open('users.json', 'r') as file:
                        SCR = dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR']
                    dermo = int(SCR) - int(arg)
                    if not(dermo<0):
                        with open('users.json', 'w') as file:
                            dataServerID[str(mr.guild.id)]['USERS'][str(mr.id)]['SCR'] = 0
                            json.dump(dataServerID, file, indent=4)
                    else:
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
                            description=f'Использование: {pref}remove_score (@Учасник) (кол-во опыта)',
                            color=ErCOLOR
                        ))
            else:
                    await ctx.send(embed=discord.Embed(
                            title='Ошибка',
                            description=f'Использование: {pref}remove_score (@Учасник) (кол-во опыта)',
                            color=ErCOLOR
                        ))
        except:
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f'Использование: {pref}remove_score (@Учасник) (кол-во опыта)',
                color=ErCOLOR
            ))
    @remove_score.error
    async def error(self, ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)
            pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
            
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f'Использование: {pref}remove_score (@Учасник) (кол-во опыта)',
                color=ErCOLOR
            ))
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear_score(self, ctx, mr: discord.Member = None):
        mrr = mr or ctx.author
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            SCR = dataServerID[str(ctx.author.guild.id)]['USERS'][str(ctx.author.id)]['SCR']
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            with open('users.json', 'w') as file:
                dataServerID[str(mrr.guild.id)]['USERS'][str(mrr.id)]['SCR'] = int(0)
                json.dump(dataServerID, file, indent=4)
            await ctx.send(embed=discord.Embed(
                title='Успешно',
                description=f'{mrr} потерял все очки!',
                color=COLOR
            ))
    @commands.command()
    async def set_lvl(self, ctx, user = discord.Member, arg = None):
        try:
            userr = user #or ctx.author
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            if not(arg<0):
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
        except:
            pass

def setup(bot):
    bot.add_cog(Score(bot))