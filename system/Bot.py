import discord
from discord.ext import commands
from typing import *
import json 
from BTSET import BD
from discord import app_commands
from discord.ext.commands.bot import _DefaultRepr
from discord.ext.commands.help import HelpCommand

_default: Any = _DefaultRepr()

def schitat_ycherbstvo(function_to_decorate):
    def the_wrapper(data, ctx):
        with open(f'{BD}users.json', 'r') as file:
            data =  json.load(file)
        return function_to_decorate(data, ctx)

    return the_wrapper


class WaveBot(commands.Bot):
    def __init__(
        self,
        command_prefix,
        *,
        help_command: Optional[HelpCommand] = _default,
        tree_cls = app_commands.CommandTree,
        description=None,
        intents: discord.Intents,
        **options: Any
        ) -> None:
        super().__init__(
            command_prefix=command_prefix,
            intents=intents,
            description=description,
            tree_cls=tree_cls,
            **options
        )

    @schitat_ycherbstvo
    def db_get_check(data, ctx):
        return data[str(ctx.guild.id)]['LANG']

    