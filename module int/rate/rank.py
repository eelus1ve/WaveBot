import discord
import json
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from typing import Optional
from discord import File
import interactions
from BD import bdint
class Rankint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="rank",
        description="Показаь ваш текущий ранк",
    )
    async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
        userr = user or ctx.author
        xp = bdint(ctx)['USERS'][str(userr.id)]["SCR"]
        lvl = bdint(ctx)['USERS'][str(userr.id)]["LvL"]
        nlx = (lvl+1) * 100
        setcard = bdint(ctx)['card']
        textColor = bdint(ctx)['text_color']
        barColor = bdint(ctx)['bar_color']
        blend = bdint(ctx)['blend']

        percentage = int(((xp * 100)/ nlx))

        if percentage < 1:
            percentage = 0
        
        background = Editor(f"D:/Windows/Рабочий стол/wave1/module/rate/img/{setcard}")
    
        profile = await load_image_async(str(userr.avatar_url))

        profile = Editor(profile).resize((150, 150)).circle_image()
        
        FONT = Font.caveat(size=60)
        FONT_small = Font.caveat(size=50)

        
        if blend == 1:
            ima = Editor("D:/Windows/Рабочий стол/wave1/module/rate/set/zBLACK.png")
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
        background.text((200, 40), str(userr.name), font=FONT, color=textColor)

        background.rectangle((200, 100), width=350, height=2, fill=barColor)
        background.text(
            (200, 130),
            f"Level : {lvl}   "
            + f" XP : {xp} / {(lvl+1) * 100}",
            font=FONT_small,
            color=textColor,
        )

        card = File(fp=background.image_bytes, filename="D:/Windows/Рабочий стол/wave1/module/rate/set/zCARD.png")
        await ctx.send(files=card)
def setup(client):
    Rankint(client)