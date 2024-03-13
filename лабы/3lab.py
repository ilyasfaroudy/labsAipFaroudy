# N = int(input("введите количество слов: "))
# rez = ""
# for _ in range(N):
#     word = input("введите слово: ")
#     rez += word + " "
# print("результат:", result.strip())





# rez = ""
# while True:
#     word = input("Введите слово: ")
#     if word.lower() == "stop":
#         break
#     rez += word + " "
# print("Результат:", rez.strip())



#a = input("введите слово:")
#if "ф" in a:
#    print("ого! это редкое слово!")
#else:
#    print("эх, это не очень редкое слово...")



import random
cor = 0
wrong = 0
while wrong < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    cor_rez = num1 + num2

    uAns = input(f"{num1} + {num2} = ")
    if uAns.isdigit() and int(uAns) == cor_rez:
        print("правильно!")
        cor += 1
    else:
        print("ошибка")
        wrong += 1
print(f"игра окончена. правильных ответов: {cor}")
