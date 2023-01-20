import discord
from discord.ext import commands
from discord_components import Select, SelectOption
from BTSET import bdpy, BD
from discord_components import SelectOption as Sel

class Selectpy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def select(self, ctx, arg=None):
        COLOR = bdpy(ctx)['COLOR']
        roles = bdpy(ctx)['ROLES']
        selftitle = bdpy(ctx)['SelfTitle']

        if arg == None: #сам сюда что-то делай (мне лень)
            pass

        elif arg in [k for k in roles.keys()]:
                await ctx.send(embed=discord.Embed(
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

    @commands.Cog.listener('on_select_option')
    async def ion_select_option(self, interaction):
        try:
            COLOR = bdpy(ctx=interaction)['COLOR']
            ErCOLOR = bdpy(ctx=interaction)['ErCOLOR']
            roles = bdpy(ctx=interaction)['ROLES']
            if interaction.component.placeholder in [k for k in roles.keys()]:
                a = interaction.author
                try:
                    await interaction.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"Роли выбраны!",
                        color=COLOR
                    ))
                    
                except IndexError:
                    await interaction.send(embed=discord.Embed(
                        title="Успешно",
                        description="*Роли успешно сняты!*",
                        color=ErCOLOR
                    ))

                try:
                    await a.remove_roles(*[interaction.guild.get_role(role_id=int(ii)) for ii in roles[str(interaction.component.placeholder)][0] if not(ii in interaction.values)])
                    await a.add_roles(*[interaction.guild.get_role(int(i)) for i in interaction.values])
                except:
                    pass
        except:
            pass

        

        
def setup(bot):
    bot.add_cog(Selectpy(bot))