import numpy as np

#1
x = np.array(range(100))
print(x.sum())

#2
a = int(input("Введите число для подсчета суммы ряда: "))
x = np.arange(0,a+1)
print(x.sum())

#3
z = np.random.random(100)
print("Среднее среди 100 случайных чисел равно", z.mean())