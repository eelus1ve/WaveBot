from multiprocessing.resource_sharer import stop #гит игнор чекнуть че не так
import discord
from discord import Spotify, File
from typing import Optional
from discord.ext import commands
import pytz
import requests
import dateutil.parser
from PIL import Image, ImageFont, ImageDraw
from BTSET import embpy, bdpy

class Sptfpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['spotinf'])
    async def spotify_info(self, ctx: commands.Context, user: Optional[discord.Member]):
        COLOR = bdpy(ctx)['COLOR']
        userr = user or ctx.author
        spotifyActivity = next((activity for activity in userr.activities if isinstance(activity, discord.Spotify)), None)
        if spotifyActivity is None:
            if str(userr.status) ==  'offline':
                await ctx.send(f"{userr.mention} офлайн!")
            else:
                await embpy(ctx, comp='e', des=f'Пользователь {userr.name} сейчас не слушает спотифай!', time=10.00)
        else:
            embed = discord.Embed(
                title=f"{userr.name}'s Spotify",
                description=f"Слушает [{spotifyActivity.title}](https://open.spotify.com/track/{spotifyActivity.track_id})",
                clr=COLOR
            )
            embed.set_thumbnail(url=spotifyActivity.album_cover_url)
            embed.add_field(name="Исполнитель", value=spotifyActivity.artist)
            embed.add_field(name="Альбом", value=spotifyActivity.album)
            embed.set_footer(text=f"Песня началась в {spotifyActivity.created_at.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%H:%M')}")
            await ctx.send(embed=embed)


    @commands.command(aliases=['sptf'])
    async def spotify(self, ctx, user: discord.Member = None):
        userr = user or ctx.author
        spotifyActivity = next((activity for activity in userr.activities if isinstance(activity, Spotify)), None)

        if spotifyActivity is None:
            if str(userr.status) ==  'offline':
                await ctx.send(f"{userr.mention} офлайн!")
            else:
                await ctx.send(embed=embpy(ctx, comp='s', des=f'Пользователь {userr.name} сейчас не слушает спотифай!'))
        else:
            background_img = Image.open('.\\module\\info\\img\\spotify_template1.png')
            albImage = Image.open(requests.get(spotifyActivity.album_cover_url, stream=True).raw).convert('RGBA')
            clr = 'white'
            albColor = albImage.getpixel((70, 80))#((250, 100))

            titleFont = ImageFont.truetype('system/Fonts/allFonts.otf', 16)
            artistFont = ImageFont.truetype('system/Fonts/allFonts.otf', 14)
            startFont = ImageFont.truetype('system/Fonts/allFonts.otf', 12)
            
            albFont = artistFont
            endFont = startFont
            if len([i for i in albColor if int(i) >= 150]) == 4:
                background_img_dark = Image.open('.\\module\\info\\img\\spotify_template2.png')
                background_img.paste(background_img_dark)
                clr = 'black'

            draw = ImageDraw.Draw(background_img)
        
            tps =140 + 430/2-(len(str(spotifyActivity.title))/2)*9.5
            title_pos = tps, 30
            draw.text(title_pos, spotifyActivity.title, clr, font=titleFont)
            
            aps =140 + 430/2-(len(str(spotifyActivity.artist))/2)*8.5 - 3*3
            artist_pos = aps, 60
            draw.text(artist_pos, f'by {spotifyActivity.artist}', clr, font=artistFont)
            
            alps =140 + 430/2-(len(str(spotifyActivity.album))/2)*9
            album_pos = alps, 80
            draw.text(album_pos, spotifyActivity.album, clr, font=albFont)

            start_position = 150, 122
            draw.text(start_position, '0:00', clr, font=startFont)

            end_pos = 515, 122
            draw.text(end_pos, f"{dateutil.parser.parse(str(spotifyActivity.duration)).strftime('%M:%S')}", clr, font=endFont)
            

            background_image_color = Image.new('RGBA', background_img.size, albColor)
            background_image_color.paste(background_img, (0, 0), background_img)
            albImgResize = albImage.resize((140, 160))
            background_image_color.paste(albImgResize, (0, 0), albImgResize)
            background_image_color.convert('RGB').save('module/info/img/spotify.jpg', 'JPEG')

            await ctx.send(file=File('module/info/img/spotify.jpg'))

def setup(bot):
    bot.add_cog(Sptfpy(bot))


