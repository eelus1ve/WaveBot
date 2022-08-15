import discord
from discord.ext import commands
from distutils.log import error
import interactions
from BD import bdint

class Banint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name='ban',
        description='Забанить пользователя'
    )
    async def ban(self, ctx, member: interactions.Member, reason = None):
        COLOR = bdint(ctx)['COLOR']
        Modrole = bdint(ctx)['ModRoles']
        if Modrole != None:
            if ctx.guild.get_role(int(Modrole)) in member.roles:
                await member.ban(reason=reason)
                await ctx.send(embeds=interactions.Embed(
                        title="Успешно",
                        description=f"*{member.mention} был забанен !*",
                        color=COLOR
                    ))
            else:
                await ctx.send(embeds=interactions.Embed(
                        title="Ошибка",
                        description=f"*У вас нет прав что бы использовать эту команду*",
                        color=COLOR
                    ))
        else:               #НАПИСАТЬ ПРОВЕРКУ НА АДМ РОЛЬ @commands.has_permissions(administrator=True)
            pass            


    @ban.error
    async def error(self, ctx, error):
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*ban (@Участник)*",
                color = ErCOLOR
            ))
            
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color = ErCOLOR
            ))
            
def setup(client):
    Banint(client)