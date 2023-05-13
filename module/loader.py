from module.fun.fun import FunSetup
from module.info.info import InfoSetup
from module.moderation.moderation import ModerationSetup
# from module.rate.rate import RateSetup
from module.utility.utility import UtilitySetup
from module.self.commands.support import SupportAnswer
from module.self.commands.support import Suppot
from module.moderation.joiner import Joiner
from module.moderation.error import BotError
from system.Bot import WaveBot


async def setup(bot: WaveBot):
    await bot.add_cog(Joiner(bot))
    await bot.add_cog(ModerationSetup(bot))
    await bot.load_extension('module.moderation.commands.btst')
    await bot.add_cog(InfoSetup(bot))
    # await bot.add_cog(RateSetup(bot))
    await bot.add_cog(FunSetup(bot))
    await bot.add_cog(UtilitySetup(bot))
    await bot.add_cog(SupportAnswer(bot))
    await bot.add_cog(Suppot(bot))
    await bot.add_cog(BotError(bot))
