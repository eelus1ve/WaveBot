import discord
from discord import Spotify
from discord.ext import commands
from BTSET import ADMINS, Moderation, Info, Score_presets
import pytz
from discord_components import ComponentsBot

class UserInfo(commands.Cog):
    def __init__(self, bot: ComponentsBot):
        self.bot: ComponentsBot = bot

    async def command_user(self, ctx: commands.Context, member: discord.Member):    
        # member = await self.bot.get_user(int(member.id))
        # interactions.PresenceActivityType
        mr = None
        if member.activities:
            for i in member.activities:
                if str(i.type) == 'ActivityType.playing':
                    mr = i


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
                            color=Info(ctx).color
                            )
        # if bdpy(ctx)['Modules']['Rank']:
        # if bdpy(ctx)['Modules']['Warns']:  
        #потом заменить на list из включеных модулей и проверять нличее включения на севере а не колво xp lvl и warns !!!!!!!!!!!!!
        if Score_presets(member).score or Score_presets(member).lvl:
            emb.add_field(name='***XP***', value=Score_presets(member).score, inline=True)
            emb.add_field(name='***LVL***', value=Score_presets(member).lvl, inline=True) #добавить if
        if Moderation(member).warns:
            emb.add_field(name='***Предупреждения***', value=f'{Moderation(member).warns}/{Moderation(member).nWarns}', inline=True)
        
        emb.set_thumbnail(url=member.avatar)
        emb.set_footer(text=f'ID: {member.id}')
        
        await ctx.send(embed=emb)


