import discord
from discord.ext import commands
from typing import Optional
from commands.score import *
from commands.leaders import Leaders
from commands.rank import Rank
from commands.mrate import Mrate


class RateSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def score(self, ctx: commands.Context, memberr: Optional[discord.Member], arg: Optional[str]):
        member: discord.Member = memberr or ctx.author
        await Score_commands(self.bot).command_score(ctx, member, arg)
    
    @commands.command()
    async def clear_score(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Score_commands(self.bot).command_clear_score(ctx, member)

    @commands.command()
    async def set_lvl(self, ctx: commands.Context, memberr: Optional[discord.Member], arg = None):
        member: discord.Member = memberr or ctx.author
        await Score_commands(self.bot).command_set_lvl(ctx, member, arg)

    @commands.command()
    async def clear_rank(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Score_commands(self.bot).command_clear_rank(ctx, member)

    @commands.command()
    async def voice_time(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Score_commands(self.bot).command_voice_time(ctx, member)

    @commands.command()
    async def leaders(self, ctx: commands.Context, range_num: int = 10):
        await Leaders(self.bot).command_leaders(ctx, range_num)

    @commands.command()
    async def rank(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Rank(self.bot).command_rank(ctx, member)

    #Снести листенер в отдельный класс

    @commands.Cog.listener('on_voice_state_update')
    async def score_on_voice_state_update(self, member: discord.Member, before, after):
        await Score_listener(self.bot).listener_score_on_voice_state_update(member, before, after)

    @commands.Cog.listener('on_message')
    async def my_message(self, message: discord.Message):
        await Mrate(self.bot).command_my_message(message)
