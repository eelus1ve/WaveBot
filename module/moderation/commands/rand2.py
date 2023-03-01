import discord
from discord.ext import commands
from BTSET import Moderation, bdpy, InteractionComponents
from discord.ui import Button, Select, View
from email.errors import InvalidMultipartContentTransferEncodingDefect


class SelectRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def command_select(self, ctx: commands.Context, arg=None):
        roles = bdpy(ctx)['ROLES']
        selftitle = bdpy(ctx)['SelfTitle']

        if arg == None: #сам сюда что-то делай (мне лень)
            pass

        elif arg in [k for k in roles.keys()]:
            sel = Select(
                placeholder=arg,
                max_values=len(roles[arg][0]),
                min_values=0,
            )
            [sel.add_option(label=ctx.guild.get_role(int(i)).name, value=i, emoji=ctx.guild.get_role(int(i)).icon) for i in roles[arg][0]]
            vw = View(timeout=None)
            vw.add_item(sel)
            await ctx.send(embed=discord.Embed(
                title=selftitle,
                color=Moderation(ctx.author).color
            ),
                view=vw
            )

    async def listener_on_select_option_select(self, interaction: discord.Interaction):
        try:
            ErCOLOR = bdpy(ctx=interaction)['ERCOLOR']
            roles = bdpy(ctx=interaction)['ROLES']
            if InteractionComponents(interaction).placeholder in [k for k in roles.keys()]:
                a = interaction.user
                try:
                    await interaction.response.send_message(embed=discord.Embed(
                        title="Успешно",
                        description=f"Роли выбраны!",
                        color=Moderation(interaction.user).color
                    ), ephemeral=True)
                    
                except IndexError:
                    await interaction.response.send_message(embed=discord.Embed(
                        title="Успешно",
                        description="*Роли успешно сняты!*",
                        color=Moderation(interaction.user).color
                    ), ephemeral=True)

                try:
                    await a.remove_roles(*[interaction.guild.get_role(int(ii)) for ii in roles[str(InteractionComponents(interaction).placeholder)][0] if not(ii in InteractionComponents(interaction).values)])
                    await a.add_roles(*[interaction.guild.get_role(int(i)) for i in InteractionComponents(interaction).values])
                except:
                    pass
        except:
            pass