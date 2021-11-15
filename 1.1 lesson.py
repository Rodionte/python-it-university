# Заменить все буквы x на y
a = "qwewedszczxczxcvnfgytywtewzxxxxx"
a1 = ""
for x in a:
    if x == "x":
        a1 += "y"
    else:
        a1 += x
print('Исходная: ' + a )
print('Новая: ' + a1)

#Сосчитать произведение чисел, кратных 3 и 5

b = [1,2,3,4,5,6,5,4,2,3,155,6,7]
b1 = 1 
for x in b:
    if x // 5 == x / 5 or x // 3 == x / 3:
        b1 *= x
print('Произведение: ',  b1)

#Заменить все буквы X на y в исходной строчке без использования дополнительной 
a = 'qwewedszczxczxcvnfgytywtewzxxxxx'.replace('x', 'y')
print('Измененная строчка: ' + a)