import discord
from discord import Spotify
from discord.ext import commands
from BTSET import ADMINS, Score_presets, Lang
import pytz
from system.Bot import WaveBot

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def command_user(self, ctx: commands.Context, member: discord.Member):

        lstdisc = [f"\n***{Lang(ctx).language['user_name']}***  {member.name}#{member.discriminator} \n"]

        if member.activities:
            for activity in member.activities:
                if str(activity.type) == 'ActivityType.playing':
                    lstdisc.append(f"***{Lang(ctx).language['user_playing']}*** {activity.name}\n")

                if isinstance(activity, Spotify):
                    lstdisc.append(f"***{Lang(ctx).language['user_listening']}*** {activity.artist} — [{activity.title}](https://open.spotify.com/track/{activity.track_id}) \n")

        lstdisc.append(f"***{Lang(ctx).language['user_status']}*** {Lang(ctx).language[f'user_status_{member.status}']} \n")
        lstdisc.append(f"***{Lang(ctx).language['user_top_role']}*** {member.top_role.mention} \n")
        lstdisc.append(f"***{Lang(ctx).language['user_connected']}*** {member.joined_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%d.%m.%y')} \n")
        lstdisc.append(f"***{Lang(ctx).language['user_reged']}*** {member.created_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%d.%m.%y')}\n")
        if str(member.id) in ADMINS: lstdisc.append(f"***{Lang(ctx).language['user_dev']}*** \n")
        emb = discord.Embed(title=f"{Lang(ctx).language['user_info_about']} ***{member.name}***",
                            description=f"***{Lang(ctx).language['user_some_info']}***\n" + "".join(lstdisc),
                            color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="INFOCOLOR")
        )
        if Score_presets(member).score or Score_presets(member).lvl:
            emb.add_field(name=f"***{Lang(ctx).language['user_xp']}***", value=Score_presets(member).score, inline=True)
            emb.add_field(name=f"***{Lang(ctx).language['user_lvl']}***", value=Score_presets(member).lvl, inline=True) #добавить if
        if self.bot.db_get_user_warns:
            emb.add_field(name=f"***{Lang(ctx).language['user_warns']}***", value=f'{self.bot.db_get_user_warns(ctx=member)}/{self.bot.db_get_nwarns(ctx=member)}', inline=True)
        
        emb.set_thumbnail(url=member.avatar)
        emb.set_footer(text=f"{Lang(ctx).language['user_footer']} {member.id}")
        
        await ctx.send(embed=emb)


