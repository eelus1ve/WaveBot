import discord
from discord.ext import commands
from discord.utils import get
from BD import bdpy, bdmpy

class Mbrjnpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener('on_member_join')
    async def mbrjn(self, mbr):
        COLOR = bdmpy(mr=mbr)['COLOR']
        rls = bdmpy(mr=mbr)['JoinRoles']
        if len(rls) != 0:
            for role in rls:
                await mbr.add_roles(mbr.guild.get_role(int(role)))
        else:
            pass
        if len(bdmpy(mr=mbr)['JNMSG']) != 0:
            await mbr.send(embed=discord.Embed(
                        title=f'Приветствуем Вас на сервере {mbr.guild.name}',
                        description=bdmpy(mr=mbr)['JNMSG'],
                        color=COLOR
                    ))
        else:
            await mbr.send(embed=discord.Embed(
                        title=f'Приветствуем Вас на сервере {mbr.guild.name}',
                        description='Надеемся вам здесь понравиться!',
                        color=COLOR
                    ))

    @commands.command()
    async def is_stream(self, ctx, arg=None):
        COLOR = bdpy(ctx)['COLOR']
        while 1:
            if arg == 'off':
                break
            for i in ctx.author.guild.members:
                for ii in i.activities:
                    if str(ii.type) == 'ActivityType.streaming':
                        await ctx.send(embed=discord.Embed(
                    title=f'Пользователь {i.name} провоит трансляцию',
                    description=ii.urls,
                    color=COLOR
                ))
def setup(bot):
    bot.add_cog(Mbrjnpy(bot))