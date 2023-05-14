import discord
from discord.ext import commands
from system.Bot import WaveBot


class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_vote(self, ctx: commands.Context, arg):
        em = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣⃣', '7️⃣', '8️⃣', '9️⃣', '0️⃣']
        arg = ''.join(arg)
        arg = arg.split(';')
        title = []
        title.append(arg.pop(0))
        e = 0
        for i in arg:
            title.append('\n' + str(em[e]) + ' ' + str(i))
            e += 1
        ms = await ctx.send(embed=discord.Embed(title=title.pop(0), description=''.join(title), color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="UTILITYCOLOR")))
        
        for i in range(len(title)):
            await ms.add_reaction(em[i])

