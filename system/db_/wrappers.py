import discord
from discord.ext import commands
from typing import *
import json
from BTSET import BD


def db_read(function_to_decorate):
    def the_wrapper(self, ctx, data=None):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        return function_to_decorate(self, ctx=ctx, data=data)

    return the_wrapper


def db_write(function_to_decorate):
    def the_wrapper(self, ctx: Union[commands.Context, discord.Interaction], wt_data, data=None):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        data = function_to_decorate(self, ctx=ctx, wt_data=wt_data, data=data)
        print(int(data[str(ctx.guild.id)]['FUNCOLOR'], 16))
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)

    return the_wrapper
