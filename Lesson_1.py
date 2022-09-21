# x = int(input("Введите число от 1 до 9: "))
# if  (1 <= x) and (x <= 3):
#     s = input("Введите строку: ")
#     n = int(input("Число повторов: "))
#     for i in range(n):
#         print(s)
# elif (4 <= x) and (x <=6):
#     m = int(input("Введите степень: "))
#     print(x**m)
# elif (7 <= x) and (x < 9):
#     for i in range(10):
#         x += 1
#         print(x)
#         i += 1
# else:
#     print("Ошибка ввода!")


#Задание 2
print("Общество в начале XXI века")
x = int(input("Введите свой возраст: "))
if  (0 < x) and (x < 7):
    print("Вам в детский сад")
elif (7 < x) and (x < 18):
    print("Вам в школу")
elif (18 < x) and (x < 25):    
    print("Вам в профессиональное учебное заведение")
elif (25 < x) and (x < 60):
    print("Вам на работу")
elif (60 < x) and (x < 120):
    print("Вам предоставляется выбор...")
else:
    for i in range(5):
        print("Ошибка! Эта программа для людей!")
        i+=1
