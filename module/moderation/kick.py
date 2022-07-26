

config = {
    'prefix': '!' #поиграться с префиксами
}

def setup(bot):
        
    import discord
    import json
    from discord.ext import commands
    from distutils.log import error
    

    @bot.command(aliases=['кик', 'Кик', 'КИК'])
    @commands.has_permissions(administrator=True)
    async def kick(ctx, member: discord.Member, *, reason=None, amount=1):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)

        await ctx.channel.purge(limit=int(amount))
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*{member.mention} был кикнут!*",
                color=COLOR
            ))
    @kick.error
    async def error(ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)
            
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* " + str(config['prefix']) + "*kick (@Участник)*",
                color = ErCOLOR
            ))
            '''components = [
                [
                    Button(label = "Удалить", style=4),
                ]
            ]
        )
        while 1:
            interaction = await bot.wait_for("button_click")
            if interaction.component.label.startswith("Удалить"):
                await msg.delete()
                await ctx.message.delete()'''
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color = ErCOLOR
            ))
            '''components = [
                [
                    Button(label = "Удалить", style=4),
                ]
            ]
        )
        while 1:
            interaction = await bot.wait_for("button_click")
            if interaction.component.label.startswith("Удалить"):
                await msg.delete()
                await ctx.message.delete()'''

