import numpy as np
import matplotlib.pyplot as plt

while True:
    print("请输入插值节点：")
    print("示例：[1.0,2,0,3.0]")
    x = np.array(eval(input()),dtype = np.float64)  # 总插值节点 x
    print("请输入插值节点对应的函数值：")
    print("示例：[4.0,5.0,6.0]")
    y = np.array(eval(input()),dtype = np.float64)  # 总插值节点 x 对应的函数值
    print("请输入插值点：")
    print("示例：2.1")
    x_inter = float(eval(input())) # 插值点 x_inter
    print("请输入插值次数：")
    print("示例：2")
    n = int(eval(input()))  # 插值次数 n
    m = np.shape(x)[0]
    if n > m-1:
        print("节点数与插值次数不匹配，请重新输入")
        continue
    else:
        index = np.argsort(np.fabs(x-x_inter))[:n+1]  # 选取最接近插值点的 n+1 个点
        x_close = x[index]
        index_up = x_close.argsort()
        x_close.sort()  # 再将最近的插值节点升序排列，不能赋值
        y_close = y[index][index_up] 
        l_x_inter = 0  # 插值结果
        for k in range(n+1):
            mid = (x_inter-x_close)/(x_close[k]-x_close)
            l_x_inter = l_x_inter+mid[:k].prod()*mid[k+1:].prod()*y_close[k]
    print("插值结果为：",l_x_inter)
    
    plt.plot(x_close,y_close)
    plt.scatter(x_inter,l_x_inter,s = 10,color = "r")  # scatter 绘制一个点，s 设置点的大小
    
    plt.xlabel('x')
    plt.title('拉格朗日插值图',fontproperties = 'SimHei',fontsize = 15)
    plt.show()
