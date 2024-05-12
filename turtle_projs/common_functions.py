import random
from turtle import colormode

colormode(cmode=255)

hirst_colors = [(235, 228, 211), (217, 218, 223), (104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32), (225, 212, 109), (199, 147, 173), (237, 215, 225), (105, 112, 170), (177, 159, 47), (218, 224, 219), (186, 19, 9), (38, 40, 21), (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132), (190, 187, 218), (230, 176, 172), (231, 65, 82)]
def pickThreeColors(colors=None,Hirst=True):
    rd = random.Random()
    if Hirst == True:
        return rd.choice(hirst_colors)
    
    if  colors is None or len(colors)==0:
        
        tp = []
        for i in range(3):
            tp.append(rd.randint(0,255))
        tp = tuple(tp)
        return tp
    else:
        return rd.choice(colors)



