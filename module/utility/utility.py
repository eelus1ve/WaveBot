import discord
from discord.ext import commands
from typing import Optional
from commands.vote import Vote
from commands.rand import Rand
from commands.avatar import Avatar
from commands.translits import Translits
from system.Bot import WaveBot


class UtilitySetup(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    @commands.command()
    async def vote(self, ctx: commands.Context, *arg):
        await Vote(self.bot).command_vote(ctx, arg)

    @commands.command()
    async def tr(self, ctx: commands.Context, *arg):
        await Translits(self.bot).command_tr(ctx, arg)

    @commands.command(aliases=['ранд', 'РАНД', 'Ранд'])
    async def rand(self, ctx: commands.Context, arg: int = None, arg2: int = None):
        await Rand(self.bot).command_rand(ctx, arg, arg2)

    @commands.command()
    async def avatar(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Avatar(self.bot).command_avatar(ctx, member)
