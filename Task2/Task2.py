#Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
#Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
lst = list(map(int,input('Введите числа списка через пробел ').split()))
listResult = []
for i in range((len(lst) +1) // 2):
    mult = lst[i] * lst[len(lst) -1 -i]
    listResult.append(mult)
print(listResult)

    