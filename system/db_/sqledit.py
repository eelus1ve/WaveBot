import sqlite3
from BTSET import BD
from typing import Union
import json

class SQLeditor():

    def read_sql(self, db: str, guild: str, key: str):
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""SELECT {key} from {db} WHERE ID == {guild}""")
        records: Union[str, int] = cursor.fetchone()[0]
        cursor.close()
        if "COLOR" in key:
            return int(records, 16)
        if key in "JOINROLE, BADWORDS, LINKS, IGNORECHANNELS, IGNOREROLES":
            return records.split(", ")
        if key in "AUDIT, MODROLES, ROLES, SELFROOM, SELFROOMS, MAFROOMS":
            return json.loads(records)
        return records


    def write_sql(self, db: str, guild: str, key: str, value: Union[str, int]):
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        if type(value) == str:
            cursor.execute(f"UPDATE {db} SET {key} ="+value+f"WHERE ID = {guild}")
        elif type(value) == list:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (", ".join(value), guild))
        elif type(value) == dict:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (json.dumps(value), guild))
        else:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (value, guild))
        sqlite_connection.commit()
        cursor.close()