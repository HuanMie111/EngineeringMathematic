import numpy as np

def Judge_TridiagonalMatrix(A):
    [m,n] = np.shape(A)
    s = 0  # 条件判断计数器
    if m != n:
        print("判断矩阵不是方阵")
    else:
        for i in range(2,n):
            A_Diagonal = np.diagonal(A, offset=i)  # 取右上元素
            if np.all(A_Diagonal == 0):
                s = s+1
        for i in range(2,n):
            A_Diagonal = np.diagonal(A, offset=-i)  # 取左下元素
            if np.all(A_Diagonal == 0):
                s = s+1
        if s == 2*n-4:
            return True
        else:
            return False
        
def Judge_Mastersub(A):
    [m,n] = np.shape(A)
    s = 0  # 条件判断计数器
    if m != n:
        print("判断矩阵不是方阵")
    else:
        for i in range(n):
            A_mastersub = A[:i+1,:i+1]
            if np.linalg.det(A_mastersub) != 0:
                s = s+1
        if s == n:
            return True
        else:
            return False
    
while True:
    print("请输入系数矩阵：")
    print("示例：[[1.0,2,0],[3.0,4.0]]")
    A = np.array(eval(input()),dtype = np.float64)  # 系数矩阵 A
    D = np.linalg.det(A)  # A 行列式
    print("请输入右端项：")
    print("示例：[1.0,2.0]")
    b = np.array(eval(input()),dtype = np.float64)  # 右端项 b
    if Judge_TridiagonalMatrix(A):  # 判断是否为三对角矩阵
        if Judge_Mastersub(A):  # 判断各阶顺序主子式是否均不为0
            [m,n] = np.shape(A)
            x = np.zeros(n)
            a = np.diagonal(A)
            c = np.diagonal(A,offset = 1)
            d = np.diagonal(A,offset = -1)
            u = a.copy()  # 注意使用 copy()
            l = np.zeros(n)
            y = b.copy()
            for i in range(1,n):
                l[i] = d[i-1]/u[i-1]
                u[i] = a[i] - l[i]*c[i-1]
            for i in range(1,n):
                y[i] = b[i] - l[i]*y[i-1]  # 追
            x[n-1] = y[n-1]/u[n-1]
            for i in range(n-1):
                i = n-i-2
                x[i] = (y[i]-c[i]*x[i+1])/u[i]  # 赶
            print('解为：',x)
        else:
            print("系数矩阵不能三角分解")
    else:
        print("系数矩阵不是三对角矩阵")
