from dataclasses import replace
import random
import discord
from discord.ui import Button
from discord.ext import commands
from BTSET import Fun, Lang

def game_over(body):
    if not [1 for i in body if 0 in i] and [[1 for ii in range(len(i[:3])) if i[ii] == i[ii + 1]] for i in body] == [[], [], [], []] and [[1 for ii in range(len(body[:3])) if body[i][ii] == body[i+1][ii]] for i in range(3)] == [[], [], []]:
        return 1
    elif [2048 for i in body if 2048 in i]:
        return 2
    else:
        return 0

def randomaizer(body):
    number = 2 if int(random.randint(0, 11)) else 4
    a = []

    for strng in range(len(body)):
        for indx in range(len(body[strng])):
            if not body[strng][indx]:
                a.append(indx + 4*strng)

    rplace = random.choice(a)

    place = rplace-(rplace//4)*4
    rplace = rplace//4

    body[rplace][place] = number

async def check_1(body, interaction):
    if game_over(body) == 2:
        emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title_win'],
                            description=Lang(ctx=interaction).language['p2048_des_win'],
                            color=Fun(interaction).color)
        await interaction.message.edit(embed=emb)

    elif game_over(body):
        asd = body[0] + body[1] + body[2] + body[3]
        emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title_loose'],
                            description='{} {} {}'.format(
                                Lang(ctx=interaction).language['p2048_des_loose_sum_1'], sum(asd),
                                Lang(ctx=interaction).language['p2048_des_loose_sum_2'],
                                Lang(ctx=interaction).language['p2048_des_loose_max'], max(asd)),
                            color=Fun(interaction).color)
        await interaction.message.edit(embed=emb)


class Game2048(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    lang_num = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    lang_emo = []

    async def listener_on_button_click_2048_left(self, interaction: discord.Interaction):
        await interaction.response.defer()
        des = []
        text = interaction.message.embeds[0].description
        text = text.replace('\n', '')
        text = text.split('<')[1:]
        body = [[Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[0:4]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[4:8]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[8:12]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[12:16]]]

        for strng in body:
            for iiii in range(3):
                for i in range(len(strng)):
                    if strng[i] and i and not strng[i - 1]:
                        a = strng[i]
                        strng[i] = 0
                        strng[i - 1] = a
            for i in range(len(strng)):
                if strng[i] and i and strng[i] == strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i - 1] = a * 2
            for i in range(len(strng)):
                if strng[i] and i and not strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i - 1] = a
        randomaizer(body)
        trans = [[Game2048.lang_emo[Game2048.lang_num.index(ii)] for ii in i] for i in body]

        for i in trans:
            des.append(str(''.join(map(str, i)) + str('\n')))
        emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title'],
                            description=''.join(des),
                            color=Fun(interaction).color)
        await interaction.message.edit(embed=emb)
        await check_1(body, interaction)

    async def listener_on_button_click_2048_up(self, interaction: discord.Interaction):
        await interaction.response.defer()
        des = []
        text = interaction.message.embeds[0].description
        text = text.replace('\n', '')
        text = text.split('<')[1:]
        body = [[Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[0:4]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[4:8]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[8:12]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[12:16]]]

        for ind in range(4):
            for iiii in range(3):
                for strng_number in range(len(body)):
                    if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                        a = body[strng_number][ind]
                        body[strng_number][ind] = 0
                        body[strng_number - 1][ind] = a
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and body[strng_number][ind] == \
                        body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a * 2
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a
        randomaizer(body)
        trans = [[Game2048.lang_emo[Game2048.lang_num.index(ii)] for ii in i] for i in body]
        for i in trans:
            des.append(str(''.join(map(str, i)) + str('\n')))
        emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title'],
                            description=''.join(des),
                            color=Fun(interaction).color)
        await interaction.message.edit(embed=emb)
        await check_1(body, interaction)

    async def listener_on_button_click_2048_right(self, interaction: discord.Interaction):
        await interaction.response.defer()
        des = []
        text = interaction.message.embeds[0].description
        text = text.replace('\n', '')
        text = text.split('<')[1:]
        body = [[Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[0:4]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[4:8]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[8:12]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[12:16]]]

        for strng in body:
            strng.reverse()
            for _ in range(3):
                for i in range(len(strng)):
                    if strng[i] and i and not strng[i - 1]:
                        a = strng[i]
                        strng[i] = 0
                        strng[i - 1] = a
            for i in range(len(strng)):
                if strng[i] and i and strng[i] == strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i - 1] = a * 2
            for i in range(len(strng)):
                if strng[i] and i and not strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i - 1] = a
            strng.reverse()
        randomaizer(body)
        trans = [[Game2048.lang_emo[Game2048.lang_num.index(ii)] for ii in i] for i in body]
        for i in trans:
            des.append(str(''.join(map(str, i)) + str('\n')))
        emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title'],
                            description=''.join(des),
                            color=Fun(interaction).color)
        await interaction.message.edit(embed=emb)
        await check_1(body, interaction)

    async def listener_on_button_click_2048_down(self, interaction: discord.Interaction):
        await interaction.response.defer()
        des = []
        text = interaction.message.embeds[0].description
        text = text.replace('\n', '')
        text = text.split('<')[1:]
        body = [[Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[0:4]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[4:8]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[8:12]],
                [Game2048.lang_num[Game2048.lang_emo.index('<' + i)] for i in text[12:16]]]

        body.reverse()
        for ind in range(4):
            for iiii in range(3):
                for strng_number in range(len(body)):
                    if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                        a = body[strng_number][ind]
                        body[strng_number][ind] = 0
                        body[strng_number - 1][ind] = a
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and body[strng_number][ind] == \
                        body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a * 2
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a
        body.reverse()
        randomaizer(body)
        trans = [[Game2048.lang_emo[Game2048.lang_num.index(ii)] for ii in i] for i in body]
        for i in trans:
            des.append(str(''.join(map(str, i)) + str('\n')))
        emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title'],
                            description=''.join(des),
                            color=Fun(interaction).color)
        await interaction.message.edit(embed=emb)
        await check_1(body, interaction)

    async def listener_on_button_2048(self, interaction: discord.Interaction):
        inter_children = interaction.message.components[0].children
        inter_id = interaction.data['custom_id']
        if inter_children[1] == inter_id: await Game2048(self.bot).listener_on_button_click_2048_left(interaction)
        if inter_children[0] == inter_id: await Game2048(self.bot).listener_on_button_click_2048_left(interaction)
        if inter_children[2] == inter_id: await Game2048(self.bot).listener_on_button_click_2048_left(interaction)
        if inter_children[3] == inter_id: await Game2048(self.bot).listener_on_button_click_2048_left(interaction)


    async def command_p2048(self, ctx: commands.Context): 
        stb_gld: discord.Guild = self.bot.get_guild(981511419042361344)
        e0 = str(await stb_gld.fetch_emoji(1034165149105389568))
        e2 = str(await stb_gld.fetch_emoji(1032695398848008274))
        e4 = str(await stb_gld.fetch_emoji(1032695400316026939))
        e8 = str(await stb_gld.fetch_emoji(1032695401582690304))
        e16 = str(await stb_gld.fetch_emoji(1034159672627826838))
        e32 = str(await stb_gld.fetch_emoji(1034159670811705375))
        e64 = str(await stb_gld.fetch_emoji(1034159669641490533))
        e128 = str(await stb_gld.fetch_emoji(1032695394179764384))
        e256 = str(await stb_gld.fetch_emoji(1032695395651964979))
        e512 = str(await stb_gld.fetch_emoji(1032695397010898944))
        e1024= str(await stb_gld.fetch_emoji(1032695402903912559))
        e2048 = str(await stb_gld.fetch_emoji(1032695404443218051))
        lsd = [e0, e2, e4, e8, e16, e32, e64, e128, e256, e512, e1024, e2048]
        Game2048.lang_emo.extend(lsd)
        body = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        randomaizer(body)

        trans = [[Game2048.lang_emo[Game2048.lang_num.index(ii)] for ii in i] for i in body]
        des=[]
        for i in trans:
            des.append(str(''.join(map(str, i)) + str('\n')))
        emb = discord.Embed(title=Lang(ctx).language['p2048_title'],
                            description=''.join(des),
                            color = Fun(ctx).color)

        vw = discord.ui.View(timeout=None)

        bt1 = Button(emoji='🔚')
        bt2= Button(emoji='⬆')
        bt3 = Button(emoji='⬇')
        bt4 = Button(emoji='🔜')

        vw.add_item(bt1)
        vw.add_item(bt2)
        vw.add_item(bt3)
        vw.add_item(bt4)

        await ctx.send(embed=emb, view=vw)

