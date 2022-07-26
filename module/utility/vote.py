def setup(bot):
    
    import discord
    import json
    from discord.ext import commands
    
    @bot.command()
    async def vote(ctx, *arg):
        with open('users.json', 'r') as file:
            dataServerID = json.load(file)
            COLOR = int(dataServerID[str(ctx.author.guild.id)]['COLOR'], 16)

        em = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣⃣', '7️⃣', '8️⃣', '9️⃣', '0️⃣']
        arg = ''.join(arg)
        arg = arg.split(';')
        title = []
        title.append(arg.pop(0))
        e = 0
        for i in arg:
            title.append('\n' + str(em[e]) + ' ' + str(i))
            e += 1
        ms = await ctx.send(embed=discord.Embed(title=title.pop(0), description=''.join(title), color = COLOR))
        
        for i in range(len(title)):
            await ms.add_reaction(em[i])
