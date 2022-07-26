from BTSET import ADMINS


config = {
    'prefix': '!' #поиграться с префиксами
}

def setup(bot):

    import discord
    import asyncio
    import json
    from discord.ext import commands

    @bot.command(aliases=['очистить', 'Очистить', 'ОЧИСТИТЬ'])
    @commands.has_permissions(administrator=True)
    async def clear(ctx, amount: int):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
        if amount <= 1000:
            await ctx.channel.purge(limit=int(amount))
            msg = await ctx.send(embed=discord.Embed(
                title="Очистка прошла успешно",
                description="*Очищено* " + str(amount) + " *сообщений*",
                color=COLOR
            ))
            
        else:
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* " + str(config['prefix']) + "*clear (количество до 1000 за 1 раз)*",
                color=ErCOLOR
            ))
        await asyncio.sleep(5)
        await msg.delete()
    @clear.error
    async def error(ctx, error):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            
        if isinstance(error, commands.MissingRequiredArgument):
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Использование:* " + str(config['prefix']) + "*clear (количество до 1000 за 1 раз)*",
                color=ErCOLOR
            ))
        elif isinstance(error, commands.MissingPermissions):
            msg = await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*У вас недостаточно прав!*",
                color=ErCOLOR
            ))
        await asyncio.sleep(2)
        await msg.delete()

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def clear_channels(ctx):
        if ctx.author.id == ctx.guild.owner.id or ctx.author.id in ADMINS:
            guild = ctx.guild
            for channel in guild.channels:
                await channel.delete()
        else:
            with open('users.json', 'r') as file:
                dataServerID = json.load(file)
                ErCOLOR = int(dataServerID[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            await ctx.send(embed=discord.Embed(
                title="Ошибка",
                description="*Пошел нахуй!*",
                color=ErCOLOR
            ))