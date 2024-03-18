import qrcode
from discord.ext import commands
import io
import discord
from system.Bot import WaveBot


class CreateQR(commands.Cog):
    def __init__(self, bot): 
        self.bot: WaveBot = bot
    
    @staticmethod
    async def command_get_qr(ctx: commands.Context):
        im = qrcode.make(ctx.message.content[8:]).get_image()
        bt = io.BytesIO() 
        im.save(bt, format="PNG")
        bt.seek(0)
        await ctx.send(file=discord.File(bt, filename='qr.png'))
