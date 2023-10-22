import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot
from discord.utils import get
from system.db_.sqledit import SQLEditor

class SrInfo(commands.Cog):
    def __init__(self, bot: WaveBot, color):
        self.bot = bot
        self.color = color


    async def command_server_info(self, ctx: commands.Context):
        emb = discord.Embed(title='{} ***{}***'.format(Lang(ctx).language['server_info_title'], str(ctx.message.guild)),
                            description=Lang(ctx).language['server_info_des'],
                            color=self.color
                            )
        emb.set_thumbnail(url=ctx.author.guild.icon)
        emb.add_field(name=Lang(ctx).language['server_info_members'], value=ctx.message.guild.member_count)
        emb.add_field(name=Lang(ctx).language['server_info_own'], value=ctx.message.guild.owner)
        emb.add_field(name=Lang(ctx).language['server_info_date'], value=ctx.message.guild.created_at.strftime("%d.%m.%y"))
        await ctx.send(embed=emb)

    async def command_server_info_channel(self, ctx: commands.Context, arg: str):
        command_name = "server_info_channel"

        if arg == 'on':
            print(SQLEditor.get_info_channels())
            if not SQLEditor.get_info_channels():
                roomNames=[f'{Lang(ctx).language["server_info_channel_members_1"]} {len(ctx.guild.members)}{Lang(ctx).language["server_info_channel_members_2"]}', f'{Lang(ctx).language["server_info_channel_bots_1"]} {len([i for i in ctx.guild.members if i.bot])}{Lang(ctx).language["server_info_channel_bots_2"]}', f'{Lang(ctx).language["server_info_channel_humans_1"]} {len(ctx.guild.members) - len([i for i in ctx.guild.members if i.bot])}{Lang(ctx).language["server_info_channel_humans_2"]}']
                ct = await ctx.guild.create_category(name='📊Info📊', position=0)
                first_channel = await ctx.guild.create_voice_channel(name=roomNames[0], category=ct)
                second_channel = await ctx.guild.create_voice_channel(name=roomNames[1], category=ct)
                third_channel = await ctx.guild.create_voice_channel(name=roomNames[2], category=ct)
                pr = discord.PermissionOverwrite()
                pr.connect = False
                [await chlen.set_permissions(target=ctx.guild.roles[0], overwrite=pr) for chlen in ct.channels]
                SQLEditor.add_info_channels(ch1=first_channel.id, ch2=second_channel.id, ch3=third_channel.id, ct=ct.id)
        elif arg == 'off':
            channelsid = SQLEditor.remove_info_channels()
            print(channelsid)
            if channelsid:
                [await i.delete() for i in ctx.guild.voice_channels if i.id in channelsid]
                [await i.delete() for i in ctx.guild.categories if i.id in channelsid]
        else:
            raise commands.BadArgument(f"{Lang(ctx).language['server_info_channel_er']} {self.bot.read_sql(db='servers', guild=str(ctx.guild.id), key='PREFIX')}{command_name} on/off")

class SrInfo_listeners(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot: WaveBot = bot

    async def listener_srinf_join(self, member: discord.Member):
        channelsid = SQLEditor.get_info_channels()
        roomNames=[f'{Lang(member).language["server_info_channel_members_1"]} {len(member.guild.members)}{Lang(member).language["server_info_channel_members_2"]}', f'{Lang(member).language["server_info_channel_bots_1"]} {len([i for i in member.guild.members if i.bot])}{Lang(member).language["server_info_channel_bots_2"]}', f'{Lang(member).language["server_info_channel_humans_1"]} {len(member.guild.members) - len([i for i in member.guild.members if i.bot])}{Lang(member).language["server_info_channel_humans_2"]}']
        channels = [i for i in member.guild.voice_channels if str(i.id) in channelsid][1:]
        [await i.edit(name=roomNames) for i in channels]

    async def listener_srinf_remove(self, member: discord.Member):
        channelsid = SQLEditor.get_info_channels()
        roomNames=[f'{Lang(member).language["server_info_channel_members_1"]} {len(member.guild.members)}{Lang(member).language["server_info_channel_members_2"]}', f'{Lang(member).language["server_info_channel_bots_1"]} {len([i for i in member.guild.members if i.bot])}{Lang(member).language["server_info_channel_bots_2"]}', f'{Lang(member).language["server_info_channel_humans_1"]} {len(member.guild.members) - len([i for i in member.guild.members if i.bot])}{Lang(member).language["server_info_channel_humans_2"]}']
        channels = [i for i in member.guild.voice_channels if str(i.id) in channelsid][1:]
        [await i.edit(name=roomNames) for i in channels]