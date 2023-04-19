import discord
from discord.ext import commands
from discord.utils import get
from BTSET import Moderation, bdpy
from system.JSONwriter import Json_write
from system.Bot import WaveBot


class BotJoin(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot
    
    # @commands.Cog.listener('on_guild_join')
    # async def new_guild(self, ctx):
    #     Json_write(self.bot).jsonwrite()
    #     member: discord.Member = ctx.guild.owner
    #     emb = discord.Embed(
    #         title='',
    #         description='',
    #         timestamp=ctx.message.created_at,
    #         color=0x00FFFF
    #     )
    #     emb.add_field(name='', value='')
    #     emb.add_footer(text='')
    #     emb.
    #     await member.send(embed=emb, components=[
    #                     Select(                                             
    #                         placeholder=arg,
    #                         max_values=len(roles[arg][0]),
    #                         min_values=0,
    #                         options=[SelectOption(label=ctx.guild.get_role(int(i)).name, value=i) for i in roles[arg][0]]
    #                     )
    #                 ]
    #             )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # @commands.Cog.listener('on_member_join')
    # async def mbrjn(self, mbr):
    #     rls = bdpy(ctx=mbr)['JoinRoles']
    #     if len(rls) != 0:
    #         for role in rls:
    #             await mbr.add_roles(mbr.guild.get_role(int(role)))
    #     else:
    #         pass
    #     if len(bdpy(ctx=mbr)['JNMSG']) != 0:
    #         await mbr.send(embed=discord.Embed(
    #                     title=f'Приветствуем Вас на сервере {mbr.guild.name}',
    #                     description=bdpy(ctx=mbr)['JNMSG'],
    #                     color=Moderation(member=mbr).color
    #                 ))
    #     else:
    #         await mbr.send(embed=discord.Embed(
    #                     title=f'Приветствуем Вас на сервере {mbr.guild.name}',
    #                     description='Надеемся вам здесь понравиться!',
    #                     color=Moderation(member=mbr).color
    #                 ))

def setup(bot):
    bot.add_cog(BotJoin(bot))