def setup(bot):

    import discord
    from discord import Spotify
    import json

    @bot.command()
    async def spotify(ctx, user: discord.Member = None):
        print(1)
        with open('users.json', 'r') as file:
            data = json.load(file)
            COLOR = int(data[str(ctx.author.guild.id)]['COLOR'], 16)
            ErCOLOR = int(data[str(ctx.author.guild.id)]['ErCOLOR'], 16)
            
            
        userr = user or ctx.author
        print(2)
        if userr.activities:
            print(3)
            for activity in userr.activities:
                print(4)
                if isinstance(activity, Spotify):
                    print(5)
                    embed = discord.Embed(
                        title=f"{userr.name}'s Spotify",
                        description="Слушает {}".format(activity.title),
                        color=COLOR)#0x008000)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Исполнитель", value=activity.artist)
                    embed.add_field(name="Альбом", value=activity.album)
                    embed.set_footer(text="Песня началась в {}".format(activity.created_at.strftime("%H:%M")))
                    print(6)
                    await ctx.send(embed=embed)