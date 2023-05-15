import json
from discord.ext import commands
import os
from BTSET import BD, DEFGUILD, DEFGUILDSQL, DEFUSERSQL
import sqlite3
import discord
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


class SQL_write(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def newguildsql(self, guild):
        conn = sqlite3.connect(f'{BD}WaveDateBase.db')
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM servers WHERE ID == {guild.id}")
        data = cur.fetchall()
        if not(data):
            conn.execute(f'''CREATE TABLE IF NOT EXISTS server{guild.id}
                        (ID TEXT(20),
                        WARNS INTEGER,
                        CAPS INTEGER,
                        XP INTEGER,
                        TIME INTEGER
                        )''')
            
            serversaset = tuple(str(guild.id) if i == "id" else i for i in DEFGUILDSQL.values())
            conn.execute("INSERT INTO servers ("+", ".join([i for i in DEFGUILDSQL.keys()]) + ") VALUES ("+", ".join(["?" for i in DEFGUILDSQL.keys()])+")", serversaset)
            conn.commit()
        
        for member in guild.members:
            cur = conn.cursor()
            cur.execute(f"SELECT 1 FROM server{guild.id} WHERE ID == {member.id}")
            data = cur.fetchall()
            if not(data):
                useraset = tuple(str(member.id) if i == "id" else i for i in DEFUSERSQL.values())
                conn.execute(f"INSERT INTO server{guild.id} ("+", ".join([i for i in DEFUSERSQL.keys()]) + ") VALUES ("+", ".join(["?" for i in DEFUSERSQL.keys()])+")", useraset)
                conn.commit()
                conn.close


    def createsqltabel(self):
        if not os.path.exists(f'{BD}WaveDateBase.db'):

            conn = sqlite3.connect(f'{BD}WaveDateBase.db')

            conn.execute('''CREATE TABLE IF NOT EXISTS servers
                        (ID INTAGER,
                        CHEK TEXT(25),
                        LANG TEXT(25),
                        COLOR TEXT(25),
                        FUNCOLOR TEXT(25),
                        INFOCOLOR TEXT(25),
                        MODERATIONCOLOR TEXT(25),
                        RATECOLOR TEXT(25),
                        UTILITYCOLOR TEXT(25),
                        ERCOLOR TEXT(25),
                        FUNERCOLOR TEXT(25),
                        INFOERCOLOR TEXT(25),
                        MODERATIONERCOLOR TEXT(25),
                        RATEERCOLOR TEXT(25),
                        UTILITYERCOLOR TEXT(25),
                        AUDIT TEXT(25),
                        AUDITCHANNEL TEXT(25),
                        JOINROLES TEXT(25),
                        MODROLES TEXT(25),
                        ROLES TEXT(25),
                        ACTMODULES TEXT(25),
                        NCAPS INTAGER,
                        NWARNS INTAGER,
                        ADMINCHANNEL INTEGER,
                        IDMAINCH INTAGER,
                        SELFROOM TEXT(25),
                        BADWORDS TEXT(25),
                        LINKS TEXT(25),
                        PREFIX TEXT(25),
                        JNMSG TEXT(25),
                        SELFTITLE TEXT(25),
                        SELFROOMS TEXT(25),
                        MAFROOMS TEXT(25),
                        IGNORECHANNELS TEXT(25),
                        IGNOREROLES TEXT(25),
                        CARD TEXT(25),
                        TEXTCOLOR TEXT(25),
                        BARCOLOR TEXT(25),
                        BLEND INTAGER,
                        FIRSTROLE TEXT(25)
                        )''')
            conn.close

            for guild in self.bot.guilds:
                SQL_write(self.bot).newguildsql(guild)


    def newmembersql(self, member: discord.Member):
        conn = sqlite3.connect(f'{BD}WaveDateBase.db')
        cur = conn.cursor()
        cur.execute(f"SELECT ID FROM server{member.guild.id} WHERE ID == {member.id}")
        data = cur.fetchall()
        if not(data):
            useraset = tuple(str(member.id) if i == "id" else i for i in DEFUSERSQL.values())
            conn.execute(f"INSERT INTO server{member.guild.id} ("+", ".join([i for i in DEFUSERSQL.keys()]) + ") VALUES ("+", ".join(["?" for i in DEFUSERSQL.keys()])+")", useraset)
            conn.commit()
