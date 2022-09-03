from turtle import color, title
import interactions
import discord
from BD import bdpy, bdint 

BOTVERSION = '***ALPHA 1.0***'
ADMINS = ['466609421863354388', '758734389072625685', '840307986228707368']
IGNORE = ['error', 'btst', 'mafia', 'warns', 'ban', 'kick', 'mwarns']

def embpy(ctx, comp, des):
    try:
        if comp == 's':
            emb = discord.Embed(
                title='Успешно',
                description=des,
                color=bdpy(ctx)['COLOR']
            )
        elif comp == 'e':
            emb = interactions.Embed(
                title='Ошибка',
                description=des,
                color=bdint(ctx)['ErCOLOR']
            )
    except:
        pass
    return(emb)
def embint(ctx, comp, des):
    try:
        if comp == 's':
            emb = interactions.Embed(
                title='Успешно',
                description=des,
                color=bdint(ctx)['COLOR']
            )
        elif comp == 'e':
            emb = interactions.Embed(
                title='Ошибка',
                description=des,
                color=bdint(ctx)['ErCOLOR']
            )
    except:
        pass
    return(emb)