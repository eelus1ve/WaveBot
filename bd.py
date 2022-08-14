import json
def bdpy(ctx):
    with open('users.json', 'r') as file:
        dataServerID = json.load(file)
    return {
        "COLOR": int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16),
        "ErCOLOR": int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16),
        "JoinRoles": dataServerID[str(ctx.author.guild.id)]['JoinRoles'],
        "ModRoles": dataServerID[str(ctx.author.guild.id)]['ModRoles'],
        "ROLES": dataServerID[str(ctx.author.guild.id)]['ROLES'],
        "actmoduls": dataServerID[str(ctx.author.guild.id)]['actmoduls'],
        "nCaps": dataServerID[str(ctx.author.guild.id)]['nCaps'],
        "nWarns": dataServerID[str(ctx.author.guild.id)]['nWarns'],
        "idAdminchennel": dataServerID[str(ctx.author.guild.id)]['idAdminchennel'],
        "idMainch": dataServerID[str(ctx.author.guild.id)]['idMainch'],
        "selfRoom": dataServerID[str(ctx.author.guild.id)]['selfRoom'],
        "BADWORDS": dataServerID[str(ctx.author.guild.id)]['BADWORDS'],
        "LINKS": dataServerID[str(ctx.author.guild.id)]['LINKS'],
        "PREFIX": dataServerID[str(ctx.author.guild.id)]['PREFIX'],
        "JNMSG": dataServerID[str(ctx.author.guild.id)]['JNMSG'],
        "SelfTitle": dataServerID[str(ctx.author.guild.id)]['SelfTitle'],
        "Selfrooms": dataServerID[str(ctx.author.guild.id)]['Selfrooms'],
        "Mafrooms": dataServerID[str(ctx.author.guild.id)]['Mafrooms'],
        "IgnoreChannels": dataServerID[str(ctx.author.guild.id)]['IgnoreChannels'],
        "IgnoreRoles": dataServerID[str(ctx.author.guild.id)]['IgnoreRoles'],
        "card": dataServerID[str(ctx.author.guild.id)]['card'],
        "text_color": dataServerID[str(ctx.author.guild.id)]['text_color'],
        "bar_color": dataServerID[str(ctx.author.guild.id)]['bar_color'],
        "blend": dataServerID[str(ctx.author.guild.id)]['blend'],
        "USERS": dataServerID[str(ctx.author.guild.id)]['USERS']
    }
def bdint(ctx):
    with open('users.json', 'r') as file:
        dataServerID = json.load(file)
    return {
        "COLOR": int(dataServerID[str(ctx.guild_id)]['COLOR'], 16),
        "ErCOLOR": int(dataServerID[str(ctx.guild_id)]['ErCOLOR'], 16),
        "JoinRoles": dataServerID[str(ctx.guild_id)]['JoinRoles'],
        "ModRoles": dataServerID[str(ctx.guild_id)]['ModRoles'],
        "ROLES": dataServerID[str(ctx.guild_id)]['ROLES'],
        "actmoduls": dataServerID[str(ctx.guild_id)]['actmoduls'],
        "nCaps": dataServerID[str(ctx.guild_id)]['nCaps'],
        "nWarns": dataServerID[str(ctx.guild_id)]['nWarns'],
        "idAdminchennel": dataServerID[str(ctx.guild_id)]['idAdminchennel'],
        "idMainch": dataServerID[str(ctx.guild_id)]['idMainch'],
        "selfRoom": dataServerID[str(ctx.guild_id)]['selfRoom'],
        "BADWORDS": dataServerID[str(ctx.guild_id)]['BADWORDS'],
        "LINKS": dataServerID[str(ctx.guild_id)]['LINKS'],
        "PREFIX": dataServerID[str(ctx.guild_id)]['PREFIX'],
        "JNMSG": dataServerID[str(ctx.guild_id)]['JNMSG'],
        "SelfTitle": dataServerID[str(ctx.guild_id)]['SelfTitle'],
        "Selfrooms": dataServerID[str(ctx.guild_id)]['Selfrooms'],
        "Mafrooms": dataServerID[str(ctx.guild_id)]['Mafrooms'],
        "IgnoreChannels": dataServerID[str(ctx.guild_id)]['IgnoreChannels'],
        "IgnoreRoles": dataServerID[str(ctx.guild_id)]['IgnoreRoles'],
        "card": dataServerID[str(ctx.guild_id)]['card'],
        "text_color": dataServerID[str(ctx.guild_id)]['text_color'],
        "bar_color": dataServerID[str(ctx.guild_id)]['bar_color'],
        "blend": dataServerID[str(ctx.guild_id)]['blend'],
        "USERS": dataServerID[str(ctx.guild_id)]['USERS']
    }