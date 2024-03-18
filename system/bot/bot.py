import discord
from discord.ext import commands
from typing import *
from discord import app_commands
from discord.ext.commands.help import HelpCommand
from system.db.db_functions import DbMethods

class WaveBot(commands.Bot, DbMethods):
    language = Lang()
    def __init__(
            self,
            command_prefix,
            *,
            help_command: Optional[HelpCommand] = None,
            description=None,
            intents: discord.Intents,
            **options: Any,

    ) -> None:
        super().__init__(
            command_prefix=command_prefix,
            intents=intents,
            description=description,
            **options
        )

