import sqlite3
from BTSET import BD

class SQLeditor():
    def read_sql(db, guild, arg):
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""SELECT {arg} from {db} WHERE ID == {guild}""")
        records = cursor.fetchone()
        cursor.close()
        return records


    def write_sql(db, guild, key, value):
        sqlite_connection = sqlite3.connect(f'{BD}WaveDateBase.db')
        cursor = sqlite_connection.cursor()
        if type(value) == str:
            cursor.execute(f"UPDATE {db} SET {key} ="+value+f"WHERE ID = {guild}")
        else:
            cursor.execute(f"UPDATE {db} SET {key} = ? WHERE ID = ?", (value, guild))
        sqlite_connection.commit()
        cursor.close()