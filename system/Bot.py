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
    def db_get_lang(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['LANG']

    @schitat_ycherbstvo
    def db_get_color(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['COLOR'], 16)

    @schitat_ycherbstvo
    def db_get_ercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None)-> int:
        return int(data[str(ctx.guild.id)]['ERCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_joinroles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['JoinRoles']

    @schitat_ycherbstvo
    def db_get_modroles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['ModRoles']

    @schitat_ycherbstvo
    def db_get_roles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['ROLES']

    @schitat_ycherbstvo
    def db_get_firstrole(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['FirstRole']

    @schitat_ycherbstvo
    def db_get_actmoduls(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['actmoduls']

    @schitat_ycherbstvo
    def db_get_ncaps(self, ctx: Union[commands.Context, discord.Interaction], data=None)-> int:
        return data[str(ctx.guild.id)]['NCAPS']

    @schitat_ycherbstvo
    def db_get_nwarns(self, ctx: Union[commands.Context, discord.Interaction], data=None)-> int:
        return data[str(ctx.guild.id)]['NWARNS']

    @schitat_ycherbstvo
    def db_get_adminchannel(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['ADMINCHANNEL']

    @schitat_ycherbstvo
    def db_get_idmainch(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['idMainch']

    @schitat_ycherbstvo
    def db_get_selfroom(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['SELFROOM']

    @schitat_ycherbstvo
    def db_get_badwords(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> list:
        return data[str(ctx.guild.id)]['BADWORDS']

    @schitat_ycherbstvo
    def db_get_links(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> list:
        return data[str(ctx.guild.id)]['LINKS']

    @schitat_ycherbstvo
    def db_get_prefix(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['PREFIX']

    @schitat_ycherbstvo
    def db_get_jnmsg(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['JNMSG']

    @schitat_ycherbstvo
    def db_get_selftitle(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['SelfTitle']

    @schitat_ycherbstvo
    def db_get_selfrooms(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['Selfrooms']

    @schitat_ycherbstvo
    def db_get_mafrooms(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['Mafrooms']

    @schitat_ycherbstvo
    def db_get_ignorechannels(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['IgnoreChannels']

    @schitat_ycherbstvo
    def db_get_ignoreroles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['IgnoreRoles']

    @schitat_ycherbstvo
    def db_get_card(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['card']

    @schitat_ycherbstvo
    def db_get_textcolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['text_color'], 16)

    @schitat_ycherbstvo
    def db_get_barcolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['bar_color'], 16)

    @schitat_ycherbstvo
    def db_get_blend(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['blend']

    @schitat_ycherbstvo
    def db_get_users(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['USERS']

    @schitat_ycherbstvo
    def db_get_funcolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['FUNCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_infocolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['INFOCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_modercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['MODERATIONCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_utilitycolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        print(self, ctx, data)
        return int(data[str(ctx.guild.id)]['UTILITYCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_user_warns(self, member: discord.Member, data = None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS']

    @schitat_ycherbstvo
    def db_get_user_caps(self, member: discord.Member, data = None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['CAPS']

    @schitat_ycherbstvo
    def db_get_user_scr(self, member: discord.Member, data = None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['SCR']

    @schitat_ycherbstvo
    def db_get_user_lvl(self, member: discord.Member, data = None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['LvL']

    @schitat_ycherbstvo
    def db_get_user_time(self, member: discord.Member, data=None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['TIME']

    @schitat_ycherbstvo
    def db_get_funercolor(self, ctx: Union[commands.Context, discord.Interaction], data = None ) -> int:
        return int(data[str(ctx.guild.id)]['FUNERCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_infoercolor(self, ctx: Union[commands.Context, discord.Interaction], data = None ) -> int:
        return int(data[str(ctx.guild.id)]['INFOERCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_moderercolor(self, ctx: Union[commands.Context, discord.Interaction], data = None ) -> int:
        return int(data[str(ctx.guild.id)]['MODERATIONERCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_utilityercolor(self, ctx: Union[commands.Context, discord.Interaction], data = None ) -> int:
        return int(data[str(ctx.guild.id)]['UTILITYERCOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_ratecolor(self, ctx: Union[commands.Context, discord.Interaction], data = None) -> int:
        return int(data[str(ctx.guild.id)]['RATECOLOR'], 16)

    @schitat_ycherbstvo
    def db_get_rateercolor(self, ctx: Union[commands.Context, discord.Interaction], data = None) -> int:
        return int(data[str(ctx.guild.id)]['RATEERCOLOR'], 16)

