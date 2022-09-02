import discord
import json
from discord.ext import commands
from distutils.log import error
import interactions
from BD import bdint

class Kickint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name='kick',
        description='Кикнуть пользователя'
    )
    async def kick(self, ctx, member: interactions.Member, *, reason=None, amount=1):
        COLOR = bdint(ctx)['COLOR']
        await ctx.channel.purge(limit=int(amount))
        await member.kick(reason=reason)
        await ctx.send(embeds=interactions.Embed(
                title="Успешно",
                description=f"*{member.mention} был кикнут!*",
                color=COLOR
            ))
    @kick.error
    async def error(self, ctx, error):
        ErCOLOR = bdint(ctx)['ErCOLOR']
        pref = bdint(ctx)['PREFIX']
            
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*Использование:* {pref}*kick (@Участник)*",
                color = ErCOLOR
            ))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color = ErCOLOR
            ))
def setup(client):
    Kickint(client)