import discord
import json
from discord.ext import commands
import interactions
from BD import bdint
class Leadersint(interactions.Extension):
    def __init__(self, client: interactions.Client) -> None:
        self.client: interactions.Client = client
    @interactions.extension_command(
        name="leaders",
        description="Показать таюлицу лидеров",
    )
    async def leaders(self, ctx, range_num=10):
        with open("users.json", "r") as f:
            data = json.load(f)
        COLOR = bdint(ctx)['COLOR']
        l = {}
        total_xp = []
        for userid in data[str(ctx.guild.id)]['USERS']:
            xp = bdint(ctx)['USERS'][str(userid)]['SCR']+(sum([i for i in range((bdint(ctx)['USERS'][str(userid)]['LvL']) + 1)])*100)

            l[xp] = f"{userid};{data[str(ctx.guild.id)]['USERS'][str(userid)]['LvL']};{data[str(ctx.guild.id)]['USERS'][str(userid)]['SCR']}"
            total_xp.append(xp)

        total_xp = sorted(total_xp, reverse=True)
        index=1
        
        mbed = interactions.Embed(
        title="Доска лидеров",
        color=COLOR
        )

        for amt in total_xp:
            id_ = int(str(l[amt]).split(";")[0])
            level = int(str(l[amt]).split(";")[1])
            xp = int(str(l[amt]).split(";")[2])

            member = await ctx.bot.fetch_user(id_)
            if member is not None:
                name = member.name
                mbed.add_field(name=f"{index}. {name}",
                value=f"**Level: {level} | XP: {xp}**", 
                inline=False)
                
                if index == range_num:
                    break
                else:
                    index += 1
        await ctx.send(embeds = mbed)
def setup(client):
    Leadersint(client)