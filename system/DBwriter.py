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

    def write_db(self):
        if not os.path.exists(f'{BD}WaveDateBase.db'):

            conn = sqlite3.connect(f'{BD}WaveDateBase.db')

            conn.execute('''CREATE TABLE IF NOT EXISTS cheak(
            SERVER_ID INTEGER,
            VALUE BOOLEAN
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS lang(
            SERVER_ID INTEGER,
            VALUE TEXT(5)
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS colors(
            SERVER_ID INTEGER,
            COLOR INTEGER,
            FUNCOLOR INTEGER,
            INFOCOLOR INTEGER,
            MODERATIONCOLOR INTEGER,
            RATECOLOR INTEGER,
            UTILITYCOLOR INTEGER,
            ERCOLOR INTEGER,
            ERFUNCOLOR INTEGER,
            ERINFOCOLOR INTEGER,
            ERMODERATIONCOLOR INTEGER,
            ERRATECOLOR INTEGER,
            ERUTILITYCOLOR INTEGER
            )''')
            
            conn.execute('''CREATE TABLE IF NOT EXISTS audit(
            SERVER_ID INTEGER,
            CHANNEL INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS joinroles(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS modroles(
            SERVER_ID INTEGER,
            KICK BOOLEAN,
            BAN BOOLEAN,
            UNBAN BOOLEAN,
            TEMPBAN BOOLEAN,
            WARN BOOLEAN,
            TEMPWARN BOOLEAN,
            UNWARN BOOLEAN,
            CLEARWARNS BOOLEAN,
            SETTINGS BOOLEAN,
            CLEAR BOOLEAN,
            SCORE BOOLEAN,
            CLEARSCORE BOOLEAN,
            SETLVL BOOLEAN,
            CLEARRANK BOOLEAN,
            TEMPROLE BOOLEAN,
            GIVEROLE BOOLEAN
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS roles(
            SERVER_ID INTEGER,
            CLASS TEXT(20),
            ROLE_ID INTEGER,
            EMO TEXT(20)
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS moderation(
            SERVER_ID INTEGER,
            NCAPS INTEGER,
            NWARNS INTEGER,
            ADMINCHANNEL INTEGER,
            MAINCHANNEL INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS badwords(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS links(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS prefix(
            SERVER_ID INTEGER,
            VALUE TEXT(1)
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS joinmess(
            SERVER_ID INTEGER,
            LS TEXT(1000),
            SERVER TEXT(1000)
            )''')
            
            conn.execute('''CREATE TABLE IF NOT EXISTS create_selfroom(
            SERVER_ID INTEGER,
            CT INTEGER,
            VOICE_CH INTEGER,
            TEXT_CH INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS selfrooms(
            SERVER_ID INTEGER,
            VOICE_CH INTEGER,
            OWNER INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS moderation_ignore_ch(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS moderation_ignore_role(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS rate_ignore_ch(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS rate_ignore_role(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS rate(
            SERVER_ID INTEGER,
            CARD TEXT(10),
            TEXT_COLOR TEXT(7),
            BAR_COLOR TEXT(7),
            BLEND INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS firstrole(
            SERVER_ID INTEGER,
            VALUE INTEGER
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS users(
            SERVER_ID INTEGER,
            USER_ID INTEGER,
            WARNS INTEGER,
            CAPS INTEGER,
            XP INTEGER,
            TIME INTEGER
            )''')
            conn.commit()
            conn.close
            for guild in self.bot.guilds:
                SQL_write(self.bot).newguildsql(guild)

    def newguildsql(self, guild: discord.Guild):
        conn = sqlite3.connect(f'{BD}WaveDateBase.db')
        cur = conn.cursor()  
        if not cur.execute(f"SELECT 1 FROM cheak WHERE SERVER_ID == {guild.id}").fetchall():
            conn.execute('''INSERT INTO cheak (SERVER_ID, VALUE) VALUES (?, ?)''', (guild.id, False))
            conn.execute('''INSERT INTO lang (SERVER_ID, VALUE) VALUES (?, ?)''', (guild.id, None))
            conn.execute('''INSERT INTO prefix (SERVER_ID, VALUE) VALUES (?, ?)''', (guild.id, "~"))
            conn.execute('''INSERT INTO rate (SERVER_ID, CARD, TEXT_COLOR, BAR_COLOR, BLEND) VALUES (?, ?, ?, ?, ?)''', (guild.id, "wave.png", "#d0ed2b", "#ec5252", 1))
            conn.execute("INSERT INTO colors (SERVER_ID, COLOR, FUNCOLOR, INFOCOLOR, MODERATIONCOLOR, RATECOLOR, UTILITYCOLOR, ERCOLOR, ERFUNCOLOR, ERINFOCOLOR, ERMODERATIONCOLOR, ERRATECOLOR, ERUTILITYCOLOR) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (guild.id, 0x0000FF, 0x0000FF, 0x0000FF, 0x0000FF, 0x0000FF, 0x0000FF, 0x8B0000, 0x8B0000, 0x8B0000, 0x8B0000, 0x8B0000, 0x8B0000))
            conn.commit()
            conn.close()
            for member in guild.members:
                SQL_write(self.bot).newmembersql(member)
            
                
    def newmembersql(self, member: discord.Member):
        conn = sqlite3.connect(f'{BD}WaveDateBase.db')
        cur = conn.cursor()
        if not cur.execute(f"SELECT 1 FROM users WHERE USER_ID == {member.id}").fetchall():
            conn.execute('''INSERT INTO users (SERVER_ID, USER_ID, WARNS, CAPS, XP, TIME) VALUES (?, ?, ?, ?, ?, ?)''', (member.guild.id, member.id, 0, 0, 0, 0))
        conn.commit()
        conn.close()