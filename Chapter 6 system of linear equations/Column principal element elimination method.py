# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:50:36 2020

@author: girlfriend
"""

import numpy as np

while True:
    print("请输入系数矩阵：")
    print("示例：[[1.0,2,0],[3.0,4.0]]")
    A = np.array(eval(input()),dtype = np.float64)  # 系数矩阵 A
    D = np.linalg.det(A)  # A 行列式
    print("请输入右端项：")
    print("示例：[1.0,2.0]")
    b = np.array(eval(input()),dtype = np.float64)  # 右端项 b
    A_b = np.c_[A,b]  # 和并 A 和 b
    [m,n] = np.shape(A_b)
    x = np.zeros(n-1)
    if D != 0:
        for k in range(m-1):
            l = np.zeros(m)
            A_b_k = np.fabs(A_b[:,k])  # 主元素所在列取绝对值
            # 找到绝对值最大的元素位置,返回一个元素为 array 类型的元组
            index_a_max = np.where(A_b_k == np.max(A_b_k[k:]))
            index_a_max = index_a_max[0][0]  # 将单元素元组转化为 int
            A_b[[k,index_a_max]] = A_b[[index_a_max,k]]  # 交换行 
            for i in range(k+1,m):                                 
                l[i] = A_b[i,k]/A_b[k,k]
                A_b[i,:] = A_b[i,:]-l[i]*A_b[k,:]  # 消去
        for k in range(n-1):
            k = n-k-2
            s = np.dot(A_b[k,:n-1],x)  # 求 simga(a_ki*x_i)
            x[k] = (A_b[k,-1] - s)/A_b[k,k]
        print('解为：',x)
    else:
        print("系数矩阵行列式为零，无解或解不唯一")              
                
                
        
        