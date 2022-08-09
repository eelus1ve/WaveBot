import discord
from discord.ext import commands
from distutils.log import error
import json
class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def b(self, ctx):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            rls = dataServerID[str(ctx.author.guild.id)]['JoinRoles']
        if len(rls) != 0:
            for role in rls:
                await ctx.author.add_roles(ctx.author.guild.get_role(int(role)))
def setup(bot):
    bot.add_cog(test(bot))