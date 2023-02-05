import discord
import discord_components
from discord.ext import commands
from BTSET import BOTVERSION, bdpy
from discord_components import Select, SelectOption, Button


class Help(commands.Cog):

    help_dict = {
        'модерация': {
            'warn': 'Выдать предупреждение',
            'unwarn': 'Убрать предупреждение',
            'clear_warns': 'Очистка предупреждений',
            'ban': 'Забанить пользователя',
            'clear': 'Очистка чата',
            'kick': 'Кикнуть пользователя',
            'select': 'Выдача ролей',
            'btst': 'Вызвать меню настройки бота',
            'set': 'Настройка бота через чат'
        },
        'развлечения': {
            'rand': 'рандомайзер',
            'coin': 'Кинуть монетку',
            'MagicBall': 'Магический шар',
            'send_an_message': 'Отправить анонимное сообщение пользователю',
            'p2048': 'Вызвать игру 2048',
            'get_qr': 'зашифровать Ваш текст в QR код',
            'dice': 'Кинуть игральные кости'
        },
        'информация': {
            'info': 'Информация о боте',
            'help': 'Информация о командах',
            'user': 'Информация о юзере',
            'spotify_info': '',
            'spotify': 'Информация юзера о прослушивании spotify',
            'server_info': 'Информация о сервере',
            'server_info_channel': 'Создать каналы со статистикой сервера',
        },
        'рейтинг': {
            'leaders': '',
            'rank': 'Показать ваш ранк на сервере',
            'add_score': '',
            'remove_score': '',
            'clear_score': '',
            'score': 'осмотреть счет учасника',
        },
        'утилиты': {
            'tr': 'Перевести текст',
            'avatar': 'Отправить в чат аватар пользователя',
            'vote': 'Вызвать голосование',
        },
    }

    def __init__(self, bot):
        self.bot = bot

    async def command_help(self, ctx, arg=None):
        COLOR = bdpy(ctx)['COLOR']
        pref = bdpy(ctx)['PREFIX']
        if arg:
            await ctx.author.send(embed=discord.Embed(
                title=f'***{arg}***',
                description=f"*Использование: {pref} {arg}\n\
                    {[i[arg] for i in self.help_dict if arg in i]}*",
                color=COLOR
            ))
            await ctx.send(embed=discord.Embed(
                title='Успешно',
                description=f'Информация о комманде {arg} отправлена вам в личные сообщения!',
                color=COLOR
            ))

        else:
            var = list(self.help_dict[list(self.help_dict.keys())[0]].keys())
            emb = discord.Embed(title='*Список доступных команд:*',
                description = '',
                color=COLOR)
            emb.add_field(name='', value='**`модерация`**' + '\n' + f'\n'.join([i for i in self.help_dict if i != 'модерация']))
            emb.add_field(name='', value=f'**`{var[0]}`**' + '\n' + f'\n'.join([i for i in var if i != var[0]]))
            emb.add_field(name='='*len(self.help_dict['модерация']['warn']), value=f"{self.help_dict['модерация']['warn']}", inline=True)
            await ctx.author.send(embed=emb, components=[[
                Button(label='←'),
                Button(label='↑'),
                Button(label='→'),
            ], [
                Button(label='.', disabled=True),
                Button(label='↓'),
                Button(label='.', disabled=True),
            ]])
            await ctx.send(embed=discord.Embed(
                title='Успешно',
                description=f'Список доступных комманд отправлен вам в личные сообщения!',
                color=COLOR
            ))

    async def listener_on_button_click_help(self, interaction: discord_components.Interaction):
        COLOR = 0x0000FF
        pref = '~'

        if interaction.component.label == '→':
            old_field0_value = interaction.message.embeds[0].fields[0].value
            old_field1_value = interaction.message.embeds[0].fields[1].value.split()

            for i in range(len(old_field1_value)):
                if '*' in old_field1_value[i]:
                    old_field1_value[i] = old_field1_value[i].replace('*', '')
                    old_field1_value[i] = old_field1_value[i].replace('`', '')
                    if i < len(old_field1_value) - 1:
                        des_name = old_field1_value[i+1]
                        old_field1_value[i+1] = f'**`{old_field1_value[i+1]}`**'
                    else:
                        des_name = old_field1_value[0]
                        old_field1_value[0] = f'**`{old_field1_value[0]}`**'
                    break

            for i in old_field0_value.split():
                if '*' in i:
                    first_key = i.replace('*', '').replace('`', '')

            emb = discord.Embed(title='*Список доступных команд:*',
                                description='',
                                color=COLOR)

            emb.add_field(name='', value=old_field0_value)
            emb.add_field(name='', value=f'\n'.join(old_field1_value))
            emb.add_field(name='='*len(self.help_dict[first_key][des_name]), value=f'{self.help_dict[first_key][des_name]}', inline=True)

            await interaction.message.edit(embed=emb)
            await interaction.edit_origin()

        if interaction.component.label == '←':
            old_field0_value = interaction.message.embeds[0].fields[0].value
            old_field1_value = interaction.message.embeds[0].fields[1].value.split()

            for i in range(len(old_field1_value)):
                if '*' in old_field1_value[i]:
                    old_field1_value[i] = old_field1_value[i].replace('*', '')
                    old_field1_value[i] = old_field1_value[i].replace('`', '')
                    des_name = old_field1_value[i - 1]
                    old_field1_value[i - 1] = f'**`{old_field1_value[i - 1]}`**'
                    break

            for i in old_field0_value.split():
                if '*' in i:
                    first_key = i.replace('*', '').replace('`', '')

            emb = discord.Embed(title='*Список доступных команд:*',
                                description='',
                                color=COLOR)

            emb.add_field(name='', value=old_field0_value)
            emb.add_field(name='', value=f'\n'.join(old_field1_value))
            emb.add_field(name='=' * len(self.help_dict[first_key][des_name]),
                          value=f'{self.help_dict[first_key][des_name]}', inline=True)

            await interaction.message.edit(embed=emb)
            await interaction.edit_origin()
        
        if interaction.component.label == '↑':
            old_field0_value = interaction.message.embeds[0].fields[0].value.split()

            for i in range(len(old_field0_value)):
                if '*' in old_field0_value[i]:
                    old_field0_value[i] = old_field0_value[i].replace('*', '')
                    old_field0_value[i] = old_field0_value[i].replace('`', '')
                    first_key = old_field0_value[i-1]
                    old_field0_value[i-1] = f'**`{old_field0_value[i-1]}`**'
                    break

            var = list(self.help_dict[first_key].keys())

            emb = discord.Embed(title='*Список доступных команд:*',
                                description='',
                                color=COLOR)

            emb.add_field(name='', value='\n'.join(old_field0_value))
            emb.add_field(name='', value=f'**`{var[0]}`**' + '\n' + f'\n'.join([i for i in var if i != var[0]]))
            emb.add_field(name='='*len(self.help_dict[first_key][var[0]]), value=f'{self.help_dict[first_key][var[0]]}', inline=True)

            await interaction.message.edit(embed=emb)
            await interaction.edit_origin()
            
        if interaction.component.label == '↓':
            old_field0_value = interaction.message.embeds[0].fields[0].value.split()

            for i in range(len(old_field0_value)):
                if '*' in old_field0_value[i]:
                    old_field0_value[i] = old_field0_value[i].replace('*', '')
                    old_field0_value[i] = old_field0_value[i].replace('`', '')
                    if i < len(old_field0_value) - 1:
                        first_key = old_field0_value[i + 1]
                        old_field0_value[i + 1] = f'**`{old_field0_value[i + 1]}`**'
                    else:
                        first_key = old_field0_value[0]
                        old_field0_value[0] = f'**`{old_field0_value[0]}`**'
                    break

            var = list(self.help_dict[first_key].keys())

            emb = discord.Embed(title='*Список доступных команд:*',
                                description='',
                                color=COLOR)

            emb.add_field(name='', value='\n'.join(old_field0_value))
            emb.add_field(name='', value=f'**`{var[0]}`**' + '\n' + f'\n'.join([i for i in var if i != var[0]]))
            emb.add_field(name='=' * len(self.help_dict[first_key][var[0]]),
                          value=f'{self.help_dict[first_key][var[0]]}', inline=True)

            await interaction.message.edit(embed=emb)
            await interaction.edit_origin()
