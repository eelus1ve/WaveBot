import discord #                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ИНВАЛИДА НАХУЙ УСЫПИТЬ
import discord_components
from discord.utils import get
from email.errors import InvalidMultipartContentTransferEncodingDefect
import asyncio
import json
import StringProgressBar
import interactions
from interactions import TextInput, Modal, TextStyleType, SelectMenu, SelectOption, Option
from youtube_dl import YoutubeDL
import time
from discord.ext import commands



YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'quiet': True,
                'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'}


class Add_music(interactions.Extension):
    def __init__(self, client):
        self.client = client

    @interactions.extension_command(
        name='music',
        description='.......',
        options=[Option(
            name="msc",
            description="......",
            type=3,
            required=True
        )])
    async def add_msc(self, ctx: interactions.CommandContext, msc: str):

        with open('music.json', 'r') as file:
            data: dict = json.load(file)
            if not (ctx.guild_id in data):
                data.update(
                    {
                        int(ctx.guild_id): {
                            'songs': [msc],
                            'pl_id': None,
                            'chl_id': None
                        }
                    }
                )
            else:
                data[ctx.guild_id]['songs'].append(msc)

        with open('music.json', 'w') as file:
            json.dump(data, file, indent=4)

        await ctx.send('успешно', ephemeral=True)

class Player_edit():
    def __init__(self, bot):
        self.bot = bot
    async def player_edit(self, gld: discord.Guild, chlen: discord.TextChannel):#==================================================================================================================    plaer edit
        try:
            start_time = time.time()
            with open('music.json', 'r') as file:
                data: dict = json.load(file)
            with YoutubeDL(YDL_OPTIONS) as ydl:
                if 'https://' in data[str(gld.id)]['songs'][0]:
                    main_info = ydl.extract_info(data[str(gld.id)]['songs'][0], download=False)
                else:
                    main_info = ydl.extract_info(f"ytsearch:{data[str(gld.id)]['songs'][0]}", download=False)['entries'][0]
                if 'https://' in data[str(gld.id)]['songs'][1]:
                    next_info = ydl.extract_info(data[str(gld.id)]['songs'][1], download=False)
                else:
                    next_info = ydl.extract_info(f"ytsearch:{data[str(gld.id)]['songs'][1]}", download=False)['entries'][0]

                url = main_info['formats'][0]['url']
                urll = url.split('&')
                for i in urll:
                    if i.startswith('dur='):
                        i = i.split('=')
                        song_time = i[1]

                player = await chlen.fetch_message(data[str(gld.id)]['pl_id'])

                song_list = []
                for i in data[str(gld.id)]['songs']:
                    if i != data[str(gld.id)]['songs'][0]:
                        with YoutubeDL(YDL_OPTIONS) as ydl:
                            if 'https://' in i:
                                info = ydl.extract_info(i, download=False)
                            else:
                                info = ydl.extract_info(f"ytsearch:{i}", download=False)['entries'][0]
                            url = info['formats'][0]['url']
                        song_list.append(f'{info.get("title", None)} \n')

                song_time = float(song_time)

                song_time = float(song_time)
                while song_time - (time.time() - start_time):
                    await asyncio.sleep(2)
                    embd = discord.Embed(
                        title='***                               wave player***',
                        description=f'=================================',
                        colour=0x36393f
                    )
                    embd.add_field(name='сейчас играет:',
                                   value=f'{main_info.get("title", None)} \n {int(float(song_time) / 60)}:{int((float(song_time) / 60 - int(float(song_time) / 60)) * 60)}')

                    embd.add_field(name='потом', value=f'{next_info.get("title", None)}' + ''.join(song_list), inline=False)
                    embd.add_field(name='.', value=f'{StringProgressBar.progressBar.splitBar(int(song_time*100), int((time.time() - start_time)*100), size=25)[0]}', inline=False)

                    await player.edit(embed=embd)

        except IndexError:
            player = await chlen.fetch_message(data[str(gld.id)]['pl_id'])
            embd = discord.Embed(
                title='***                               wave player***',
                description=f'=================================',
                colour=0x00FFFF
            )
            embd.add_field(name='сейчас играет:', value='ничего')

            await player.edit(embed=embd)


class Auto_resume():
    def __init__(self, bot):
        self.bot = bot


    async def after_song(self, vc: discord.VoiceClient):#==================================================================================================================    after song
        try:
            print(vc.is_playing(), 'это в афтер сонг ')
            with open('music.json', 'r') as file:
                data: dict = json.load(file)
            gld: discord.Guild = vc.guild
            chlen = self.bot.get_channel(data[str(gld.id)]['chl_id'])
            with YoutubeDL(YDL_OPTIONS) as ydl:
                if 'https://' in data[str(gld.id)]['songs'][0]:
                    info = ydl.extract_info(data[str(gld.id)]['songs'][0], download=False)
                else:
                    info = ydl.extract_info(f"ytsearch:{data[str(gld.id)]['songs'][0]}", download=False)['entries'][0]

            async def new_song(gld):
                await asyncio.sleep(10)
                pop = data[str(gld.id)]['songs'].pop(0)
                data[str(gld.id)]['songs'].append(pop)
                with open('music.json', 'w') as file:
                    json.dump(data, file, indent=4)

            url = info['formats'][0]['url']
            urll = url.split('&')
            for i in urll:
                if i.startswith('dur='):
                    i = i.split('=')
                    song_time = i[1]
            with open('music.json', 'w') as file:
                json.dump(data, file, indent=4)

            vc.play(discord.FFmpegPCMAudio(executable="module/voice/ffmpeg/bin/ffmpeg.exe", source=url, **FFMPEG_OPTIONS))
            vc.source = discord.PCMVolumeTransformer(vc.source)


            async def timer_for_song():
                await asyncio.sleep(float(song_time))
                player_writer.cancel()
                await Auto_resume(bot=self.bot).after_song(vc)

            player_writer = asyncio.create_task(Player_edit(self.bot).player_edit(gld, chlen))
            timer = asyncio.create_task(timer_for_song())
            new_song_write = asyncio.create_task(new_song(gld))

            @commands.Cog.listener('on_button_click')
            async def iion_button_click(interaction: discord_components.Interaction):

                emo = interaction.component.emoji
                vc: discord.VoiceClient = get(self.bot.voice_clients, guild=self.bot.get_guild(interaction.guild_id))

                if str(emo) == '▶' and vc.is_playing():
                    timer.cancel()
                    new_song_write.cancel()
                    player_writer.cancel()

                elif str(emo) == '◀' and vc.is_playing():
                    timer.cancel()
                    new_song_write.cancel()
                    player_writer.cancel()

        except InvalidMultipartContentTransferEncodingDefect:
            pass


    async def befor_song(self, vc: discord.VoiceClient):#==================================================================================================================    befor song
        try:
            print(vc.is_playing(), 'это в бефор сонг ')
            with open('music.json', 'r') as file:
                data: dict = json.load(file)

            gld: discord.Guild = vc.guild
            chlen = self.bot.get_channel(data[str(gld.id)]['chl_id'])

            sng = data[str(gld.id)]['songs'].pop(-1)
            data[str(gld.id)]['songs'].insert(0, sng)
            with open('music.json', 'w') as file:
                json.dump(data, file, indent=4)

            with YoutubeDL(YDL_OPTIONS) as ydl:
                if 'https://' in data[str(gld.id)]['songs'][0]:
                    info = ydl.extract_info(data[str(gld.id)]['songs'][0], download=False)
                else:
                    info = ydl.extract_info(f"ytsearch:{data[str(gld.id)]['songs'][0]}", download=False)['entries'][0]

            async def new_song(gld):
                await asyncio.sleep(10)
                pop = data[str(gld.id)]['songs'].pop(0)
                data[str(gld.id)]['songs'].append(pop)
                with open('music.json', 'w') as file:
                    json.dump(data, file, indent=4)

            url = info['formats'][0]['url']
            urll = url.split('&')
            for i in urll:
                if i.startswith('dur='):
                    i = i.split('=')
                    song_time = i[1]
            with open('music.json', 'w') as file:
                json.dump(data, file, indent=4)

            vc.play(discord.FFmpegPCMAudio(executable="module/voice/ffmpeg/bin/ffmpeg.exe", source=url, **FFMPEG_OPTIONS))
            vc.source = discord.PCMVolumeTransformer(vc.source)

            async def timer_for_song():
                await asyncio.sleep(float(song_time) + 2)
                await Auto_resume(bot=self.bot).after_song(vc)

            timer = asyncio.create_task(timer_for_song())
            player_writer = asyncio.create_task(Player_edit(self.bot).player_edit(gld, chlen))
            new_song_write = asyncio.create_task(new_song(gld))

            @commands.Cog.listener('on_button_click')
            async def iion_button_click(interaction: discord_components.Interaction):

                emo = interaction.component.emoji
                vc: discord.VoiceClient = get(self.bot.voice_clients, guild=self.bot.get_guild(interaction.guild_id))

                if str(emo) == '▶' and vc.is_playing():
                    timer.cancel()
                    new_song_write.cancel()
                    player_writer.cancel()

                elif str(emo) == '◀' and vc.is_playing():
                    timer.cancel()
                    new_song_write.cancel()
                    player_writer.cancel()

        except InvalidMultipartContentTransferEncodingDefect:
            pass


class Button_start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()#==================================================================================================================    play
    async def play(self, ctx):
        await ctx.message.author.voice.channel.connect()

    @commands.Cog.listener('on_button_click')#==================================================================================================================    button
    async def _click(self, interaction: discord_components.Interaction):
        with open('music.json', 'r') as file:
            data: dict = json.load(file)

        try:
            user = interaction.author
            messageid = data[str(interaction.guild.id)]['pl_id']
            channel: discord.TextChannel = interaction.channel
            message = await channel.fetch_message(messageid)
            emo = interaction.component.emoji
            vc: discord.VoiceClient = get(self.bot.voice_clients, guild=self.bot.get_guild(interaction.guild_id))

            if str(emo) == '▶' and vc.is_playing():
                vc.stop()
                await Auto_resume(bot=self.bot).after_song(vc)

            elif str(emo) == '⏯':
                if not vc.is_playing() and not vc.is_paused():
                    await Auto_resume(bot=self.bot).after_song(vc)
                elif vc.is_paused():
                    vc.resume()
                elif vc.is_playing() and not vc.is_paused():
                    vc.pause()

            elif str(emo) == '⏹' and vc.is_playing():
                vc.stop()

            elif str(emo) == '🔊' and vc.is_playing():
                vc.source.volume = float(vc.source._volume) + 0.2


            elif str(emo) == '🔈' and vc.is_playing():
                vc.source.volume = float(vc.source._volume) - 0.2

            elif str(emo) == '🔇' and vc.is_playing():
                if vc.source._volume != 0:
                    vc.source.volume = 0
                else:
                    vc.source.volume = 0.3

            elif str(emo) == '◀' and vc.is_playing():
                vc.stop()
                await Auto_resume.befor_song(vc)
        except AttributeError:
            pass


def setup(bot):
    if str(bot).startswith('<d'):
        bot.add_cog(Button_start(bot))
    elif str(bot).startswith('<i'):
        Add_music(bot)