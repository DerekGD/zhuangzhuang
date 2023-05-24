##打印长方形
import turtle
turtle.setup(900,800,20,20)##设置画布的大小，起始点的位置
turtle.penup()##画笔抬起
turtle.fd(-10)##向前走
turtle.pendown()##画笔落下
turtle.pensize(25)##设置画笔的粗细
turtle.pencolor("yellow")##设置画笔的颜色
turtle.seth(-90)##设置画笔的角度
turtle.fd(400)##向前走
turtle.seth(0)##设置画笔的角度
turtle.fd(500)##向前走
turtle.seth(90)##设置画笔的角度
turtle.fd(400)##向前走
turtle.seth(180)##设置画笔的角度
turtle.fd(300)##向前走
turtle.done()##画笔结束