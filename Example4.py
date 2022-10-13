# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число N: '))
some_list = list(range(-N, N + 1))
print('Список [-N; N]:', some_list)
data = open('file.txt', 'r')
numbers = []
for number in data:
    numbers.append(int(number))
data.close()
answer = some_list[numbers[0]] * some_list[numbers[1]]
print('Произведение элементов с позициями {} и {} равна {}'
      .format(numbers[0], numbers[1], answer))