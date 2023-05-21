import discord
from discord.ext import commands
import json
from typing import Optional, Union
import sqlite3
import os

ADMINS = ['466609421863354388', '758734389072625685', '840307986228707368']
BOTVERSION = '***ALPHA 1.0***'
BETATESTERS = ['224930494314315776', '281070552465145857', '347027993530728448', '352413086096818176',
               '406124614729859073', '496021942877552660', '539848793693224970', '544279889470291989',
               '547077175308713994', '583722104059592757', '666768779174346782', '858638662160613376',
               '992771455500681307']
BD = 'system/Database/'
IGNORE = ['commands']
IGNORE_SIMV = ['<WaveEmb>']
DEFGUILDSQL = {
    'ID': "id",
    'CHEK': False,
    'LANG': None,
    'COLOR': '0x0000FF',
    'FUNCOLOR': '0x0000FF',
    'INFOCOLOR': '0x0000FF',
    'MODERATIONCOLOR': '0x0000FF',
    'RATECOLOR': '0x0000FF',
    'UTILITYCOLOR': '0x0000FF',
    'ERCOLOR': '0x8B0000',
    'FUNERCOLOR': '0x8B0000',
    'INFOERCOLOR': '0x8B0000',
    'MODERATIONERCOLOR': '0x8B0000',
    'RATEERCOLOR': '0x8B0000',
    'UTILITYERCOLOR': '0x8B0000',
    'SRINFROOMS': None,
    'AUDIT': None,
    'AUDITCHANNEL': None,
    'JOINROLES': None,
    'MODROLES': None,
    'ROLES': None,
    'ACTMODULES': None,
    'NCAPS': None,
    'NWARNS': None,
    'ADMINCHANNEL': None,
    'IDMAINCH': None,
    'SELFROOM': None,
    'BADWORDS': None,
    'LINKS': None,
    'PREFIX': '~',
    'JNMSG': None,
    'SELFTITLE': '*Выберите ваши роли:* ',
    'SELFROOMS': None,
    'MAFROOMS': None,
    'IGNORECHANNELS': None,
    'IGNOREROLES': None,
    'CARD': 'wave.png',
    'TEXTCOLOR': '#d0ed2b',
    'BARCOLOR': '#ec5252',
    'BLEND': 1,
    'FIRSTROLE': None
}

DEFUSERSQL = {
    'ID': 'id',
    'WARNS': 0,
    'CAPS': 0,
    "XP": 0,
    "TIME": 0
}

DEFGUILD = {
    '': "id",
    'check': False,
    'LANG': 'ru',
    'COLOR': '0x0000FF',
    'FUNCOLOR': '0x0000FF',
    'INFOCOLOR': '0x0000FF',
    'MODERATIONCOLOR': '0x0000FF',
    'RATECOLOR': '0x0000FF',
    'UTILITYCOLOR': '0x0000FF',
    'ERCOLOR': '0x8B0000',
    'FUNERCOLOR': '0x8B0000',
    'INFOERCOLOR': '0x8B0000',
    'MODERATIONERCOLOR': '0x8B0000',
    'RATEERCOLOR': '0x8B0000',
    'UTILITYERCOLOR': '0x8B0000',
    'AUDIT': {},
    'AUDIT_CHANNEL': '0',
    'JoinRoles': [],
    'ModRoles': {},
    'ROLES': {},
    'actmoduls': '',
    'NCAPS': -1,
    'NWARNS': 10,
    'ADMINCHANNEL': '0',
    'idMainch': '0',
    'SELFROOM': {},
    'BADWORDS': [],
    'LINKS': [],
    'PREFIX': '~',
    'JNMSG': '',
    'SelfTitle': '*Выберите ваши роли:* ',
    'Selfrooms': {},
    'Mafrooms': {},
    'IgnoreChannels': [[], []],
    'IgnoreRoles': [[], []],
    'card': 'wave.png',
    'text_color': '#d0ed2b',
    'bar_color': '#ec5252',
    'blend': 1,
    'FirstRole': '',
    'USERS': {},
}

DBSTR = [i for i in DEFGUILD.keys() if (type(DEFGUILD[i]) in [str, int, bool])]

DEFMODROLE = {
    "kick": True, 
    "ban": True, 
    "unban": True, 
    "tempban": True,
    "warn": True,
    "tempwarn": True,
    "unwarn": True,
    "clearwarns": True,
    "settings": True,
    "clear": True,
    "score": True,
    "clearscore": True,
    "setlvl": True,
    "clearrank": True,
    "temprole": True, 
    "giverole": True
}

class Moderation:
    def __init__(self, member):
        self.warns: int = bdpy(member)['USERS'][str(member.id)]['WARNS']
        self.nWarns: int = bdpy(member)['NWARNS']
        self.idadminchannel: str = bdpy(member)["ADMINCHANNEL"]
        self.NCAPS: int = bdpy(member)['NCAPS']
        self.color = bdpy(member)['COLOR']
        self.ercolor = bdpy(member)['ERCOLOR']
        self.prefix: str = bdpy(member)["PREFIX"]
        self.badwords = bdpy(member)['BADWORDS']
        self.links = bdpy(member)['LINKS']


class InteractionComponents:
    def __init__(self, interaction: discord.Interaction):
        inter = None
        for rw in interaction.message.components:
            inter = [i for i in rw.children if i.custom_id == interaction.data["custom_id"]] or inter
        inter = inter[0]

        self.inter_type = interaction.data['component_type']

        if self.inter_type == 2:
            self.label = inter.label
            self.emoji = inter.emoji

            self.placeholder = None
            self.values = None

        if self.inter_type == 3:
            self.placeholder = inter.placeholder
            self.values = interaction.data['values']

            self.label = None
            self.emoji = None

def bdpy(ctx: commands.Context):
    with open(f'{BD}users.json', 'r') as file:
        data = json.load(file)
    return {
        "LANG": data[str(ctx.guild.id)]['LANG'],
        "COLOR": int(data[str(ctx.guild.id)]['COLOR'], 16),
        "ERCOLOR": int(data[str(ctx.guild.id)]['ERCOLOR'], 16),
        "JoinRoles": data[str(ctx.guild.id)]['JoinRoles'],
        "ModRoles": data[str(ctx.guild.id)]['ModRoles'],
        "ROLES": data[str(ctx.guild.id)]['ROLES'],
        "FirstRole": data[str(ctx.guild.id)]['FirstRole'],
        "actmoduls": data[str(ctx.guild.id)]['actmoduls'],
        "NCAPS": data[str(ctx.guild.id)]['NCAPS'],
        "NWARNS": data[str(ctx.guild.id)]['NWARNS'],
        "ADMINCHANNEL": data[str(ctx.guild.id)]['ADMINCHANNEL'],
        "idMainch": data[str(ctx.guild.id)]['idMainch'],
        "SELFROOM": data[str(ctx.guild.id)]['SELFROOM'],
        "BADWORDS": data[str(ctx.guild.id)]['BADWORDS'],
        "LINKS": data[str(ctx.guild.id)]['LINKS'],
        "PREFIX": data[str(ctx.guild.id)]['PREFIX'],
        "JNMSG": data[str(ctx.guild.id)]['JNMSG'],
        "SelfTitle": data[str(ctx.guild.id)]['SelfTitle'],
        "Selfrooms": data[str(ctx.guild.id)]['Selfrooms'],
        "Mafrooms": data[str(ctx.guild.id)]['Mafrooms'],
        "IgnoreChannels": data[str(ctx.guild.id)]['IgnoreChannels'],
        "IgnoreRoles": data[str(ctx.guild.id)]['IgnoreRoles'],
        "card": data[str(ctx.guild.id)]['card'],
        "text_color": data[str(ctx.guild.id)]['text_color'],
        "bar_color": data[str(ctx.guild.id)]['bar_color'],
        "blend": data[str(ctx.guild.id)]['blend'],
        "USERS": data[str(ctx.guild.id)]['USERS']
    }


class Rool():
    def __init__(self, ctx: commands.Context):
        sql = sqlite3.connect(f'{BD}WaveDateBase.db').cursor().execute(f"""SELECT MODROLES from servers WHERE ID == {ctx.guild.id}""").fetchone()[0]
        if sql != {}:
            mods = sql[str([str(i.id) for i in ctx.author.roles if str(i.id) in sql][0])]

            self.clearRank = mods['Rate']['CLearRank'] == "True" or ctx.author.guild_permissions.administrator
            self.score = mods['Rate']['Score'] == "True" or ctx.author.guild_permissions.administrator
            self.setlvl = mods['Rate']['SetLvl'] == "True" or ctx.author.guild_permissions.administrator
            self.clearScore = mods['Rate']['ClearScore'] == "True" or ctx.author.guild_permissions.administrator
            self.warn = mods['Warns']['Warn'] == "True" or ctx.author.guild_permissions.administrator
            self.unwarn = mods['Warns']['UnWarn'] == "True" or ctx.author.guild_permissions.administrator
            self.clearWarn = mods['Warns']['ClearWarn'] == "True" or ctx.author.guild_permissions.administrator
            self.kick = mods['Kick'] == "True" or ctx.author.guild_permissions.administrator
            self.clear = mods['Clear'] == "True" or ctx.author.guild_permissions.administrator
            self.ban = mods['Bans']['Ban'] == "True" or ctx.author.guild_permissions.administrator
        else:
            self.clearRank = ctx.author.guild_permissions.administrator
            self.score = ctx.author.guild_permissions.administrator
            self.setlvl = ctx.author.guild_permissions.administrator
            self.clearScore = ctx.author.guild_permissions.administrator
            self.warn = ctx.author.guild_permissions.administrator
            self.unwarn = ctx.author.guild_permissions.administrator
            self.clearWarn = ctx.author.guild_permissions.administrator
            self.kick = ctx.author.guild_permissions.administrator
            self.clear = ctx.author.guild_permissions.administrator
            self.ban = ctx.author.guild_permissions.administrator


# SQLeditor.read_sql(db="servers", guild=str(ctx.guild.id), key="ADMINCHANNEL")

    def role(quest: str):
        def predicate(ctx: commands.Context):
            chn = sqlite3.connect(f'{BD}WaveDateBase.db').cursor().execute(f"""SELECT AUDITCHANNEL from servers WHERE ID == {ctx.guild.id}""").fetchone()[0]
            if quest == 'clear' and Rool(ctx).clear and (str(ctx.channel.id) != str(chn) or ctx.author.id == ctx.guild.owner.id):
                return True
            elif quest == 'clearRank' and Rool(ctx).clearRank:
                return True
            elif quest == 'score' and Rool(ctx).score:
                return True
            elif quest == 'setlvl' and Rool(ctx).setlvl:
                return True
            elif quest == 'warn' and Rool(ctx).warn:
                return True
            elif quest == 'unwarn' and Rool(ctx).unwarn:
                return True
            elif quest == 'clearWarn' and Rool(ctx).clearWarn:
                return True
            elif quest == 'kick' and Rool(ctx).kick:
                return True
            elif quest == 'ban' and Rool(ctx).ban:
                return True
            raise commands.MissingPermissions(['nomoder'])

        return commands.check(predicate)


async def embpy(ctx: commands.Context, comp: str, des, time: Optional[float] = None,
                member: Optional[discord.Member] = None):
    if comp == 's':
        emb = discord.Embed(
            title='Успешно',
            description=des,
            color=bdpy(ctx)['COLOR']
        )
    elif comp == 'e':
        emb = discord.Embed(
            title='Ошибка',
            description=des,
            color=bdpy(ctx)['ERCOLOR']
        )
    elif comp == 'n':
        emb = discord.Embed(
            title=des,
            color=bdpy(ctx)['COLOR']
        )
    if member:
        if time:
            await member.send(embed=emb, delete_after=time)

        else:
            await member.send(embed=emb)
    else:
        if time:
            await ctx.send(embed=emb, delete_after=time)
        else:
            await ctx.send(embed=emb)

class Lang():
    def __init__(self, ctx: Union[commands.Context, discord.Interaction]):
        self.language = self.lang(ctx)

    def lang(self, ctx: commands.Context):
        sql = sqlite3.connect(f'{BD}WaveDateBase.db').cursor().execute(f"""SELECT LANG from servers WHERE ID == {ctx.guild.id}""").fetchone()[0]
        lang_dict = {}
        part = 'system\\Languages\\ru.wave'     #потом заменить на en-US
        if os.path.exists('system\\Languages\\{}.wave'.format(str(ctx.guild.preferred_locale) if not sql else sql)):
            part = 'system\\Languages\\{}.wave'.format(str(ctx.guild.preferred_locale) if not sql else sql)
        with open(f'{part}', 'r', encoding='utf-8') as f:
            for line in f:
                if not (line.startswith('//')) and not (line == '\n'):
                    key, *value = line.split()
                    lang_dict[key] = ' '.join([i.replace('\\n', '\n') for i in value])
        return lang_dict
