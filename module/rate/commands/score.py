import discord
from discord.ext import commands
from typing import Optional
from distutils.log import error
import re
from discord.utils import get
import datetime
import pytz
import time
from BTSET import Score_presets, Rool, embpy, bdpy, BD, Lang
from system.Bot import WaveBot

memberInfo = {}
beforeTime = {}


# else:
#         await ctx.send(embed=discord.Embed(
#             title='Ошибка',
#             description=f'Максимально количество выданого опыта не может привешать 10000!',
#             color=self.ercolor
#         ))

class Score_audit(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    async def audit1(self, ctx: commands.Context, arg, mr):
        #====================================================================
        #audit
        #====================================================================
        if self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="ADMINCHANNEL"):
            msc_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M')
            emb=discord.Embed(
                title=Lang(ctx).language[f'score_audit_{arg[0]}_title'],
                description=f"{Lang(ctx).language[f'score_audit_{arg[0]}_des_1']} {mr.mention} {Lang(ctx).language[f'score_audit_{arg[0]}_des_2']} {arg} {Lang(ctx).language[f'score_mes_reason_{arg[-1]}']}!",
                # timestamp=msc_time,
                color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
            )
            emb.set_footer(text=f"{Lang(ctx).language[f'score_audit_{arg[0]}_footer_1']} {ctx.author.name}#{ctx.author.discriminator} {Lang(ctx).language[f'score_audit_{arg[0]}_footer_2']} {ctx.author.id}")
            await get(ctx.guild.text_channels, id=int(self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="ADMINCHANNEL"))).send(embed=emb)
        #====================================================================
        #rep
        #====================================================================
        await ctx.send(embed=discord.Embed(
            title=Lang(ctx).language[f'score_rep_{arg[0]}_title'],
            description=f"{Lang(ctx).language[f'score_rep_{arg[0]}_des_1']} {mr.name} {Lang(ctx).language[f'score_rep_{arg[0]}_des_2']} {arg} {Lang(ctx).language[f'score_mes_reason_{arg[-1]}']}!",
            color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
        ))

class Score_commands(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    @Rool.role(quest='score')
    def edit_xp(self, ctx: commands.Context, arg: str, member: discord.Member):
        if not(arg[1:]):
            raise commands.BadArgument(f'Использование: {self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="PREFIX")}score (@Учасник) +/-(кол-во опыта)')
        if arg.startswith('+'):
            self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(member), key="XP", value=self.bot.read_sql(db=f"server{ctx.guild.id}", guild=str(member), key="XP")+int(arg[1:]))
        elif arg.startswith('-'):
            xp = self.bot.read_sql(db=f"server{ctx.guild.id}", guild=str(member), key="XP")-int(arg[1:])
            if xp >= 0:
                self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(member), key="XP", value=xp)
            else:
                self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(member), key="XP", value=0)
        else:
            self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(member), key="XP", value=int(arg[1:]))


    async def command_score(self, ctx: commands.Context, mr: discord.Member, arg: Optional[str]):
        if arg:
            Score_commands(self.bot).edit_xp(ctx, arg, mr)
            await Score_audit(self.bot).audit1(ctx, arg, mr)
        else:
            await ctx.send(embed=discord.Embed(
                title=f"{Lang(ctx).language[f'score_info']} {mr.name}",
                description=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="XP"),
                color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
            ))

    async def command_set_lvl(self, ctx: commands.Context, member: discord.Member, arg = None):
        if not(int(arg)<=0):
            self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(member), key="XP", value = int(arg))    #СЮДА ФОРМУЛУ
            await ctx.send(embed=discord.Embed(
                title=Lang(ctx).language[f'command_set_lvl_title'],
                description=f"{Lang(ctx).language[f'command_set_lvl_des_1']} {member.name} {Lang(ctx).language[f'command_set_lvl_des_2']} {arg} {Lang(ctx).language[f'command_set_lvl_des_3']}",
                color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
            ))
        else:
            raise commands.BadArgument(Lang(ctx).language[f'command_set_lvl_er'])

    # @clear_rank.error
    # async def error(self, ctx, error):
    #     with open(f'{BD}users.json', 'r') as file:
    #         data = json.load(file)
    #     if isinstance(error, commands.errors.MemberNotFound):
    #         found = re.findall(r'Member \s*"([^\"]*)"', str(error))
    #         if found == ["all"]:
    #             for member in ctx.guild.members:
    #                 data[str(member.guild.id)]['USERS'][str(member.id)]['LvL'] = 1
    #                 data[str(member.guild.id)]['USERS'][str(member.id)]['SCR'] = 0
    #             await ctx.send(embed=discord.Embed(
    #                 title=f'Успешно',
    #                 description=f'Все участники этого сервера потерял свой ранк!',
    #                 color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
    #             ))
    #             with open(f'{BD}users.json', 'w') as file:
    #                 json.dump(data, file, indent=4)
    #         else:
    #             await ctx.send(embed=discord.Embed(
    #                 title="Ошибка",
    #                 description=f"*Участник `{''.join(found)}` не найден*",
    #                 color = self.ercolor
    #             ))

    async def command_voice_time(self, ctx: commands.Context, member: discord.Member):
        sec = bdpy(ctx)['USERS'][str(member.id)]['TIME']
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        emb = discord.Embed(
            title=f'Voice {member.name}',
            description=f'{int(hours)}:{int(mins)}:{sec}',
            color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="RATECOLOR")
        )
        await ctx.send(embed=emb)


class Score_listener(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    def mbtime(self, member: discord.Member):
        endTime = time.time()
        sec = endTime - beforeTime[member.id]
        sec = round(sec, 2)
        self.bot.write_sql(db=f"server{member.guild.id}", guild=str(member.id), key="TIME", value=self.bot.read_sql(db=f"server{member.guild.id}", guild=str(member.id), key="TIME") + sec)


    async def listener_score_on_voice_state_update(self, member: discord.Member, before, after):
        try:
            if before.channel and after.channel:
                if str(before.channel.id) != str(after.channel.id):
                    Score_listener.mbtime(member)
                    startTime = time.time()
                    beforeTime.update({member.id: startTime})
            elif before.channel and not(after.channel):
                Score_listener.mbtime(member)
            elif after.channel and not(before.channel):
                startTime = time.time()
                beforeTime.update({member.id: startTime})
        except Exception as ex:
            print(f'error eblan:\n{ex}')

