import discord.ext.commands; import qrcode; from discord.ext import commands; import io
class CreateQR(commands.Cog):
    def __init__(self, bot): self.bot = bot
    @commands.command()
    async def get_qr(self, ctx: discord.ext.commands.Context, *arg): argg = []; [argg.append(i + ' ') for i in arg]; im = qrcode.make(''.join(argg)).get_image(); bt = io.BytesIO(); im.save(bt, format="PNG"); bt.seek(0); await ctx.send(file=discord.File(bt, filename='lox.png'))
def setup(bot): bot.add_cog(CreateQR(bot))