import discord
from discord.ext import commands
from typing import *
from discord import app_commands
from discord.ext.commands.help import HelpCommand
from .db_.db_read import DataBaseRead
from .db_.db_write import DataBaseWrite
from .db_.sqledit import SQLEditor


class WaveBot(commands.Bot, DataBaseWrite, DataBaseRead, SQLEditor):
    def __init__(
            self,
            command_prefix,
            *,
            help_command: Optional[HelpCommand] = None,
            description=None,
            intents: discord.Intents,
            **options: Any
    ) -> None:
        super().__init__(
            command_prefix=command_prefix,
            intents=intents,
            description=description,
            **options
        )
