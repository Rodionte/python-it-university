#Словарь визуальнее более понятет в отличии от списка.
#Список сложно понять без другого списка, где будет описание столбцов.
#Словарь утобно можно сворачивать по ФИО напирмер. 

#Словарь 
group = {
    ('Терёхин', 'Родион', 'Павлович'):
        {'Род.': 1996,
         'Город': 'Пермь',
         'Улица': 'Кав',
         'дом': '22',
         'кв': '24'
        }
}
#Cписок
group1 = [
    ['Терёхин Р.П', 'м', 24, 'правша' ]
]
print(group) 
print(group1)