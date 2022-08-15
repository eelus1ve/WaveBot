import discord
import json
from discord.ext import commands
from discord.utils import get
from BD import bdpy

class Warnspy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, reason: str):
        COLOR = bdpy(ctx)['COLOR']
        nWarns = bdpy(ctx)['nWarns']
        BADWORDS = bdpy(ctx)['BADWORDS']
        LINKS = bdpy(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        with open('users.json', 'r') as file:
            data = json.load(file)
        with open('users.json', 'w') as file:
            data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] += 1
            json.dump(data, file, indent=4)
        emb = discord.Embed(
            title='Нарушение',
            description=f"*Ранее, у нарушителя было уже {data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
            timestamp=ctx.message.created_at,
            color=COLOR
        )
        emb.add_field(name='Канал:', value='Не определён', inline=True)
        emb.add_field(name='Нарушитель:', value=member.mention, inline=True)
        emb.add_field(name='Причина:', value=f'{reason}', inline=True)
        await get(ctx.guild.text_channels, id=int(data[str(ctx.author.guild.id)]['idAdminchennel'])).send(embed=emb)
        if data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] >= nWarns:
            await member.ban(reason='Вы привысили допустимое количество нарушений')
        await ctx.message.reply(embed=discord.Embed(
            title="Успешно",
            description="*Предупреждение выдано*",
            timestamp=ctx.message.created_at,
            color=COLOR
        ))


    @warn.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
        BADWORDS = bdpy(ctx)['BADWORDS']
        LINKS = bdpy(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование: {pref}warn (@Участник) (Причина)",
                color=ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unwarn(self, ctx, member: discord.Member):

        COLOR = bdpy(ctx)['COLOR']
        BADWORDS = bdpy(ctx)['BADWORDS']
        LINKS = bdpy(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        with open('users.json', 'r') as file:
            data = json.load(file)
        with open('users.json', 'w') as file:
            data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] -= 1
            json.dump(data, file, indent=4)

            
        await ctx.send(embed=discord.Embed(
            title="Успешно",
            description="Предупреждение снято!",
            timestamp=ctx.message.created_at,
            color=COLOR
        ))


    @unwarn.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
        BADWORDS = bdpy(ctx)['BADWORDS']
        LINKS = bdpy(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование: {pref}unwarn (@Участник)",
                color=ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear_warns(self, ctx, member: discord.Member):
        COLOR = bdpy(ctx)['COLOR']
        BADWORDS = bdpy(ctx)['BADWORDS']
        LINKS = bdpy(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        with open('users.json', 'r') as file:
            data = json.load(file)
        with open('users.json', 'w') as file:
            data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] = 0
            json.dump(data, file, indent=4)

            
        await ctx.send(embed=discord.Embed(
            title="Успешно",
            description="Предупреждения сняты!",
            timestamp=ctx.message.created_at,
            color=COLOR
        ))


    @clear_warns.error
    async def error(self, ctx, error):
        ErCOLOR = bdpy(ctx)['ErCOLOR']
        pref = bdpy(ctx)['PREFIX']
        BADWORDS = bdpy(ctx)['BADWORDS']
        LINKS = bdpy(ctx)['LINKS']
        WARN = []
        WARN.extend(BADWORDS); WARN.extend(LINKS)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование: {pref}clear_warns (@Участник)",
                color=ErCOLOR

            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))
def setup(bot):
    bot.add_cog(Warnspy(bot))