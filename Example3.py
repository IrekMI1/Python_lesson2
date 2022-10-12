# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}, сумма 9,06

number = int(input('Введите целое число: '))
sum = 0
print('{ ', end='')
for i in range(1, number + 1):
    element = (1 + 1 / i) ** i
    sum += element
    if i != number:
        print(f'{i}: {round(element, 2)}', end=', ')
    else:
        print(f'{i}: {round(element, 2)}','}')
print('Сумма элементов последовательности: ', round(sum, 2))