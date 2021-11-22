## Тренеровка
# Квадратный корень
def sq(x):
    print('Квадрат числа ',x,'=',x**2)
for i in range(1,11):
    sq(i)

#Умножение 
def mul(a,b):
    print(a*b)
mul(3,5)

#Четное число или нет
def ev(a):
    if a%2==0:
        print(a, 'Четное')
    else:
        print(a,'Не четное')
for i in range(1,11):
    ev(i)

##  Задание 1 Задание функции, работа со списком

def test1 ():
    Group=[['Виктор', 1999,'яблоко', 2, 175, 80],
            ['Артем', 2005,'банан',2, 193, 100],
            ['Роман', 2001,'киви',21, 166, 70]]
    
    # передаем год рождения первого
    year=Group[0][1] 
    for x in [1,2]:    
        y=Group[x][1]
    #Находим самого молодого
        if year < y:
            year =y
            man=Group[x][0]
    print ("Самый молодой", man,"его год рождения",year)
test1()

##  Задание 2 Работа над словарем 

def test2 ():
    Group ={
            'Жуйкин':{'год рождения' : 1988, 'рост' : 175,  'вес' : 80},     
            'Пусин':{'год рождения' : 1983, 'рост' : 196,  'вес' : 100}, 
            'Мосин':{'год рождения' : 2003, 'рост' : 166,  'вес' : 70}    
            }         
    key0 ='Жуйкин'
    key01 ='год рождения'
    key02 = 'рост'
    key03 = 'вес'
    
    z=list(Group)
    weight=Group[key0][key03]  
    for key in Group:
          if Group [key][key03] > weight:
              weight = Group [key][key03]
          
                 
              print ("Самый толстый" , key, "его вес", weight, "кг") 
test2()              

##  Задание 3 не четкое сравнение элементов

def test3(S1, S2):
    ngrams = [S1[i+i:3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count/max(len(S1), len(S2))

Group=[['Виктор', 1999,'яблоко', 2, 175, 80],
            ['Артем', 2005,'банан',2, 193, 100],
            ['Роман', 2001,'киви',21, 166, 70]]

S1 = Group[0][0]
S2 = Group[1][0]
c = test3 (S1, S2)
    
print (c, S1, S2)