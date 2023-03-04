import discord
from discord.ext import commands
from typing import *
import json
from BTSET import BD
from .wrappers import db_write


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


class DataBaseWrite(Color):
    pass
