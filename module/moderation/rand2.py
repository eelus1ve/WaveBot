import discord
from discord.ext import commands
from discord_components import Select, SelectOption
from BTSET import bdpy, bdmpy, BD
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
            COLOR = bdmpy(mr=interaction)['COLOR']
            ErCOLOR = bdmpy(mr=interaction)['ErCOLOR']
            roles = bdmpy(mr=interaction)['ROLES']
            import json
            with open(f'{BD}users.json', 'r') as file:
                data = json.load(file)
            #========================================Часть мейна=====================================================
            if interaction.component.placeholder.startswith('Укажите'):
                serverRoles = []
                for i in range(0, len(interaction.guild.roles),
                            24):  # первый важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    serverRoles.append(interaction.guild.roles[
                                    i:i + 24])  # второй важный комент !!!!!!!!!!!!!!!!!!!!!!!!! нужно при случаи ошибки заменить на 25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                if interaction.component.placeholder == 'Укажите классы в которые вы хотите добавить роли':
                    for i in interaction.values:
                        for rls in serverRoles:
                            await interaction.send(embed=discord.Embed(
                                title=f'Укажите роли которые вы хотите добавить в класс {i}',
                                color=COLOR
                            ),
                            components=[
                                Select(
                                    placeholder=f'Укажите роли которые вы хотите добавить в класс *{i}',
                                    max_values=len(rls),
                                    min_values=0,
                                    options=[Sel(label=i.name, value=i.id) for i in rls]
                                )
                                ]
                            )

                elif interaction.component.placeholder.startswith('Укажите роли которые вы хотите добавить в класс'):
                    data[str(interaction.author.guild.id)]['ROLES'][interaction.component.placeholder.split('*')[1]][0] = interaction.values
                    data[str(interaction.author.guild.id)]['ROLES'][interaction.component.placeholder.split('*')[1]][1] = [0 for i in interaction.values]
                    await interaction.send(embed=discord.Embed(
                        title=f'Роли выбранны',
                        color=COLOR
                    ))

                with open(f'{BD}users.json', 'w') as file:
                  json.dump(data, file, indent=4) 
            #========================================================================================================
            elif interaction.component.placeholder in [k for k in roles.keys()]:
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
                except:
                    pass
                    
                try:
                    
                    await a.add_roles(*[interaction.guild.get_role(int(i)) for i in interaction.values])
                except:
                    pass
        except:
            pass

        

        
def setup(bot):
    bot.add_cog(Selectpy(bot))