
def setup(bot):
    import discord
    import random
    from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
    import json

    @bot.command()
    async def dice(ctx):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            
        msg = await ctx.send(embed=discord.Embed(
                title="Игральная кость говорит:",
                description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                color = COLOR
            ),
            components=[
                Button(label='Перебросить', style=3)
            ]
        )
        for i in range(5):
            await msg.edit(
                embed=discord.Embed(
                    title="Игральная кость говорит: ",
                    description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                    color=COLOR
                )
            )
        while 1:
            it = await bot.wait_for("button_click")
            await it.send(embed=discord.Embed(
                title="Успешно",
                description= "Вы успешно перебросили кости",
                color = COLOR
            ))
            #await delm.message.delete()
            for i in range(5):
                await msg.edit(
                embed=discord.Embed(
                        title="Игральная кость говорит: ",
                        description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                        color=COLOR
                    )
                )







                '''global bbb
    @commands.Cog.listener('on_ready')
    async def n_ready():
        global bbb
        bbb = subprocess.Popen('python bot1.py')
    @commands.command()
    async def b(self, ctx):
        global bbb
        bbb = subprocess.Popen('python bot1.py')
    @commands.command()
    async def bb(self, ctx):
        global bbb
        bbb.kill()'''