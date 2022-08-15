import discord
from discord.ext import commands
from discord_components import Select, SelectOption
import interactions
from BD import bdint
class Selectint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name='select',
        description='Вызвать панель для выдачи ролей'
    )
    async def select(self, ctx, arg=None):
        COLOR = bdint(ctx)['COLOR']
        roles = bdint(ctx)['ROLES']
        selftitle = bdint(ctx)['SelfTitle']

        if arg == None: #сам сюда что-то делай (мне лень)
            pass

        elif arg in [k for k in roles.keys()]:
                await ctx.send(embeds=interactions.Embed(
                    title=selftitle,
                    color=COLOR
                ),
                    components=[
                        Select(                                             
                            placeholder=arg,
                            max_values=len(roles[arg][0]),
                            min_values=0,
                            options=[SelectOption(label=ctx.guild.get_role(role_id=int(i)).name, value=i) for i in roles[arg][0]]
                        )
                    ]
                )
def setup(bot):
    Selectint(bot)