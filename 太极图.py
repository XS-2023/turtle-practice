from turtle import *
# import time


def tai(r, angle):
    home()  # 到画布中心
    setheading(angle)  # 设置当前朝向为angle角度
    up()  # 拿起画笔
    fd(r)  # 前进r的距离
    down()  # 放下画笔
    right(90)  # 调整海龟角度
    # 画阳鱼
    color("black")  # 填充为黑色
    begin_fill()  # 开始填充
    circle(-r / 2, 180)
    circle(r / 2, 180)
    circle(r, 180)
    end_fill()  # 填充结束
    circle(r, 180)  # 画另一半
    # 画阴鱼眼
    up()
    setheading(angle)
    fd(r / 2)
    down()
    dot(r / 4, "white")  # dot()绘制具有特定大小和颜色的圆点
    # 画阳鱼眼
    up()
    fd(r)
    down()
    dot(r / 4, "black")
    up()


tai(200, 90)
for i in range(10000):  # 这里设置了1w次，也可以是其他次数
    tracer(0)  # 将刷新率置为0，即不刷新
    clear()  # 清空画布
    tai(200, i)
    # time.sleep(0.01)  # 休眠时间，这一句可以没有，但是如果没有······
    update()  # 更新绘图
done()
