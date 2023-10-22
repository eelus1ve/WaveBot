import time
import asyncio
import multiprocessing
import os
import subprocess
from discord.ext import commands
import datetime
from system import DBwriter
from system.Bot import WaveBot
from BTSET import BD
import sqlite3


def check(bot: WaveBot):
    conn = sqlite3.connect(f'{BD}WaveDateBase.db')
    conn.execute("""PRAGMA foreign_keys=on""")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT ID FROM servers""")
    records: tuple = cursor.fetchall()
    guilds = [guild.id for guild in bot.guilds]
    for server_id in records:
        server_id = server_id[0]
        if not(server_id in guilds):
            conn.execute(f"""UPDATE servers SET STATUS = STATUS - 1 WHERE ID = {server_id}""")
            conn.execute("""DELETE FROM servers WHERE STATUS = 0""")
        else:
            conn.execute(f"""UPDATE servers SET STATUS = 7 WHERE ID = {server_id}""")
    conn.commit()
    conn.close()

def res_copy():
    if not int(datetime.datetime.now().time().hour) and int(datetime.datetime.now().minute) <= 1:
        for i in os.listdir('.'):
            if i.endswith('.json'):
                subprocess.call(fr'copy {i} system\rezerv\{i[:-5]}_rez.json', shell=True, stdout=subprocess.DEVNULL)

def prnt():
    while 1:
        res_copy()

        time.sleep(60)

            
            # if not(id in no_active_servers.keys()):
            #     no_active_servers.update({id: 7})
            # else:
            #     no_active_servers[id] = no_active_servers[id]-1
            # if not(no_active_servers[id]):
            #     conn.execute("""DELETE FROM servers WHERE SERVER_ID = ?""", (id))
            #     no_active_servers.pop(id)
    
            


class Wile_on(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        DBwriter.Json_write(self.bot).jsonwrite()  # эту строчку смыть в унитаз
        pr = multiprocessing.Process(target=prnt)
        pr.start()


async def setup(bot):
    await bot.add_cog(Wile_on(bot))
    pass
