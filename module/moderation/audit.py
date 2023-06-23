import discord
from discord.ext import commands
from BTSET import embpy
from discord.utils import get
import datetime
import pytz
from BTSET import Lang
from system.Bot import WaveBot


class Audit(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    async def audit(self, ctx: commands.Context, member: discord.Member, reason: str, text: str, num: int = 0):
        moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        COLOR = self.bot.read_sql(db="servers", guild=ctx.guild.id, key="MODERATIONCOLOR")
        #====================================================================
        #audit
        #====================================================================
        if self.bot.read_sql(db="servers", guild=ctx.guild.id, key="ADMINCHANNEL") in [str(i.id) for i in ctx.guild.channels]:
            emb=discord.Embed(
                title=Lang(ctx).language['audit_title'],
                description='{} {}#{} {} {}!\n{} {}'.format(Lang(ctx).language['audit_des_1'], member.name, member.discriminator, Lang(ctx).language['audit_des_2'], text, Lang(ctx).language['audit_des_3'], reason),
                timestamp=moscow_time,
                color=COLOR
            )
            if not(num):
                emb.set_footer(text='{} {}#{} {} {}'.format(Lang(ctx).language['audit_footer_1'], ctx.author.name, ctx.author.discriminator, Lang(ctx).language['audit_footer_2'], ctx.author.id))
            else:
                emb.set_footer(text=Lang(ctx).language['audit_footer_wave'])
            await get(ctx.guild.text_channels, id=self.bot.db_get_adminchannel(ctx)).send(embed=emb)

        #====================================================================
        #rep
        #====================================================================
        if not(num):
            emb=discord.Embed(
            title=Lang(ctx).language['audit_title_rep'],
            description="*{} {} {}.*".format(member.mention, Lang(ctx).language['audit_des_rep_s'], text),
            timestamp=moscow_time,
            color=COLOR
            )
        #====================================================================
        #ls
        #====================================================================
        emb=discord.Embed(
            title=f'{ctx.guild.name}',
            description=f"{Lang(ctx).language['audit_des_ls_1']} {text}{Lang(ctx).language['audit_des_ls_2']}\n{Lang(ctx).language['audit_des_ls_3']} {reason}",
            timestamp=moscow_time,
            color=COLOR
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
        if self.bot.db_get_adminchannel(ctx) in [str(i.id) for i in ctx.guild.channels]:
            emb = discord.Embed(
                title='Аудит',
                description=f"*Ранее, у нарушителя было уже {self.bot.db_get_user_warns(member) - 1} нарушений, после {self.bot.db_get_nwarns(ctx)} он будет забанен!*",
                timestamp=ctx.message.created_at,
                color=self.bot.db_get_modercolor(ctx)
            )
            emb.add_field(name='Канал:', value='Не определён', inline=True)
            emb.add_field(name='Участник:', value=member.mention, inline=True)
            emb.add_field(name='Причина:', value=f'{reason}', inline=True)
            emb.set_footer(text=f'Предупреждение выдано {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
            await get(ctx.guild.text_channels, id=self.bot.db_get_user_warns(member)).send(embed=emb)
        #====================================================================
        #rep
        #====================================================================
        await ctx.message.reply(embed=discord.Embed(
            title="Успешно",
            description="*Предупреждение выдано*",
            timestamp=ctx.message.created_at,
            color=self.bot.db_get_modercolor(ctx)
        ), delete_after=10.0) 
        #====================================================================
        #ls
        #====================================================================
        emb=discord.Embed(
            title='Нарушение',
            description=f'Вы получили нарушение на сервере ***{ctx.guild.name}***\nПричина: {reason}',
            timestamp=ctx.message.created_at,
            color=self.bot.db_get_modercolor(ctx)
        )
        emb.add_field(name='Текущее кол-во нарушений', value=f'{self.bot.db_get_user_warns}/{self.bot.db_get_nwarns(ctx)}', inline=True)
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




        async def mwarns_audit(self, message: discord.Message, data):
            if self.bot.db_get_adminchannel(message) in [str(i.id) for i in message.guild.channels]:
                emb = discord.Embed(
                    title='Нарушение',
                    description=f"*Ранее, у нарушителя было уже {self.bot.db_get_user_warns(message.author) - 1} нарушений, после {self.bot.db_get_nwarns(message)} он будет забанен!*",
                    timestamp=message.created_at,
                    color=self.bot.db_get_modercolor(message)
                )
                emb.add_field(name='Сообщение нарушителя:', value=message.content, inline=False)
                emb.add_field(name='Канал:', value=message.channel.mention, inline=True)
                emb.add_field(name='Нарушитель:', value=message.author.mention, inline=True)
                emb.add_field(name='Тип нарушения:', value='Ругательства/ссылки', inline=True)
                emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')
                await get(message.guild.text_channels, id=self.bot.db_get_adminchannel(message)).send(embed=emb)


            #====================================================================
            #ls
            #====================================================================
            emb = discord.Embed(
                title='Нарушение',
                description=f'Вам выдали предупреждение на сервере {message.guild.name}\nСообщение с нарушением: {message.content}',
                timestamp=message.created_at,
                color=self.bot.db_get_modercolor(message)
            )
            emb.add_field(name='Канал', value=message.channel.mention, inline=True)
            emb.add_field(name='Тип нарушения:', value=f'Ругательства/ссылки', inline=True)
            emb.add_field(name='Кол-во нарушений', value=f'{self.bot.db_get_user_warns(message.author)}/{self.bot.db_get_nwarns(message)}', inline=True)
            emb.set_footer(text=f'Предупреждение выдано автомодератором WaveBot')
            
            await message.author.send(embed=emb)
        #================================================================================================================================================================================


            #====================================================================
            #ban
            #====================================================================
            if data[str(message.guild.id)]['USERS'][str(message.author.id)]['WARNS'] >= self.bot.db_get_nwarns(message):
                ReasoN = 'Вы привысили допустимое количество нарушений'
                emb = discord.Embed(
                title=f'Вас забанили на сервере {message.guild.name}',
                description=f'{ReasoN}',
                timestamp=message.created_at,
                color=self.bot.db_get_modercolor(message)
                )
                await message.author.send(embed=emb)
                await message.author.ban(reason=ReasoN)
            #========================================================================================

