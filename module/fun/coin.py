def setup(bot):

    import discord
    import random
    import json
    from discord.ext import commands

    @bot.command(aliases=['монетка', 'Монетка', 'МОНЕТКА'])
    async def coin(ctx, *arg):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)

        if random.randint(1, 2) == 1:
            msg = await ctx.send(embed=discord.Embed(
                title="Выпал: ",
                description="*Орел*",
                color=COLOR
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="Выпала: ",
                description="*Решка*",
                color=COLOR
            ))


