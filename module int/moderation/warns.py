import discord
import json
from discord.ext import commands
from discord.utils import get
import interactions
from BD import bdint
from distutils.log import error
class Warnsint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="warn",
        description="Выдать перепреждение учаснику",
    )
    async def warn(self, ctx, member: discord.Member, reason: str):
            COLOR = bdint(ctx)['COLOR']
            nWarns = bdint(ctx)['nWarns']
            BADWORDS = bdint(ctx)['BADWORDS']
            LINKS = bdint(ctx)['LINKS']
            WARN = []
            WARN.extend(BADWORDS); WARN.extend(LINKS)
            with open('users.json', 'r') as file:
                data = json.load(file)
            with open('users.json', 'w') as file:
                bdint(ctx)['USERS'][str(member.id)]['WARNS'] += 1
                json.dump(data, file, indent=4)
            emb = interactions.Embed(
                title='Нарушение',
                description=f"*Ранее, у нарушителя было уже {bdint(ctx)['USERS'][str(member.id)]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
                timestamp=ctx.message.created_at,
                color=COLOR
            )
            emb.add_field(name='Канал:', value='Не определён', inline=True)
            emb.add_field(name='Нарушитель:', value=member.mention, inline=True)
            emb.add_field(name='Причина:', value=f'{reason}', inline=True)
            await get(ctx.guild.text_channels, id=int(bdint(ctx)['idAdminchennel'])).send(embeds=emb)
            if bdint(ctx)['USERS'][str(member.id)]['WARNS'] >= nWarns:
                await member.ban(reason='Вы привысили допустимое количество нарушений')
            await ctx.message.reply(embeds=interactions.Embed(
                title="Успешно",
                description="*Предупреждение выдано*",
                timestamp=ctx.message.created_at,
                color=COLOR
            ))


    @warn.error
    async def error(self, ctx, error):
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']
        BADWORDS = bdint(ctx)['BADWORDS']
        LINKS = bdint(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*Использование: {pref}warn (@Участник) (Причина)",
                color=ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))


    @interactions.extension_command(
        name="unwarn",
        description="Удалить предупреждение у учатсника",
    )
    async def unwarn(self, ctx, member: discord.Member):
        with open('users.json', 'w') as file:
            data = json.load(file)
        COLOR = bdint(ctx)['COLOR']
        BADWORDS = bdint(ctx)['BADWORDS']
        LINKS = bdint(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
            
        with open('users.json', 'w') as file:
            bdint(ctx)['USERS'][str(member.id)]['WARNS'] -= 1
            json.dump(data, file, indent=4)

            
        await ctx.send(embeds=interactions.Embed(
            title="Успешно",
            description="Предупреждение снято!",
            timestamp=ctx.message.created_at,
            color=COLOR
        ))


    @unwarn.error
    async def error(self, ctx, error):
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']
        BADWORDS = bdint(ctx)['BADWORDS']
        LINKS = bdint(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*Использование: {pref}unwarn (@Участник)",
                color=ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))


    @interactions.extension_command(
        name="clear warns",
        description="Отчистить предупреждения у участника",
    )
    async def clear_warns(self, ctx, member: discord.Member):
        COLOR = bdint(ctx)['COLOR']
        BADWORDS = bdint(ctx)['BADWORDS']
        LINKS = bdint(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        with open('users.json', 'r') as file:
            data = json.load(file)
            

        with open('users.json', 'w') as file:
            bdint(ctx)['USERS'][str(member.id)]['WARNS'] = 0
            json.dump(data, file, indent=4)

            
        await ctx.send(embeds=interactions.Embed(
            title="Успешно",
            description="Предупреждения сняты!",
            timestamp=ctx.message.created_at,
            color=COLOR
        ))


    @clear_warns.error
    async def error(self, ctx, error):
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']
        BADWORDS = bdint(ctx)['BADWORDS']
        LINKS = bdint(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*Использование: {pref}clear_warns (@Участник)",
                color=ErCOLOR

            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))
def setup(bot):
    Warnsint(bot)