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
            '''components=[
                    Button(label="Удалить ", style=4)
                ]
            )
            interaction = await bot.wait_for("button_click")
            if interaction.component.label.startswith("Удалить "):
                await msg.edit(content = '', embed = {})
                await interaction.edit_origin(
                    components=[]
                )'''
        else:
            msg = await ctx.send(embed=discord.Embed(
                title="Выпала: ",
                description="*Решка*",
                color=COLOR
            ))
        '''components=[
                    Button(label="Удалить ", style=4)
                ]
            )
            interaction = await bot.wait_for("button_click")
            if interaction.component.label.startswith("Удалить "):
                await msg.edit(content = '', embed = {})
                await interaction.edit_origin(
                    components=[]
                )'''
    @bot.command()
    async def a(ctx):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
        for i in ctx.guild.members:
            if str(i.id) == '136845059717988354':
                await ctx.send(embed=discord.Embed(
                title=f"{i.name}",
                description="",
                color=COLOR
            ))

