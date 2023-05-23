#打印一个圆
# library
import matplotlib.pyplot as plt


# ----- 步骤一
 
# create data
# 创建数据
size_of_groups=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
 
# Create a pieplot
# 创建饼图
plt.pie(size_of_groups)
#plt.show()
 
# ----- 步骤二

# add a circle at the center
# 添加一个圆
my_circle=plt.Circle( (0,0), 0.7, color='white')
# 获得当前显示的图表，也就是前面画的饼图
p=plt.gcf()
# 将两图相加
p.gca().add_artist(my_circle)

 
# 设置等比例轴，x和y轴等比例
plt.axis('equal') 
plt.show();
