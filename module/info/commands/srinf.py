import discord
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class SrInfo(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot: WaveBot = bot

    async def command_server_info(self, ctx: commands.Context):
        emb = discord.Embed(title='{} ***{}***'.format(Lang(ctx).language['server_info_title'], str(ctx.message.guild)),
                            description=Lang(ctx).language['server_info_des'],
                            color=self.bot.read_sql(db="servers", guild=str(ctx.guild.id), key="INFOCOLOR")
                            )
        emb.set_thumbnail(url=ctx.author.guild.icon)
        emb.add_field(name=Lang(ctx).language['server_info_members'], value=ctx.message.guild.member_count)
        emb.add_field(name=Lang(ctx).language['server_info_own'], value=ctx.message.guild.owner)
        emb.add_field(name=Lang(ctx).language['server_info_date'], value=ctx.message.guild.created_at.strftime("%d.%m.%y"))
        await ctx.send(embed=emb)

    #Доделать. Знаю что доделать делаю делаю и думаю о том что ты пидр ведь мог бы и сам сделать а ты что-то другое делаешь а мне ещё документацию писать я тут сдохну 
    async def command_server_info_channel(self, ctx: commands.Context, arg: str):
        if arg == 'on':
            if not('📊Info📊' in [i.name for i in ctx.guild.categories]):
                ct = await ctx.guild.create_category(name='📊Info📊', position=0)
                await ctx.guild.create_voice_channel(name=f'👥Members: {len(ctx.guild.members)}👥', category=ct)
                await ctx.guild.create_voice_channel(name=f'🤖Bots: {len([i for i in ctx.guild.members if i.bot])}🤖', category=ct)
                await ctx.guild.create_voice_channel(name=f'👤Humans: {len(ctx.guild.members) - len([i for i in ctx.guild.members if i.bot])}👤', category=ct)
                pr = discord.PermissionOverwrite()
                pr.connect = False
                [await chlen.set_permissions(target=ctx.guild.roles[0], overwrite=pr) for chlen in ct.channels]
        else:
            if '📊Info📊' in [i.name for i in ctx.guild.categories]:
                [await i.delete() for i in [ii.channels for ii in ctx.guild.categories if ii.name == '📊Info📊'][0]]
                [await ii.delete() for ii in ctx.guild.categories if ii.name == '📊Info📊']


class SrInfo_listeners(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def listener_srinf_join(self, member: discord.Member):
        roomNames=[f'👥Members: {len(member.guild.members)}👥', f'🤖Bots: {len([i for i in member.guild.members if i.bot])}🤖', f'👤Humans: {len(member.guild.members) - len([i for i in member.guild.members if i.bot])}👤']
        if '📊Info📊' in [i.name for i in member.guild.categories]:
                [await i.edit(name=roomNames.pop(0)) for i in [ii.channels for ii in member.guild.categories if ii.name == '📊Info📊'][0]]

    async def listener_srinf_remove(self, member: discord.Member):
        roomNames=[f'👥Members: {len(member.guild.members)}👥', f'🤖Bots: {len([i for i in member.guild.members if i.bot])}🤖', f'👤Humans: {len(member.guild.members) - len([i for i in member.guild.members if i.bot])}👤']
        if '📊Info📊' in [i.name for i in member.guild.categories]:
                [await i.edit(name=roomNames.pop(0)) for i in [ii.channels for ii in member.guild.categories if ii.name == '📊Info📊'][0]]