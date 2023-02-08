import discord
from discord.ext import commands
from discord_components import ComponentsBot
from typing import Optional
from module.utility.commands.vote import Vote
from module.utility.commands.rand import Rand
from module.utility.commands.avatar import Avatar
from module.utility.commands.translits import Translits


class UtilitySetup(commands.Cog):
    def __init__(self, bot: ComponentsBot):
        self.bot = bot

    @commands.command()
    async def vote(self, ctx: commands.Context, *arg):
        await Vote(self.bot).command_vote(ctx, arg)

    @commands.command()
    async def tr(self, ctx: commands.Context, *arg):
        await Translits(self.bot).command_tr(ctx, arg)

    @commands.command(aliases = ['ранд', 'РАНД', 'Ранд'])
    async def rand(self, ctx: commands.Context, arg: int = None, arg2: int = None):
        await Rand(self.bot).command_rand(ctx, arg, arg2)

    @commands.command()
    async def avatar(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Avatar(self.bot).command_avatar(ctx, member)
