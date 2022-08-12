import discord
import json
from discord import Spotify
from discord.ext import commands
from typing import Optional
from BTSET import ADMINS
import pytz

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['юзер', 'Юзер', 'ЮЗЕР'])
    async def user(self, ctx: commands.Context, memberr: Optional[discord.Member]):
        member = memberr or ctx.author
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
        
        mr = None
        if member.activities:
            for i in member.activities:
                if str(i.type) == 'ActivityType.playing':
                    mr = i

        warns = dataServerID[str(member.guild.id)]['USERS'][str(member.id)]['WARNS']
        score = dataServerID[str(member.guild.id)]['USERS'][str(member.id)]['SCR']
        LVL = dataServerID[str(member.guild.id)]['USERS'][str(member.id)]['LvL']

        lstdisc = [f'\n***Имя пользователя:***  {member.name}#{member.discriminator} \n']

        if mr: lstdisc.append(f'***Играет:*** {mr.name}\n')

        if member.activities:
            for activity in member.activities:
                if isinstance(activity, Spotify):
                    lstdisc.append(f'***Слушает:*** {activity.artist} — {activity.title} \n')

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
        emb.add_field(name='***XP***', value=score, inline=True)
        emb.add_field(name='***LVL***', value=LVL, inline=True) #добавить if
        emb.add_field(name='***Предупреждения***', value=warns, inline=True)
        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text=f'ID: {member.id}')
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(user(bot))    