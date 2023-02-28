import discord
import json
from discord.ext import commands
from typing import Optional
from distutils.log import error
import re
from discord.utils import get
from BTSET import bdpy, BD
import datetime
import pytz

n = {}

memberInfo = {}

class Score_interactions(interactions.Extension):
    def __init__(self, client):
        self.client = client
    
    @interactions.extension_user_command(
        name='score'
    )
    async def score_int(self, ctx: interactions.CommandContext):
        memberInfo.update({str(ctx.author.id): [str(ctx.target.user.id), str(ctx.target.name)]})
        await ctx.popup(Modal(
                custom_id='Score',
                title=' ',
                components=[
                    TextInput(
                        style=TextStyleType.SHORT,
                        custom_id='qwertyuiop',
                        label='укажите знак(+/-) и кол-во очков',
                        min_length=2,
                        max_length=5
                    )
                ]
            ))
    
    @interactions.extension_modal('Score')
    async def scrya(self, ctx: interactions.CommandContext, shrt):
        print(ctx.author.avatar)
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        SCR = bdint(ctx)['USERS'][str(memberInfo[str(ctx.author.id)][0])]['SCR']
        LVL = bdint(ctx)['USERS'][str(memberInfo[str(ctx.author.id)][0])]['LvL']
        if str(shrt).startswith('+'):
            argg = str(shrt).replace('+', '')
            dermo = int(SCR) + int(argg)
            Lvl1 = LVL-1
            xp = (400+100*(Lvl1-1))/2*Lvl1 + dermo
            d = (3**2+4*2*xp/100)**0.5
            if (-3-d)/2 > (-3+d)/2:
                level = (-3-d)/2
            else:
                level = (-3+d)/2
            xpp = xp - (400+100*(int(level-1)))/2*int(level)
            with open(f'{BD}users.json', 'w') as file:
                data[str(ctx.guild_id)]['USERS'][str(memberInfo[str(ctx.author.id)][0])]['SCR'] = int(xpp)
                data[str(ctx.guild_id)]['USERS'][str(memberInfo[str(ctx.author.id)][0])]['LvL'] = int(level+1)
                json.dump(data, file, indent=4)
            await ctx.send(embeds = embint(ctx, comp='s', des=f'Участник {str(memberInfo[str(ctx.author.id)][1])} получил {argg}'))
        elif str(shrt).startswith('-'):
            argg = str(shrt).replace('-', '')
            dermo = int(SCR) - int(argg)
            Lvl1 = LVL-1
            xp = (400+100*(Lvl1-1))/2*Lvl1 + dermo
            d = (3**2+4*2*xp/100)**0.5
            if (-3-d)/2 > (-3+d)/2:
                level = (-3-d)/2
            else:
                level = (-3+d)/2
            xpp = xp - (400+100*(int(level-1)))/2*int(level)
            if str(level).startswith('-') or str(xpp).startswith('-'):
                with open(f'{BD}users.json', 'w') as file:
                    data[str(ctx.guild_id)]['USERS'][str(memberInfo[str(ctx.author.id)][0])]['SCR'] = 0
                    data[str(ctx.guild_id)]['USERS'][str(memberInfo[str(ctx.author.id)][0])]['LvL'] = 1
                    json.dump(data, file, indent=4)
            else:
                with open(f'{BD}users.json', 'w') as file:
                    data[str(ctx.guild_id)]['USERS'][str(memberInfo[str(ctx.author.id)][0])]['SCR'] = int(xpp)
                    data[str(ctx.guild_id)]['USERS'][str(memberInfo[str(ctx.author.id)][0])]['LvL'] = int(level+1)
                    json.dump(data, file, indent=4)
            await ctx.send(embeds = embint(ctx, comp='s', des=f'Участник {str(memberInfo[str(ctx.author.id)][1])} получил {argg}'), ephemeral=True)
        else:
            await ctx.send(embeds = embint(ctx, comp='e', des=f'укажите знак(+/-) и кол-во очков'), ephemeral=True)
        for i in [k for k in memberInfo.keys()]:
            if i == str(ctx.author.id):
                memberInfo.pop(i)



class Warnsint(interactions.Extension):
    def __init__(self, client):
        self.client = client
        
    @interactions.extension_message_command(
        name='warns'
    )
    async def warns_int(self, ctx: interactions.CommandContext):
        try:
            if bdpy(ctx)['ModRoles'] != {}:
                quest = bdpy(ctx)['ModRoles'][[str(i.id) for i in ctx.author.roles if str(i.id) in bdpy(ctx)['ModRoles']][0]]['Warns']['Warn'] == "True" or ctx.author.guild_permissions.administrator
            else:
                quest = ctx.author.guild_permissions.administrator
            if quest:
                n.update({str(ctx.author.id): [str(ctx.target.author.id), str(ctx.target.author.mention), str(ctx.target.content), str(ctx.target.timestamp.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')).strftime('%H:%M || %d.%m.%y')), str(ctx.target.channel_id)]})
                await ctx.popup(Modal(
                        custom_id='warns',
                        title=' ',
                        components=[
                            TextInput(
                                style=TextStyleType.SHORT,
                                custom_id='qwertyuiop',
                                label='тип нарушения'
                            )
                        ]
                    ))
            else:
                await ctx.send(embeds = embint(ctx, comp='e', des=f'У вас недостаточно прав!'), ephemeral=True)
        except:
            await ctx.send(embeds = embint(ctx, comp='e', des=f'У вас недостаточно прав!'), ephemeral=True)
    
    @interactions.extension_modal('warns')
    async def wrn(self, ctx: interactions.CommandContext, shrt):
        with open(f'{BD}users.json', 'r') as file:
            data = json.load(file)
        moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        COLOR = bdint(ctx)['COLOR']
        nWarns = bdint(ctx)['nWarns']
        warns = bdpy(ctx)['USERS'][str(memberr.id)]['WARNS']
        idAdminchennel = bdint(ctx)['idAdminchennel']
        #====================================================================
        #audit
        #====================================================================
        if bdpy(ctx)['idAdminchennel'] in [str(i.id) for i in ctx.guild.channels]:
            emb = interactions.Embed(
                title='Нарушение',
                description=f"*Ранее, у нарушителя было уже {bdint(ctx)['USERS'][str(n[str(ctx.author.id)][0])]['WARNS'] - 1} нарушений, после {nWarns} он будет забанен!*",
                timestamp=moscow_time,
                color=COLOR
            )
            
            emb.add_field(name='Сообщение нарушителя:', value=str(n[str(ctx.author.id)][2]), inline=True)
            emb.add_field(name='Время нарушения:', value=n[str(ctx.author.id)][3])
            a = await ctx.get_guild()
            b = await a.get_all_channels()
            for i in b:
                if str(i.id) == str(n[str(ctx.author.id)][4]):
                    emb.add_field(name='Канал:', value=i.mention, inline=True)
            emb.add_field(name='Нарушитель:', value=n[str(ctx.author.id)][1], inline=True)
            emb.add_field(name='Тип нарушения:', value=str(shrt), inline=True)
            emb.set_footer(text=f'Нарушение выдал учасник {ctx.author.name}, ID учасника: {ctx.author.id}')
            c = await ctx.get_guild()
            d = await c.get_all_channels()
            for i in d:
                if str(i.id) == str(idAdminchennel):
                    await i.send(embeds=emb)
            with open(f'{BD}users.json', 'w') as file:
                data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['WARNS'] +=1
                json.dump(data, file, indent=4)
            for i in [k for k in n.keys()]:
                if i == str(ctx.author.id):
                    n.pop(i)
        #====================================================================
        #rep
        #====================================================================
        await ctx.send(embeds=interactions.Embed(
            title='Успешно',
            description=f'Предупреждение успешно выдано участнику {n[str(ctx.author.id)][1]}!',
            timestamp=ctx.message.created_at,
            color=COLOR
        ), ephemeral=True)
        #====================================================================
        #ls
        #====================================================================
        emb=discord.Embed(
            title='Нарушение',
            description=f'Вы получили нарушение на сервере ***{ctx.guild.name}***\nПричина: {shrt}',
            timestamp=ctx.message.created_at,
            color = COLOR
        )
        emb.add_field(name='Текущее кол-во нарушений', value=f'{warns}/{nWarns}', inline=True)
        emb.set_footer(text=f'Нарушение выдано {ctx.author.name}#{ctx.author.discriminator} ID модератора: {ctx.author.id}')
        memberr = [ i for i in ctx.guild.get_all_mambers() if str(i.id) == str(n[str(ctx.author.id)][0])][0]
        await memberr.send(embed=emb)                                                                               #найти юзера
        #====================================================================
        if data[str(ctx.guild_id)]['USERS'][str(n[str(ctx.author.id)][0])]['WARNS'] >= nWarns:
            await memberr.ban(reason='Вы привысили допустимое количество нарушений')                                 #найти юзера
        #====================================================================


def setup(bot):
    Score_interactions(bot)
    Warnsint(bot)