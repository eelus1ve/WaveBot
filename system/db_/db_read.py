import discord
from discord.ext import commands
from typing import *
import json
from BTSET import BD
from .wrappers import db_read


class Color:
    @db_read
    def db_get_funercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['FUNERCOLOR'], 16)

    @db_read
    def db_get_infoercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['INFOERCOLOR'], 16)

    @db_read
    def db_get_moderercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['MODERATIONERCOLOR'], 16)

    @db_read
    def db_get_utilityercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['UTILITYERCOLOR'], 16)

    @db_read
    def db_get_ratecolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['RATECOLOR'], 16)

    @db_read
    def db_get_rateercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['RATEERCOLOR'], 16)

    @db_read
    def db_get_funcolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['FUNCOLOR'], 16)

    @db_read
    def db_get_infocolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['INFOCOLOR'], 16)

    @db_read
    def db_get_modercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['MODERATIONCOLOR'], 16)

    @db_read
    def db_get_utilitycolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['UTILITYCOLOR'], 16)

    @db_read
    def db_get_color(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['COLOR'], 16)

    @db_read
    def db_get_ercolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return int(data[str(ctx.guild.id)]['ERCOLOR'], 16)

    @db_read
    def db_get_textcolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['text_color']

    @db_read
    def db_get_barcolor(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['bar_color']


class UserData:
    @db_read
    def db_get_user_caps(self, member: discord.Member, data=None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['CAPS']

    @db_read
    def db_get_user_scr(self, member: discord.Member, data=None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['SCR']

    @db_read
    def db_get_user_lvl(self, member: discord.Member, data=None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['LvL']

    @db_read
    def db_get_user_time(self, member: discord.Member, data=None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['TIME']

    @db_read
    def db_get_users(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['USERS']

    @db_read
    def db_get_user_warns(self, member: discord.Member, data=None) -> int:
        return data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS']


class Roles:
    @db_read
    def db_get_joinroles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['JoinRoles']

    @db_read
    def db_get_modroles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['ModRoles']

    @db_read
    def db_get_roles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['ROLES']

    @db_read
    def db_get_firstrole(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['FirstRole']


class Moderation:
    @db_read
    def db_get_ncaps(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['NCAPS']

    @db_read
    def db_get_nwarns(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['NWARNS']

    @db_read
    def db_get_adminchannel(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['ADMINCHANNEL']

    @db_read
    def db_get_idmainch(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> int:
        return data[str(ctx.guild.id)]['idMainch']

    @db_read
    def db_get_badwords(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> list:
        return data[str(ctx.guild.id)]['BADWORDS']

    @db_read
    def db_get_links(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> list:
        return data[str(ctx.guild.id)]['LINKS']


class Rate:
    @db_read
    def db_get_ignorechannels(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['IgnoreChannels']

    @db_read
    def db_get_ignoreroles(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['IgnoreRoles']

    @db_read
    def db_get_card(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['card']

    @db_read
    def db_get_blend(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['blend']


class DataBaseRead(Color, UserData, Rate, Roles, Moderation):
    @db_read
    def db_get_lang(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['LANG']

    @db_read
    def db_get_actmoduls(self, ctx: Union[commands.Context, discord.Interaction], data=None):
        return data[str(ctx.guild.id)]['actmoduls']

    @db_read
    def db_get_selfroom(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> dict:
        return data[str(ctx.guild.id)]['SELFROOM']

    @db_read
    def db_get_prefix(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['PREFIX']

    @db_read
    def db_get_jnmsg(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['JNMSG']

    @db_read
    def db_get_selftitle(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> str:
        return data[str(ctx.guild.id)]['SelfTitle']

    @db_read
    def db_get_selfrooms(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> dict:
        return data[str(ctx.guild.id)]['Selfrooms']

    @db_read
    def db_get_mafrooms(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> dict:
        return data[str(ctx.guild.id)]['Mafrooms']

    @db_read
    def db_get_check(self, ctx: Union[commands.Context, discord.Interaction], data=None) -> bool:
        return data[str(ctx.guild.id)]['check']
