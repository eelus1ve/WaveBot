import discord
from discord.ext import commands
from BTSET import Lang, BD
from system.Bot import WaveBot
from module.rate.commands.rank import Rank
import sqlite3

class Leaders(commands.Cog):
    def __init__(self, bot: WaveBot, color):
        self.bot = bot
        self.color = color

    async def command_leaders(self, ctx: commands.Context, range_num: int):
        members = []
        members.append(f"ㅤ`{Lang(ctx).language['leaders_command_leaders_list_2']}` {Lang(ctx).language['leaders_command_leaders_list_3']} {Lang(ctx).language['leaders_command_leaders_list_4']}")
        for i in range(range_num):
            lvl = Rank.levelFunction(int(records[i][0]))
            xp = int(records[i][0])-int(Leaders.xpFunction(lvl))
            members.append(f"{i+1}. `{ctx.guild.get_member(int(records[i][1]))}` {Lang(ctx).language['leaders_command_leaders_list_lvl']} {lvl} {Lang(ctx).language['leaders_command_leaders_list_xp']} {xp}/{Rank.xpFunction(lvl)}")
        emb = discord.Embed(
            title=Lang(ctx).language['leaders_command_leaders_title'],
            description='\n '.join(members),
            color = self.color
        )
        await ctx.send(embed = emb)
