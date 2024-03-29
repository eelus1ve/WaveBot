from discord.ext import commands
import discord
from module.fun.commands.dice import Dice
from module.fun.commands.MagicBall import MagicBall
from module.fun.commands.coin import Coin
from module.fun.commands.QRcode import CreateQR
from module.fun.commands.anMessage import GetMessage
from module.fun.commands.p2048 import Game2048
# from module.fun.mafia import
# from module.fun.xo import
from system.Bot import WaveBot


class FunSetup(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx: commands.Context):
        await Dice(self.bot).command_dice(ctx)

    @commands.command(aliases=['монетка', 'Монетка', 'МОНЕТКА'])
    async def coin(self, ctx: commands.Context):
        await Coin(self.bot).command_coin(ctx)

    @commands.command(aliases=['Волшебный_шар', '8ball', 'MagicBall', '8Ball'])
    async def Magicball(self, ctx: commands.Context):
        await MagicBall(self.bot).command_magicball(ctx)

    @commands.command()
    async def p2048(self, ctx: commands.Context):
        await Game2048(self.bot).command_p2048(ctx)

    @commands.command()
    async def get_qr(self, ctx: commands.Context):
        await CreateQR(self.bot).command_get_qr(ctx)

    @commands.command()
    async def send_an_message(self, ctx: commands.Context):
        await GetMessage(self.bot).command_send_an_message(ctx)

    @commands.Cog.listener('on_interaction')
    async def on_button_click_2048(self, interaction: discord.Interaction):
        await Game2048(self.bot).listener_on_button_2048(interaction)

    @commands.Cog.listener('on_button_click')
    async def on_button_click_anMessage(self, interaction: discord.Interaction):
        await GetMessage(self.bot).listener_on_button_click_anMessage(interaction)
