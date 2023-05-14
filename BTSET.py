import discord
from discord.ext import commands
import json
from typing import Optional, Union
# from system.db_.sqledit import SQLeditor
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
    'CHEK': 'False',
    'LANG': 'ru_RU',
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
    'AUDIT': '{}',
    'AUDITCHANNEL': '0',
    'JOINROLES': '[]',
    'MODROLES': '{}',
    'ROLES': '{}',
    'ACTMODULES': '-1',
    'NCAPS': -1,
    'NWARNS': 10,
    'ADMINCHANNEL': '0',
    'IDMAINCH': '0',
    'SELFROOM': '{}',
    'BADWORDS': '[]',
    'LINKS': '[]',
    'PREFIX': '~',
    'JNMSG': '-1',
    'SELFTITLE': '*Выберите ваши роли:* ',
    'SELFROOMS': '{}',
    'MAFROOMS': '{}',
    'IGNORECHANNELS': '[[], []]',
    'IGNOREROLES': '[[], []]',
    'CARD': 'wave.png',
    'TEXTCOLOR': '#d0ed2b',
    'BARCOLOR': '#ec5252',
    'BLEND': 1,
    'FIRSTROLE': '-1'
}

DEFUSERSQL = {
    'ID': 'id',
    'WARNS': 0,
    'CAPS': 0,
    "SCR": 0,
    'LVL': 1,
    "TIME": 0
}




DEFGUILD = {
    '': "id",
    'check': False,
    'LANG': 'ru_RU',
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

# with open(f'{BD}users.json', 'r') as file:
#     d: dict = json.load(file)
# SERVERS = [i for i in d.keys()]


class Score_presets:
    def __init__(self, member):
        self.ignorechannels = bdpy(member)['IgnoreChannels']
        self.ignoreroles = bdpy(member)['IgnoreRoles']
        self.score = bdpy(member)['USERS'][str(member.id)]['SCR']
        self.lvl = bdpy(member)['USERS'][str(member.id)]['LvL']
        self.idadminchannel = int(bdpy(member)["ADMINCHANNEL"])  # тут для
        self.color = bdpy(member)['COLOR']  # это надо для разделения цветов
        self.ercolor = bdpy(ctx=member)['ERCOLOR']
        self.prefix: str = bdpy(member)["PREFIX"]


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


class Fun:
    def __init__(self, ctx):
        self.color = bdpy(ctx)['COLOR']
        self.ercolor = bdpy(ctx)['ERCOLOR']


class Info:
    def __init__(self, ctx):
        self.color = bdpy(ctx)['COLOR']
        self.ercolor = bdpy(ctx)['ERCOLOR']


class Utility:
    def __init__(self, ctx):
        self.color = bdpy(ctx)['COLOR']
        self.ercolor = bdpy(ctx)['ERCOLOR']


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


# class Audit():
#     def __init__(self, ctx):
#         self.color = bdpy(ctx)['COLOR']
#     def auditEmb(self, ctx):
#         emb = discord.Embed(
#             title='Нарушение снято!',
#             description=f"*Ранее, у участника было уже {Moderation(ctx).warns - 1} нарушений, после {Moderation(ctx).NWARNS} он будет забанен!*",
#             timestamp=ctx.message.created_at,
#             color=self.color
#         )                                                                                                                   #переписать под unwarn
#         emb.add_field(name='Канал:', value='Не определён', inline=True)
#         emb.add_field(name='Участник:', value=ctx.mention, inline=True)
#         emb.set_footer(text=f'Предупреждение снято участником {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
# await get(ctx.guild.text_channels, id=Moderation(member).idadminchannel).send(embed=emb)

# class DateBaseEditor():
#     def __init__(self, ctx):
#         self.color = bdpy(ctx)['COLOR']
#         self.ercolor = bdpy(ctx)['ERCOLOR']
#         # with open(f'{BD}users.json', 'r') as file:
#         #     data = json.load(file)
#         # self.color = int(data[str(ctx.guild.id)]['COLOR'], 16)
#         # self.ercolor = int(data[str(ctx.guild.id)]['ERCOLOR'], 16)
#         # self.joinroles = data[str(ctx.guild.id)]['JoinRoles']
#         # self.modroles = data[str(ctx.guild.id)]['ModRoles']
#         # self.roles = data[str(ctx.guild.id)]['ROLES']
#         # self.firstrole = data[str(ctx.guild.id)]['FirstRole']
#         # self.actmoduls = data[str(ctx.guild.id)]['actmoduls']
#         # self.ncaps = data[str(ctx.guild.id)]['NCAPS']
#         # self.nwarns = data[str(ctx.guild.id)]['NWARNS']
#         # self.idadminchennel =  data[str(ctx.guild.id)]['idAdminchennel']
#         # self.idmainch = data[str(ctx.guild.id)]['idMainch']
#         # self.selfroom = data[str(ctx.guild.id)]['selfRoom']
#         # self.badwords = data[str(ctx.guild.id)]['BADWORDS']
#         # self.links = data[str(ctx.guild.id)]['LINKS']
#         # self.prefix = data[str(ctx.guild.id)]['PREFIX']
#         # self.jnmsg = data[str(ctx.guild.id)]['JNMSG']
#         # self.selftitle = data[str(ctx.guild.id)]['SelfTitle']
#         # self.selfrooms = data[str(ctx.guild.id)]['Selfrooms']
#         # self.mafrooms =  data[str(ctx.guild.id)]['Mafrooms']
#         # self.ignorechannels = data[str(ctx.guild.id)]['IgnoreChannels']
#         # self.ignoreroles = data[str(ctx.guild.id)]['IgnoreRoles']
#         # self.card =  data[str(ctx.guild.id)]['card']
#         # self.text_color = data[str(ctx.guild.id)]['text_color']
#         # self.bar_color = data[str(ctx.guild.id)]['bar_color']
#         # self.blend = data[str(ctx.guild.id)]['blend']
#         # self.users = data[str(ctx.guild.id)]['USERS']


# def db_write(db: str, ctx: commands.Context, locate: str, arg):
#     with open(f'{BD}{db}.json', 'r') as file:
#         data = json.load(file)
#     if locate in DBSTR:
#         data[locate] = arg
#     else:
#         pass
#     with open(f'{BD}{db}.json', 'w') as file:
#         json.dump(data, file, indent=4)

# def db_read(db: str, ctx: commands.Context, locate: str):
#     with open(f'{BD}{db}.json', 'r') as file:
#         date = json.load(file)
#     return date[ctx][locate]


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
        if bdpy(ctx)['ModRoles'] != '{}':
            mods = bdpy(ctx)['ModRoles'][
                str([str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0])]

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
            if quest == 'clear' and Rool(ctx).clear and (ctx.channel.id != bdpy(ctx)["idadminchannel"] or ctx.author.id == ctx.guild.owner.id):
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
        lang_dict = {}
        with open('system\\Languages\\{}.wave'.format(bdpy(ctx)['LANG']), 'r', encoding='utf-8') as f:
            for line in f:
                if not (line.startswith('//')) and not (line == '\n'):
                    key, *value = line.split()
                    lang_dict[key] = ' '.join([i.replace('\\n', '\n') for i in value])
        return lang_dict
