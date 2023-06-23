import sqlite3
from BTSET import BD
from typing import Union
import json

class SQLeditor():

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
        cursor.execute(f"""SELECT {key} from {table} WHERE SERVER_ID == {guild}""")
        records: Union[str, int] = cursor.fetchone()[0]
        cursor.close()
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
            cursor.execute(f"UPDATE {db} SET {key} ="+value+f" WHERE ID = {guild}")
        elif type(value) == list:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (", ".join(value), str(guild)))
        elif type(value) == dict:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (json.dumps(value), str(guild)))
        else:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = {guild}", (value))
        sqlite_connection.commit()
        cursor.close()