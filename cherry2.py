# coding=utf-8
# 画一棵樱花

import turtle
import random
from turtle import *
from time import sleep


# 画樱花的躯干(60,t)
def tree(branchLen, t):
    sleep(0.0005)
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branchLen / 3)
        elif branchLen < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branchLen / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branchLen / 10)  # 6
        t.forward(branchLen)    # 向前绘制枝干
        a = 1.5 * random.random()
        t.right(20 * a)     # 向右转动一个随机角度
        b = 1.5 * random.random()
        tree(branchLen - 10 * b, t)     # 递归地绘制左子枝干
        t.left(40 * a)
        tree(branchLen - 10 * b, t)     # 递归地绘制右子枝干
        t.right(20 * a)
        t.up()
        t.backward(branchLen)
        t.down()        # 抬起画笔，后退到枝干起点，放下画笔


# 掉落的花瓣
def petal(m, t):
    for i in range(m):
        # 生成随机的位置和角度
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()    # 移动到花瓣的位置
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)     # 绘制花瓣
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)   # 回到起始位置


def main():
    # 绘图区域
    t = turtle.Turtle()
    # 画布大小
    w = turtle.Screen()
    t.hideturtle()  # 隐藏画笔
    getscreen().tracer(5, 0)    # 设置绘图速度
    w.screensize(bg='wheat')  # wheat小麦
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    # 设置画笔的初始位置和颜色

    # 画樱花的躯干
    tree(60, t)
    # 掉落的花瓣
    petal(200, t)
    w.exitonclick()


main()
