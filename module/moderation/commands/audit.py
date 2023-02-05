import discord
from discord.ext import commands
from BTSET import Moderation, embpy, bdpy
from discord.utils import get
import datetime
import pytz

class Audit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    async def audit(self, ctx, member, reason, text, num=0):
        moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        #====================================================================
        #audit
        #====================================================================
        if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
            emb=discord.Embed(
                title='Аудит',
                description=f'Учасник {member.name}#{member.discriminator} был {text}!\nПричина: {reason}',
                timestamp=moscow_time,
                color=Moderation(member).color
            )
            if not(num):
                emb.set_footer(text=f'Модератор {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
            else:
                emb.set_footer(text=f'Автомодератор WaveBot')
            await get(ctx.guild.text_channels, id=Moderation(member).idadminchannel).send(embed=emb)

        #====================================================================
        #rep
        #====================================================================
        if not(num):
            await embpy(ctx, comp='s', des=f"*{member.mention} был {text}!*", time=10.00)
        #====================================================================
        #ls
        #====================================================================
        emb=discord.Embed(
            title=f'{ctx.guild.name}',
            description=f'Вы были {text}ы!\nПричина: {reason}',
            timestamp=moscow_time,
            color=Moderation(member).color
        )
        if not(num):
            emb.set_footer(text=f'Модератор {ctx.author.name}#{ctx.author.discriminator} ID: {ctx.author.id}')
        else:
            emb.set_footer(text=f'Автомодератор WaveBot')
        await member.send(embed=emb)
        #====================================================================

    async def warn_audit(self, ctx, member, reason, text):
        moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        #====================================================================
        #audit
        #====================================================================
        if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
            emb = discord.Embed(
                title='Аудит',
                description=f"*Ранее, у нарушителя было уже {Moderation(member).warns - 1} нарушений, после {Moderation(member).nWarns} он будет забанен!*",
                timestamp=ctx.message.created_at,
                color=Moderation(member).color
            )
            emb.add_field(name='Канал:', value='Не определён', inline=True)
            emb.add_field(name='Участник:', value=member.mention, inline=True)
            emb.add_field(name='Причина:', value=f'{reason}', inline=True)
            emb.set_footer(text=f'Предупреждение выдано {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
            await get(ctx.guild.text_channels, id=Moderation(member).idadminchannel).send(embed=emb)
        #====================================================================
        #rep
        #====================================================================
        await ctx.message.reply(embed=discord.Embed(
            title="Успешно",
            description="*Предупреждение выдано*",
            timestamp=ctx.message.created_at,
            color=Moderation(member).color
        ), delete_after=10.0) 
        #====================================================================
        #ls
        #====================================================================
        emb=discord.Embed(
            title='Нарушение',
            description=f'Вы получили нарушение на сервере ***{ctx.guild.name}***\nПричина: {reason}',
            timestamp=ctx.message.created_at,
            color = Moderation(member).color
        )
        emb.add_field(name='Текущее кол-во нарушений', value=f'{Moderation(member).warns}/{Moderation(member).nWarns}', inline=True)
        emb.set_footer(text=f'Нарушение выдано {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
        await member.send(embed=emb)

        # if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
        #     emb = discord.Embed(
        #         title='Нарушение снято!',
        #         description=f"*Ранее, у участника было уже {Moderation(member).warns - 1} нарушений, после {Moderation(member).nWarns} он будет забанен!*",
        #         timestamp=ctx.message.created_at,
        #         color=Moderation(member).color
        #     )                                                                                                                   #переписать под unwarn
        #     emb.add_field(name='Канал:', value='Не определён', inline=True)
        #     emb.add_field(name='Участник:', value=member.mention, inline=True)
        #     emb.set_footer(text=f'Предупреждение снято участником {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
        #     await get(ctx.guild.text_channels, id=Moderation(member).idadminchannel).send(embed=emb)
        # #====================================================================
        # #rep
        # #==================================================================== 
        # await embpy(ctx, comp='s', des="Предупреждение снято!", time=10.00)
            
        # #====================================================================
        # #ls
        # #====================================================================
        # emb=discord.Embed(
        #     title='Нарушение',
        #     description=f'Вам было прощено нарушение!',
        #     timestamp=ctx.message.created_at,
        #     color = Moderation(ctx).color
        # )
        # emb.add_field(name='Текущее кол-во нарушений', value=f'{Moderation(member).warns}/{Moderation(member).nWarns}', inline=True)
        # emb.set_footer(text=f'Нарушение снято учасником{ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
        # await member.send(embed=emb)




        # #====================================================================
        # #audit
        # #====================================================================
        # if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
        #     emb = discord.Embed(
        #         title='Нарушения очищены',
        #         description=f"*Ранее, у нарушителя было уже {Moderation(member).warns - 1} нарушений, после {Moderation(member).nWarns} он будет забанен!*",
        #         timestamp=ctx.message.created_at,
        #         color=Moderation(ctx).color
        #     )                                                                                                               #переписать под clear_warn
        #     emb.add_field(name='Канал:', value='Не определён', inline=True)
        #     emb.add_field(name='Участник:', value=member.mention, inline=True)
        #     emb.set_footer(text=f'Нарушения очищены учасником{ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
        #     await get(ctx.guild.text_channels, id=Moderation(member).idadminchannel).send(embed=emb)
        # #====================================================================
        # #rep
        # #====================================================================
        # await embpy(ctx, comp='s', des="Предупреждения сняты!", time=10.00)
        # #====================================================================
        # #ls
        # #====================================================================
        # emb=discord.Embed(
        #     title='Нарушение',
        #     description=f'С вас сняли все предупреждения!',
        #     timestamp=ctx.message.created_at,
        #     color = Moderation(ctx).color
        # )
        # emb.add_field(name='Текущее кол-во нарушений', value=f'{Moderation(member).warns}/{Moderation(member).nWarns}', inline=True)
        # emb.set_footer(text=f'Нарушения сняты участником{ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
        # await member.send(embed=emb)