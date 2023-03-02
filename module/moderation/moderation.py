import discord
from discord.ext import commands
from typing import Optional
from BTSET import Rool
from module.moderation.commands.warns import Warns
from module.moderation.commands.clean import Clean
from module.moderation.commands.audit import Audit
from module.moderation.commands.stngs import Stngs
from module.moderation.commands.mwarns import Mwarns
from module.moderation.commands.btst import *
# from module.moderation.mbrjn import 
from module.moderation.commands.rand2 import SelectRole
from module.moderation.commands.roomedit import Roomedit


class ModerationSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @Rool.role(quest='warn')
    async def warn(self, ctx: commands.Context, member: discord.Member, reason: str):
        await Warns(self.bot).command_warn(ctx, member, num=1)

    @commands.command()
    @Rool.role(quest='unwarn')
    async def unwarn(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Warns(self.bot).command_warn(ctx, member, num=-1)

    @commands.command()
    @Rool.role(quest='clearWarn')
    async def clear_warns(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Warns(self.bot).commands_clearWarns(ctx, member)

    @commands.command(aliases=['кик', 'Кик', 'КИК'])
    @Rool.role(quest='kick')
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason):
        await Warns(self.bot).command_kick(self, ctx, member, reason)

    @commands.command(aliases=['бан', 'Бан', 'БАН'])
    @Rool.role(quest='ban') 
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason):
        await Warns(self.bot).command_ban(ctx, member, reason)

    @commands.command(aliases=['очистить', 'Очистить', 'ОЧИСТИТЬ'])
    @Rool.role(quest='clear') 
    async def clear(self, ctx: commands.Context, amount: int):
        await Clean(self.bot).command_clear(ctx, amount)

    @commands.command(aliases=['settings'])
    @commands.has_permissions(administrator=True)
    async def set(self, ctx: commands.Context, arg=None, clArg=None, roleClass=None, emo=None):
        await Stngs(self.bot).command_set(ctx, arg, clArg, roleClass, emo)

    @commands.command()
    async def server_set(self, ctx: commands.Context):
        await Stngs(self.bot).command_server_set(ctx)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def select(self, ctx: commands.Context, arg=None):
        await SelectRole(self.bot).command_select(ctx, arg)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def room(self, ctx: commands.Context):
        await Roomedit(self.bot).command_room(ctx)# это временная функция нужно будет потом удалить сейчас не работает

    #листенеры в отдельный класс
    @commands.Cog.listener('on_message')
    async def on_message_mwarns(self, message: discord.Message):
        await Mwarns(self.bot).listener_on_message_mwarns(message)
        
    @commands.Cog.listener('on_interaction')
    async def on_select_option_select(self, interaction: discord.Interaction):
        await SelectRole(self.bot).listener_on_select_option_select(interaction)

    @commands.Cog.listener('on_voice_state_update')
    async def on_voice_state_update_roomedit_move(self, member: discord.Member, before, after):
        await Roomedit(self.bot).listener_on_voice_state_update_roomedit_move(member, before, after)

    @commands.Cog.listener('on_interaction')
    async def roomedit_start(self, interaction: discord.Interaction):
        await Roomedit(self.bot).listener_roomedit_start(interaction)

    @commands.Cog.listener('on_voice_state_update')
    async def on_voice_state_update_roomedit_mute(self, member: discord.Member, before, after):
        await Roomedit(self.bot).listener_on_voice_state_update_roomedit_mute(member, before, after)
