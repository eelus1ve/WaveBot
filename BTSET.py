import interactions
import discord
import json


BOTVERSION = '***ALPHA 1.0***'
ADMINS = ['466609421863354388', '758734389072625685', '840307986228707368']
IGNORE = ['error', 'mafia', 'vcbot', 'xo']
BD = 'system/Bd/'


def bdpy(ctx):
    with open(f'{BD}users.json', 'r') as file:
        data = json.load(file)
    return {
        "COLOR": int(data[str(ctx.author.guild.id)]['COLOR'], 16),
        "ErCOLOR": int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16),
        "JoinRoles": data[str(ctx.author.guild.id)]['JoinRoles'],
        "ModRoles": data[str(ctx.author.guild.id)]['ModRoles'],
        "ROLES": data[str(ctx.author.guild.id)]['ROLES'],
        "FirstRole": data[str(ctx.author.guild.id)]['FirstRole'],
        "actmoduls": data[str(ctx.author.guild.id)]['actmoduls'],
        "nCaps": data[str(ctx.author.guild.id)]['nCaps'],
        "nWarns": data[str(ctx.author.guild.id)]['nWarns'],
        "idAdminchennel": data[str(ctx.author.guild.id)]['idAdminchennel'],
        "idMainch": data[str(ctx.author.guild.id)]['idMainch'],
        "selfRoom": data[str(ctx.author.guild.id)]['selfRoom'],
        "BADWORDS": data[str(ctx.author.guild.id)]['BADWORDS'],
        "LINKS": data[str(ctx.author.guild.id)]['LINKS'],
        "PREFIX": data[str(ctx.author.guild.id)]['PREFIX'],
        "JNMSG": data[str(ctx.author.guild.id)]['JNMSG'],
        "SelfTitle": data[str(ctx.author.guild.id)]['SelfTitle'],
        "Selfrooms": data[str(ctx.author.guild.id)]['Selfrooms'],
        "Mafrooms": data[str(ctx.author.guild.id)]['Mafrooms'],
        "IgnoreChannels": data[str(ctx.author.guild.id)]['IgnoreChannels'],
        "IgnoreRoles": data[str(ctx.author.guild.id)]['IgnoreRoles'],
        "card": data[str(ctx.author.guild.id)]['card'],
        "text_color": data[str(ctx.author.guild.id)]['text_color'],
        "bar_color": data[str(ctx.author.guild.id)]['bar_color'],
        "blend": data[str(ctx.author.guild.id)]['blend'],
        "USERS": data[str(ctx.author.guild.id)]['USERS']
    }
def bdmpy(mr):
    with open(f'{BD}users.json', 'r') as file:
        data = json.load(file)
    return {
        "COLOR": int(data[str(mr.guild.id)]['COLOR'], 16),
        "ErCOLOR": int(data[str(mr.guild.id)]['ErCOLOR'], 16),
        "JoinRoles": data[str(mr.guild.id)]['JoinRoles'],
        "ModRoles": data[str(mr.guild.id)]['ModRoles'],
        "ROLES": data[str(mr.guild.id)]['ROLES'],
        "FirstRole": data[str(mr.guild.id)]['FirstRole'],
        "actmoduls": data[str(mr.guild.id)]['actmoduls'],
        "nCaps": data[str(mr.guild.id)]['nCaps'],
        "nWarns": data[str(mr.guild.id)]['nWarns'],
        "idAdminchennel": data[str(mr.guild.id)]['idAdminchennel'],
        "idMainch": data[str(mr.guild.id)]['idMainch'],
        "selfRoom": data[str(mr.guild.id)]['selfRoom'],
        "BADWORDS": data[str(mr.guild.id)]['BADWORDS'],
        "LINKS": data[str(mr.guild.id)]['LINKS'],
        "PREFIX": data[str(mr.guild.id)]['PREFIX'],
        "JNMSG": data[str(mr.guild.id)]['JNMSG'],
        "SelfTitle": data[str(mr.guild.id)]['SelfTitle'],
        "Selfrooms": data[str(mr.guild.id)]['Selfrooms'],
        "Mafrooms": data[str(mr.guild.id)]['Mafrooms'],
        "IgnoreChannels": data[str(mr.guild.id)]['IgnoreChannels'],
        "IgnoreRoles": data[str(mr.guild.id)]['IgnoreRoles'],
        "card": data[str(mr.guild.id)]['card'],
        "text_color": data[str(mr.guild.id)]['text_color'],
        "bar_color": data[str(mr.guild.id)]['bar_color'],
        "blend": data[str(mr.guild.id)]['blend'],
        "USERS": data[str(mr.guild.id)]['USERS']
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


def embpy(ctx, comp, des):
    try:
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
    except:
        pass
    return(emb)
def embint(ctx, comp, des):
    try:
        if comp == 's':
            emb = interactions.Embed(
                title='Успешно',
                description=des,
                color=bdint(ctx)['COLOR']
            )
        elif comp == 'e':
            emb = interactions.Embed(
                title='Ошибка',
                description=des,
                color=bdint(ctx)['ErCOLOR']
            )
    except:
        pass
    return(emb)