


def setup(bot):
    import discord
    from discord.ext import commands
    from discord_components import Select, SelectOption
    from email.errors import InvalidMultipartContentTransferEncodingDefect
    import json

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def select(ctx, arg=None):
        global a
        with open('users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            AdminchennelID = data[str(ctx.author.guild.id)]['idAdminchennel']
            roles = data[str(ctx.author.guild.id)]['ROLES']
            selftitle = data[str(ctx.author.guild.id)]['SelfTitle']

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

    @bot.event
    async def on_select_option(interaction):
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                COLOR = int(data[str(interaction.guild.id)]['COLOR'], 16)
                ErCOLOR = int(data[str(interaction.guild.id)]['ErCOLOR'], 16)
                AdminchennelID = data[str(interaction.guild.id)]['idAdminchennel']
                roles = data[str(interaction.guild.id)]['ROLES']

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
                    print(str([ii for ii in roles[str(interaction.component.placeholder)][0] if not(ii in interaction.values)]), '1')
                    await a.remove_roles([interaction.guild.get_role(role_id=int(ii)) for ii in roles[str(interaction.component.placeholder)][0] if not(ii in interaction.values)])
                except InvalidMultipartContentTransferEncodingDefect:
                    pass
                    
                try:
                    
                    await a.add_roles([interaction.guild.get_role(int(i)) for i in interaction.values])
                except InvalidMultipartContentTransferEncodingDefect:
                    pass
        except InvalidMultipartContentTransferEncodingDefect:
            pass

            
