import discord
from discord.ext import commands
from typing import *
from discord import app_commands
from discord.ext.commands.help import HelpCommand
from system.db_.db_read import DataBaseRead
from system.db_.db_write import DataBaseWrite
from system.db_.sqledit import SQLEditor


class WaveBot(commands.Bot, DataBaseWrite, DataBaseRead, SQLEditor):
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
