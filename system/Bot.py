import discord
from discord.ext import commands
from typing import *
import json
from BTSET import BD
from discord import app_commands
from discord.ext.commands.help import HelpCommand
from db_.db_read import DataBaseRead
from db_.db_write import DataBaseWrite


def db_read(function_to_decorate):
    def the_wrapper(self, ctx, data=None):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        return function_to_decorate(self, ctx=ctx, data=data)

    return the_wrapper


def db_write(function_to_decorate):
    def the_wrapper(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        data = function_to_decorate(self, ctx=ctx, data=data)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)

    return the_wrapper


class WaveBot(commands.Bot, DataBaseWrite, DataBaseRead):
    def __init__(
            self,
            command_prefix,
            *,
            help_command: Optional[HelpCommand] = None,
            tree_cls=app_commands.CommandTree,
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


