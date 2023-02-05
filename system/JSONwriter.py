import json
from discord.ext import commands
import os
from BTSET import BD, DEFGUILD
class Json_write(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if not os.path.exists(f'{BD}support.json'):
            with open(f'{BD}support.json', 'w') as file:
                json.dump({
                    'idea': {},
                    'que': {},
                    'err': {},
                    'message': {}
                }, file, indent=4)
        else:
            with open(f'{BD}support.json', 'r') as file:
                if not file.read():
                    with open(f'{BD}support.json', 'w') as file:
                        json.dump({
                            'idea': {},
                            'que': {},
                            'err': {},
                            'message': {}
                        }, file, indent=4)
                    print("Пока json(support)")

        if not os.path.exists(f'{BD}glb_vote.json'):
            with open(f'{BD}glb_vote.json', 'w') as file:
                file.write('{}')
        else:
            with open(f'{BD}glb_vote.json', 'r') as file:
                if not file.read():
                    with open(f'{BD}glb_vote.json', 'w') as file:
                        file.write('{}')
                        print("Пока json(vote)")

        if not os.path.exists(f'{BD}users.json'):
            with open(f'{BD}users.json', 'w') as file:
                file.write('{}')
        else:
            with open(f'{BD}users.json', 'r') as file:
                if not file.read():
                    with open(f'{BD}users.json', 'w') as file:
                        file.write('{}')
                    print("Пока json")

        if not os.path.exists(f'{BD}music.json'):
            with open(f'{BD}music.json', 'w') as file:
                file.write('{}')
        else:
            with open(f'{BD}music.json', 'r') as file:
                if not file.read():
                    with open(f'{BD}music.json', 'w') as file:
                        file.write('{}')

        if not os.path.exists(f'{BD}anmess.json'):
            with open(f'{BD}anmess.json', 'w') as file:
                file.write('{}')
        else:
            with open(f'{BD}anmess.json', 'r') as file:
                if not file.read():
                    with open(f'{BD}anmess.json', 'w') as file:
                        file.write('{}')

    def jsonwrite(self):
        for guild in self.bot.guilds:
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
                if not (str(guild.id) in [k for k in data.keys()]):
                    data.update({
                        guild.id: DEFGUILD})

            with open(f'{BD}users.json', 'w') as file:
                json.dump(data, file, indent=4)
            for member in guild.members:
                with open(f'{BD}users.json', 'r') as file:
                    dat = json.load(file)
                if not (str(member.id) in [str(k) for k in dat[str(guild.id)]['USERS'].keys()]):
                    dat[str(guild.id)]['USERS'].update({
                        str(member.id): {
                            'WARNS': 0,
                            'CAPS': 0,
                            "SCR": 0,
                            'LvL': 1,
                            "TIME": 0.00
                        }})
                with open(f'{BD}users.json', 'w') as file:
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
