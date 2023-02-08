import discord
from discord.ext import commands
from discord_components import ComponentsBot, Interaction
from typing import Optional
from BTSET import Rool
from module.moderation.commands.warns import Warns
from module.moderation.commands.clean import Clean
from module.moderation.commands.audit import Audit
from module.moderation.commands.stngs import Stngs
from module.moderation.commands.mwarns import Mwarns
# from module.moderation.btst
# from module.moderation.mbrjn import 
from module.moderation.commands.rand2 import Select
from module.moderation.commands.roomedit import Roomedit


class ModerationSetup(commands.Cog):
    def __init__(self, bot: ComponentsBot):
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
        await member.kick(reason=reason)
        await Audit(self.bot).audit(ctx, member, reason, text='исключен')

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
    async def server_set(self, ctx):
        await Stngs(self.bot).command_server_set(ctx)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def select(self, ctx: commands.Context, arg=None):
        await Select(self.bot).command_select(ctx, arg)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def room(self, ctx: commands.Context):
        await Roomedit(self.bot).command_room(ctx)

    #листенеры в отдельный класс

    @commands.Cog.listener('on_select_option')
    async def on_select_option_select(self, interaction: Interaction):
        await Select(self.bot).listener_on_select_option_select(interaction)

    @commands.Cog.listener('on_voice_state_update')
    async def on_voice_state_update_roomedit_move(self, member: discord.Member, before, after):
        await Roomedit(self.bot).listener_on_voice_state_update_roomedit_move(member, before, after)

    @commands.Cog.listener('on_button_click')
    async def roomedit_start(self, interaction: Interaction):
        await Roomedit(self.bot).listener_roomedit_start(interaction)

    @commands.Cog.listener('on_voice_state_update')
    async def on_voice_state_update_roomedit_mute(self, member: discord.Member, before, after):
        await Roomedit(self.bot).listener_on_voice_state_update_roomedit_mute(member, before, after)