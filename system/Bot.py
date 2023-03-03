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
    def the_wrapper(self, data, ctx):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        return function_to_decorate(self, data, ctx)
    return the_wrapper


def db_write(function_to_decorate):
    def the_wrapper(self, data, ctx):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        data = function_to_decorate(self, data, ctx)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
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
    def db_get_lang(self, data, ctx):
        return data[str(ctx.guild.id)]['LANG']

    @schitat_ycherbstvo
    def db_get_color(self, data, ctx):
        return int(data[str(ctx.guild.id)]['COLOR'], 16)

    @schitat_ycherbstvo
    def db_get_ercolor(self, data, ctx):
        return int(data[str(ctx.guild.id)]['ERCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_joinroles(self, data, ctx):
        return data[str(ctx.guild.id)]['JoinRoles']

    @schitat_ycherbstvo
    def db_get_modroles(self, data, ctx):
        return data[str(ctx.guild.id)]['ModRoles']

    @schitat_ycherbstvo
    def db_get_roles(self, data, ctx):
        return data[str(ctx.guild.id)]['ROLES']

    @schitat_ycherbstvo
    def db_get_firstrole(self, data, ctx):
        return data[str(ctx.guild.id)]['FirstRole']

    @schitat_ycherbstvo
    def db_get_actmoduls(self, data, ctx):
        return data[str(ctx.guild.id)]['actmoduls']

    @schitat_ycherbstvo
    def db_get_ncaps(self, data, ctx):
        return data[str(ctx.guild.id)]['NCAPS']

    @schitat_ycherbstvo
    def db_get_nwarns(self, data, ctx):
        return data[str(ctx.guild.id)]['NWARNS']

    @schitat_ycherbstvo
    def db_get_adminchannel(self, data, ctx):
        return data[str(ctx.guild.id)]['ADMINCHANNEL']

    @schitat_ycherbstvo
    def db_get_idmainch(self, data, ctx):
        return data[str(ctx.guild.id)]['idMainch']

    @schitat_ycherbstvo
    def db_get_selfroom(self, data, ctx):
        return data[str(ctx.guild.id)]['SELFROOM']

    @schitat_ycherbstvo
    def db_get_badwords(self, data, ctx):
        return data[str(ctx.guild.id)]['BADWORDS']

    @schitat_ycherbstvo
    def db_get_links(self, data, ctx):
        return data[str(ctx.guild.id)]['LINKS']

    @schitat_ycherbstvo
    def db_get_prefix(self, data, ctx):
        return data[str(ctx.guild.id)]['PREFIX']

    @schitat_ycherbstvo
    def db_get_jnmsg(self, data, ctx):
        return data[str(ctx.guild.id)]['JNMSG']

    @schitat_ycherbstvo
    def db_get_selftitle(self, data, ctx):
        return data[str(ctx.guild.id)]['SelfTitle']

    @schitat_ycherbstvo
    def db_get_selfrooms(self, data, ctx):
        return data[str(ctx.guild.id)]['Selfrooms']

    @schitat_ycherbstvo
    def db_get_mafrooms(self, data, ctx):
        return data[str(ctx.guild.id)]['Mafrooms']

    @schitat_ycherbstvo
    def db_get_ignorechannels(self, data, ctx):
        return data[str(ctx.guild.id)]['IgnoreChannels']

    @schitat_ycherbstvo
    def db_get_ignoreroles(self, data, ctx):
        return data[str(ctx.guild.id)]['IgnoreRoles']

    @schitat_ycherbstvo
    def db_get_card(self, data, ctx):
        return data[str(ctx.guild.id)]['card']

    @schitat_ycherbstvo
    def db_get_textcolor(self, data, ctx):
        return data[str(ctx.guild.id)]['text_color']

    @schitat_ycherbstvo
    def db_get_barcolor(self, data, ctx):
        return data[str(ctx.guild.id)]['bar_color']

    @schitat_ycherbstvo
    def db_get_blend(self, data, ctx):
        return data[str(ctx.guild.id)]['blend']

    @schitat_ycherbstvo
    def db_get_users(self, data, ctx):
        return data[str(ctx.guild.id)]['USERS']

