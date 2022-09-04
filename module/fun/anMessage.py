import datetime
from discord_components import ComponentsBot
import discord
from discord.ext import commands
from discord_components import Button

class Get_message(commands.Cog):
    def __init__(self, bot):
        self.bot: ComponentsBot = bot

    @commands.command()
    async def send_an_message(self, ctx: commands.Context):
        if not ctx.guild:
            await ctx.send(embed=discord.Embed(
                title='Внимание, Ваше сообщение может быть просмотренно модератором',
                description='напишите получателя',
                color=0x0000FF
            ))

        def check(mes):
            return ctx.author == mes.author and not mes.guild

        ms1: discord.Message = self.bot.wait_for('message', check=check)

        await ctx.send(embed=discord.Embed(
            title='Внимание, Ваше сообщение может быть просмотренно модератором',
            description='напишите сообщение',
            color=0x0000FF
        ))

        ms2: discord.Message = self.bot.wait_for('message', check=check)

        adm_user = await self.bot.fetch_user(758734389072625685)
        await adm_user.send(f'{ms1.author.name} отправил сообщение для {ms1.content} с содержанием: \n\n{ms2.content}', components=[Button(label='одобрить'), Button(label='послать')])

        @commands.Cog.listener('on_button_click')
        async def zxcvbnmsdfghjkhgfd(interaction):
            if interaction.component.label == 'одобрить':
                await SendMessage.send_mess(ms2.author, ms2.content)
            elif interaction.component.label == 'послать':
                await SendMessage.not_send_mess(ms1.author)


class SendMessage:
    async def send_mess(self, member, content):
        await member.send(embed=discord.Embed(
            title='Вам отправили анонимное сообшение',
            description=f'{content}'
        ))

    async def not_send_mess(self, member):
        await member.send(embed=discord.Embed(
            title='Лох',
            description=f'Ваше сообщение не одобренно'
        ))




def setup(bot):
    bot.add_cog(Get_message(bot))