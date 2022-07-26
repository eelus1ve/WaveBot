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