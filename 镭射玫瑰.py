"""
在计算机中，颜色可以通过多种模式来表示，其中RGB模式是最常用的一种。
RGB模式通过红色（Red）、绿色（Green）、蓝色（Blue）三个分量来合成各种颜色。
每个分量的取值范围通常是0到255之间的整数，这个范围代表了该颜色分量的强度或亮度。
"""
from turtle import *
from random import *
speed("fastest")


def dw():
    bgcolor('black')
    x = 1
    while x < 400:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)    # 设置颜色模式为255，这意味着颜色值将在0到255的范围内。
        pencolor(r, g, b)
        fd(50 + x)
        rt(90.911)
        # rt(90)
        x += 1
    exitonclick()

dw()
