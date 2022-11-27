
# №1 Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
#number =float(input('Введите число: '))
#if number != 0:
 #   n=number*100000
 #   a=int(n)
 #   sum=0
 #   while a !=0:
 #       sum=sum+ a%10
 #       a=a//10
 #   print(sum)


# 2й вариант
#numbers = input("Введите дробное число: ")
#x = numbers.split(".")
#a = int(x[0])
#b = int(x[1])
#suma = 0
#while (a != 0):
#    suma = suma + (a % 10)
#    a = a // 10
#while (b != 0):
 #   suma = suma + (b % 10)
  #  b = b // 10
#print("Сумма цифр равно:", suma)

# 3й вариант
#numbers = input("Введите дробное число: ")
#res= numbers.replace('.', '')
#a=0
#for i in res:
#    c=int(i)
#    #print(c)
#    if c > 0:
#        a=a+c
#print(a)


# №2 Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывестив консоль сам список и сумму его элементов.

#N=int(input('N: '))
#summa=0
#for i in range(1, N+1):
   # t=(1+1/i)**i
   # print(round(t, 2))
   # summa=summa+t
#print(f'Сумма: {round(summa, 2)}')

#№3 Реализуйте алгоритм перемешивания списка.
#Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
#import random
#list1= [1, 3, 5, 6]
#print(random.sample(list1, 4 ))

#ИЛИ ТАК
#B = sorted(list1, key=lambda A: random.random())
#print(B)











