import discord
from random import *
from discord.ext import commands
from typing import Optional

from setuptools import Command

lang_num = [0, 1, 2]
lang_emo = []


def cheack(body, player: int):
        for i in range(0, len(body), 3):
            if body[i] == body[i+1] and body[i] == body[i+2] and body[i]:
                print(f'Win {player} 1')
                return ...
        
        for ii in range(3):
            if len(set([body[i] for i in range(ii, len(body), 3)])) == 1 and set([body[i] for i in range(ii, len(body), 3)]) != {0}:
                print(f'Win {player} 2')
                return ...

        if len(set([body[i] for i in range(0, len(body), 4)])) == 1 and set([body[i] for i in range(0, len(body), 4)]) != {0}:
            print(f'Win {player} 3')
            return ...
        
        if len(set([body[i] for i in range(2, len(body), 2)][:3])) == 1 and set([body[i] for i in range(2, len(body), 2)][:3]) != {0}:
            print(f'Win {player} 4')
            return ...
        
        if not 0 in body:
            print('ничья')
            return ...

#====================================================================

def play(body, player: int):
    inp = int(input()) - 1
    if inp == 0:
        body[inp] = player
    elif inp == 1:
        body[inp] = player
    elif inp == 2:
        body[inp] = player
    elif inp == 3:
        body[inp] = player
    elif inp == 4:
        body[inp] = player
    elif inp == 5:
        body[inp] = player
    elif inp == 6:
        body[inp] = player
    elif inp == 7:
        body[inp] = player
    elif inp == 8:
        body[inp] = player
    cheack(player)

#====================================================================

def autoplay_start(body):
    if body[4]:
        body[choice([0, 2, 6, 8])] = 2
    else:
        body[4] = 2

#====================================================================

def autoplay(body):
    n=True

    for i in range(0, len(body), 3):
        if body[i:i+3].count(0) == 1 and len(set(body[i:i+3])) == 2 and 2 in body[i:i+3] and n:
            lsd = [k for k in range(len(body[i:i+3])) if body[i:i+3][k] == 0]
            body[lsd[0]+i] = 2
            n=0

    for i in range(0, len(body), 3):
        if body[i:i+3].count(0) == 1 and len(set(body[i:i+3])) == 2 and 0 in body[i:i+3] and n:
            lsd = [k for k in range(len(body[i:i+3])) if body[i:i+3][k] == 0]
            body[lsd[0]+i] = 2
            n=0


    for ii in range(3):
        lsd = [body[i] for i in range(ii, len(body), 3)]
        if lsd.count(0) == 1 and len(set(lsd)) == 2 and 2 in lsd and n:
            zerind = [i for i in range(ii, len(body), 3) if body[i] == 0]
            body[zerind[0]] = 2
            n=0

    for ii in range(3):
        lsd = [body[i] for i in range(ii, len(body), 3)]
        if lsd.count(0) == 1 and len(set(lsd)) == 2 and 0 in lsd and n:
            zerind = [i for i in range(ii, len(body), 3) if body[i] == 0]
            body[zerind[0]] = 2
            n=0
    

    lsd = [body[i] for i in range(0, len(body), 4)]
    if n and lsd.count(0) == 1 and len(set(lsd)) == 2 and 2 in lsd:
        body[lsd.index(0)*4] = 2
        n = 0

    lsd = [body[i] for i in range(0, len(body), 4)]
    if n and lsd.count(0) == 1 and len(set(lsd)) == 2:
        body[lsd.index(0)*4] = 2
        n = 0
    

    lsd = [body[i] for i in range(2, len(body), 2)][:3]
    if n and lsd.count(0) == 1 and len(set(lsd)) == 2 and 2 in lsd:
        body[lsd.index(0)*2+2] = 2
        n = 0

    lsd = [body[i] for i in range(2, len(body), 2)][:3]
    if n and lsd.count(0) == 1 and len(set(lsd)) == 2:
        body[lsd.index(0)*2+2] = 2
        n = 0
    
    if n and 0 in body:
        if body[4] == 2:
            if body.count(0) == 6:
                body_pod_lsd = []; body_pod_lsd.extend(body); body_pod_lsd.reverse()
                lsd = [i for i in range(1, len(body), 2) if body[i] == 0 and body[i] == body_pod_lsd[i]]
                if 1 in [body[0], body[2], body[4], body[6]] and lsd:
                    body[lsd[0]] = 2
                else:
                    body_pod_lsd = []; body_pod_lsd.extend(body); body_pod_lsd.reverse()
                    lsd = [i for i in range(0, len(body), 2) if body[i] == 0 and body[i] == body_pod_lsd[i] and ((not(body[i+1]) or (not(body[i+3])) if i < 2 else False) or (not(body[i-1]) or (not(body[i+3])) if i < 5 and i > 2 else False) or (not(body[i+1]) or not(body[i-3]) if i > 5 and i < 7 else False) or (not(body[i-1]) or not(body[i-3]) if i > 7 else False))]
                    if lsd:
                        body[lsd[-1]] = 2
                    else:
                        body[body.index(0)] = 2
            else:
                body_pod_lsd = []; body_pod_lsd.extend(body); body_pod_lsd.reverse()
                lsd = [i for i in range(0, len(body), 2) if body[i] == 0 and body[i] == body_pod_lsd[i] and ((not(body[i+1]) or (not(body[i+3])) if i < 2 else False) or (not(body[i-1]) or (not(body[i+3])) if i < 5 and i > 2 else False) or (not(body[i+1]) or not(body[i-3]) if i > 5 and i < 7 else False) or (not(body[i-1]) or not(body[i-3]) if i > 7 else False))]
                if lsd:
                    body[lsd[-1]] = 2
                else:
                    body[body.index(0)] = 2
            n = 0
        else:
            body_pod_lsd = []; body_pod_lsd.extend(body); body_pod_lsd.reverse()
            lsd = [i for i in range(0, len(body), 2) if body[i] == 0 and body[i] == body_pod_lsd[i] and ((not(body[i+1]) or (not(body[i+3])) if i < 2 else False) or (not(body[i-1]) or (not(body[i+3])) if i < 5 and i > 2 else False) or (not(body[i+1]) or not(body[i-3]) if i > 5 and i < 7 else False) or (not(body[i-1]) or not(body[i-3]) if i > 7 else False))]
            if 1 in [body[0], body[2], body[4], body[6]] and lsd:
                body[lsd[0]] = 2
            else:
                body[body.index(0)] = 2
    
    cheack(2)

#====================================================================
#Визуалы
#====================================================================


# if input() == '0':
#     print(body[6:9], body[3:6], body[0:3], sep='\n')
#     while 1:
#         play(1)
#         print(body[6:9], body[3:6], body[0:3], sep='\n')

#         play(2)
#         print(body[6:9], body[3:6], body[0:3], sep='\n')
# else:
#     print(body[6:9], body[3:6], body[0:3], sep='\n')
#     play(1)

#     autoplay_start()
#     print(body[6:9], body[3:6], body[0:3], sep='\n')

#     while 1:
#         play(1)

#         autoplay()
#         print(body[6:9], body[3:6], body[0:3], sep='\n')



class Dicepy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def xo(self, ctx: commands.Context, user: Optional[discord.Member]):
    
    body = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if user in ctx.guild.members:
        pass