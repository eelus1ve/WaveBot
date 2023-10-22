import discord
from discord.ext import commands
from typing import Optional
from module.utility.commands.vote import Vote
from module.utility.commands.rand import Rand
from module.utility.commands.avatar import Avatar
from module.utility.commands.translits import Translits
from system.Bot import WaveBot
from system.db_.sqledit import SQLEditor

class UtilitySetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @staticmethod
    def __ctx_to_color(ctx):
        return SQLEditor.get_color(ctx)(name="UTILITY")
    
    @commands.command()
    async def vote(self, ctx: commands.Context, *arg):
        await Vote(self.bot, self.__ctx_to_color(ctx)).command_vote(ctx, arg)

    @commands.command()
    async def tr(self, ctx: commands.Context, *arg):
        await Translits(self.bot, self.__ctx_to_color(ctx)).command_tr(ctx, arg)

    @commands.command(aliases=['ранд', 'РАНД', 'Ранд'])
    async def rand(self, ctx: commands.Context, arg: int = None, arg2: int = None):
        await Rand(self.bot, self.__ctx_to_color(ctx)).command_rand(ctx, arg, arg2)

    @commands.command()
    async def avatar(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Avatar(self.bot, self.__ctx_to_color(ctx)).command_avatar(ctx, member)
