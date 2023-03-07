import discord
from discord.ext import commands
from typing import *
import json
from BTSET import BD
from discord import app_commands
from discord.ext.commands.help import HelpCommand
from .db_.db_read import DataBaseRead
from .db_.db_write import DataBaseWrite


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

