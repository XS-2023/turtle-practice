import turtle

# 创建画布和海龟
window = turtle.Screen()
window.bgcolor("white")
t = turtle.Turtle()

# 设置笔的速度
t.speed(0)

# 绘制彩色螺旋线
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(360):
    t.color(colors[i % 6])  # 切换颜色
    t.forward(i)  # 向前移动
    t.left(59)  # 左转59度

# 隐藏海龟并完成绘图
t.hideturtle()
window.mainloop()