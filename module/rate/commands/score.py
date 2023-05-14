import discord
import json
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

    async def audit1(self, ctx, arg, mr):
        #====================================================================
        #audit
        #====================================================================
        emb=discord.Embed(
            title=Lang(ctx).language[f'score_audit_{arg}_title'],
            description=f"{Lang(ctx).language[f'score_audit_{arg}_des_1']} {mr.mention} {Lang(ctx).language[f'score_audit_{arg}_des_2']} {arg} {Lang(ctx).language[f'score_mes_reason_{str(arg)[-1]}']}!",
            timestamp=datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d:%H:%M'),
            color=Score_presets(ctx).color
        )
        emb.set_footer(text=f"{Lang(ctx).language[f'score_audit_{arg}_footer_1']} {ctx.author.name}#{ctx.author.discriminator} {Lang(ctx).language[f'score_audit_{arg}_footer_2']} {ctx.author.id}")
        await get(ctx.guild.text_channels, id=int(Score_presets(member=mr).idadminchannel)).send(embed=emb)
        #====================================================================
        #rep
        #====================================================================
        await ctx.send(embed=discord.Embed(
            title=Lang(ctx).language[f'score_rep_{arg}_title'],
            description=f"{Lang(ctx).language[f'score_rep_{arg}_des_1']} {mr.name} {Lang(ctx).language[f'score_rep_{arg}_des_2']} {arg} {Lang(ctx).language[f'score_mes_reason_{str(arg)[-1]}']}!",
            color=Score_presets(ctx).color
        ))

class Score_commands(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    @Rool.role(quest='score')
    def edit_xp(self, ctx: commands.Context, arg: str):
        if not(arg[1:]):
            raise commands.BadArgument(f'Использование: {self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="PREFIX")}remove_score (@Учасник) +/-(кол-во опыта)')
        if arg.startswith('+'):
            self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="XP", value=self.bot.read_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="XP")+int(arg[1:]))
        elif arg.startswith('-'):
            xp = self.bot.read_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="XP")-int(arg[1:])
            if xp >= 0:
                self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="XP", value=xp)
            else:
                self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="XP", value=0)
        else:
            self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="XP", value=int(arg[1:]))


    async def command_score(self, ctx: commands.Context, mr: discord.Member, arg: Optional[str]):
        if arg:
            Score_commands(self.bot).edit_xp(ctx, arg)
            Score_audit(self.bot).audit1(ctx, arg[0], mr)
        else:
            await ctx.send(embed=discord.Embed(
                title=f"{Lang(ctx).language[f'score_info']} {mr.name}",
                description=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="XP"),
                color=Score_presets(ctx).color
            ))

    async def command_set_lvl(self, ctx: commands.Context, member: discord.Member, arg = None):
        if not(int(arg)<=0):
            self.bot.write_sql(db=f"server{ctx.guild.id}", guild=str(ctx.author.id), key="XP", value = int(arg))    #СЮДА ФОРМУЛУ
            await ctx.send(embed=discord.Embed(
                title=f'Успешно',
                description=f'Участнику {member.name} был выдан {arg} уровень!',
                color=Score_presets(ctx).color
            ))
        else:
            description='Нельзя поставить лвл меньше или равный 0 '

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
    #                 color=Score_presets(ctx).color
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
            color=Score_presets(ctx).color
        )
        await ctx.send(embed=emb)


class Score_listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def mbtime(member):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        endTime = time.time()
        sec = endTime - beforeTime[member.id]
        sec = round(sec, 2)
        data[str(member.guild.id)]['USERS'][str(member.id)]['TIME'] += sec
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)


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