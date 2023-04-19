import discord
import json
from discord.ext import commands
from discord.utils import get
from BTSET import embpy, BD, Lang
from module.moderation.commands.audit import Audit
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
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)

        data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] += num

        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)

        if data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] >= self.bot.db_get_nwarns(ctx):
            await self.command_ban(ctx, member, reason=Lang(ctx).language['warns_command_warn_reason'])
        
        # Audit(self.bot).warn_audit(ctx, )

    async def commands_clearWarns(self, ctx: commands.Context, member):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] = 0
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)