import discord
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from typing import Optional
from discord import File
from BTSET import bdpy, bdint
# import interactions
from PIL import Image, ImageFont, ImageDraw


class Rankpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
        userr = user or ctx.author
        xp = bdpy(ctx)['USERS'][str(userr.id)]["SCR"]
        lvl = bdpy(ctx)['USERS'][str(userr.id)]["LvL"]
        nlx = (lvl+1) * 100
        setcard = bdpy(ctx)['card']
        textColor = bdpy(ctx)['text_color']
        barColor = bdpy(ctx)['bar_color']
        blend = bdpy(ctx)['blend']

        percentage = int(((xp * 100)/ nlx))

        if percentage < 1:
            percentage = 0
        
        background = Editor(f"module/rate/img/{setcard}")
        profile = await load_image_async(str(userr.avatar_url))

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
        background.text((200, 40), f'{userr.name}#{userr.discriminator}', font=FONT, color=textColor)

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

# class Rankint(interactions.Extension):
#     def __init__(self, client):
#         self.client = client
#     @interactions.extension_user_command(
#         name='rank'
#     )
#     async def rank(self, ctx: interactions.CommandContext):
#         userr = ctx.target.user
#         xp = bdint(ctx)['USERS'][str(userr.id)]["SCR"]
#         lvl = bdint(ctx)['USERS'][str(userr.id)]["LvL"]
#         nlx = (lvl+1) * 100
#         setcard = bdint(ctx)['card']
#         textColor = bdint(ctx)['text_color']
#         barColor = bdint(ctx)['bar_color']
#         blend = bdint(ctx)['blend']

#         percentage = int(((xp * 100)/ nlx))

#         if percentage < 1:
#             percentage = 0
        
#         background = Editor(f"module/rate/img/{setcard}")
#         profile = await load_image_async(f'https://cdn.discordapp.com/avatars/{userr.id}/{userr.avatar}.webp?size=1024')

#         profile = Editor(profile).resize((150, 150)).circle_image()
        
#         FONT = ImageFont.truetype('allFonts.otf', 12) #Font.caveat(size=60) 
#         FONT_small = ImageFont.truetype('allFonts.otf', 12) #Font.caveat(size=50)

        
#         if blend == 1:
#             ima = Editor("module/rate/set/zBLACK.png")
#             background.blend(image=ima, alpha=.5, on_top=False)

#         background.paste(profile.image, (30, 30))

#         background.rectangle((30, 220), width=650, height=40, fill="#fff", radius=20)
#         background.bar(
#             (30, 220),
#             max_width=650,
#             height=40,
#             percentage=percentage,
#             fill=barColor,
#             radius=20,
#         )
#         background.text((200, 40), str(ctx.target.name), font=FONT, color=textColor)

#         background.rectangle((200, 100), width=350, height=2, fill=barColor)
#         background.text(
#             (200, 130),
#             f"Level : {lvl}   "
#             + f" XP : {xp} / {(lvl+1) * 100}",
#             font=FONT_small,
#             color=textColor,
#         )

#         card = File(fp=background.image_bytes, filename="module/rate/set/zCARD.png")
#         await ctx.send(file=card)

def setup(bot):
    if str(bot).startswith('<d'):
        bot.add_cog(Rankpy(bot))
    # elif str(bot).startswith('<i'):
    #     Rankint(bot)