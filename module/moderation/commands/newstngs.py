import discord
from discord.ext import commands
import json
from BTSET import BD, Lang, DEFGUILD, DEFMODROLE
import asyncio
from system.Bot import WaveBot

#все работает но в место даты надо подставить функцию из db_write
class NewStngs(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot

    command_name = "settings"

    def add_rem_role(self, ctx: commands.Context, functionName: str, roleId: str, roleClass: str, aset: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(roleId and roleClass):
            raise commands.MissingRequiredArgument("*{}* {}{} {} {}".format(Lang(ctx).language[f'settings_command_set_role_{functionName}_error_1'], self.bot.db_get_prefix(ctx)), NewStngs.command_name, functionName, Lang(ctx).language[f'settings_command_set_role_{functionName}_error_2'])
        if not(roleClass in data[str(ctx.author.guild.id)]['ROLES']):
            raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_role_{functionName}_not_ex_1'], roleClass, Lang(ctx).language[f'settings_command_set_role_{functionName}_not_ex_2']))
        if functionName == 'add_role':
            if len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26 and not(roleId in data[str(ctx.author.guild.id)]['ROLES'][roleClass]):
                data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].append(str(roleId))
                if aset:
                    data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(str(aset))
                else:
                    data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].append(' ')

            elif not(len([i for i in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]]) < 26):
                raise commands.BadArgument(Lang(ctx).language[f'settings_command_set_role_{functionName}_error_much'])
            else:
                raise commands.BadArgument("{} {} {}".format(Lang(ctx).language[f'settings_command_set_role_{functionName}_error_been_1'], roleId, Lang(ctx).language[f'settings_command_set_role_{functionName}_error_been_2']))
        else:
            if not(roleId in data[str(ctx.author.guild.id)]['ROLES'][roleClass][0]):
                raise commands.BadArgument("*{} {} {} {}!*".format(Lang(ctx).language[f'settings_command_set_role_{functionName}_error_not_ex_1'], roleId, Lang(ctx).language[f'settings_command_set_role_{functionName}_error_not_ex_2'], roleClass))
            data[str(ctx.author.guild.id)]['ROLES'][roleClass][1].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(roleId)))
            data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].pop(data[str(ctx.author.guild.id)]['ROLES'][roleClass][0].index(str(roleId)))
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return "*{} {} {} {}*".format(Lang(ctx).language[f'settings_command_set_role_{functionName}_1'], roleClass, Lang(ctx).language[f'settings_command_set_role_{functionName}_2'], roleId)

    def add_rem_class(self, ctx: commands.Context, functionName: str, className: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(className):
            raise commands.MissingRequiredArgument("*{} {}{} {} {}*".format(Lang(ctx).language[f'settings_command_set_class_{functionName}_error_1'], self.bot.db_get_prefix(ctx), NewStngs.command_name, functionName, Lang(ctx).language[f'settings_command_set_class_{functionName}_error_2']))
        ermes = "*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_class_{functionName}_not_ex_1'], className, Lang(ctx).language[f'settings_command_set_class_{functionName}_not_ex_2'])
        if functionName == 'add_class':
            if className in data[str(ctx.author.guild.id)]['ROLES']:
                raise commands.BadArgument(ermes)
            data[str(ctx.author.guild.id)]['ROLES'].update({className: [[],[]]})
        else:
            if not(className in data[str(ctx.author.guild.id)]['ROLES']):
                raise commands.BadArgument(ermes)
            data[str(ctx.author.guild.id)]['ROLES'].pop(className)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return "*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_class_{functionName}_1'], className, Lang(ctx).language[f'settings_command_set_class_{functionName}_2'])

    def set_color(self, ctx: commands.Context, functionName: str, color: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(color):
            raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_color_{functionName}_not_ex_1'], color, Lang(ctx).language[f'settings_command_set_color_{functionName}_not_ex_2']))
        if [i for i in [color[ii] for ii in range(len(color))] if not(i in '#0123456789abcdef' or i in '#0123456789abcdef'.upper())]:
            raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_color_{functionName}_not_ex_1'], color, Lang(ctx).language[f'settings_command_set_color_{functionName}_not_ex_2']))
        if [color[i] for i in range(len(color))][0] == '#':
            if len(color) != 7:
                raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_color_{functionName}_not_ex_1'], color, Lang(ctx).language[f'settings_command_set_color_{functionName}_not_ex_2']))

            data[str(ctx.author.guild.id)][functionName.upper()] ='0x' + str(''.join([color[i] for i in range(len(color))][1:]))
        else:
            if len(color) != 6:
                raise commands.BadArgument("*{}* {}{} {} {}".format(Lang(ctx).language[f'settings_command_set_color_{functionName}_error_1'], WaveBot.db_get_prefix(ctx), NewStngs.command_name, functionName, Lang(ctx).language[f'settings_command_set_color_{functionName}_error_2']))

            data[str(ctx.author.guild.id)][functionName.upper()] ='0x' + str(color)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return "*{} {}*".format(Lang(ctx).language[f'settings_command_set_color_{functionName}'], color)
    
    def text_set(self, ctx: commands.Context, functionName: str, ans: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(ans):
            raise commands.BadArgument("*{} {}{} {}*".format(Lang(ctx).language[f'settings_command_set_{functionName}_error_1'], self.bot.db_get_prefix(ctx), NewStngs.command_name, Lang(ctx).language[f'settings_command_set_{functionName}_error_2']))
        data[str(ctx.author.guild.id)][functionName.upper()] = str(ans)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return "*{} {}*".format(Lang(ctx).language[f'settings_command_set_{functionName}'], ans)
    
    def add_rem_badword(self, ctx: commands.Context, functionName: str, word: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(word):
            raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_badword_{ functionName}_error_1']} {WaveBot.db_get_prefix(ctx)}{NewStngs.command_name} { functionName} {Lang(ctx).language[f'settings_command_set_badword_{ functionName}_error_2']}*")
        if  functionName == 'add_badword':
            if word in data[str(ctx.author.guild.id)]['BADWORDS']:
                raise commands.BadArgument("*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{ functionName}_not_ex_1'], word, Lang(ctx).language[f'settings_command_set_badword_{ functionName}_not_ex_2']))
            data[str(ctx.author.guild.id)]['BADWORDS'].append(str(word))
        else:
            if not(word in data[str(ctx.author.guild.id)]['BADWORDS']):
                raise commands.BadArgument("*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{ functionName}_not_ex_1'], word, Lang(ctx).language[f'settings_command_set_badword_{ functionName}_not_ex_2']))
            data[str(ctx.author.guild.id)]['BADWORDS'].pop(data[str(ctx.author.guild.id)]['BADWORDS'].index(str(word)))
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return "*{} ||{}|| {}*".format(Lang(ctx).language[f'settings_command_set_badword_{ functionName}_1'], word, Lang(ctx).language[f'settings_command_set_badword_{ functionName}_2'])
    
    def add_rem_join_role(self, ctx: commands.Context, functionName: str, roleId: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(roleId):
            raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_join_roles_{functionName}_eroor_1']} {WaveBot.db_get_prefix(ctx)}{NewStngs.command_name} {functionName} {Lang(ctx).language[f'settings_command_set_join_roles_{functionName}_eroor_2']}")
        if functionName == 'add_join_role':
            if roleId in data[str(ctx.author.guild.id)]['JoinRoles']:
                raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_join_roles_{functionName}_ex_1']} {rl1} {Lang(ctx).language[f'settings_command_set_join_roles_{functionName}_ex_2']}")
            data[str(ctx.author.guild.id)]['JoinRoles'].append(str(roleId))
            rl1 = ctx.guild.get_role(int(roleId))
        else:
            if not(roleId in data[str(ctx.author.guild.id)]['JoinRoles']):
                raise commands.BadArgument(Lang(ctx).language[f'settings_command_set_join_roles_{functionName}not_ex_1'])
            data[str(ctx.author.guild.id)]['JoinRoles'].pop(data[str(ctx.author.guild.id)]['JoinRoles'].index(str(roleId)))
            rl1 = ctx.guild.get_role(int(roleId))
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return f"{Lang(ctx).language[f'settings_command_set_join_roles_{functionName}_1']} {rl1} {Lang(ctx).language[f'settings_command_set_join_roles_{functionName}_2']}"

    def add_rem_ignorechannel(self, ctx: commands.Context, functionName: str, channelId: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(channelId):
            raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_error_1']} {WaveBot.db_get_prefix(ctx)}{NewStngs.command_name} {functionName} {Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_error_2']}*")
        if functionName == 'add_ignorechannel':
            if channelId in data[str(ctx.author.guild.id)]['IgnoreChannels']:
                raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_ex_1']} {channelId} {Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_ex_2']}*")
            data[str(ctx.author.guild.id)]['IgnoreChannels'].update(channelId)
        else:
            if not(channelId in data[str(ctx.author.guild.id)]['IgnoreChannels']):
                raise commands.BadArgument(f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_not_ex_1']} {channelId} {Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_not_ex_2']}*")
            data[str(ctx.author.guild.id)]['IgnoreChannels'].pop(channelId)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return f"*{Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_1']} {channelId} {Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}_2']}*"
    
    def add_rem_ignoreRole(self, ctx: commands.Context, functionName: str, roleId: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(roleId):
            raise commands.BadArgument("*{} {}{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_1'], WaveBot.db_get_prefix(ctx), NewStngs.command_name, functionName, Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_2']))
        if functionName == 'add_IgnoreRole':
            if roleId in data[str(ctx.author.guild.id)]['IgnoreRoles']:
                raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_ex_1'], roleId, Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_ex_2']) )
            data[str(ctx.author.guild.id)]['IgnoreRoles'].update(roleId)
        else:
            if not(roleId in data[str(ctx.author.guild.id)]['IgnoreRoles']):
                raise commands.BadArgument("*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_not_ex_1'], roleId, Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_not_ex_2']) )
            data[str(ctx.author.guild.id)]['IgnoreRoles'].pop(roleId)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return "*{} {} {}*".format(Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_1'], roleId, Lang(ctx).language[f'settings_command_set_ignorerole_{functionName}_2'])

    def set_modrole(self, ctx: commands.Context, functionName: str, roleId: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(str(roleId) in [str(i.id) for i in ctx.author.guild.roles]):
            raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_modrole_{functionName}_error_1']} {str(roleId)} {Lang(ctx).language[f'settings_command_set_modrole_{functionName}_error_2']}")
        data[str(ctx.guild.id)]['ModRoles'].update({
            roleId: DEFMODROLE
        })
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return f"{Lang(ctx).language[f'settings_command_set_modrole_{functionName}_1']} {[i for i in ctx.author.guild.roles if str(i.id) == str(roleId)]} {Lang(ctx).language[f'settings_command_set_modrole_{functionName}_2']}"

    def set_mods(self, ctx: commands.Context, functionName: str, roleId: str, aset: str, boool: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(roleId):
            raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_modrole_{functionName}_error_1']} {roleId} {Lang(ctx).language[f'settings_command_set_modrole_{functionName}_error_2']}")
        if not str(aset) in [k for k in  data[str(ctx.author.guild.id)]['ModRoles'].keys()]:
            raise commands.BadArgument(Lang(ctx).language[f'settings_command_set_modrole_{functionName}_not_ex_1'])
        data[str(ctx.author.guild.id)]['ModRoles'][str(roleId)][str(aset)] = 'True' in boool
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return Lang(ctx).language[f'settings_command_set_modrole_{functionName}']
    
    async def set_join_message(self, ctx: commands.Context, functionName: str, messageId: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(messageId):
            raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_{functionName}_error_1']} {WaveBot.db_get_prefix(ctx)}{NewStngs.command_name} {functionName} {Lang(ctx).language[f'settings_command_set_{functionName}_error_2']}")
        msg: discord.Message = await ctx.channel.fetch_message(messageId)
        data[str(ctx.author.guild.id)]['JNMSG'] = str(msg.content)
        with open(f'{BD}users.json', 'w') as file:
            json.dump(data, file, indent=4)
        return f"{Lang(ctx).language[f'settings_command_set_{functionName}']} \n {msg.content}"
        
#тут дописать emb-ы

class NewStngsviewer(commands.Cog):
    def __init__(self, bot):
        self.bot: WaveBot = bot
    
    def view_join_roles(self, ctx: commands.Context):
        emb = discord.Embed(title="", description="Роли:", color="")
        for i in self.bot.db_get_joinroles(ctx):
            emb.add_field(name = f'{ctx.guild.get_role(int(i))}', value =f'{i}', inline=True)
        return emb
    
    def view_ignorechannels(self, ctx: commands.Context, functionName: str):
        emb = discord.Embed(title="", description=Lang(ctx).language[f'settings_command_set_ignorechannel_{functionName}'], color="")
        for i in self.bot.db_get_ignorechannels:
            emb.add_field(name=ctx.guild.get_channel(i), value=''.join(i), inline=True)
        return emb
    
    def view_ignoreroles(self, ctx: commands.Context, functionName: str):
        emb = discord.Embed(title="", description=Lang(ctx).language[f'settings_command_set_ignoreRole_{functionName}'], color="")
        for i in self.bot.db_get_ignoreroles:
            emb.add_field(name=ctx.guild.get_channel(i), value=''.join(i), inline=True)
        return emb
    
    def view_class(self, ctx: commands.Context, functionName: str, className: str):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        if not(className):
            raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_class_{functionName}_error_1']} {WaveBot.db_get_prefix(ctx)}{NewStngs.command_name} {functionName} {Lang(ctx).language[f'settings_command_set_class_{functionName}_error_2']}")
        if not(className in data[str(ctx.author.guild.id)]['ROLES']):
            raise commands.BadArgument(f"{Lang(ctx).language[f'settings_command_set_class_{functionName}_not_ex_1']} {className} {Lang(ctx).language[f'settings_command_set_class_{functionName}_not_ex_2']}")
        emb = discord.Embed(title="", description=Lang(ctx).language[f'settings_command_set_class_{functionName}'], color="")
        for i in self.bot.db_get_roles(ctx)[className]:
            emb.add_field(name = f'{ctx.guild.get_role(int(i))}', value =f'{i}', inline=True)
        return emb
    
    def view_classes(self, ctx: commands.Context, functionName: str):
        emb = discord.Embed(title="", description=Lang(ctx).language[f'settings_command_set_class_{functionName}'], color="")
        for i in self.bot.db_get_roles(ctx):
            emb.add_field(name = f'{str(i)}', value =''.join(self.bot.db_get_roles(ctx)[str(i)][0]), inline=True)
        return emb