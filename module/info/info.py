import discord
from discord.ext import commands
from typing import Optional
from discord_components import ComponentsBot, Interaction
from module.info.commands.user import UserInfo
from module.info.commands.sptf import SpotifyInfo
from module.info.commands.botinfo import BotInfo
from module.info.commands.help import Help
from module.info.commands.srinf import SrInfo, SrInfo_listeners


class InfoSetup(commands.Cog):
    def __init__(self, bot: ComponentsBot):
        self.bot: ComponentsBot = bot

    @commands.command(aliases=['юзер', 'Юзер', 'ЮЗЕР'])
    async def user(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await UserInfo(self.bot).command_user(ctx, member)

    @commands.command(aliases=['spotinf'])
    async def spotify_info(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member = memberr or ctx.author
        await SpotifyInfo(self.bot).command_spotify_info(ctx, member)

    @commands.command(aliases=['sptf'])
    async def spotify(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member = memberr or ctx.author
        await SpotifyInfo(self.bot).command_spotify_info(ctx, member)
    
    @commands.command(aliases =['Инфо', 'инфо', 'ИНФО'])
    async def info(self, ctx: commands.Context):
        await BotInfo(self.bot).command_info(ctx)

    @commands.command()
    async def server_info(self, ctx: commands.Context):
        await SrInfo(self.bot).command_server_info(ctx)

    @commands.command()
    async def server_info_channel(self, ctx: commands.Context, arg: str):
        await SrInfo(self.bot).command_server_info_channel(ctx, arg)

    @commands.command(aliases = ['хелп', 'Хелп', 'ХЕЛП'])
    async def help(self, ctx: commands.Context, *arg):
        await Help(self.bot).command_help(ctx, arg)
    
    #Все лисенеры потом убрать в другое место

    @commands.Cog.listener('on_member_join')
    async def srinf_join(self, member: discord.Member):
        await SrInfo_listeners(self.bot).listener_srinf_join(member)

    @commands.Cog.listener('on_member_remove')
    async def srinf_remove(self, member: discord.Member):
        await SrInfo_listeners(self.bot).listener_srinf_remove(member)

    @commands.Cog.listener('on_button_click')
    async def on_button_click_help(self, interaction: Interaction):
        await Help(self.bot).listener_on_button_click_help(interaction)