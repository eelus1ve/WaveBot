import discord
import json
from typing import Optional


BOTVERSION = '***ALPHA 1.0***'
BETATESTERS = ['224930494314315776', '281070552465145857', '347027993530728448', '352413086096818176', '406124614729859073', '496021942877552660', '539848793693224970', '544279889470291989', '547077175308713994', '583722104059592757', '666768779174346782', '858638662160613376', '992771455500681307']
ADMINS = ['466609421863354388', '758734389072625685', '840307986228707368']
IGNORE = ['error', 'mafia', 'vcbot', 'xo']
BD = 'system/Database/'

def bdpy(ctx):
    with open(f'{BD}users.json', 'r') as file:
        data = json.load(file)
    return {
        "COLOR": int(data[str(ctx.guild.id)]['COLOR'], 16),
        "ErCOLOR": int(data[str(ctx.guild.id)]['ErCOLOR'], 16),
        "JoinRoles": data[str(ctx.guild.id)]['JoinRoles'],
        "ModRoles": data[str(ctx.guild.id)]['ModRoles'],
        "ROLES": data[str(ctx.guild.id)]['ROLES'],
        "FirstRole": data[str(ctx.guild.id)]['FirstRole'],
        "actmoduls": data[str(ctx.guild.id)]['actmoduls'],
        "nCaps": data[str(ctx.guild.id)]['nCaps'],
        "nWarns": data[str(ctx.guild.id)]['nWarns'],
        "idAdminchennel": data[str(ctx.guild.id)]['idAdminchennel'],
        "idMainch": data[str(ctx.guild.id)]['idMainch'],
        "selfRoom": data[str(ctx.guild.id)]['selfRoom'],
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
def bdint(ctx):
    with open(f'{BD}users.json', 'r') as file:
        data = json.load(file)
    return {
        "COLOR": int(data[str(ctx.guild_id)]['COLOR'], 16),
        "ErCOLOR": int(data[str(ctx.guild_id)]['ErCOLOR'], 16),
        "JoinRoles": data[str(ctx.guild_id)]['JoinRoles'],
        "ModRoles": data[str(ctx.guild_id)]['ModRoles'],
        "ROLES": data[str(ctx.guild_id)]['ROLES'],
        "FirstRole": data[str(ctx.guild_id)]['FirstRole'],
        "actmoduls": data[str(ctx.guild_id)]['actmoduls'],
        "nCaps": data[str(ctx.guild_id)]['nCaps'],
        "nWarns": data[str(ctx.guild_id)]['nWarns'],
        "idAdminchennel": data[str(ctx.guild_id)]['idAdminchennel'],
        "idMainch": data[str(ctx.guild_id)]['idMainch'],
        "selfRoom": data[str(ctx.guild_id)]['selfRoom'],
        "BADWORDS": data[str(ctx.guild_id)]['BADWORDS'],
        "LINKS": data[str(ctx.guild_id)]['LINKS'],
        "PREFIX": data[str(ctx.guild_id)]['PREFIX'],
        "JNMSG": data[str(ctx.guild_id)]['JNMSG'],
        "SelfTitle": data[str(ctx.guild_id)]['SelfTitle'],
        "Selfrooms": data[str(ctx.guild_id)]['Selfrooms'],
        "Mafrooms": data[str(ctx.guild_id)]['Mafrooms'],
        "IgnoreChannels": data[str(ctx.guild_id)]['IgnoreChannels'],
        "IgnoreRoles": data[str(ctx.guild_id)]['IgnoreRoles'],
        "card": data[str(ctx.guild_id)]['card'],
        "text_color": data[str(ctx.guild_id)]['text_color'],
        "bar_color": data[str(ctx.guild_id)]['bar_color'],
        "blend": data[str(ctx.guild_id)]['blend'],
        "USERS": data[str(ctx.guild_id)]['USERS']
    }


async def embpy(ctx, comp: str, des , time: Optional[float] = None, member: Optional[discord.Member] = None):
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
                color=bdpy(ctx)['ErCOLOR']
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

def embint(ctx, comp, des):
    try:
        if comp == 's':
            pass
        elif comp == 'e':
            pass
    except:
        pass