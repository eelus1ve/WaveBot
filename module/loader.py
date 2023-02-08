from module.fun.fun import FunSetup
from module.info.info import InfoSetup
from module.moderation.moderation import ModerationSetup
from module.rate.rate import RateSetup
from module.utility.utility import UtilitySetup
from module.moderation.error import BotError
from module.self.commands.support import SupportAnswer
from module.self.commands.support import Suppot

def setup(bot):
    bot.add_cog(FunSetup(bot))
    bot.add_cog(InfoSetup(bot))
    bot.add_cog(ModerationSetup(bot))
    bot.add_cog(RateSetup(bot))
    bot.add_cog(UtilitySetup(bot))
    bot.add_cog(BotError(bot))
    bot.add_cog(SupportAnswer(bot))
    bot.add_cog(Suppot(bot))
