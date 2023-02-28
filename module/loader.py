from module.fun.fun import FunSetup
from module.info.info import InfoSetup
from module.moderation.moderation import ModerationSetup
from module.rate.rate import RateSetup
from module.utility.utility import UtilitySetup
from module.moderation.error import BotError
# from module.self.commands.support import SupportAnswer
# from module.self.commands.support import Suppot

async def setup(bot):
    await bot.add_cog(FunSetup(bot))
    await bot.add_cog(InfoSetup(bot))
    await bot.add_cog(ModerationSetup(bot))
    await bot.add_cog(RateSetup(bot))
    await bot.add_cog(UtilitySetup(bot))
    await bot.add_cog(BotError(bot))
    # await bot.add_cog(SupportAnswer(bot))
    # await bot.add_cog(Suppot(bot))
