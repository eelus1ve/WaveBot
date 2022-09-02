import discord
from operator import index
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, Select
from discord_components import SelectOption as Sel
from discord.utils import get
from email.errors import InvalidMultipartContentTransferEncodingDefect
import asyncio
import json
from discord_components import ComponentsBot
import interactions
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption, Option
from youtube_dl import YoutubeDL
import os


client = interactions.Client('OTgxNTExNjgyOTYwNTQ3ODYw.GpV6bM.XIGASOaT6YPnhU2Q0sAPOqRwBrFfWzcRsvkv6E')
bot: ComponentsBot = ComponentsBot(command_prefix='~')

YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
                'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'}

@client.event
async def on_ready():
   # await btst1.stp(bot, client)

    if not os.path.exists('music.json'):
        with open('music.json', 'w') as file:
            file.write('{}')
    else:
        with open('music.json', 'r') as file:
            if not file.read():
                with open('music.json', 'w') as file:
                    file.write('{}')


async def player_edit(gld: discord.Guild, chlen: discord.TextChannel):
    try:
        with open('music.json', 'r') as file:
            data: dict = json.load(file)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in data[str(gld.id)]['songs'][0]:
                info = ydl.extract_info(data[str(gld.id)]['songs'][0], download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{data[str(gld.id)]['songs'][0]}", download=False)['entries'][0]

            player: discord.Message = await chlen.fetch_message(data[str(gld.id)]['pl_id'])

            embd = discord.Embed(
                title='***                               wave player***',
                description=f'=================================',
                colour=0x00FFFF
            )
            embd.add_field(name='сейчас играет:', value=f'{info.get("title", None)}')

            await player.edit(embed=embd)
    except IndexError:
        player: discord.Message = await chlen.fetch_message(data[str(gld.id)]['pl_id'])
        embd = discord.Embed(
            title='***                               wave player***',
            description=f'=================================',
            colour=0x00FFFF
        )
        embd.add_field(name='сейчас играет:', value='ничего')

        await player.edit(embed=embd)





def after_song(gld: discord.Guild, vc, chlen: discord.TextChannel):
    try:
        print(vc.is_playing(), 'это в афтер сонг ')
        with open('music.json', 'r') as file:
            data: dict = json.load(file)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            if 'https://' in data[str(gld.id)]['songs'][0]:
                info = ydl.extract_info(data[str(gld.id)]['songs'][0], download=False)
            else:
                info = ydl.extract_info(f"ytsearch:{data[str(gld.id)]['songs'][0]}", download=False)['entries'][0]

        url = info['formats'][0]['url']
        data[str(gld.id)]['songs'].pop(0)
        with open('music.json', 'w') as file:
            json.dump(data, file, indent=4)

        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source=url, **FFMPEG_OPTIONS), after=lambda e: after_song(gld, vc, chlen))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.3

    except:
        pass


@bot.command()
async def play(ctx):
    with open('music.json', 'r') as file:
        data: dict = json.load(file)
    await ctx.message.author.voice.channel.connect()

    ''' with YoutubeDL(YDL_OPTIONS) as ydl:
        if 'https://' in data[str(ctx.guild.id)]['songs'][0]:
            info = ydl.extract_info(data[str(ctx.guild.id)]['songs'][0], download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{data[str(ctx.guild.id)]['songs'][0]}", download=False)['entries'][0]

    url = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source=url, **FFMPEG_OPTIONS), after=lambda e: after_song(ctx.guild, vc))
    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 0.5'''


@client.command(
    name='music',
    description='.......',
    options=[Option(
            name="msc",
            description="......",
            type=3,
            required=True
    )])
async def add_msc(ctx: interactions.CommandContext, msc: str):

    with open('music.json', 'r') as file:
        data: dict = json.load(file)
        if not(ctx.guild_id in data):
            data.update(
                {
                    int(ctx.guild_id): {
                        'songs': [msc],
                        'pl_id': None
                    }
                }
            )
        else:
            data[ctx.guild_id]['songs'].append(msc)


    with open('music.json', 'w') as file:
        json.dump(data, file, indent=4)

    await ctx.send('успешно', ephemeral=True)

@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    with open('music.json', 'r') as file:
        data: dict = json.load(file)

    channelid = payload.channel_id
    user = payload.member
    messageid = payload.message_id
    channel = bot.get_channel(channelid)
    message = await channel.fetch_message(messageid)
    emo = payload.emoji
    vc: discord.VoiceClient = get(bot.voice_clients, guild=bot.get_guild(payload.guild_id))

    if messageid == data[str(payload.guild_id)]['pl_id']:
        for reaction in message.reactions:
            if reaction.emoji == emo.name:
                await reaction.remove(user)
                if str(reaction.emoji) == '➡' and vc.is_playing():
                    vc.stop()
                    await player_edit(bot.get_guild(payload.guild_id), channel)
                    after_song(bot.get_guild(payload.guild_id), vc, channel)

                elif str(reaction.emoji) == '▶':
                    if not vc.is_playing() and not vc.is_paused():
                        await player_edit(bot.get_guild(payload.guild_id), channel)
                        after_song(bot.get_guild(payload.guild_id), vc, channel)
                    elif vc.is_paused():
                        vc.resume()

                elif str(reaction.emoji) == '⏸' and not vc.is_paused():
                    vc.pause()

                elif str(reaction.emoji) == '⏹' and vc.is_playing():
                    vc.stop()






loop = asyncio.get_event_loop()

task2 = loop.create_task(bot.start("OTgxNTExNjgyOTYwNTQ3ODYw.GpV6bM.XIGASOaT6YPnhU2Q0sAPOqRwBrFfWzcRsvkv6E"))
task1 = loop.create_task(client._ready())

gathered = asyncio.gather(task1, task2, loop=loop)
loop.run_until_complete(gathered)