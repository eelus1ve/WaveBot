import discord
import random
import json
from discord.ext import commands

class ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Волшебный_шар', '8ball', 'MagicBall', '8Ball'])
    async def Magicball(self, ctx, *arg):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
        randball = random.randint(1, 3) #мб сюда if добвать на arg?
        if randball == 1:
            await ctx.send(embed=discord.Embed(
                title="Шар судьбы говорит: ",
                description="*Да!*",
                color=COLOR
            ))
        elif randball == 2:
            await ctx.send(embed=discord.Embed(
                title="Шар судьбы говорит: ",
                description="*Может быть.*",
                color=COLOR
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="Шар судьбы говорит: ",
                description="*Нет!*",
                color=COLOR
            ))

def setup(bot):
    bot.add_cog(ball(bot))