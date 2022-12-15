# №2 Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывестив консоль сам список и сумму его элементов.
#ДО:
#N=int(input('N: '))
#summa=0
#for i in range(1, N+1):
   # t=(1+1/i)**i
   # print(round(t, 2))
   # summa=summa+t
#print(f'Сумма: {round(summa, 2)}')
#После:
# N=int(input('N: '))
# summa=0
# d=[(1+1/i)**i for i in range(1, N+1)]
# print(d)
# print(sum(d))


#Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#До:
#my_list=[]
#my_listtwo=[]
#summa=0
#for i in range(5):
#    import random
#    x=random.randint(1,10)
#    my_list.append(x)

#    if i%2==1:
#        my_listtwo.append(my_list[i])
#        summa=summa+my_list[i]

#print(f'Случайный список из 5 чисел: {my_list}')
#print(f'Список чисел на нечетных позициях: {my_listtwo}')
#print()
#print(f'Сумма чисел на нечётных позициях: {summa}')
#После:
# import random
# def rando(x,function):
#     my_list=[]
#     new_list=[]
#     for i in range(x):
#        o=random.randint(1,10)
#        my_list.append(o)
#     print(my_list)
#     for i in range(len(my_list)):
#         if function(i):
#             new_list.append(my_list[i])
#     return sum(my_list)
# print('Сумма чисел на нечётных позициях', rando(5, lambda i: i%2==1))
# print('Сумма чисел на чётных позициях',rando(5, lambda i: i%2==0))


# №1 Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
#До:
#number =float(input('Введите число: '))
# if number != 0:
#    n=number*100000
#    a=int(n)
#    sum=0
#    while a !=0:
#        sum=sum+ a%10
#        a=a//10
#    print(sum)
#После:
# number =input('Введите число: ')
# print(type(number))
# number=number.replace(',','')
# my_list = [int(i) for i in number]
# print(sum(my_list))
