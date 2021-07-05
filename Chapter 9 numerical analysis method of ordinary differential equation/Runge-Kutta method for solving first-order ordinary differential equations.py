# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:42:24 2021

@author: girlfriend
"""

import numpy as np
import matplotlib.pyplot as plt

# 返回初值问题的f(x,y)值
def f(x,y,z,str_f):
    return eval(str_f)

while True:
    print("请输入初值问题第一个方程的 f(x,y,z)：")
    print("示例：1.0/(3*x+y**2)+2*z")
    str_f = input()
    print("请输入初值 y(a) = :")
    print("示例：1.0")
    y_0 = float(eval(input()))
    print("请输入初值问题第二个方程的 g(x,y,z)：")
    print("示例：1.0/(3*x+y**2)+2*z")
    str_g = input()
    print("请输入初值 z(a) = :")
    print("示例：1.0")
    z_0 = float(eval(input()))
    print("请输入求解区间：")
    print("示例：[1.0,2.0]")
    [a,b] =[float(x) for x in eval(input())]
    print("请输入节点个数（包含区间端点）:")
    print("示例：11")
    N = int(eval(input()))-1
    
    # str_f = "-8*y+7*z"
    # str_g = "x**2+y*z"
    # [a,b] =[0.0,1.0]
    # y_0 = 1.0
    # z_0 = 0
    # N = 10
    
    h = (b-a)/N  # h 为步长
    k = np.zeros((4,N))
    l = np.zeros((4,N))
    x = np.linspace(a,b,N+1)
    y = np.zeros(N+1)
    y[0] = y_0
    z = np.zeros(N+1)
    z[0] = z_0   
    
    for i in range(N):
        k[0,i] = f(x[i],y[i],z[i],str_f)
        l[0,i] = f(x[i],y[i],z[i],str_g)       
        k[1,i] = f(x[i]+h/2,y[i]+h/2*k[0,i],z[i]+h/2*l[0,i],str_f)
        l[1,i] = f(x[i]+h/2,y[i]+h/2*k[0,i],z[i]+h/2*l[0,i],str_g)
        k[2,i] = f(x[i]+h/2,y[i]+h/2*k[1,i],z[i]+h/2*l[1,i],str_f)
        l[2,i] = f(x[i]+h/2,y[i]+h/2*k[1,i],z[i]+h/2*l[1,i],str_g)
        k[3,i] = f(x[i]+h,y[i]+h*k[2,i],z[i]+h*l[2,i],str_f)
        l[3,i] = f(x[i]+h,y[i]+h*k[2,i],z[i]+h*l[2,i],str_g)
        y[i+1] = y[i] + h/6*(k[0,i]+2*k[1,i]+2*k[2,i]+k[3,i])
        z[i+1] = z[i] + h/6*(l[0,i]+2*l[1,i]+2*l[2,i]+l[3,i])
    SolutionResult = np.c_[x,y,z]
    
    plt.plot(x,y,marker = "o",label = "y")
    plt.plot(x,z,marker = ".",label = "z")
    
    plt.legend(loc = 'best')
    plt.xlabel('x')
    plt.title('偏微分方程组积分曲线',fontproperties = 'SimHei',fontsize = 15)
    plt.show()