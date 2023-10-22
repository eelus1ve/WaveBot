import sqlite3
from BTSET import BD
from typing import Union
import json
import inspect
import mysql.connector
class SQLEditor():
    # db = mysql.connector.connect(
    #     host="sql7.freemysqlhosting.net",
    #     user="sql7639281",
    #     password="BEUSuLyfwn",
    #     database="sql7639281"
    #     )
    # # db = mysql.connector.connect(
    # #     host="localhost",
    # #     user="mysql",
    # #     password="mysql",
    # #     database="wavebot"

    # # )
    # conn = db.cursor()
    '''
    COLOR INT UNSIGNED,
    ERCOLOR INT UNSIGNED,

    FUNCOLOR INT UNSIGNED,
    INFOCOLOR INT UNSIGNED,
    MODERATIONCOLOR INT UNSIGNED,
    RATECOLOR INT UNSIGNED,
    UTILITYCOLOR INT UNSIGNED,
    FUNERCOLOR INT UNSIGNED,
    INFOERCOLOR INT UNSIGNED,
    MODERATIONERCOLOR INT UNSIGNED,
    RATEERCOLOR INT UNSIGNED,
    UTILITYERCOLOR INT UNSIGNED,
    '''
    # conn = db.cursor()
    
    @staticmethod
    def __get_guild(current_frame) -> Union[int, None]:
        variables = current_frame.f_back.f_locals
        for word in ['ctx', 'interaction', 'member', 'message', 'ms']:
            anyctx  = variables.get(word)
            print(anyctx)
            if anyctx: break

        return anyctx.guild.id

    # def add_privatrooms_category(guild_id, text_id, voice_id, ct_id):
    #     SQLEditor.conn = sqlite3.connect(f'{BD}WaveDateBase.db')
    #     SQLEditor.conn.execute(f'''INSERT INTO privatrooms_category(server_id, TEXT_CHANNEL_ID, VOICE_CHANNEL_ID, CATEGORY_ID) 
    #                 SELECT * FROM (SELECT %s as server_id, %s as TEXT_CHANNEL_ID, %s as VOICE_CHANNEL_ID, %s as CATEGORY_ID) AS val
    #                 WHERE NOT EXISTS (
    #                 SELECT * FROM classes WHERE server_id = %s) 
    #                 LIMIT 1
    #                 ''')
    @staticmethod
    def get_info_channels(guild_id = None):
        guild_id = guild_id or SQLEditor.__get_guild(inspect.currentframe())
        cursor = SQLEditor.conn
        cursor.execute('''
            SELECT sir.ch1_id, sir.ch2_id, sir.ch3_id, sir.ct 
            FROM server_info_channel AS sic, server 
            WHERE sic.server_id = server.id 
            LIMIT 1
        ''', (guild_id, ))
        records = cursor.fetchone()
        return records
    
    @staticmethod
    def remove_info_channels():
        guild_id = SQLEditor.__get_guild(inspect.currentframe())
        records = SQLEditor.get_info_channels(guild_id)
        SQLEditor.conn.execute('''
            DELETE 
            FROM server_info_channel 
            WHERE server_id = (SELECT id FROM server WHERE server_id = %s LIMIT 1) 
            LIMIT 1
        ''', (guild_id, ))
        SQLEditor.db.commit()
        return records
    
    @staticmethod
    def add_info_channels(ch1, ch2, ch3, ct):
        guild_id = SQLEditor.__get_guild(inspect.currentframe())
        SQLEditor.conn.execute('''
            INSERT INTO server_info_channel(server_id, CH1_ID, CH2_ID, CH3_ID, CT) 
            VALUES 
            ((SELECT id FROM server WHERE server_id = %s LIMIT 1), %s, %s, %s, %s)
        ''', (guild_id, ch1, ch2, ch3, ct))
        SQLEditor.db.commit()

    @staticmethod
    def rem_privatrooms_category():
        guild_id = SQLEditor.__get_guild(inspect.currentframe())
        SQLEditor.conn.execute('''
            DELETE 
            FROM server_privatroom_category 
            WHERE server_id = (SELECT id FROM server WHERE server_id = %s LIMIT 1) 
            LIMIT 1
        ''', (guild_id, ))

    @staticmethod
    def add_privatrooms_channels(guild_id, voice_id, owner_id):
        SQLEditor.conn.execute('''
            INSERT INTO server_privatroom_channel(server_id, voice_channel_id, owner_id) 
            SELECT * FROM (SELECT (SELECT id FROM server WHERE server_id = %s LIMIT 1) as server_id, %s as voice_channel_id, %s as owner_id) AS val
            WHERE NOT EXISTS (
            SELECT * FROM server_privatroom_channel WHERE voice_channel_id = voice_channel_id) 
            LIMIT 1
        ''', (guild_id, voice_id, owner_id))
        
    @staticmethod
    def add_privatrooms_channels(guild_id, text_id, voice_id, ct_id):
        SQLEditor.conn.execute('''
            INSERT INTO server_privatroom_channel(server_id, voice_channel_id, owner_id) 
            SELECT * FROM (SELECT (SELECT id FROM server WHERE server_id = %s LIMIT 1) as server_id, %s as voice_channel_id, %s as owner_id) AS val
            WHERE NOT EXISTS (
            SELECT * FROM server_privatroom_channel WHERE voice_channel_id = voice_channel_id) 
            LIMIT 1
        ''', ())
    
    @staticmethod
    def get_leaders():
        '''
        Ниже в коде есть альтернатива для более лучшего варика
        '''

        guild_id = SQLEditor.__get_guild(inspect.currentframe())
        cursor = SQLEditor.conn
        # def get_leaders(n1:int = 10, n2:int = ''):
        #     guild_id = SQLEditor.__get_guild(inspect.currentframe())
        #     cursor = SQLEditor.conn
        #     if n2:
        #         n2 = f"OFFSET {n2}"
        #     sql = f"""SELECT su.xp, su.user_id FROM server_user AS su, server AS s WHERE su.server_id = s.id ORDER BY su.xp DECS {n2} LIMIT {n1}"""
        cursor.execute("""
            SELECT su.xp, su.user_id 
            FROM server_user AS su, server AS s 
            WHERE su.server_id = s.id AND s.server_id = %s 
            ORDER BY su.xp DECS 
            LIMIT 10
        """, (guild_id, ))
        records: tuple = cursor.fetchall()
        return records


    @staticmethod
    def get_color(name: str, er: str = ''):
        guild_id = SQLEditor.__get_guild(inspect.currentframe())
        cursor = SQLEditor.conn
        color = f"{er}color"
        colorname = f"{name}{color}"
        cursor.execute("""
            SELECT sc.color 
            FROM server_color AS tsc, color AS tc, server AS ts 
            WHERE (tsc.color_id = tc.id AND tsc.server_id = ts.id AND ts.server_id = %s) AND (name = %s OR name = %s) 
            ORDER BY tsc.color_id DESC 
            LIMIT 1
        """, (guild_id, colorname, color))
        records: tuple = cursor.fetchone()[0]
        return records

    @staticmethod
    def write_color(name: str, value = None):
        guild_id = SQLEditor.__get_guild(inspect.currentframe())
        SQLEditor.conn.execute("""
            INSERT INTO server_color
            VALUES
            (SELECT ts.id AS server_id, tc.id AS color_id, %s AS color FROM server AS ts, color AS tc WHERE ts.server_id = %s AND tc.name = %s)        
            ON DUPLICATE KEY UPDATE
            color = color
        """, (value, guild_id, name))
        SQLEditor.db.commit()
        
    @staticmethod
    def add_class(guild_id, name: str):
        SQLEditor.conn.execute('''
            INSERT INTO classes(server_id, name) 
            SELECT * FROM (SELECT %s as server_id, %s as name) AS val
            WHERE NOT EXISTS (
            SELECT * FROM classes WHERE server_id = server_id AND name = name)
            LIMIT 1
        ''', (guild_id, name))
        SQLEditor.db.commit()

    @staticmethod
    def rem_class(guild_id, name: str):
        SQLEditor.conn.execute('''
            DELETE 
            FROM classes 
            WHERE server_id = %s, name = %s 
            LIMIT 1
        ''', (guild_id, name))
        SQLEditor.db.commit()

    @staticmethod
    def add_role(guild_id, name: str, role_id):
        SQLEditor.conn.execute('''
            INSERT INTO roles(CLASS_ID, role_id) 
            SELECT * FROM (SELECT (SELECT id FROM classes WHERE server_id = %s AND name = %s) as CLASS_ID, %s as role_id) AS val
            WHERE NOT EXISTS (
            SELECT * FROM roles WHERE CLASS_ID = (SELECT id FROM classes WHERE server_id = server_id AND name = name) AND role_id = role_id) 
            LIMIT 1
        ''', (guild_id, name, role_id, guild_id, name, role_id))
        SQLEditor.db.commit()

    @staticmethod
    def rem_role(guild_id, name: str, role_id):
        SQLEditor.conn.execute('''DELETE FROM roles WHERE CLASS_ID = (SELECT id FROM classes WHERE server_id = %s AND name = %s LIMIT 1) AND role_id = %s''', (guild_id, name, role_id))
        SQLEditor.db.commit()

    @staticmethod
    def get_roles(guild_id, name: str):
        cursor = SQLEditor.conn
        cursor.execute('''SELECT * FROM roles WHERE CLASS_ID = (SELECT id FROM classes WHERE server_id = %s AND name = %s LIMIT 1)''', (guild_id, name))
        req = cursor.fetchall()
        return req

    def read_sql(self, table: str, guild: Union[str, int], key: str) -> Union[str, int]:
        """
        Method parameters
        -----------------------------------------------
        db = "servers"       | f"server{ctx.guild.id}"
        
        guild = ctx.guild.id | ctx.author.id
        
        key = "KEY"
        """
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""SELECT {key} from {table} WHERE server_id == {guild}""")
        records: Union[str, int] = cursor.fetchone()[0]
        return records


    def write_sql(self, db: str, guild: Union[str, int], key: str, value: Union[str, int]) -> None:
        """
        Method parameters
        -----------------------------------------------
        db = "servers"       | f"server{ctx.guild.id}"

        guild = ctx.guild.id | ctx.author.id
        
        key = "KEY"
        
        value = your_value
        """
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        if type(value) == str:
            value = f'"{value}"'
            cursor.execute(f"UPDATE {db} SET {key} ="+value+f" WHERE id = {guild}")
        elif type(value) == list:
            cursor.execute(f"UPDATE {db} SET {key} = %s WHERE id = %s", (", ".join(value), str(guild)))
        elif type(value) == dict:
            cursor.execute(f"UPDATE {db} SET {key} = %s WHERE id = %s", (json.dumps(value), str(guild)))
        else:
            cursor.execute(f"UPDATE {db} SET {key} = %s WHERE id = {guild}", (value))
        sqlite_connection.commit()