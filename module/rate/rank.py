import discord
import json
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from typing import Optional
from discord import File
class rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
        userr = user or ctx.author
        with open("users.json", "r") as f:
            data = json.load(f)
        xp = data[str(ctx.guild.id)]['USERS'][str(userr.id)]["SCR"]
        lvl = data[str(ctx.guild.id)]['USERS'][str(userr.id)]["LvL"]
        next_level_xp = (lvl+1) * 100
        xp_need = next_level_xp
        xp_have = data[str(ctx.guild.id)]['USERS'][str(userr.id)]["SCR"]
        setcard = str(data[str(ctx.guild.id)]['card'])
        text_color = str(data[str(ctx.guild.id)]['text_color'])
        bar_color = str(data[str(ctx.guild.id)]['bar_color'])
        blend = int(data[str(ctx.guild.id)]['blend'])

        percentage = int(((xp_have * 100)/ xp_need))

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
            fill=bar_color,
            radius=20,
        )
        background.text((200, 40), str(userr.name), font=FONT, color=text_color)

        background.rectangle((200, 100), width=350, height=2, fill=bar_color)
        background.text(
            (200, 130),
            f"Level : {lvl}   "
            + f" XP : {xp} / {(lvl+1) * 100}",
            font=FONT_small,
            color=text_color,
        )

        card = File(fp=background.image_bytes, filename="D:/Windows/Рабочий стол/wave1/module/rate/set/zCARD.png")
        await ctx.send(file=card)
def setup(bot):
    bot.add_cog(rank(bot))