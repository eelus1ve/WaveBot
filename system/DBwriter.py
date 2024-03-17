import json
from discord.ext import commands
import os
from BTSET import BD, DEFGUILD, DEFGUILDSQL, DEFUSERSQL
import discord
import mysql.connector
from mysql.connector import connect, Error
from mysql.connector.connection_cext import CMySQLConnection, CMySQLCursor

mysql.connector.connect()


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

        if not os.path.exists(f'{BD}user.json'):
            with open(f'{BD}user.json', 'w') as file:
                file.write('{}')
        else:
            with open(f'{BD}user.json', 'r') as file:
                if not file.read():
                    with open(f'{BD}user.json', 'w') as file:
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
            with open(f'{BD}user.json', 'r') as file:
                data = json.load(file)
                if not (str(guild.id) in [k for k in data.keys()]):
                    data.update({
                        guild.id: DEFGUILD})

            with open(f'{BD}user.json', 'w') as file:
                json.dump(data, file, indent=4)
            for member in guild.members:
                with open(f'{BD}user.json', 'r') as file:
                    dat = json.load(file)
                if not (str(member.id) in [str(k) for k in dat[str(guild.id)]['USERS'].keys()]):
                    dat[str(guild.id)]['USERS'].update({
                        str(member.id): {
                            'warns': 0,
                            'caps': 0,
                            "SCR": 0,
                            'LvL': 1,
                            "time": 0.00
                        }})
                with open(f'{BD}user.json', 'w') as file:
                    json.dump(dat, file, indent=4)

class GetConnection:
    def __init__(
        self, 
        user: str, 
        password: str, 
        host: str,
        db_name: str
    ) -> None:
        self.__user: str = user
        self.__password: str = password
        self.__host: str = host
        self.__db_name: str = db_name
        #TODO брать из env хешированные данные и далле преобразовывать их
        try:
            self.connection: CMySQLConnection = connect(
                host=self.__host,
                user=self.__user,
                database=self.__db_name, #! Будет ошибка при отсутствии БД (Но только в случае рега db на лок пк)
                password=self.__password
            )
    
        except Error as e:
            print(e)
            if e.errno == 1049: # ! Все строчки в execpt для легкой работы в время разработки в дальнейшей эксплуатации удалить
                try:
                    connection: CMySQLConnection = connect(
                        host=self.__host,
                        user=self.__user,
                        password=self.__password,
                    )
                    with connection.cursor() as cursor:
                        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db_name};")
                    connection.close()
                    self.connection: CMySQLConnection = connect(
                        host=self.__host,
                        user=self.__user,
                        database=self.__db_name,
                        password=self.__password,
                    )
                except:
                    pass
        # self.db = mysql.connector.connect(
        # host="sql7.freemysqlhosting.net",
        # user="sql7639281",
        # password="BEUSuLyfwn",
        # database="sql7639281"
        # )
        # self.host = "sql7.freemysqlhosting.net"
        # self.user = "sql7639284"
        # self.pas = "dj3Ra3RTuu"
        # self.namedb = "sql7639284"
    def create_tables(self, cursor: CMySQLCursor):
        cursor.execute('''      
        CREATE TABLE IF NOT EXISTS server(
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        server_id BIGINT UNSIGNED NOT NULL UNIQUE,
        prefix CHAR(1) DEFAULT '~',
        PRIMARY KEY (id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS text_name(
        id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
        name TEXT,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_text(
        server_id INT UNSIGNED NOT NULL,
        text_id TINYINT UNSIGNED NOT NULL,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE,
        INDEX (text_id), FOREIGN KEY (text_id) REFERENCES text_name(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_vip(
        server_id INT UNSIGNED NOT NULL UNIQUE,
        status BOOLEAN NOT NULL,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_audit(
        server_id INT UNSIGNED NOT NULL UNIQUE,
        auditchannel BIGINT UNSIGNED NOT NULL UNIQUE,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lang(
        id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(5) UNIQUE,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_lang(
        server_id INT UNSIGNED NOT NULL UNIQUE,
        lang_id TINYINT UNSIGNED NOT NULL UNIQUE,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE,
        INDEX (lang_id), FOREIGN KEY (lang_id) REFERENCES lang(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS module(
        id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(17) UNIQUE,
        PRIMARY KEY (id)
        ) ENGINE = INNODB;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_module(
        server_id INT UNSIGNED NOT NULL,
        module_id TINYINT UNSIGNED NOT NULL,
        UNIQUE (server_id, module_id),
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE,
        INDEX (module_id), FOREIGN KEY (module_id) REFERENCES module(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')


        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_moderation(
        server_id INT UNSIGNED NOT NULL UNIQUE,
        ncaps INT UNSIGNED,
        nwarns INT UNSIGNED,
        adminchannel BIGINT UNSIGNED,
        mainch BIGINT UNSIGNED,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_rate(
        server_id INT UNSIGNED NOT NULL UNIQUE,       
        card TEXT,
        textcolor VARCHAR(7),
        barcolor VARCHAR(7),
        blend INT UNSIGNED,
        firstrole INT UNSIGNED,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE   
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS color(
        id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(17) NOT NULL UNIQUE,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_color(
        server_id INT UNSIGNED NOT NULL,
        color_id TINYINT UNSIGNED NOT NULL,
        color INT UNSIGNED,
        UNIQUE (server_id, color_id),
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server(id) ON DELETE CASCADE,
        INDEX (color_id), FOREIGN KEY (color_id) REFERENCES color(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        ''')

        cursor.execute('''     
        CREATE TABLE IF NOT EXISTS user(
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        discord_id BIGINT UNSIGNED UNIQUE,
        tg_link VARCHAR(20) UNIQUE,
        anilagann INT UNIQUE,
        PRIMARY KEY(id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_user(
        server_id INT UNSIGNED,
        user_id INT UNSIGNED,
        warns INT UNSIGNED,
        caps INT UNSIGNED,
        xp INT UNSIGNED,
        time INT UNSIGNED,
        UNIQUE (server_id, user_id),
        INDEX (user_id), FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''         
        CREATE TABLE IF NOT EXISTS user_social_rate(
        from_id INT UNSIGNED,
        to_id INT UNSIGNED,
        rate INT UNSIGNED,
        UNIQUE (from_id, to_id),
        INDEX (from_id), FOREIGN KEY (from_id) REFERENCES user(id) ON DELETE CASCADE,
        INDEX (to_id), FOREIGN KEY (to_id) REFERENCES user(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''      
        CREATE TABLE IF NOT EXISTS server_social_rate(
        from_id INT UNSIGNED,
        to_id INT UNSIGNED,
        rate INT UNSIGNED,
        UNIQUE (from_id, to_id),
        INDEX (from_id), FOREIGN KEY (from_id) REFERENCES user(id) ON DELETE CASCADE,
        INDEX (to_id), FOREIGN KEY (to_id) REFERENCES server(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''      
        CREATE TABLE IF NOT EXISTS user_review(
        from_id INT UNSIGNED,
        to_id INT UNSIGNED,
        review TEXT,
        UNIQUE (from_id, to_id),
        INDEX (from_id), FOREIGN KEY (from_id) REFERENCES user(id) ON DELETE CASCADE,
        INDEX (to_id), FOREIGN KEY (to_id) REFERENCES user(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS server_review(
        from_id INT UNSIGNED,
        to_id INT UNSIGNED,
        review TEXT,
        UNIQUE (from_id, to_id),
        INDEX (from_id), FOREIGN KEY (from_id) REFERENCES user(id) ON DELETE CASCADE,
        INDEX (to_id), FOREIGN KEY (to_id) REFERENCES server(id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_class(
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        server_id INT UNSIGNED,
        name VARCHAR(25),
        PRIMARY KEY(id),
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')
                    
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS class_role(
        class_id INT UNSIGNED,
        role_id BIGINT UNSIGNED,
        INDEX (class_id), FOREIGN KEY (class_id) REFERENCES server_class (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''        
        CREATE TABLE IF NOT EXISTS server_modrole(
        server_id INT UNSIGNED NOT NULL,
        role_id BIGINT UNSIGNED UNIQUE,
        kick BOOLEAN,
        ban BOOLEAN,
        unban BOOLEAN,
        tempban BOOLEAN,
        warn BOOLEAN,
        tempwarn BOOLEAN,
        unwarn BOOLEAN,
        clearwarns BOOLEAN,
        settings BOOLEAN,
        clear BOOLEAN,
        score BOOLEAN,
        clearscore BOOLEAN,
        setlvl BOOLEAN,
        clearrank BOOLEAN,
        temprole BOOLEAN,
        giverole BOOLEAN,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''    
        CREATE TABLE IF NOT EXISTS server_privatroom_category(
        server_id INT UNSIGNED UNIQUE,
        text_channel_id INT UNSIGNED UNIQUE,
        voice_channel_id INT UNSIGNED UNIQUE,
        category_id INT UNSIGNED UNIQUE,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''             
        CREATE TABLE IF NOT EXISTS server_privatroom_channel(
        server_id INT UNSIGNED,
        voice_channel_id INT UNSIGNED UNIQUE,
        owner_id INT UNSIGNED UNIQUE,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS word(
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        word VARCHAR(100) UNIQUE,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS list_type(
        id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
        type VARCHAR(18) UNIQUE,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_word(
        server_id INT UNSIGNED,
        type TINYINT UNSIGNED,
        word_id INT UNSIGNED,
        UNIQUE (server_id, type, word_id),
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE,
        INDEX (type), FOREIGN KEY (type) REFERENCES list_type (id) ON DELETE CASCADE,
        INDEX (word_id), FOREIGN KEY (word_id) REFERENCES word (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''           
        CREATE TABLE IF NOT EXISTS server_list(
        server_id INT UNSIGNED,
        type TINYINT UNSIGNED,
        value BIGINT,
        UNIQUE (server_id, type, value),
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE,
        INDEX (type), FOREIGN KEY (type) REFERENCES list_type (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

        cursor.execute('''      
        CREATE TABLE IF NOT EXISTS server_info_channel(
        server_id INT UNSIGNED UNIQUE,
        ch1_id INT UNSIGNED UNIQUE,
        ch2_id INT UNSIGNED UNIQUE,
        ch3_id INT UNSIGNED UNIQUE,
        ct INT UNSIGNED,
        INDEX (server_id), FOREIGN KEY (server_id) REFERENCES server (id) ON DELETE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')
    
    def create_triggers(self, cursor: CMySQLCursor):
        pass
    def create_procedures(self, cursor: CMySQLCursor):
        pass
class DbMethods:
    """
    Class of methods to work with connection
    -------------------------------
    """
    def __init__(
        self, 
        сonn_obj: GetConnection
    ) -> None:
        self.__conn_obj = сonn_obj
    
    def __get_cursor(function_to_decorate) -> CMySQLCursor:
        """
        Wrapper to get cursor
        ---------------------
        * Using only in class DbMethods
        """
        def the_wrapper(
            self: DbMethods, 
            cursor: CMySQLCursor | None = None
        ) -> None:
            with self.__conn_obj.connection.cursor() as cursor:
                return function_to_decorate(self, cursor)
        return the_wrapper
    
    @__get_cursor
    def create_db(self, cursor):
        self.__conn_obj.create_tables(cursor)
        self.__conn_obj.create_triggers(cursor)
        self.__conn_obj.create_procedures(cursor)

    @__get_cursor
    def write_db(self):
            #!-----------------------------------------
            import time 
            start_time = time.time()
            # все форки принтануть и избавиться
            full_inserts = {
                'server': [],
                'color': [(i.lower(), ) for i in ['color', 'FUNCOLOR', 'INFOCOLOR', 'MODERATIONCOLOR', 'RATECOLOR', 'UTILITYCOLOR', 'ERCOLOR', 'FUNERCOLOR', 'INFOERCOLOR', 'MODERATIONERCOLOR', 'RATEERCOLOR', 'UTILITYERCOLOR']],
                'module': [(i.lower(), ) for i in ['FUN', 'INFO', 'MODERATION', 'rate', 'UTILITY', 'ALL']],
                'list_type': [(i.lower(), ) for i in ['BADWORDS', 'LINKS', 'IgnoreChannelsRate', 'IgnoreRolesRate', 'IgnoreChannelsMod', 'IgnoreRolesMod', 'JoinRoles']],
                'server_prefix': [],
                'server_color': [],
                'user': [],
                'server_user': [],
                'text_names': [i.lower() for i in ['JNMSG', 'SELFTITLE']]
            }
            for guild in self.bot.guilds:

                full_inserts['server'].append((guild.id, ))
                # full_inserts['servers_2'].append((guild.id, False, 1, None, 255, None, None, None, None, None, 9109504, None, None, None, None, None, None, None, None, None, None, None, None, '~', None, '*Выберите ваши роли:* ', None, 'wave.png', '#d0ed2b', '#ec5252', 1, None, guild.id))
                full_inserts['server_prefix'].append((guild.id, '~'))
                full_inserts['server_color'].append((255, guild.id, 'color'))
                full_inserts['server_color'].append((guild.id, 'ercolor', 9109504))
                for member in guild.members:
                    full_inserts['user'].append((member.id, None, None))
                    full_inserts['server_user'].append((member.guild.id, member.id, member == member.guild.owner, 0, 0, 0, 0))
                # SQL_write(self.bot).newguildsql(guild)
            # print(full_inserts['server'])
            # quit()
            # for i in full_inserts.keys():
            #     for ii in full_inserts[i]:
            #         print(ii, type(ii), sep="\n--------------------------------------------------------\n")
            # quit()

            cursor.execute("""INSERT IGNORE INTO server(server_id) VALUES ?""", full_inserts['server'])
            self.db.commit()

            cursor.executemany("""INSERT IGNORE INTO color(name) VALUES ?""", full_inserts['color'])
            self.db.commit()

            cursor.executemany("""INSERT IGNORE INTO module(name) VALUES ?""", full_inserts['module'])
            self.db.commit()

            cursor.executemany("""INSERT IGNORE INTO list_type(type) VALUES ?""", full_inserts['list_type'])
            self.db.commit()

            cursor.executemany("""INSERT IGNORE INTO server_prefix(server_id, prefix) VALUES (SELECT id FROM server WHERE server_id = %s LIMIT 1), %s""", full_inserts['server_prefix'])
            self.db.commit()

            cursor.executemany("""
            INSERT IGNORE INTO server_color(server_id, color_id, color) VALUES (SELECT id FROM server WHERE server_id = %s), (SELECT id FROM color WHERE name = %s), %s""", full_inserts['server_color'])
            self.db.commit()

            # cursor.execute("""
            # SELECT * FROM (SELECT (SELECT id FROM server WHERE server_id = %s) AS server_id, (SELECT id FROM color WHERE name = %s) AS color_id, %s, AS color) as val
            # WHERE NOT EXISTS (
            # SELECT server_id FROM server_color WHERE server_id = val.server_id AND color_id = val.color_id)
            # LIMIT 1""",
            # full_inserts['server_color'][0])
            # print(cursor.fetchall())
            # self.db.commit()

            cursor.executemany('''INSERT INTO user(discord_id, tg_link, anilagann) VALUES ?''', full_inserts['user'])

            self.db.commit()

            cursor.executemany('''INSERT INTO server_user(server_id, user_id, IS_OWNER, warns, caps, xp, time) 
                        SELECT * FROM (SELECT (SELECT server.id AS server_id, user.discord_id AS user_id, %s as IS_OWNER,%s as warns, %s as caps, %s as xp, %s as time FROM server, user WHERE (server_id, discord_id) = (%s, %s) LIMIT 1)) AS val
                        WHERE NOT EXISTS (
                        SELECT user_id FROM server_user WHERE (user_id, server_id) = (val.user_id, val.server_id)) 
                        LIMIT 1''', full_inserts['server_user'])

            self.db.commit()

            cursor.close()
            print("--- %s seconds ---" % (time.time() - start_time))

    def newmembersql(self, member: discord.Member):
        cursor.execute('''INSERT INTO user(discord_id, tg_link, anilagann) 
                    SELECT * FROM (SELECT %s as discord_id, %s as tg_link, %s as anilagann) AS val
                    WHERE NOT EXISTS (
                    SELECT id FROM user WHERE discord_id = discord_id or tg_link = tg_link or anilagann = anilagann) 
                    LIMIT 1;
                    ''', (member.id, None, None))
        self.db.commit()
                
    def memberjoinsql(self, member: discord.Member):
        cursor.execute('''INSERT INTO server_user(server_id, user_id, IS_OWNER, warns, caps, xp, time) 
                    SELECT * FROM (SELECT (SELECT server.id AS server_id, user.id AS user_id FROM server, user WHERE (server_id, discord_id) = (%s, %s), %s as IS_OWNER,%s as warns, %s as caps, %s as xp, %s as time) AS val
                    WHERE NOT EXISTS (
                    SELECT user_id FROM server_user WHERE (user_id, server_id) = (user_id, server_id)) 
                    LIMIT 1;
                    ''', (member.guild.id, member.id, member == member.guild.owner, 0, 0, 0, 0))
        self.db.commit()


    def newguildsql(self, guild):
        
        # Это для создания новых db
        # serversaset = tuple(str(guild.id) if i == "id" else i for i in DEFGUILDSQL.values())
        # prINT UNSIGNED(", ".join([i for i in DEFGUILDSQL.keys()]))
        # prINT UNSIGNED('----------------------------------------------------------')
        # prINT UNSIGNED(", ".join([f"%s as {i}" for i in DEFGUILDSQL.keys()]))
        # prINT UNSIGNED('----------------------------------------------------------')
        # prINT UNSIGNED(serversaset)
        # print(guild.id)
        cursor.execute("""INSERT INTO server(server_id)
                          SELECT * FROM (SELECT %s AS server_id) as val
                          WHERE NOT EXISTS (
                          SELECT id FROM server WHERE server_id = %s)
                          LIMIT 1;""", (guild.id, guild.id))
        self.db.commit()
        
        cursor.execute("""INSERT INTO server_settings(server_id, CHEK, status, LANG, color, FUNCOLOR, INFOCOLOR, MODERATIONCOLOR, RATECOLOR, UTILITYCOLOR, ERCOLOR, FUNERCOLOR, INFOERCOLOR, MODERATIONERCOLOR, RATEERCOLOR, UTILITYERCOLOR, AUDIT, auditchannel, ACTMODULES, ncaps, nwarns, adminchannel, IDMAINCH, prefix, JNMSG, SELFTITLE, MAFROOMS, card, textcolor, barcolor, blend, firstrole) 
                    SELECT * FROM (SELECT (SELECT id FROM server WHERE server_id = %s) as server_id, %s as CHEK, %s as status,%s as LANG, %s as color, %s as FUNCOLOR, %s as INFOCOLOR, %s as MODERATIONCOLOR, %s as RATECOLOR, %s as UTILITYCOLOR, %s as ERCOLOR, %s as FUNERCOLOR, %s as INFOERCOLOR, %s as MODERATIONERCOLOR, %s as RATEERCOLOR, %s as UTILITYERCOLOR, %s as AUDIT, %s as auditchannel, %s as ACTMODULES, %s as ncaps, %s as nwarns, %s as adminchannel, %s as IDMAINCH, %s as prefix, %s as JNMSG, %s as SELFTITLE, %s as MAFROOMS, %s as card, %s as textcolor, %s as barcolor, %s as blend, %s as firstrole) AS val 
                    WHERE NOT EXISTS (
                    SELECT id FROM server WHERE id = (SELECT id FROM server WHERE server_id = %s)) 
                    LIMIT 1;""", (guild.id, False, 1, None, 255, None, None, None, None, None, 9109504, None, None, None, None, None, None, None, None, None, None, None, None, '~', None, '*Выберите ваши роли:* ', None, 'wave.png', '#d0ed2b', '#ec5252', 1, None, guild.id))
        self.db.commit()
        for member in guild.members:
            SQL_write(self.bot).newmembersql(member)
            SQL_write(self.bot).memberjoinsql(member)
