import turtle as t
import random

t.setup(1.0, 1.0)
t.bgcolor('black')
t.ht()
# 金庸小说人物
persons = '''阿青—阿珂—阿紫—慕容复—乔峰—王语嫣—段誉—虚竹—天山童姥—李秋水—扫地僧—鸠摩智
—游坦之—丁春秋—包不同—风波恶—邓百川—公冶乾—康敏—钟灵—木婉清—王夫人—玄慈—玄苦—玄难—慕容博—
萧远山—游氏双雄—宋远桥—俞岱岩—张翠山—宋青书—莫声谷—周芷若—小昭—殷离—殷天正—白眉鹰王—杨逍
—范遥—成昆—胡青牛—金花婆婆—谢逊—阳顶天—冷谦—灭绝师太—公孙绿萼—完颜萍—耶律燕—郭芙—周伯通
—孤鸿子—纪晓芙—韦一笑—五散人—胡斐—程灵素—袁紫衣—南兰—马春花—商宝震—田归农—苗人凤—程英
—胡一刀—平阿四—一灯大师—洪七公—王重阳—石破天—阿秀—汤沛—戚长发—万震山—言达平—戚芳—水笙—狄云
—丁典—血刀老祖—刘乘风—鲁大师—任我行—向问天—令狐冲—岳不群—宁中则—林平之—余沧海—柯镇恶
—定闲师太—蓝凤凰—岳灵珊—仪琳—仪清—仪和—平一指—桃谷六仙—不戒和尚—田伯光—莫大先生
—刘正风—曲洋—任盈盈—向大年—祖千秋—丹青生—黄药师—欧阳锋—洪七公—黄蓉—郭靖—杨过—郭襄
—小龙女—李莫愁—公孙止—裘千仞—裘千尺—金轮法王—尼摩星—潇湘子—尹克西—穆念慈'''

persons = persons.replace('\n', '')
words = persons.split('—')
print(words)

# 小说人物类
class Xiaoshuo():
    def __init__(self):
        self.x = random.randint(-1000, 1000)  # 横坐标
        self.y = random.randint(-500, 500)    # 纵坐标
        self.f = random.uniform(-10, 10)   # 左右移动
        self.speed = random.randint(2, 6)  # 移动速度
        self.word = random.choice(words)  # 文字
        # 文字的颜色
        self.color = "#%02x%02x%02x" % (random.randint(0, 255),
                    random.randint(0, 255), random.randint(0, 255))

    # 1.写字
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.color(self.color)
        t.write(self.word, font=('楷体', 24))

    # 2.xy坐标变化，实现文字的移动
    def move(self):
        # 当文字还在画布中时
        if self.y <= 500:
            self.y += self.speed  # 设置上下移动,y逐渐增加
            self.x -= self.speed + self.f  # 左右移动速度
        # 当文字漂出了画布时，重新生成文字
        else:
            self.x = random.randint(-1000, 1000)
            self.y = -500
            self.f = random.uniform(-10, 10)  # 左右移动
            self.speed = random.randint(2, 6)  # 移动速度
            self.word = random.choice(words)  # 文字
            # 文字的颜色
            self.color = "#%02x%02x%02x" % (random.randint(0, 255),
                                            random.randint(0, 255), random.randint(0, 255))

# 用列表保存对象
xiaoshuos = []
for i in range(180):
    xiaoshuos.append(Xiaoshuo())

# 开始写字+移动
while True:
    t.tracer(0)
    t.clear()
    for i in range(150):
        xiaoshuos[i].move()
        xiaoshuos[i].draw()
    t.update()

t.done()
