# python程序设计第一周学生作业

**土木工程-24-李芊墨-24190030224**

## 使用指南

### 运行*task1:* 

$`poetry run task1`

```python
sstr = 225.0

atk = sstr * 1.5

sdef = 120.0

dmg = sstr - sdef

print(dmg)
```



### 运行*task2*: 

$`poetry run task2`

```python
for i in range(10):

    for j in range(10 - i):

        print('*', *end* = '')

    print()
```



### 运行*task3*: 

$`poetry run task3`

```python
a = int(input("请输入长方形的长："))

b = int(input("请输入长方形的宽："))

print("长方形的面积是：", a * b)
```



### 运行*task4*: 

$`poetry run task4`

```python
x = int(input("请输入一个整数："))

while x:

    n = x % 10;

    print(n)

    x = x // 10;
```



### 运行*task5*: 

$`poetry run task5`

```python
x = float(input("请输入长度（尺子）："))

y = x * 0.333333

print("转换长度（尺->米）：", y)
```

