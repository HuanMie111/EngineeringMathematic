import numpy as np

while True:
    print("请输入系数矩阵：")
    print("示例：[[1.0,2,0],[3.0,4.0]]")
    A = np.array(eval(input()),dtype = np.float64)  # 系数矩阵 A
    D = np.linalg.det(A)  # A 行列式
    print("请输入右端项：")
    print("示例：[1.0,2.0]")
    b = np.array(eval(input()),dtype = np.float64)  # 右端项 b
    A_b = np.c_[A,b]
    [m,n] = np.shape(A_b)
    x = np.zeros(n-1)
    if D != 0:
        for k in range(m-1):
            l = np.zeros(m)
            for i in range(k+1,m):                       
                l[i] = A_b[i,k]/A_b[k,k]
                A_b[i,:] = A_b[i,:]-l[i]*A_b[k,:]
        for k in range(n-1):
            k = n-k-2
            s = 0  # s 为每行 a_ki*x_i 的和
            for i in range(n-1):
                s = s+A_b[k,i]*x[i]
            x[k] = (A_b[k,-1] - s)/A_b[k,k]
        print('解为：',x)
    else:
        print("系数矩阵行列式为零，无解或解不唯一")                          
                
                
        
        
