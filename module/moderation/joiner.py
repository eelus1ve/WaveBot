import discord
from discord.ext import commands
from system.DBwriter import SQL_write, Json_write


class Joiner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_member_join')
    async def n_mr_join(self, member: discord.Member):
        SQL_write(self.bot).newmembersql(member)
        Json_write(self.bot).jsonwrite()

    @commands.Cog.listener('on_member_remove')
    async def on_meove(self, member: discord.Member):
        Json_write(self.bot).jsonwrite()

    @commands.Cog.listener('on_guild_join')
    async def on_gld_jn(self, guild: discord.Guild):
        SQL_write(self.bot).newguildsql(guild)
        Json_write(self.bot).jsonwrite()

    @commands.Cog.listener('on_guild_remove')
    async def on_gld_remove(self, guild: discord.Guild):
        Json_write(self.bot).jsonwrite()