import discord
from discord.ext import commands
from BD import bdpy

class Leaderspy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def leaders(self, ctx, range_num=10):
        COLOR = bdpy(ctx)['COLOR']
        l = {}
        total_xp = []
        for userid in bdpy(ctx)['USERS']:
            xp = bdpy(ctx)['USERS'][str(userid)]['SCR']+(sum([i for i in range((bdpy(ctx)['USERS'][str(userid)]['LvL']) + 1)])*100)

            l[xp] = f"{userid};{bdpy(ctx)['USERS'][str(userid)]['LvL']};{bdpy(ctx)['USERS'][str(userid)]['SCR']}"
            total_xp.append(xp)

        total_xp = sorted(total_xp, reverse=True)
        index=1
        
        mbed = discord.Embed(
        title="Доска лидеров",
        color=COLOR
        )

        for amt in total_xp:
            id_ = int(str(l[amt]).split(";")[0])
            level = int(str(l[amt]).split(";")[1])
            xp = int(str(l[amt]).split(";")[2])

            member = await ctx.bot.fetch_user(id_)
            if member is not None:
                name = member.name
                mbed.add_field(name=f"{index}. {name}",
                value=f"**Level: {level} | XP: {xp}**", 
                inline=False)
                
                if index == range_num:
                    break
                else:
                    index += 1
        await ctx.send(embed = mbed)
def setup(bot):
    bot.add_cog(Leaderspy(bot))