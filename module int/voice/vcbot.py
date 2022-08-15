import discord
from discord.utils import get
import json
from youtube_dl import YoutubeDL
from discord.ext import commands
import interactions
from BD import bdint
class Voicbotint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="join",
        description="Присоединить бота",
    )
    async def join(self, ctx, chlen = None):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        
        global voice
        try:
            channel = ctx.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
                await ctx.send(embeds=interactions.Embed(
                    title='Успешно',
                    description=f'Бот успешно прискоединен в {channel.name}',
                    color=COLOR
                ))
        except:
            await ctx.send(embeds=interactions.Embed(
                title="Ошибка",
                description=f"*{ctx.author.mention} Вы не в голосовом канале !*",
                color=ErCOLOR
            ))

    @interactions.extension_command(
        name="leave",
        description="Отключить бота",
    )
    async def leave(self, ctx):
        COLOR = bdint(ctx)['COLOR']
        try:
            channel = ctx.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)

            await voice.disconnect()
            await ctx.send(embeds=interactions.Embed(
                    title="Успешно",
                    description="Бот покинул этот канал \n\
                        ||Бот это запомнит||",
                    color=COLOR
                ))
        except:
            pass


    @interactions.extension_command(
        name="play",
        description="начать проигрывать песню",
    )
    async def play(self, ctx, url):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        vc = get(self.bot.voice_clients, guild=ctx.guild)
        if not(vc.is_playing()) and not(vc.is_paused()):

            YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
                        'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                            'options': '-vn'}

            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)

            url = info['formats'][0]['url']

            vc.play(discord.FFmpegPCMAudio(executable="D:/Windows/Рабочий стол/wave1/ffmpeg/bin/ffmpeg.exe", source=url, **FFMPEG_OPTIONS))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 0.1

            await ctx.send(embeds=interactions.Embed(
                    title="Успешно",
                    description=f"Трек запущен!",
                    color=COLOR
                ))

        else:
            await ctx.send(embeds=interactions.Embed(
                    title="Ошибка",
                    description="Трек уже играет!",
                    color=ErCOLOR
                ))
    
    @interactions.extension_command(
        name="start",
        description="Продолжить проигрывание",
    )
    async def start(self, ctx):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        vc = get(self.bot.voice_clients, guild=ctx.guild)
        if not(vc.is_playing()):
            vc.resume()
            await ctx.send(embeds=interactions.Embed(
                    title="Успешно",
                    description="Трек успешно продолжается",
                    color=COLOR
                ))
        else:
            await ctx.send(embeds=interactions.Embed(
                    title="Ошибка",
                    description="Трек уже играет!",
                    color=ErCOLOR
                ))
    
    @interactions.extension_command(
        name="pause",
        description="Приостановить проигрываение",
    )
    async def pause(self, ctx):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        vc = get(self.bot.voice_clients, guild=ctx.guild)
        if vc.is_playing():
            vc.pause()
            await ctx.message.reply(embeds=interactions.Embed(
                    title="Успешно",
                    description="Трек успешно поставлен на паузу",
                    color=COLOR
                ))
        else:
            await ctx.message.reply(embeds=interactions.Embed(
                    title="Ошибка",
                    description="Трек не играет!",
                    color=ErCOLOR
                ))

    @interactions.extension_command(
        name="stop",
        description="",      #Степ эт че такое тип скип или тип стоп
    )
    async def stop(self, ctx):
        COLOR = bdint(ctx)['COLOR']
        ErCOLOR = bdint(ctx)['ErCOLOR']
        vc = get(self.bot.voice_clients, guild=ctx.guild)
        if vc.is_playing():
            vc.stop()
            await ctx.message.reply(embeds=interactions.Embed(
                    title="Успешно",
                    description="Трек успешно скипнут",
                    color=COLOR
                ))
        else:
            await ctx.message.reply(embeds=interactions.Embed(
                    title="Ошибка",
                    description="Трек не играет!",
                    color=ErCOLOR
                ))

def setup(client):
    Voicbotint(client)