import json
from discord.ext import commands
import os

class Json_write(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        if not os.path.exists('support.json'):
            with open('support.json', 'w') as file:
                json.dump({
                    'idea': {},
                    'que': {},
                    'err': {},
                    'message': {}
                }, file, indent=4)
        else:
            with open('support.json', 'r') as file:
                if not file.read():
                    with open('support.json', 'w') as file:
                        json.dump({
                            'idea': {},
                            'que': {},
                            'err': {},
                            'message': {}
                        }, file, indent=4)
                    print("Пока json(support)")

        if not os.path.exists('glb_vote.json'):
            with open('glb_vote.json', 'w') as file:
                file.write('{"votes"}')
        else:
            with open('glb_vote.json', 'r') as file:
                if not file.read():
                    with open('glb_vote.json', 'w') as file:
                        file.write('{}')
                        print("Пока json(vote)")

        if not os.path.exists('users.json'):
            with open('users.json', 'w') as file:
                file.write('{}')
        else:
            with open('users.json', 'r') as file:
                if not file.read():
                    with open('users.json', 'w') as file:
                        file.write('{}')
                    print("Пока json")

        if not os.path.exists('music.json'):
            with open('music.json', 'w') as file:
                file.write('{}')
        else:
            with open('music.json', 'r') as file:
                if not file.read():
                    with open('music.json', 'w') as file:
                        file.write('{}')

    def jsonwrite(self):
        for guild in self.bot.guilds:
            with open('users.json', 'r') as file:
                data = json.load(file)
                if not (str(guild.id) in [k for k in data.keys()]):
                    data.update({
                        guild.id: {
                            'COLOR': '0x0000FF',
                            'ErCOLOR': '0x8B0000',
                            'AUDIT': {},
                            'AUDIT_CHANNEL': '0',
                            'JoinRoles': [],
                            'ModRoles': [],
                            'ROLES': {},
                            'actmoduls': '',
                            'nCaps': -1,
                            'nWarns': 10,
                            'idAdminchennel': '0',
                            'idMainch': '0',
                            'selfRoom': '0',
                            'BADWORDS': [],
                            'LINKS': [],
                            'PREFIX': '~',
                            'JNMSG': '',
                            'SelfTitle': '*Выберите ваши роли:* ',
                            'Selfrooms': {},
                            'Mafrooms': {},
                            'IgnoreChannels': [[], []],
                            'IgnoreRoles': [[], []],
                            'card': 'wave.png',
                            'text_color': '#d0ed2b',
                            'bar_color': '#ec5252',
                            'blend': 1,
                            'FirstRole': '',
                            'USERS': {},
                        }})

            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)
            for member in guild.members:
                with open('users.json', 'r') as file:
                    dat = json.load(file)
                if not (str(member.id) in [str(k) for k in dat[str(guild.id)]['USERS'].keys()]):
                    dat[str(guild.id)]['USERS'].update({
                        str(member.id): {
                            'WARNS': 0,
                            'CAPS': 0,
                            "SCR": 0,
                            'LvL': 1
                        }})
                with open('users.json', 'w') as file:
                    json.dump(dat, file, indent=4)



    @commands.Cog.listener('on_member_join')
    async def n_mr_join(self, ctx):
        Json_write(self.bot).jsonwrite()

    @commands.Cog.listener('on_member_remove')
    async def on_meove(self, ctx):
        Json_write(self.bot).jsonwrite()

    @commands.Cog.listener('on_guild_join')
    async def on_gld_jn(self, ctx):
        Json_write(self.bot).jsonwrite()

    @commands.Cog.listener('on_guild_remove')
    async def on_gld_remove(self, ctx):
        Json_write(self.bot).jsonwrite()

def setup(bot):
    bot.add_cog(Json_write(bot))
