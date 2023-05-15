import discord
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from typing import Optional
from discord import File
from BTSET import Score_presets, bdpy, Lang
from PIL import Image, ImageFont, ImageDraw
from system.Bot import WaveBot


class Rank(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    def levelFunction(x):
        d = (3**2+4*2*x/100)**0.5
        if (-3-d)/2 > (-3+d)/2:
            level = (-3-d)/2
        else:
            level = (-3+d)/2
        return level + 1

    def xpFunction(x):
        xp: float = 50*(x**2+x-2)
        return round(xp, 2)

    async def command_rank(self, ctx: commands.Context, member: discord.Member):
        lvl = int(Rank.levelFunction(self.bot.read_sql(db=f"server{ctx.guild.id}", guild=str(member.id), key="XP")))
        xp = int(self.bot.read_sql(db=f"server{ctx.guild.id}", guild=str(member.id), key="XP")- Rank.xpFunction(lvl))
        nlx = (lvl+1) * 100
        setcard = self.bot.read_sql(db=f"servers", guild=str(ctx.guild.id), key="CARD")
        textColor = self.bot.read_sql(db=f"servers", guild=str(ctx.guild.id), key="TEXTCOLOR")
        barColor = self.bot.read_sql(db=f"servers", guild=str(ctx.guild.id), key="BARCOLOR")
        blend = self.bot.read_sql(db=f"servers", guild=str(ctx.guild.id), key="BLEND")

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
            f"{Lang(ctx).language['rank_command_rank_level']} : {lvl}   "
            + f" {Lang(ctx).language['rank_command_rank_xp']} : {xp} / {(lvl+1) * 100}",
            font=FONT_small,
            color=textColor,
        )

        card = File(fp=background.image_bytes, filename="module/rate/set/zCARD.png")
        await ctx.send(file=card)