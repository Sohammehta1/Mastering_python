import random
from turtle import colormode

def pickThreeColors():
    rd = random.Random()
    tp = []
    for i in range(3):
        tp.append(rd.randint(0,255))
    tp = tuple(tp)
    return tp
colormode(cmode=255)