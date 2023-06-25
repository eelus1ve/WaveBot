import discord
from discord.ext import commands


class GetMessage(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    async def command_send_an_message(self, ctx: commands.Context):
        if not ctx.guild:
            await ctx.send(embed=discord.Embed(
                title='Внимание, Ваше сообщение может быть просмотрено модератором',
                description='Напишите получателя (имя#тэг)',
                color=0x0000FF
            ))

        def check(mes):
            return ctx.author == mes.author and not mes.guild

        ms1: discord.Message = await self.bot.wait_for('message', check=check)

        await ctx.send(embed=discord.Embed(
            title='Внимание, Ваше сообщение может быть просмотрено модератором',
            description='Напишите сообщение',
            color=0x0000FF
        ))

        ms2: discord.Message = await self.bot.wait_for('message', check=check)

        await ctx.send(embed=discord.Embed(
            title='Ваше сообщение будет отправлено в течении дня',
            color=0x0000FF
        ))

        adm_chlen = await self.bot.fetch_channel(1023514594414690324)
        await adm_chlen.send(f'{ms1.author.name}#{ms1.author.discriminator} отправил сообщение для {ms1.content} с содержанием: \n\n{ms2.content}')
        # components=[Button(label='одобрить'), Button(label='послать')])

    @commands.Cog.listener('on_button_click')
    async def listener_on_button_click_anMessage(self, interaction: discord.Interaction):
        if interaction.component.label == 'одобрить':
            await SendMessage(self.bot).send_mess(GetMember(self.bot).get_mem(interaction.message.content.split('\n\n')[0].split()[4]), interaction.message.content.split('\n\n')[1])
            await interaction.message.delete()
        elif interaction.component.label == 'послать':
            await SendMessage(self.bot).not_send_mess(GetMember(self.bot).get_mem(interaction.message.content.split('\n\n')[0].split()[0]))
            await interaction.message.delete()




    


class GetMember:
    def __init__(self, bot):
        self.bot = bot

    def get_mem(self, desc):
        return [i for i in self.bot.get_all_members() if i.discriminator == desc.split('#')[1] and i.name == desc.split('#')[0]][0]


class SendMessage:
    def __init__(self, bot):
        self.bot = bot

    async def send_mess(self, member, content: discord.Member):
        await member.send(embed=discord.Embed(
            title='Вам отправили анонимное сообшение',
            description=f'{content}'
        ))

    async def not_send_mess(self, member):
        await member.send(embed=discord.Embed(
            title='Лох',
            description=f'Ваше сообщение не одобренно'
        ))