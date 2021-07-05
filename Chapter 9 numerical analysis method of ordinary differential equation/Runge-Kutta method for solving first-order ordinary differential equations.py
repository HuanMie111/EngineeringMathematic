import numpy as np
import matplotlib.pyplot as plt

# 返回初值问题的f(x,y)值
def f(x,y,str_f):
    return eval(str_f)

while True:
    print("请输入初值问题的f(x,y)：")
    print("示例：1.0/(3*x+y**2)")
    str_f = input()
    print("请输入求解区间：")
    print("示例：[1.0,2.0]")
    [a,b] =[float(x) for x in eval(input())]
    print("请输入初值f(a) = :")
    print("示例：1.0")
    y_0 = float(eval(input()))
    print("请输入节点个数（包含区间端点）:")
    print("示例：11")
    N = int(eval(input()))-1
    
    # str_f = "y-2*x/y"
    # [a,b] =[0.0,1.0]
    # y_0 = 1.0
    # N = 10
    
    h = (b-a)/N  # h 为步长
    k = np.zeros((4,N))
    x = np.linspace(a,b,N+1)
    y = np.zeros(N+1)
    y[0] = y_0
    
    for i in range(N):
        k[0,i] = f(x[i],y[i],str_f)
        k[1,i] = f(x[i]+h/2,y[i]+h/2*k[0,i],str_f)
        k[2,i] = f(x[i]+h/2,y[i]+h/2*k[1,i],str_f)
        k[3,i] = f(x[i]+h,y[i]+h*k[2,i],str_f)
        y[i+1] = y[i] + h/6*(k[0,i]+2*k[1,i]+2*k[2,i]+k[3,i])
    
    SolutionResult = np.c_[x,y]
    
    plt.plot(x,y,marker='.')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('偏微分方程积分曲线',fontproperties = 'SimHei',fontsize = 15)
    plt.show()
