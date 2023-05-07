import random
import discord
from discord.ui import Button
from discord.ext import commands
from BTSET import Lang
from system.Bot import WaveBot


class Game2048Support:
    def __init__(self, bot: WaveBot):
        self.bot: WaveBot = bot

    @staticmethod
    def game_over(body):
        if not [1 for i in body if 0 in i] and [[1 for ii in range(len(i[:3])) if i[ii] == i[ii + 1]] for i in body] == [[], [], [], []] and [[1 for ii in range(len(body[:3])) if body[i][ii] == body[i+1][ii]] for i in range(3)] == [[], [], []]:
            return 1
        elif [2048 for i in body if 2048 in i]:
            return 2
        else:
            return 0

    @staticmethod
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

    async def check_1(self, body, interaction, bot):
        if Game2048Support(self.bot).game_over(body) == 2:
            emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title_win'],
                                description=Lang(ctx=interaction).language['p2048_des_win'],
                                color=bot.db_get_funcolor(interaction))
            await interaction.message.edit(embed=emb)

        elif Game2048Support(self.bot).game_over(body):
            asd = body[0] + body[1] + body[2] + body[3]
            emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title_loose'],
                                description='{} {} {}'.format(
                                    Lang(ctx=interaction).language['p2048_des_loose_sum_1'], sum(asd),
                                    Lang(ctx=interaction).language['p2048_des_loose_sum_2'],
                                    Lang(ctx=interaction).language['p2048_des_loose_max'], max(asd)),
                                color=bot.db_get_funcolor(interaction))
            await interaction.message.edit(embed=emb)

    def get_body(self, interaction: discord.Interaction) -> list:
        text = interaction.message.embeds[0].description
        text = text.replace('\n', '')
        text = text.split('<')[1:]
        return [[Game2048.lang_num[Game2048(self.bot).lang_emo.index('<' + i)] for i in text[0:4]],
                [Game2048.lang_num[Game2048(self.bot).lang_emo.index('<' + i)] for i in text[4:8]],
                [Game2048.lang_num[Game2048(self.bot).lang_emo.index('<' + i)] for i in text[8:12]],
                [Game2048.lang_num[Game2048(self.bot).lang_emo.index('<' + i)] for i in text[12:16]]]

    @staticmethod
    def vertical_play(body: list, is_up: bool) -> list:
        if is_up:
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
        if is_up:
            body.reverse()

        return body

    @staticmethod
    def horizontal_play(body: list, is_up: bool = False) -> list:
        for strng in body:
            if is_up:
                strng.reverse()
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
            if is_up:
                strng.reverse()

        return body

    async def after_play(self, interaction: discord.Interaction, body: list, bot: WaveBot) -> None:
        des = []
        Game2048Support(self.bot).randomaizer(body)
        trans = [[Game2048(self.bot).lang_emo[Game2048.lang_num.index(ii)] for ii in i] for i in body]

        for i in trans:
            des.append(str(''.join(map(str, i)) + str('\n')))
        emb = discord.Embed(title=Lang(ctx=interaction).language['p2048_title'],
                            description=''.join(des),
                            color=bot.db_get_funcolor(interaction))
        emb.set_footer(text=f'{interaction.user.name}#{interaction.user.discriminator}', icon_url=interaction.user.display_icon)
        await interaction.message.edit(embed=emb)
        await Game2048Support(self.bot).check_1(body, interaction, bot)


class Game2048(commands.Cog):
    def __init__(self, bot: WaveBot):
        self.bot: WaveBot = bot
        stb_gld: discord.Guild = self.bot.get_guild(981511419042361344)
        emos = stb_gld.emojis
        e0 = str([i for i in emos if i.id == 1034165149105389568][0])
        e2 = str([i for i in emos if i.id == 1032695398848008274][0])
        e4 = str([i for i in emos if i.id == 1032695400316026939][0])
        e8 = str([i for i in emos if i.id == 1032695401582690304][0])
        e16 = str([i for i in emos if i.id == 1034159672627826838][0])
        e32 = str([i for i in emos if i.id == 1034159670811705375][0])
        e64 = str([i for i in emos if i.id == 1034159669641490533][0])
        e128 = str([i for i in emos if i.id == 1032695394179764384][0])
        e256 = str([i for i in emos if i.id == 1032695395651964979][0])
        e512 = str([i for i in emos if i.id == 1032695397010898944][0])
        e1024 = str([i for i in emos if i.id == 1032695402903912559][0])
        e2048 = str([i for i in emos if i.id == 1032695404443218051][0])
        self.lang_emo = [e0, e2, e4, e8, e16, e32, e64, e128, e256, e512, e1024, e2048]

    lang_num = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

    async def listener_on_button_click_2048_left(self, interaction: discord.Interaction):
        body = Game2048Support(self.bot).get_body(interaction)

        Game2048Support(self.bot).horizontal_play(body)

        await Game2048Support(self.bot).after_play(interaction, body, self.bot)

    async def listener_on_button_click_2048_up(self, interaction: discord.Interaction):
        body = Game2048Support(self.bot).get_body(interaction)

        Game2048Support(self.bot).vertical_play(body, False)

        await Game2048Support(self.bot).after_play(interaction, body, self.bot)

    async def listener_on_button_click_2048_right(self, interaction: discord.Interaction):
        body = Game2048Support(self.bot).get_body(interaction)

        Game2048Support(self.bot).horizontal_play(body, True)

        await Game2048Support(self.bot).after_play(interaction, body, self.bot)

    async def listener_on_button_click_2048_down(self, interaction: discord.Interaction):
        body = Game2048Support(self.bot).get_body(interaction)

        Game2048Support(self.bot).vertical_play(body, True)

        await Game2048Support(self.bot).after_play(interaction, body, self.bot)

    async def listener_on_button_2048(self, interaction: discord.Interaction):
        try:
            assert f'{interaction.user.name}#{interaction.user.discriminator}' == interaction.message.embeds[0].footer.text

            inter_children = interaction.message.components[0].children
            inter_id = interaction.data['custom_id']

            if inter_children[0].custom_id == inter_id:
                await interaction.response.defer()
                await Game2048(self.bot).listener_on_button_click_2048_left(interaction)

            if inter_children[1].custom_id == inter_id:
                await interaction.response.defer()
                await Game2048(self.bot).listener_on_button_click_2048_up(interaction)

            if inter_children[2].custom_id == inter_id:
                await interaction.response.defer()
                await Game2048(self.bot).listener_on_button_click_2048_down(interaction)

            if inter_children[3].custom_id == inter_id:
                await interaction.response.defer()
                await Game2048(self.bot).listener_on_button_click_2048_right(interaction)
        except:
            pass

    async def command_p2048(self, ctx: commands.Context): 

        body = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        Game2048Support(self.bot).randomaizer(body)

        trans = [[Game2048(self.bot).lang_emo[Game2048.lang_num.index(ii)] for ii in i] for i in body]
        des = []
        for i in trans:
            des.append(str(''.join(map(str, i)) + str('\n')))
        emb = discord.Embed(title=Lang(ctx).language['p2048_title'],
                            description=''.join(des),
                            color=self.bot.db_get_funcolor(ctx))
        emb.set_footer(text=f'{ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.display_icon)

        vw = discord.ui.View(timeout=None)

        bt1 = Button(emoji='🔚')
        bt2 = Button(emoji='⬆')
        bt3 = Button(emoji='⬇')
        bt4 = Button(emoji='🔜')

        vw.add_item(bt1)
        vw.add_item(bt2)
        vw.add_item(bt3)
        vw.add_item(bt4)

        await ctx.send(embed=emb, view=vw)
