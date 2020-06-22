def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

def arithmeticProgression(f,n,s):
    i = 0
    while i < n:
        print(f,end = " ")
        f += s
        i += 1

arithmeticProgression(0,20,2)
# inp = int(input("Введіть число, значення факторіала якого потрібно знайти: "))
# result = factorial(inp)
# print(f"Факторіал числа {inp} рівний {result}")
