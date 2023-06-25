import sqlite3
from BTSET import BD
from typing import Union, Optional
import json
import inspect


class SQLEditor:

    @staticmethod
    def read_sql(table: str, guild_id: Optional[Union[str, int]] = None, *, key: str) -> Union[str, int]:
        """
        Method parameters
        -----------------------------------------------
        db = "servers"       | f"server{ctx.guild.id}"
        
        guild = ctx.guild.id | ctx.author.id
        
        key = "KEY"
        """

        if not guild_id:
            variables = inspect.currentframe().f_back.f_locals
            guild_id = variables.get('ctx') or variables.get('interaction') or variables.get('member') or variables.get(
                'message') or variables.get('ms')
            guild_id = guild_id.guild.id if guild_id else None
            print(guild_id)

        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""SELECT {key} from {table} WHERE SERVER_ID == {guild_id}""")
        records: Union[str, int] = cursor.fetchone()[0]
        cursor.close()
        return records

    @staticmethod
    def write_sql(db: str, guild: Union[str, int], key: str, value: Union[str, int]) -> None:
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
            cursor.execute(f"UPDATE {db} SET {key} =" + value + f" WHERE ID = {guild}")
        elif type(value) == list:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (", ".join(value), str(guild)))
        elif type(value) == dict:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (json.dumps(value), str(guild)))
        else:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = {guild}", (value))
        sqlite_connection.commit()
        cursor.close()
