import json
import discord
from discord.ext import commands
import asyncio
from BTSET import ADMINS
from discord.utils import get
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
import StringProgressBar
import discord_components
import StringProgressBar


def counter_procent():
    with open('glb_vote.json', 'r') as file:
        vt_data = json.load(file)
    
    all_votes = sum([len(t) for t in [vt_data['votes'][k] for k in vt_data['votes']]])
    procents = []
    for i in [vt_data['votes'][k] for k in vt_data['votes']]:
        len_i_votes = len(i)
        procents.append(int(len_i_votes/all_votes*100))
    return procents



class GlobalVote(commands.Cog):
    def __init__(self, bot):
        self.bot: discord_components.ComponentsBot = bot

    @commands.command()
    async def new_info(self, ctx, class_mes='m', *arg):
        if str(ctx.author.id) in ADMINS:
            if class_mes == 'w':
                with open('glb_vote.json', 'r') as file:
                    vt_data = json.load(file)

                for gld in [k for k in vt_data.keys() if k != 'votes']:
                    chlen = self.bot.get_channel(vt_data[gld]['info_id'])

                    argg = []
                    for i in arg:
                        argg.append(i + ' ')

                    await chlen.send(embed=discord.Embed(
                        title='***ВНИМАНИЕ***',
                        description=''.join(argg),
                        colour=0xFFFF00
                    ))

            elif class_mes == 'm':
                with open('glb_vote.json', 'r') as file:
                    vt_data = json.load(file)

                for gld in [k for k in vt_data.keys() if k != 'votes']:
                    chlen = self.bot.get_channel(vt_data[gld]['info_id'])

                    await chlen.send(embed=discord.Embed(
                        title='***Сообщение от WAVE team***',
                        description=''.join(arg),
                        colour=0xFFF000
                    ))


    @commands.command()
    async def new_glvote(self, ctx: commands.Context, *argg):
        if str(ctx.author.id) in ADMINS:
            with open('glb_vote.json', 'r') as file:
                vt_data = json.load(file)

            arg = []
            for i in argg:
                if not ';' in i:
                    arg.append(i + ' ')
                else:
                    arg.append(i)
            arg = ''.join(arg)
            arg = arg.split(';')

            for gld in [k for k in vt_data.keys() if k != 'votes']:

                chlen: discord.TextChannel = self.bot.get_guild(int(gld)).get_channel(vt_data[str(gld)]['vote_id'])

                await chlen.purge()

                await chlen.send(
                    embed=discord.Embed(
                        title=f'Голосование',
                        description=''.join([str(StringProgressBar.progressBar.splitBar(100, 1, 25)[0]) + '—' + i + '\n' for i in arg])
                    ),
                    components=[[Button(label=f'{i}', style=2) for i in arg[e:e+5]] for e in range(0, len(arg), 5)]
                )

            try:
                del vt_data['votes']
            except KeyError:
                pass
            vt_data.update({
                'votes':
                    {
                        i: [] for i in arg
                    }

            })
            with open('glb_vote.json', 'w') as file:
                json.dump(vt_data, file, indent=4)


    @commands.Cog.listener('on_button_click')
    async def globalvote_on_button_click(self, interaction: discord_components.Interaction):
        with open('glb_vote.json', 'r') as file:
            vt_data = json.load(file)

        if interaction.component.label in [k for k in vt_data['votes']]:
            if not [t for t in [vt_data['votes'][k] for k in vt_data['votes']] if interaction.author.id in t]:
                vt_data['votes'][interaction.component.label].append(interaction.author.id)

                with open('glb_vote.json', 'w') as file:
                    json.dump(vt_data, file, indent=4)
                
                for gld in [k for k in vt_data.keys() if k != 'votes']:

                    chlen: discord.TextChannel = self.bot.get_channel(vt_data[str(gld)]['vote_id'])
                    message: discord.Message = await chlen.fetch_message(chlen.last_message_id)

                    last_embed = message.embeds[0]
                    lst: list = counter_procent()

                    descr = [
                        StringProgressBar.progressBar.splitBar(100, lst[i], 25)[0] + str([k for k in vt_data['votes'].keys()][i]) + '\n' for i in range(len(lst))
                    ]

                    emb = discord.Embed(
                        title=last_embed.title,
                        description=''.join(descr)
                    )


                    await message.edit(embed=emb)






def setup(bot):
    bot.add_cog(GlobalVote(bot))
