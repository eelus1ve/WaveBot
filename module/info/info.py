import discord
from discord.ext import commands
from typing import Optional
from module.info.commands.user import UserInfo
from module.info.commands.sptf import SpotifyInfo
from module.info.commands.botinfo import BotInfo
from module.info.commands.help import Help
from module.info.commands.srinf import SrInfo, SrInfo_listeners
from system.db_.sqledit import SQLEditor
from system.Bot import WaveBot

class InfoSetup(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot: WaveBot = bot
    
    @staticmethod
    def __ctx_to_color(ctx):
        return SQLEditor.get_color(name="INFO")


    #Удалить до релиза
    @commands.command()
    async def new_betatesters(self, ctx: commands.Context):
        await BotInfo(self.bot, self.__ctx_to_color(ctx)).command_new_betatesters(ctx)
    #Удалить до релиза

    @commands.command(aliases=['юзер', 'Юзер', 'ЮЗЕР'])
    async def user(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await UserInfo(self.bot, self.__ctx_to_color(ctx)).command_user(ctx, member)

    @commands.command(aliases=['spotinf'])
    async def spotify_info(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await SpotifyInfo(self.bot, self.__ctx_to_color(ctx)).command_spotify_info(ctx, member)

    @commands.command(aliases=['sptf'])
    async def spotify(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member: discord.Member = memberr or ctx.author
        await SpotifyInfo(self.bot, self.__ctx_to_color(ctx)).command_spotify(ctx, member)
    
    @commands.command(aliases =['Инфо', 'инфо', 'ИНФО'])
    async def info(self, ctx: commands.Context):
        await BotInfo(self.bot, self.__ctx_to_color(ctx)).command_info(ctx)

    @commands.command()
    async def server_info(self, ctx: commands.Context):
        await SrInfo(self.bot, self.__ctx_to_color(ctx)).command_server_info(ctx)

    @commands.command()
    async def server_info_channel(self, ctx: commands.Context, arg: str):
        await SrInfo(self.bot, self.__ctx_to_color(ctx)).command_server_info_channel(ctx, arg)

    @commands.command(aliases = ['хелп', 'Хелп', 'ХЕЛП'])
    async def help(self, ctx: commands.Context, *arg):
        await Help(self.bot, self.__ctx_to_color(ctx)).command_help(ctx, arg)
    
    #Все лисенеры потом убрать в другое место

    @commands.Cog.listener('on_member_join')
    async def srinf_join(self, member: discord.Member):
        await SrInfo_listeners(self.bot, self.__ctx_to_color(member)).listener_srinf_join(member)

    @commands.Cog.listener('on_member_remove')
    async def srinf_remove(self, member: discord.Member):
        await SrInfo_listeners(self.bot, self.__ctx_to_color(member)).listener_srinf_remove(member)

    @commands.Cog.listener('on_interaction')
    async def on_button_click_help(self, interaction: discord.Interaction):
        await Help(self.bot, self.__ctx_to_color(interaction)).listener_on_button_click_help(interaction)
