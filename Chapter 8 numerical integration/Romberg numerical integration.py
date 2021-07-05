import numpy as np

# 定义被积函数
def f(x):
    if x != 0:
        f = np.sin(x)/x
    else:
        f = 1
    return f

while True:
    
    print("被积函数需在代码内修改")
    print("请输入积分区间：")
    print("示例：[1.0,2.0]")
    [a,b] = eval(input())  # 积分区间
    a = float(a)
    b = float(b)
    print("请输入精度：")
    print("示例：0.0001")
    epsilon = eval(input())
    Table = np.zeros((5,4))  # Romberg 算法表
    Table[0,0] = (b-a)/2*(f(a)+f(b))
    Table[1,0] = 0.5*Table[0,0]+(b-a)/2*f((b+a)/2)
    for i in range(2,5):
        mid = np.linspace(a,b,2**i+1)[1::2]
        mid = np.array([f(x) for x in mid]).sum()
        Table[i,0] = 0.5*Table[i-1,0]+ (b-a)/(2*2**(i-1))*mid
    for j in range(1,4):
        for i in range(j,5):
            Table[i,j] = (4**j*Table[i,j-1]-Table[i-1,j-1])/(4**j-1)
    if Table[4,3] - Table[3,3] < epsilon:
        print("数值积分值为：",Table[4,3])
            
        
        
