import turtle as t
import math

class funcGraph:
    def __init__(self, wt = "函数图", bgColor = "green", gpSize = 1, gpColor = "black", apSize = 3, apColor = "red", mpSize = 3, mpColor = "red", xAxisMag = 10):
        """
        初始化函数图类
        wt(window title): 窗口标题
        bgColor(background color): 背景颜色
        gpSize(grid pen size): 网格线大小
        gpColor(grid pen color): 网格线颜色
        apSize(axis pen size): 坐标轴大小
        apColor(axis pen color): 坐标轴颜色
        mpSize(map pen size): 映射线大小
        mpColor(map pen color): 映射线颜色
        xAxisMag(x-axis magnification): x轴放大倍数
        """
        self.P = t.Turtle()
        self.P._delay(0)
        self.P.speed(0)
        self.scr = t.Screen()
        self.scr.title(wt)
        self.scr.bgcolor(bgColor)
        self.gpSize = gpSize
        self.gpColor = gpColor
        self.apSize = apSize
        self.apColor = apColor
        self.mpSize = mpSize
        self.mpColor = mpColor
        self.xAxisMag = xAxisMag
    
    def set(self, wt = "函数图", bgColor = "green", gpSize = 1, gpColor = "black", apSize = 3, apColor = "red", mpSize = 3, mpColor = "red", xAxisMag = 10):
        """
        设置函数图类参数
        wt(window title): 窗口标题
        bgColor(background color): 背景颜色
        gpSize(grid pen size): 网格线大小
        gpColor(grid pen color): 网格线颜色
        apSize(axis pen size): 坐标轴大小
        apColor(axis pen color): 坐标轴颜色
        mpSize(map pen size): 映射线大小
        mpColor(map pen color): 映射线颜色
        xAxisMag(x-axis magnification): x轴放大倍数
        """
        self.scr.title(wt)
        self.scr.bgcolor(bgColor)
        self.gpSize = gpSize
        self.gpColor = gpColor
        self.apSize = apSize
        self.apColor = apColor
        self.mpSize = mpSize
        self.mpColor = mpColor
        self.xAxisMag = xAxisMag
    
    def draw_grid(self):
        """绘制网格线"""
        self.P.pensize(self.gpSize)
        self.P.color(self.gpColor)
        cnt = -1
        for i in range(-800, 801, 10):
            self.P.up()
            self.P.goto((i, -800))
            self.P.down()
            self.P.goto((i, 800))
            cnt += 1
            print(f"\rProgress: {int(cnt / 3.2)}% [{"=" * int(cnt / 3.2)}{" " * (100 - int(cnt / 3.2))}]", end="")
        for i in range(-800, 801, 10):
            self.P.up()
            self.P.goto((-800, i))
            self.P.down()
            self.P.goto((800, i))
            print(f"\rProgress: {int(cnt / 3.2)}% [{"=" * int(cnt / 3.2)}{">" if int(cnt / 3.2)!=100 else ""}{" " * (100 - int(cnt / 3.2) - 1)}]", end="")
            cnt += 1
        print()
    
    def draw_axis(self):
        """绘制坐标轴"""
        self.P.pensize(self.apSize)
        self.P.color(self.apColor)
        self.P.up()
        self.P.goto((-800,0))
        self.P.down()
        self.P.goto((800,0))
        self.P.up()
        self.P.goto((0,800))
        self.P.down()
        self.P.goto((0,-800))
        self.P.goto((0, 0))
    
    def clear(self):
        """清除画布"""
        self.P.clear()
    
    def draw(self, func:str):
        """
        绘制函数图
        func(function): 要绘制的函数字符串表达式
        如：
        math.pow(x, 2)
        x + 3
        1 - (math.pow((1 - x), 2))
        """
        self.P.up()
        self.P.pensize(self.mpSize)
        self.P.color(self.mpColor)
        for x in range(-50, 51):
            y = eval(func)
            print(f"x:{x}, y:{y}",end="\r")
            self.P.goto((x * self.xAxisMag, y))
            self.P.down()
        print("\nDone!")
    
    def mainloop(self):
        """进入消息循环"""
        self.scr.exitonclick()

if __name__ == "__main__" :
    app = funcGraph(apSize=5, mpSize=5)
    app.draw_grid()
    app.draw_axis()
    app.draw("x ** 2")
    app.mainloop()
