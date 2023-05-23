import sqlite3
from BTSET import BD
from typing import Union
import json

class SQLeditor():

    def read_sql(self, db: str, guild: str, key: str):
        """
        db = "servers"       || f"server{ctx.guild.id}"
        
        guild = ctx.guild.id || ctx.author.id
        
        key = "KEY"
        """
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""SELECT {key} from {db} WHERE ID == {guild}""")
        records: Union[str, int] = cursor.fetchone()[0]
        cursor.close()
        if records == None:
            return records
        if "COLOR" in key and key != "TEXTCOLOR" and key != "BARCOLOR":
            return int(records, 16)
        if key in "JOINROLE, BADWORDS, LINKS, IGNORECHANNELS, IGNOREROLES, SRINFROOMS":
            return records.split(", ")
        if key in "AUDIT, MODROLES, ROLES, SELFROOM, SELFROOMS, MAFROOMS":
            return json.loads(records)
        return records


    def write_sql(self, db: str, guild: str, key: str, value: Union[str, int]):
        """
        db = "servers"       || f"server{ctx.guild.id}"
        
        guild = ctx.guild.id || ctx.author.id
        
        key = "KEY"

        value = your_value
        """
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        if type(value) == str:
            value = f'"{value}"'
            cursor.execute(f"UPDATE {db} SET {key} ="+value+f" WHERE ID = {guild}")
        elif type(value) == list:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (", ".join(value), str(guild)))
        elif type(value) == dict:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (json.dumps(value), str(guild)))
        else:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = {guild}", (value))
        sqlite_connection.commit()
        cursor.close()