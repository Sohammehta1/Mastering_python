import random
from turtle import colormode

colormode(cmode=255)

def pickThreeColors(colors=None):
    rd = random.Random()
    if  colors is None or len(colors)==0:
        
        tp = []
        for i in range(3):
            tp.append(rd.randint(0,255))
        tp = tuple(tp)
        return tp
    else:
        return rd.choice(colors)


