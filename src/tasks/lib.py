def task1():
    sstr = 225.0
    atk = sstr * 1.5
    sdef = 120.0
    dmg = sstr - sdef
    print(dmg)

def task2():
    for i in range(10):
        for j in range(10 - i):
            print('*', end = '')
        print()

def task3():
    a = int(input("请输入长方形的长："))
    b = int(input("请输入长方形的宽："))
    print("长方形的面积是：", a * b)

def task4():
    x = int(input("请输入一个整数："))
    while x:
        n = x % 10;
        print(n)
        x = x // 10;

def task5():
    x = float(input("请输入长度（尺子）："))
    y = x * 0.333333
    print("转换长度（尺->米）：", y)