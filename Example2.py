# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
some_list = [1]
n = 1
for item in range(2, number + 1):
    n *= item
    some_list.append(n)
print(some_list)