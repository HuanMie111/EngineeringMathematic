import numpy as np

while True:
    print("请输入系数矩阵：")
    print("示例：[[1.0,2,0],[3.0,4.0]]")
    A = np.array(eval(input()),dtype = np.float64)  # 系数矩阵 M
    D = np.linalg.det(A)  # M 行列式
    [m,n] = np.shape(A)
    x_next = 100*np.ones(n)  # 下一步解向量
    x_last = np.zeros(n)  # 上一步解向量
    if D == 0:
        print("系数矩阵不满秩，请重新输入")
        continue
    else:
        print("请输入右端项：")
        print("示例：[1.0,2.0]")
        b = np.array(eval(input()),dtype = np.float64)  # 右端项 b
        # 精度计算使用向量的 2-范数
        epsilon = eval(input("请输入精度（示例：0.0001）："))
        k = 0  # 迭代次数
        ActualError = epsilon+1  # 真实误差赋初值
        while ActualError > epsilon:
            for i in range(n):
                x_next[i] = x_last[i] + (-np.dot(x_last,A[i,:])+b[i])/A[i,i]
            ActualError = np.linalg.norm(x_next-x_last)
            x_last = x_next.copy()
            k = k+1
        print('解为：',x_next)
        print("迭代次数：",k)
