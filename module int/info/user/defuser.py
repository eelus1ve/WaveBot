from discord.utils import get
from BD import bdint
from BTSET import ADMINS
from discord import Spotify
import pytz
import interactions
from discord.ext import commands
class Defuser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def duser(ctx, userid):
        member = ctx.message.server.get_member(userid)
        COLOR = bdint(ctx)['COLOR']
        
        mr = None
        if member.activities:
            for i in member.activities:
                if str(i.type) == 'ActivityType.playing':
                    mr = i

        warns = bdint(ctx)['USERS'][str(member.id)]['WARNS']
        score = bdint(ctx)['USERS'][str(member.id)]['SCR']
        LVL = bdint(ctx)['USERS'][str(member.id)]['LvL']

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
        emb = interactions.Embed(title=f'Информация о ***{member.name}***',
                            description="***Основная информация:***\n" + "".join(lstdisc),
                            color=COLOR
                            )
        emb.add_field(name='***XP***', value=score, inline=True)
        emb.add_field(name='***LVL***', value=LVL, inline=True) #добавить if
        emb.add_field(name='***Предупреждения***', value=warns, inline=True)
        emb.set_thumbnail(url=member.avatar)
        emb.set_footer(text=f'ID: {member.id}')
        return emb
def setup(bot):
    bot.add_cog(Defuser(bot))  