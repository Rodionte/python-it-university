
#1
def Max_max(arr): 
    max1 = arr[0]
    for ele in arr:
        if ele > max1:
           max1 = ele
    return max1

list1 = ["Виктор", "Артем", "Роман"]
list2 = [16, 78, 32, 67]
list3 = ["яблоко", "манго", 16, "вишня", 3.4]
#max 
max_number = max(list2)
print("Наибольшее число:", max_number)

#порядочиваются в алфавитном порядке
max_string = max(list1, key=len)
print("Самая длинная строка:", max_string)

#перебор через def
result = Max_max(list2)
print(result)


#2 - Запрос данных от пользователя 

txt = input("Введите что-нибудь, чтобы проверить это: ")
print ("Вы ввели: ",txt)

#только число
number = int(input("Введите число: "))
print ("Вы ввели число:", number)

#Проверка правильности ввода 

test3 = input("Введите число: ")
try:
    test33 = int(test3)
    print("Это правильный ввод! Ваше  число: ", test33)
except ValueError:
    print("Это не правильный ввод. Это не число ! Это строка, попробуйте еще раз.")