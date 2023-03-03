import discord
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from typing import Optional
from discord import File
from BTSET import Score_presets, bdpy
from PIL import Image, ImageFont, ImageDraw
from system.Bot import WaveBot


class Rank(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def command_rank(self, ctx: commands.Context, member: discord.Member):
        xp = Score_presets(ctx.author).score
        lvl = Score_presets(ctx.author).lvl
        nlx = (lvl+1) * 100
        setcard = bdpy(ctx)['card']
        textColor = bdpy(ctx)['text_color']
        barColor = bdpy(ctx)['bar_color']
        blend = bdpy(ctx)['blend']

        percentage = int(((xp * 100)/ nlx))

        if percentage < 1:
            percentage = 0
        
        background = Editor(f"module/rate/img/{setcard}")
        profile = await load_image_async(str(member.avatar))

        profile = Editor(profile).resize((150, 150)).circle_image()
        
        FONT = ImageFont.truetype('system/Fonts/allFonts.otf', 50) #Font.caveat(size=60)
        FONT_small = ImageFont.truetype('system/Fonts/centurygothic.ttf', 50) #Font.caveat(size=50)

        
        if blend == 1:
            ima = Editor("module/rate/set/zBLACK.png")
            background.blend(image=ima, alpha=.5, on_top=False)

        background.paste(profile.image, (30, 30))

        background.rectangle((30, 220), width=650, height=40, fill="#fff", radius=20)
        background.bar(
            (30, 220),
            max_width=650,
            height=40,
            percentage=percentage,
            fill=barColor,
            radius=20,
        )
        background.text((200, 40), f'{member.name}#{member.discriminator}', font=FONT, color=textColor)

        background.rectangle((200, 100), width=350, height=2, fill=barColor)
        background.text(
            (200, 130),
            f"Level : {lvl}   "
            + f" XP : {xp} / {(lvl+1) * 100}",
            font=FONT_small,
            color=textColor,
        )

        card = File(fp=background.image_bytes, filename="module/rate/set/zCARD.png")
        await ctx.send(file=card)