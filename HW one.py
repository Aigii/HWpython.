# #№1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# #Пример:
# #6 -> да
# #7 -> да
# #1 -> нет
# #print('Введите число')
# #day = int(input())
# #if day < 6:
#    print('yes')
# #elif day == 6 | 7:
#  #   print('not')
# #else:
#  #   print('Такого дня нет')
#
# # №3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# # и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# # Пример:x=34; y=-30 -> 4
# # x=2; y=4 -> 1
# # x=-34; y=-30 -> 3
#
#
# #print('Введите координаты точки')
#
# #x = int(input('x= '))
#
# #y = int(input('y= '))
#
# #if x>0:
#
#    #if y>0:
#
#     #   print('Точка лежит в I четверти')
#
#    #else:
#
#       # print('Точка лежит в IV четверти')
#
# #else:
#
#   #if y>0:
#
#    #    print('Точка лежит в II четверти')
#
#    #else:
#
#     #   print('Точка лежит в III четверти')
#
# # №4. Напишите программу, которая по заданному номеру четверти,
# # показывает диапазон возможных координат точек в этой четверти (x и y).
# #print('Введите номер координатной четверти ')
# #N = int(input('N: '))
# #if N == 1:
#  #    import random
#  #    xx = random.randint(1, 100)
#   #   print(f'X ={xx}')
#
#   #   import random
#   #   xx = random.randint(1, 100)
#   #   print(f'Y ={xx}')
#
# #else:
#  #   if N == 2:
#   #    import random
#   #    x = random.randint(1, 100)
#   #    c=x*-1
#   #    print(f'X ={c}')
#
#    #   import random
#    #   y = random.randint(1, 100)
#    #   print(f'Y ={y}')
#    # else:
#     #     if N == 3:
#      #        import random
#       #       x = random.randint(1, 100)
#       #       c = x * -1
#       #       print(f'X ={c}')
#
#        #      import random
#
#        #      y = random.randint(1, 100)
#        #      yy= y * -1
#        #      print(f'Y ={yy}')
#        #  else:
#        #      if N == 4:
#        #          import random
#
#        #          x = random.randint(1, 100)
#        #          print(f'X ={x}')
#
#        #          import random
#
#        #          y = random.randint(1, 100)
#        #          yy = y * -1
#        #          print(f'Y ={yy}')
#
# #  №5. Напишите программу, которая принимает на вход координаты двух точек
# #  и находит расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти расстояние в 3D пространстве)
# #  Пример: А (3,6); B (2,1) -> 5,09
# #          A (7,-5); B (1,-1) -> 7,21
#
# #print('Введите первой "A" точки')
#
# #Xa = int(input('x: '))
# #Ya = int(input('y: '))
#
# #print('Введите второй "B" точки')
#
# #Xb = int(input('x: '))
# #Yb = int(input('y: '))
# #from math import sqrt
# #AB = (Xb - Xa)**2 + (Yb - Ya)**2
# #print(sqrt(AB))
#
# # №2. Напишите программу для проверки истинности утверждения
# # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
#
# print('Введите номер координатной четверти ')
# X = int(input('X: '))
# if X == 0:
#      print (bool(X))
# else:
#   if X ==1:
#    print(bool(X))
#
# Y = int(input('Y: '))
# if Y == 0:
#      print (bool(Y))
# else:
#   if Y ==1:
#    print(bool(Y))
#
# Z = int(input('Z: '))
# if Z == 0:
#      print (bool(Z))
# else:
#   if Z ==1:
#    print(bool(Z))
#
# L = not (X or Y or Z)
#
# R = not X and not Y and not Z
#
# print(f'Проверяем "not (X or Y or Z)": {L} ')
#
# print(f'Проверяем "not X and not Y and not Z": {R}')
