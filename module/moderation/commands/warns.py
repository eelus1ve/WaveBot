import discord
import json
from discord.ext import commands
from discord.utils import get
from BTSET import embpy, BD, Lang
from module.moderation.audit import Audit
from system.Bot import WaveBot


class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_kick(self, ctx: commands.Context, member: discord.Member, reason: str):
        await member.kick(reason=reason)
        await Audit(self.bot).audit(ctx, member, reason, text=Lang(ctx).language['warns_command_kick_text'])

    async def command_ban(self, ctx: commands.Context, member: discord.Member, reason: str):
        await member.ban(reason=reason)
        await Audit.audit(self, ctx, member, reason, text=Lang(ctx).language['warns_command_ban_text'])

    async def command_warn(self, ctx: commands.Context, member: discord.Member, num: int):
        #Warn
        warns = self.bot.read_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="WARNS")
        self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="WARNS", value= warns + num)
        #Ban
        nwarns = self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="NWARNS")
        if nwarns:
            if warns+num >= nwarns:
                await self.command_ban(ctx, member, reason=Lang(ctx).language['warns_command_warn_reason'])
        
        # Audit(self.bot).warn_audit(ctx, )

    async def commands_clearWarns(self, ctx: commands.Context, member):
        self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="WARNS", value= 0)
