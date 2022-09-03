import discord.ext.commands
import qrcode
from discord.ext import commands
import io


class CreateQR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def get_qr(self, ctx: discord.ext.commands.Context, *arg):
        im = qrcode.make(''.join(arg)).get_image()
        byte_im = im.tobitmap()
        await ctx.send(file=discord.File(fp=))


def setup(bot):
    bot.add_cog(CreateQR(bot))