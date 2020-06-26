from random import randint as rnd
attempts = int(input("Введіть кількість спроб: "))
option = int(input("Оберіть дію (1 - додавання, 2 - віднімання, 3 - множення, 4 - ділення): "))
min = int(input("Введіть мінімальне значення чисел:"))
max = int(input("Введіть максимальне значення чисел:"))

i = 0
correct = 0
while i < attempts:
    first = rnd(min,max)
    second = rnd(min,max)
    if(option == 1):
        question = first+second
        answer = int(input(f"{first} + {second} = "))
    elif(option == 2):
        question = first-second
        answer = int(input(f"{first} - {second} = "))
    elif(option == 3):
        question = first*second
        answer = int(input(f"{first} * {second} = "))
    elif(option == 4):
        try:
            question = first/second
            answer = int(input(f"{first} / {second} = "))
        except ZeroDivisionError:
            question = first/1
            answer = int(input(f"{first} / 1 = "))
    else:
        print("Дія обрана неправильно, почніть спочатку!")
        break
    if (question == answer):
        correct += 1
    i += 1
print(f"{correct} правильних відповідей із {attempts} прикладів")
