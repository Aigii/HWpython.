# #    Задание №1
# import random
# def player(total: int):
#     name = input('Введи свое имя: ')
#     while total>0:
#
#         if total < 29:
#             print(f'{name} выиграл!')
#             break
#         else:
#
#             m = int(input('Введите число: '))
#
#             if m>28 or m<0:
#                 print('Ошибка! число от 1 до 28!')
#             else:
#                 total -= m
#                 print(f'{name}, ты взял {m} "Baunty", осталось {total}')
#                 if total<29:
#                     print('Я выиграла! Прости.')
#                     break
#                 else:
#                     bot=total-((total//29)*29)
#                     total-=bot
#                     print(f'Я взяла {bot} "Baunty", осталось {total}')
# def bot(total: int):
#     name = input('Введи свое имя: ')
#     while total>0:
#         bot = total - ((total // 29) * 29)
#         total -= bot
#         print(f'Я взяла {bot} "Baunty", осталось {total}')
#         m = int(input('Введите число: '))
#         if m > 28 or m < 0:
#             print('Ошибка! число от 1 до 28!')
#         else:
#             total -= m
#             print(f'{name}, ты взял {m} "Baunty", осталось {total}')
#             if total < 29:
#                 print('Я выиграла! Прости.')
#                 break
#
#
# print('Привет, мой друг! Меня зовут Айги!')
# print('Сыграем в игру? На столе лежит вкусные конфетки "Baunty" - Райское наслаждение. \n'
#       'Количество конфет выбираешь ты. '
#       'Немного о правилах игры, делаем ход друг после друга. Первый ход определяется жеребьёвкой. \n'
#       'За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему'
#       'последний ход. ')
# total = int(input('Введите количество конфет: '))
# coin = random.randint(1, 2)
# if coin == 1:
#     print('Ты ходишь первый!')
#     player(total)
# else:
#     print('Айги')
#     bot(total)


print('Задача №2')
# board = list(range (1,10))
# def d_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*12)
#
#
# def take_input(XO):
#     v= False
#     while not v:
#         player_answer = input(f'Куда поставим {XO}')
#         try:
#             player_answer = int(player_answer)
#         except:
#             print('Некорректный ввод. ')
#             continue
#         if player_answer >= 1 and player_answer<=9:
#             if (str(board[player_answer-1]) not in'XO'):
#                 board[player_answer-1]=XO
#                 v=True
#             else:
#                 print('Эта клетка уже занята.')
#         else:
#             print('Некорректный ввод.')
#
# def check(board):
#     win_coord=((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#     for i in win_coord:
#         if board[i[0]]==board[i[1]]==board[i[2]]:
#             return board[i[0]]
#     return False
#
# def turn(board):
#     count=0
#     win=False
#     while not win:
#         d_board(board)
#         if count%2==0:
#             take_input('X ')
#         else:
#             take_input('O ')
#         count+=1
#         if count > 4:
#             tmp = check(board)
#             if tmp:
#                 print(tmp, "Выиграл!")
#                 win = True
#                 break
#         if count == 9:
#             print("Ничья!")
#             break
#     d_board(board)
# turn(board)
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.




print('Задача №3')
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def coding(text):
    count = 1
    result = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        result = result + str(count) + text[-1]
    return result


def decoding(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result


c = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(c)}")
d = input("Введите текст для кодировки: ")
print(f"Текст после дешифровки: {decoding(d)}")
