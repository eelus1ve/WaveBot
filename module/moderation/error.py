import discord
from discord.ext import commands
from BTSET import Moderation, bdpy
import re
from module.moderation.moderation import ModerationSetup
class BotError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def embs(self, ctx, des):
        await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=des,
                color = Moderation(ctx.author).ercolor
            ))

    @commands.Cog.listener('on_command_error')
    async def ErFile(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            print(error)
            found = re.findall(r'Command \s*"([^\"]*)"', str(error))
            des = f"*Команды `{''.join(found)}` не существует*"
        elif isinstance(error, commands.errors.MemberNotFound):
            found = re.findall(r'Member \s*"([^\"]*)"', str(error))
            des = f"*Участник `{''.join(found)}` не найден*"
        elif isinstance(error, commands.MissingPermissions):
            des = f"*У вас недостаточно прав!*"
        elif isinstance(error, commands.errors.CommandInvokeError):
            print(f'1\n{error}')
        elif isinstance(error, commands.BadArgument):
            des  = error
        else:
            print(error)
        des = error

        await BotError.embs(self, ctx, des)

    
    @ModerationSetup.clear.error
    async def error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование:* {Moderation(ctx.author).prefix}*clear (количество до 1000 за 1 раз)*",
                color=Moderation(ctx.author).ercolor
            ))

    @ModerationSetup.ban.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {Moderation(ctx.author).prefix}*ban (@Участник)*",
                color = Moderation(ctx.author).ercolor
            ))
    @ModerationSetup.kick.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование:* {Moderation(ctx.author).prefix}*kick (@Участник)*",
                color = Moderation(ctx.author).ercolor
            ))
    @ModerationSetup.warn.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование: {pref}warn (@Участник) (Причина)",
                color = Moderation(ctx.author).ercolor
            ))
    @ModerationSetup.unwarn.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование: {pref}unwarn (@Участник)",
                color = Moderation(ctx.author).ercolor
            ))
    @ModerationSetup.clear_warns.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование: {pref}clear_warns (@Участник)",
                color = Moderation(ctx.author).ercolor
            ))

    # @Score_commands.clear_rank.error
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