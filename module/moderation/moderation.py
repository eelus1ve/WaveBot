import discord
from discord.ext import commands
from typing import Optional
from BTSET import Rool
from module.moderation.commands.warns import Warns
from module.moderation.commands.clean import Clean
from module.moderation.audit import Audit
from module.moderation.commands.stngs import Stngs
from module.moderation.commands.mwarns import Mwarns
from module.moderation.commands.btst import *
# fromodule.moderation.n.mbrjn import
from module.moderation.commands.rand2 import SelectRole
from module.moderation.commands.roomedit import Roomedit
from system.db_.sqledit import SQLEditor


class ModerationSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @staticmethod
    def __ctx_to_color(ctx):
        return SQLEditor.get_color(ctx)(name="MODERATION")
    
    @commands.command()
    @Rool.role(quest='warn')
    async def warn(self, ctx: commands.Context, member: discord.Member, reason: str):
        await Warns(self.bot, self.__ctx_to_color(ctx)).command_warn(ctx, member, num=1)

    @commands.command()
    @Rool.role(quest='unwarn')
    async def unwarn(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Warns(self.bot, self.__ctx_to_color(ctx)).command_warn(ctx, member, num=-1)

    @commands.command()
    @Rool.role(quest='clearWarn')
    async def clear_warns(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await Warns(self.bot, self.__ctx_to_color(ctx)).commands_clearWarns(ctx, member)

    @commands.command(aliases=['кик', 'Кик', 'КИК'])
    @Rool.role(quest='kick')
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason):
        await Warns(self.bot, self.__ctx_to_color(ctx)).command_kick(self, ctx, member, reason)

    @commands.command(aliases=['бан', 'Бан', 'БАН'])
    @Rool.role(quest='ban') 
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason):
        await Warns(self.bot, self.__ctx_to_color(ctx)).command_ban(ctx, member, reason)

    @commands.command(aliases=['очистить', 'Очистить', 'ОЧИСТИТЬ'])
    @Rool.role(quest='clear') 
    async def clear(self, ctx: commands.Context, amount: int):
        await Clean(self.bot, self.__ctx_to_color(ctx)).command_clear(ctx, amount)

    @commands.command(aliases=['settings'])
    @commands.has_permissions(administrator=True)
    async def set(self, ctx: commands.Context, arg=None, clArg=None, roleClass=None, emo=None):
        await Stngs(self.bot, self.__ctx_to_color(ctx)).command_set(ctx, arg, clArg, roleClass, emo)

    @commands.command()
    async def server_set(self, ctx: commands.Context):
        await Stngs(self.bot, self.__ctx_to_color(ctx)).command_server_set(ctx)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def select(self, ctx: commands.Context, arg=None):
        await SelectRole(self.bot, self.__ctx_to_color(ctx)).command_select(ctx, arg)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def room(self, ctx: commands.Context):
        await Roomedit(self.bot, self.__ctx_to_color(ctx)).command_room(ctx)# это временная функция нужно будет потом удалить сейчас не работает

    #листенеры в отдельный класс
    @commands.Cog.listener('on_message')
    async def on_message_mwarns(self, message: discord.Message):
        await Mwarns(self.bot, self.__ctx_to_color(message)).listener_on_message_mwarns(message)
        
    @commands.Cog.listener('on_interaction')
    async def on_select_option_select(self, interaction: discord.Interaction):
        await SelectRole(self.bot, self.__ctx_to_color(interaction)).listener_on_select_option_select(interaction)

    @commands.Cog.listener('on_voice_state_update')
    async def on_voice_state_update_roomedit_move(self, member: discord.Member, before, after):
        await Roomedit(self.bot, self.__ctx_to_color(member)).listener_on_voice_state_update_roomedit_move(member, before, after)

    @commands.Cog.listener('on_interaction')
    async def roomedit_start(self, interaction: discord.Interaction):
        await Roomedit(self.bot, self.__ctx_to_color(interaction)).listener_roomedit_start(interaction)

    @commands.Cog.listener('on_voice_state_update')
    async def on_voice_state_update_roomedit_mute(self, member: discord.Member, before, after):
        await Roomedit(self.bot, self.__ctx_to_color(member)).listener_on_voice_state_update_roomedit_mute(member, before, after)
