import sqlite3
from BTSET import BD
from typing import Union, Optional, Any
import json
import inspect


class SQLEditor:

    @staticmethod
    def __get_guild(current_frame) -> Union[int, None]:
        variables = current_frame.f_back.f_globals
        for word in ['ctx', 'interaction', 'member', 'message', 'ms']:
            guild_id = variables.get(word)
            if guild_id: break

        return guild_id

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
            SQLEditor.__get_guild(inspect.currentframe())

        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""SELECT {key} from {table} WHERE SERVER_ID == {guild_id}""")
        records: Union[str, int] = cursor.fetchone()[0]
        cursor.close()
        return records

    @staticmethod
    def write_sql(request: str) -> Any:
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()

        response = cursor.execute(request).fetchall()

        sqlite_connection.commit()
        cursor.close()

        return response

    @staticmethod
    def remove_sql(table: str, key: str, value: Union[str, int, bool]) -> None:
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()

        value = f'"{value}"'
        cursor.execute(f"DELETE FROM {table} WHERE {key} = {value}")

        sqlite_connection.commit()
        cursor.close()

    @staticmethod
    def add_sql(table: str, guild_id: Optional[Union[str, int]] = None, *, value: Union[str, int, bool]) -> None:
        if not guild_id:
            guild_id = SQLEditor.__get_guild(inspect.currentframe())

        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()

        cursor.execute(f"INSERT INTO {table} VALUES (?, ?)", (guild_id, value))

        sqlite_connection.commit()
        cursor.close()

    @staticmethod
    def rewrite_sql(table: str, guild_id: Optional[Union[str, int]] = None, *, key: str, value: Union[str, int, bool]) -> None:
        """
        Method parameters
        -----------------------------------------------
        table = "name of parameter"       | f"server{ctx.guild.id}"

        guild_id = ctx.guild.id | ctx.author.id

        key = "KEY"

        value = your_value
        """

        if not guild_id:
            guild_id = SQLEditor.__get_guild(inspect.currentframe())

        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()

        value = f'"{value}"'
        cursor.execute(f"UPDATE {table} SET {key} =" + value + f" WHERE SERVER_ID = {guild_id}")

        sqlite_connection.commit()
        cursor.close()
