import discord
from discord.ext import commands
import json
import re

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
@commands.Cog.listener()
async def on_command_error(self, ctx, error):
    with open('users.json', 'r') as file:
        dataServerID = json.load(file)
        ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
    if isinstance(error, commands.errors.CommandNotFound):
        found = re.findall(r'Command \s*"([^\"]*)"', str(error))
        await ctx.send(embed=discord.Embed(
            title="Ошибка",
            description=f"*Команды `{''.join(found)}` не существует*",
            color = ErCOLOR
        ))
def setup(bot):
    bot.add_cog(errors(bot))