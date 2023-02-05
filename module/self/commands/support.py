import discord
import discord_components
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select
from discord_components import SelectOption
import json
from BTSET import ADMINS
from module.fun.anMessage import GetMember


class Suppot(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

    def support_json_writer(member: discord.Member, reason: str, text: str):
        with open('support.json', 'r') as file:
            sup_data = json.load(file)

        sup_data[reason].update({
            member.id: text
        })

        with open('support.json', 'w') as file:
            json.dump(sup_data, file, indent=4)

    @commands.command()
    async def support(self, ctx):
        if not ctx.guild:
            await ctx.send(components=[
                Select(
                    max_values=1,
                    min_values=0,
                    placeholder='Выберете что Вам нужно',
                    options=[
                        SelectOption(label='Предложить идею', value='idea'),
                        SelectOption(label='Вопрос о команде', value='que'),
                        SelectOption(label='Рассказать про ошибку', value='err'),
                        SelectOption(label='Сообщение для разработчиков', value='message')
                    ]
                )
            ])
    @commands.Cog.listener('on_select_option')
    async def main_support_select(self, interaction: discord_components.Interaction):
        if interaction.component.placeholder == 'Выберете что Вам нужно':
            try:
                def check(message: discord.Message):
                    return message.author == interaction.author and not message.guild

                if interaction.values[0] == 'idea':
                    await interaction.send(embed=discord.Embed(
                        title='Напишите Вашу идею'
                    ))

                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    await ms.author.send('спасибо за идею она будет рассмотренни в течении недели')
                    await Suppot(self.bot).send_to_moder(ms.author, 'идею', ms.content)

                elif interaction.values[0] == 'que':
                    await interaction.send(embed=discord.Embed(
                        title='Напишите Ваш вопрос'
                    ))

                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    await ms.author.send('ответ будет дан в течении двух дней')
                    await Suppot(self.bot).send_to_moder(ms.author, 'вопрос', ms.content)

                elif interaction.values[0] == 'err':
                    await interaction.send(embed=discord.Embed(
                        title='Напишите найденную вами ошибку'
                    ))

                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    await ms.author.send('спасибо за помощь в поисках ошибок бота')
                    await Suppot(self.bot).send_to_moder(ms.author, 'ошибку', ms.content)

                elif interaction.values[0] == 'message':
                    await interaction.send(embed=discord.Embed(
                        title='Напишите сообщение'
                    ))

                    ms: discord.Message = await self.bot.wait_for('message', check=check)

                    await ms.author.send('ожидайте ответа в течении 9999999999999999999999 дней')
                    await Suppot(self.bot).send_to_moder(ms.author, 'сообщение', ms.content)
            except IndexError:
                pass
    
    async def send_to_moder(self, member, type_mes, message):
        adm_chlen = await self.bot.fetch_channel(1023514594414690324)
        await adm_chlen.send(f'Пользователь {member.name}#{member.discriminator} отправил {type_mes} c содержанием \n\n\n{message}', components=[
            Button(label='принять(с сообщением)'),
            Button(label='принять(без сообщения)'),
            Button(label='отклонить')
        ])


class SupportAnswer(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

    async def send_answer(self, member, his_q, ans, ans_mem='WAVE_bot'):
        await member.send(embed=discord.Embed(
            title=f'{his_q}\n\nВам ответил {ans_mem}',
            description=ans
        ))

    @commands.Cog.listener('on_button_click')
    async def answer(self, interaction: discord_components.Interaction):
        if str(interaction.author.id) in ADMINS:

            def check(message: discord.Message):
                return message.author == interaction.author and interaction.channel == message.channel

            if interaction.component.label == 'принять(с сообщением)':
                await interaction.send('ответ пиши')

                ms: discord.Message = await self.bot.wait_for('message', check=check)

                await SupportAnswer(self.bot).send_answer(GetMember(self.bot).get_mem(interaction.message.content.split()[1]), interaction.message.content.split('\n\n\n')[1], ms.content, f'{ms.author.name}#{ms.author.discriminator}')

                await interaction.message.delete()
                await ms.delete()

            elif interaction.component.label == 'принять(без сообщения)':

                ms: str = 'Cпасибо мы обязательно прислушаемся к Вам'

                await SupportAnswer(self.bot).send_answer(GetMember(self.bot).get_mem(interaction.message.content.split()[1]), interaction.message.content.split('\n\n\n')[1], ms)

                await interaction.message.delete()

            elif interaction.component.label == 'отклонить':

                ms: str = 'Cпасибо, но мы вынуждены сообщить что ваша идея скорее всего будет проигнорирована'

                await SupportAnswer(self.bot).send_answer(
                    GetMember(self.bot).get_mem(interaction.message.content.split()[1]),
                    interaction.message.content.split('\n\n\n')[1], ms)

                await interaction.message.delete()

def setup(bot):
    bot.add_cog(Suppot(bot))
    bot.add_cog(SupportAnswer(bot))

