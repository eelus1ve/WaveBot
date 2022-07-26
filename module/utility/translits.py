def setup(bot):
    import discord
    import json
    from discord.ext import commands
    
    lst = [' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
    lst1 = [' ', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.',]
    @bot.command()
    async def tr(ctx, *arg):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)

        if arg:
            bf = []
            for ii in arg:
                bf.extend([ii[i] for i in range(len(ii))] + [' '])

            await ctx.send(embed=discord.Embed(
                title="Перевод: ",
                description=''.join([lst1[lst.index(i)] for i in bf]),
                color = COLOR
            ))
        
