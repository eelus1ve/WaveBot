import discord
from discord.ext import commands
from discord_components import Select, SelectOption, Interaction
from BTSET import Moderation, bdpy

class Select(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_select(self, ctx: commands.Context, arg=None):
        roles = bdpy(ctx)['ROLES']
        selftitle = bdpy(ctx)['SelfTitle']

        if arg == None: #сам сюда что-то делай (мне лень)
            pass

        elif arg in [k for k in roles.keys()]:
                await ctx.send(embed=discord.Embed(
                    title=selftitle,
                    color=Moderation(ctx.author).color
                ),
                    components=[
                        Select(                                             
                            placeholder=arg,
                            max_values=len(roles[arg][0]),
                            min_values=0,
                            options=[SelectOption(label=ctx.guild.get_role(int(i)).name, value=i) for i in roles[arg][0]]
                        )
                    ]
                )

    async def listener_on_select_option_select(self, interaction: Interaction):
        try:
            ErCOLOR = bdpy(ctx=interaction)['ErCOLOR']
            roles = bdpy(ctx=interaction)['ROLES']
            if interaction.component.placeholder in [k for k in roles.keys()]:
                a = interaction.author
                try:
                    await interaction.send(embed=discord.Embed(
                        title="Успешно",
                        description=f"Роли выбраны!",
                        color=Moderation(interaction.author).color
                    ))
                    
                except IndexError:
                    await interaction.send(embed=discord.Embed(
                        title="Успешно",
                        description="*Роли успешно сняты!*",
                        color=Moderation(interaction.author).color
                    ))

                try:
                    await a.remove_roles(*[interaction.guild.get_role(int(ii)) for ii in roles[str(interaction.component.placeholder)][0] if not(ii in interaction.values)])
                except:
                    pass
                    
                try:
                    
                    await a.add_roles(*[interaction.guild.get_role(int(i)) for i in interaction.values])
                except:
                    pass
        except:
            pass