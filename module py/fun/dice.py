import discord
import random
import json
from discord.ext import commands

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            
        msg = await ctx.send(embed=discord.Embed(
                title="Игральная кость говорит:",
                description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                color = COLOR
            )
        )
        for i in range(5):
            await msg.edit(
                embed=discord.Embed(
                    title="Игральная кость говорит: ",
                    description=f'{random.randint(1, 6)} и {random.randint(1, 6)}',
                    color=COLOR
                )
            )
def setup(bot):
    bot.add_cog(dice(bot))