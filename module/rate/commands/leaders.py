import discord
from discord.ext import commands
from BTSET import Score_presets, bdpy, Lang
from system.Bot import WaveBot


class Leaders(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def command_leaders(self, ctx: commands.Context, range_num: int):
        Elist = []
        all_members = {}
        for i in bdpy(ctx)['USERS']:
            LVL = bdpy(ctx)['USERS'][str(i)]['LvL']
            Lvl1 = LVL - 1
            Xp = bdpy(ctx)['USERS'][str(i)]['SCR']
            All_xp = (400+100*(Lvl1-1))/2*Lvl1 + Xp
            all_members.update({str(i): int(All_xp)})

        iii = []
        [iii.append([i for i in all_members if all_members[i] == ii and not i in iii][0]) for ii in reversed(sorted([all_members[k] for k in all_members.keys()]))]

        for i in range(range_num):
            lvl = bdpy(ctx)['USERS'][iii[i]]['LvL']
            xp = bdpy(ctx)['USERS'][iii[i]]['SCR']
            member = ctx.guild.get_member(int(iii[i]))
            Elist.append(f'{i+1}. {member.name}: LVL: {lvl}, XP {xp}')
        emb = discord.Embed(
            title=Lang(ctx).language['leaders_command_leaders_title'],
            description='\n '.join(Elist),
            color = self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
        )
        await ctx.send(embed = emb)
