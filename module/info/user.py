from dis import disco
from http import client
from multiprocessing.connection import Client
from os import lseek
import discord
from discord import Spotify
from discord.ext import commands
from typing import Optional
from BTSET import ADMINS
import pytz
from BD import bdpy, bdmpy, bdint
import interactions
from discord.utils import get
from discord_components import ComponentsBot


class Duser(commands.Cog):
    def __init__(self, bot: ComponentsBot):
        self.bot: ComponentsBot = bot
    @commands.command(aliases=['юзер', 'Юзер', 'ЮЗЕР'])
    async def user(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        # member = await self.bot.get_user(int(member.id))
        # interactions.PresenceActivityType
        member = memberr or ctx.author
        mr = None
        if member.activities:
            for i in member.activities:
                if str(i.type) == 'ActivityType.playing':
                    mr = i

        warns = bdmpy(mr=member)['USERS'][str(member.id)]['WARNS']
        score = bdmpy(mr=member)['USERS'][str(member.id)]['SCR']
        LVL = bdmpy(mr=member)['USERS'][str(member.id)]['LvL']
        COLOR = bdpy(ctx)['COLOR'] or bdint(ctx)['COLOR']

        lstdisc = [f'\n***Имя пользователя:***  {member.name}#{member.discriminator} \n']

        if mr: lstdisc.append(f'***Играет:*** {mr.name}\n')

        if member.activities:
            for activity in member.activities:
                if isinstance(activity, Spotify):
                    lstdisc.append(f'***Слушает:*** {activity.artist} — [{activity.title}](https://open.spotify.com/track/{activity.track_id}) \n')

        if str(member.status) == 'dnd': status = 'Не беспокоить'
        elif str(member.status) == 'offline': status = 'Не в сети'
        elif str(member.status) ==  'idle': status = 'Неактивен'
        elif str(member.status) == 'online': status = 'В сети'

        lstdisc.append(f'***Статус:*** {status} \n')
        lstdisc.append(f'***Топ роль:*** {member.top_role.mention} \n')
        lstdisc.append(f"***Присоединился:*** {member.joined_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%d.%m.%y')} \n")
        lstdisc.append(f"***Дата регистрации:*** {member.created_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%d.%m.%y')}\n")
        if str(member.id) in ADMINS: lstdisc.append(f'***Разрабочик WaveBot*** \n')
        emb = discord.Embed(title=f'Информация о ***{member.name}***',
                            description="***Основная информация:***\n" + "".join(lstdisc),
                            color=COLOR
                            )
        # if bdpy(ctx)['Modules']['Rank']:
        # if bdpy(ctx)['Modules']['Warns']:   
        emb.add_field(name='***XP***', value=score, inline=True)
        emb.add_field(name='***LVL***', value=LVL, inline=True) #добавить if
        emb.add_field(name='***Предупреждения***', value=warns, inline=True)
        
        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text=f'ID: {member.id}')
        await ctx.send(embed=emb)

def setup(sbot):
    sbot.add_cog(Duser(sbot))