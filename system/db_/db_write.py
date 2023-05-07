import discord
from discord.ext import commands
from typing import *
import json
from BTSET import BD
from system.db_.wrappers import db_write


class Color:
    @db_write
    def db_wrt_funercolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['FUNERCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_infoercolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['INFOERCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_moderercolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['MODERATIONERCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_utilityercolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['UTILITYERCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_ratecolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['RATECOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_rateercolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['RATEERCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_funcolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        print(wt_data)
        data[str(ctx.guild.id)]['FUNCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_infocolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['INFOCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_modercolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['MODERATIONCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_utilitycolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['UTILITYCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_color(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['COLOR'] = wt_data
        return data

    @db_write
    def db_wrt_ercolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['ERCOLOR'] = wt_data
        return data

    @db_write
    def db_wrt_textcolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['text_color'] = wt_data
        return data

    @db_write
    def db_wrt_barcolor(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['bar_color'] = wt_data
        return data


class UserData:
    @db_write
    def db_wtr_user_caps(self, member: discord.Member, wt_data, data=None):
        data[str(member.guild.id)]['USERS'][str(member.id)]['CAPS'] = wt_data
        return data

    @db_write
    def db_wtr_user_scr(self, member: discord.Member, wt_data, data=None):
        data[str(member.guild.id)]['USERS'][str(member.id)]['SCR'] = wt_data
        return data

    @db_write
    def db_wtr_user_lvl(self, member: discord.Member, wt_data, data=None):
        data[str(member.guild.id)]['USERS'][str(member.id)]['LvL'] = wt_data
        return data

    @db_write
    def db_wtr_user_time(self, member: discord.Member, wt_data, data=None):
        data[str(member.guild.id)]['USERS'][str(member.id)]['TIME'] = wt_data
        return data

    @db_write
    def db_wtr_user_warns(self, member: discord.Member, wt_data, data=None):
        data[str(member.guild.id)]['USERS'][str(member.id)]['WARNS'] = wt_data
        return data


class Roles:
    @db_write
    def db_wtr_joinroles(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['JoinRoles'] = wt_data
        return data

    @db_write
    def db_wtr_modroles(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['ModRoles'] = wt_data
        return data

    @db_write
    def db_wtr_roles(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['ROLES'] = wt_data
        return data

    @db_write
    def db_wtr_firstrole(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['FirstRole'] = wt_data
        return data


class Moderation:
    @db_write
    def db_wtr_ncaps(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['NCAPS'] = wt_data
        return data

    @db_write
    def db_wtr_nwarns(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['NWARNS'] = wt_data
        return data

    @db_write
    def db_wtr_adminchannel(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['ADMINCHANNEL'] = wt_data
        return data

    @db_write
    def db_wtr_idmainch(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['idMainch'] = wt_data
        return data

    @db_write
    def db_wtr_badwords(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['BADWORDS'] = wt_data
        return data

    @db_write
    def db_wtr_links(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['LINKS'] = wt_data
        return data


class Rate:
    @db_write
    def db_wtr_ignorechannels(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['IgnoreChannels'] = wt_data
        return data

    @db_write
    def db_wtr_ignoreroles(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['IgnoreRoles'] = wt_data
        return data

    @db_write
    def db_wtr_card(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['card'] = wt_data
        return data

    @db_write
    def db_wtr_blend(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['blend'] = wt_data
        return data


class DataBaseWrite(Color, Moderation, Rate, Roles, UserData):
    @db_write
    def db_wrt_lang(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['LANG'] = wt_data
        return data

    @db_write
    def db_wrt_actmoduls(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['actmoduls'] = wt_data
        return data

    @db_write
    def db_wrt_selfroom(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['SELFROOM'] = wt_data
        return data

    @db_write
    def db_wrt_prefix(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['PREFIX'] = wt_data
        return data

    @db_write
    def db_wrt_jnmsg(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['JNMSG'] = wt_data
        return data

    @db_write
    def db_wrt_selftitle(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['SelfTitle'] = wt_data
        return data

    @db_write
    def db_wrt_selfrooms(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['Selfrooms'] = wt_data
        return data

    @db_write
    def db_wrt_mafrooms(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['Mafrooms'] = wt_data
        return data

    @db_write
    def db_wrt_check(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        data[str(ctx.guild.id)]['check'] = wt_data
        return data
