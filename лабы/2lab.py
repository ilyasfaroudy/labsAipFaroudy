# a = input("vvedite parol iz bukv:")
# b = input("vvedite parol iz bukv:")
# if a.upper() == b.upper():
#     if a == b:
#         if len(a) == len(b):
#             print("verno")
# else:
#     print("oshibka")

# n=int(input('Введите номер места(от 1 до 54): '))
# if n%2==0:
#     s='верхнее '
# else:
#     s='нижнее '
# if n in range(37, 55):
#     s=s+'боковое'
# else:
#     s=s+'плацкарт'
# if n < 55:
#     print('Ваше место - ', s)
# else:
#         print("недопустимое значение")

# a = int(input("vvedite god"))
# if a % 4 == 0:
#     print("visokosniy god")
# else:
#         print("obichniy god")

a = "красный"
b = "синий"
c = "желтый"
f = input("введи цвет нижним регистром:")
s = input("введи цвет нижним регистром:")
if f == a and s == b:
    print("фиолетовый")
elif f == a and s == c:
    print("оранжевый")
elif f == b and s == c:
    print("зеленый")
elif f == b and s == a:
    print("фиолетовый")
elif f == c and s == a:
    print("оранжевый")
elif f == c and s == b:
    print("зеленый")
else:
    print("ошибка, введите корректные цвета")