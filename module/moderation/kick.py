import discord
import json
from discord.ext import commands
from distutils.log import error

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['кик', 'Кик', 'КИК'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None, amount=1):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)
            pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
        await ctx.channel.purge(limit=int(amount))
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*{member.mention} был кикнут!*",
                color=COLOR
            ))
    @kick.error
    async def error(self, ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)
            pref = str(dataServerID[str(ctx.author.guild.id)]['PREFIX'])
            
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*kick (@Участник)*",
                color = ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color = ErCOLOR
            ))


def setup(bot):
    bot.add_cog(kick(bot))