import discord
from discord.ext import commands
from BTSET import Score_presets, bdpy, Lang, BD
from system.Bot import WaveBot
import sqlite3

class Leaders(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def levelFunction(x):
        d = (3**2+4*2*x/100)**0.5
        if (-3-d)/2 > (-3+d)/2:
            level = (-3-d)/2
        else:
            level = (-3+d)/2
        return int(level + 1)

    def xpFunction(x):
        xp: float = 50*(x**2+x-2)
        return int(round(xp, 2))

    async def command_leaders(self, ctx: commands.Context, range_num: int):
        members = []
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""SELECT XP, ID from server{ctx.guild.id}""")
        records = cursor.fetchall()
        records = list(reversed(sorted(records)))
        members.append(f"ㅤ`{Lang(ctx).language['leaders_command_leaders_list_2']}` {Lang(ctx).language['leaders_command_leaders_list_3']} {Lang(ctx).language['leaders_command_leaders_list_4']}")
        for i in range(range_num):
            lvl = Leaders.levelFunction(int(records[i][0]))
            xp = int(records[i][0])-Leaders.xpFunction(lvl)
            members.append(f"{i+1}. `{ctx.guild.get_member(int(records[i][1]))}` {Lang(ctx).language['leaders_command_leaders_list_lvl']} {lvl} {Lang(ctx).language['leaders_command_leaders_list_xp']} {xp}/{Leaders.xpFunction(lvl)}")
        emb = discord.Embed(
            title=Lang(ctx).language['leaders_command_leaders_title'],
            description='\n '.join(members),
            color = self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
        )
        await ctx.send(embed = emb)
