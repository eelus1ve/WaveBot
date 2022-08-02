def setup(bot):
    import discord
    import json
    from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption, Interaction
    from discord.ext import commands
    from easy_pil import Editor, load_image_async, Font
    from typing import Optional
    from discord import File
    import asyncio
    import random
    import os

    @bot.event
    async def on_member_join(mbr):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(mbr.guild.id)]['COLOR'], 16)
            rls = dataServerID[str(mbr.guild.id)]['JoinRoles']
        if len(rls) != 0:
            f = len(rls)
            n = 0
            for n in f:
                rl = mbr.guild.get_role(int(rls[n]))
                n = n + 1
                await mbr.add_roles(rl)
        else:
            pass
        if len(dataServerID[str(mbr.guild.id)]['JNMSG']) != 0:
            await mbr.send(embed=discord.Embed(
                        title=f'Приветствуем Вас на сервере {mbr.guild.name}',
                        description=dataServerID[str(mbr.guild.id)]['JNMSG'],
                        color=COLOR
                    ))
        else:
            await mbr.send(embed=discord.Embed(
                        title=f'Приветствуем Вас на сервере {mbr.guild.name}',
                        description='Надеемся вам здесь понравиться!',
                        color=COLOR
                    ))

    @bot.command()
    async def is_stream(ctx, arg=None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
        while 1:
            if arg == 'off':
                break
            for i in ctx.author.guild.members:
                for ii in i.activities:
                    if str(ii.type) == 'ActivityType.streaming':
                        await ctx.send(embed=discord.Embed(
                    title=f'Пользователь {i.name} провоит трансляцию',
                    description=ii.urls,
                    color=COLOR
                ))