import discord
import json
from discord.ext import commands
from discord.utils import get
from BTSET import Moderation, embpy, bdpy, BD
from module.moderation.commands.audit import Audit
n = {}

class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def command_kick(self, ctx: commands.Context, member: discord.Member, reason: str):
        await member.kick(reason=reason)
        await Audit(self.bot).audit(ctx, member, reason, text='исключен')

    async def command_ban(self, ctx: commands.Context, member: discord.Member, reason: str):
        await member.ban(reason=reason)
        await Audit.audit(self, ctx, member, reason, text='заблокирован')


    async def command_warn(self, ctx: commands.Context, member: discord.Member, num: int):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)

        data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] += num

        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)

        if data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] >= Moderation(member).nWarns:
            await self.command_ban(ctx, member, reason='Вы привысили допустимое количество нарушений')
        
        # Audit(self.bot).warn_audit(ctx, )


    async def commands_clearWarns(self, ctx: commands.Context, member):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] = 0
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)