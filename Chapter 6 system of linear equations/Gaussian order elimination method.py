import numpy as np

while True:
    print("请输入系数矩阵：")
    print("示例：[[1.0,2,0],[3.0,4.0]]")
    M = np.array(eval(input()),dtype = np.float64)  # 系数矩阵 M
    D = np.linalg.det(M)  # M 行列式
    D_i = []  # 替换后的矩阵 D_i
    x = []  # 解 x_i
    [m,n] = np.shape(M) 
    if D == 0:
        print("系数矩阵不满秩，请重新输入")
        continue
    else:
        print("请输入右端项：")
        print("示例：[1.0,2.0]")
        b = np.array(eval(input()),dtype = np.float64)  # 右端项 b
        for i in range(n):
            M_i = M.copy()
            M_i[:,i] = b  
            D_i.append(np.linalg.det(M_i))
            x.append(D_i[i]/D)
        print('解为：',x)
        
        
        
