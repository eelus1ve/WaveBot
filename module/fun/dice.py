def setup(bot):
    import discord
    import random
    import json
    from discord.ext import commands

    @bot.command()
    async def dice(ctx):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            
        await ctx.send(embed=discord.Embed(
                title="Игральная кость говорит:",
                description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                color = COLOR
            )
        )
