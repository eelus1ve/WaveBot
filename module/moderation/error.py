import discord
from discord.ext import commands
from BTSET import Moderation, bdpy
import re
from module.fun.fun import FunSetup
from module.info.info import InfoSetup
from module.moderation.moderation import ModerationSetup
# from module.rate.rate import RateSetup
from module.utility.utility import UtilitySetup
from module.self.commands.support import SupportAnswer
from module.self.commands.support import Suppot
from system.Bot import WaveBot
from system.db_.sqledit import SQLEditor

class BotError(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    @staticmethod
    def __ctx_to_color(ctx):
        return SQLEditor.get_color(ctx)(name="MODERATION", er="ER")

    @commands.Cog.listener('on_command_error')
    async def error(self, ctx, error):
        print(1)
        des = error
        if isinstance(error, commands.errors.CommandNotFound):
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
            des = error
        else:
            print(error)
        await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=des,
                color = self.__ctx_to_color(ctx)
            ))

    
    @ModerationSetup.clear.error
    async def error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование:* {Moderation(ctx.author).prefix}*clear (количество до 1000 за 1 раз)*",
                color=self.__ctx_to_color(ctx)
            ))

    @ModerationSetup.ban.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description=f"*Использование:* {Moderation(ctx.author).prefix}*ban (@Участник)*",
                color = self.__ctx_to_color(ctx)
            ))
    @ModerationSetup.kick.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование:* {Moderation(ctx.author).prefix}*kick (@Участник)*",
                color = self.__ctx_to_color(ctx)
            ))
    @ModerationSetup.warn.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование: {pref}warn (@Участник) (Причина)",
                color = self.__ctx_to_color(ctx)
            ))
    @ModerationSetup.unwarn.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"*Использование: {pref}unwarn (@Участник)",
                color = self.__ctx_to_color(ctx)
            ))
    @ModerationSetup.clear_warns.error
    async def error(self, ctx: commands.Context, error):
        pref = bdpy(ctx)['PREFIX']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"Использование: {pref}clear_warns (@Участник)",
                color = self.__ctx_to_color(ctx)
            ))

    @ModerationSetup.set.error
    async def error(self, ctx: commands.Context, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=error,
                color=self.__ctx_to_color(ctx)
            ))
        elif isinstance(error, commands.MissingRequiredArgument):
            print(3)
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=error,
                color=self.__ctx_to_color(ctx)
            ))

    @InfoSetup.spotify_info.error
    @InfoSetup.spotify.error
    async def error(self, ctx: commands.Context, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(
                title='Ошибка',
                description=f"Пользователь не слушает spotify",
                color = self.__ctx_to_color(ctx)
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
    #                 color = self.__ctx_to_color(ctx)
    #             ))