from typing import Union
import discord
from discord.ext import commands
import os

class Lang:
    def __init__(self, ctx: Union[commands.Context, discord.Interaction]):
        self.language = self.lang(ctx)

    def lang(self, ctx: commands.Context):
        # sql = sqlite3.connect(f'{BD}WaveDateBase.db').cursor().execute(f"""SELECT LANG from servers WHERE ID == {ctx.guild.id}""").fetchone()[0]
        lang_dict = {}
        part = 'system\\Languages\\ru.wave'     #потом заменить на en-US
        # if os.path.exists('system\\Languages\\{}.wave'.format(str(ctx.guild.preferred_locale) if not sql else sql)):
        #     part = 'system\\Languages\\{}.wave'.format(str(ctx.guild.preferred_locale) if not sql else sql)
        for i in os.path.
            with open(f'{part}', 'r', encoding='utf-8') as f:
                for line in f:
                    if not (line.startswith('//')) and not (line == '\n'):
                        key, *value = line.split()
                        lang_dict[key] = ' '.join([i.replace('\\n', '\n') for i in value])
        return lang_dict
