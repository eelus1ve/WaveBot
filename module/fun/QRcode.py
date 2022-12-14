import qrcode; from discord.ext import commands; import io; import discord
class CreateQR(commands.Cog):
    def __init__(self, bot): self.bot = bot
    @commands.command()
    async def get_qr(self, ctx: commands.Context, *arg): im = qrcode.make(ctx.message.content[8:]).get_image(); bt = io.BytesIO(); im.save(bt, format="PNG"); bt.seek(0); await ctx.send(file=discord.File(bt, filename='qr.png'))
def setup(bot): bot.add_cog(CreateQR(bot))