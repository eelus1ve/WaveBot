
config = {
    'prefix': '!' #поиграться с префиксами
}

def setup(bot):

    import discord
    from discord.ext import commands
    from distutils.log import error
    import json

    @bot.command(aliases=['бан', 'Бан', 'БАН'])
    @commands.has_permissions(administrator=True)
    async def ban(ctx, member: discord.Member, reason = None):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)
        await member.ban(reason=reason)
        await ctx.send(embed=discord.Embed(
                title="Успешно",
                description=f"*{member.mention} был забанен !*",
                color=COLOR
            ))

    @ban.error
    async def error(ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            AdminchennelID = int(dataServerID[str(ctx.author.guild.id)]['idAdminchennel'], 16)
        
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* " + str(config['prefix']) + "*ban (@Участник)*",
                color = ErCOLOR
            ))
            
        if isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color = ErCOLOR
            ))
            