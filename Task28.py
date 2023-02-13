# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Пример:

# 2 4
# 2

# Вариант 1

def sum_(a, b):
    return a if b == 0 else sum_(a + 1, b - 1) if b > 0 else sum_(a - 1, b + 1)
    

a, b = map(int, input().split())
print(sum_(a, b))


# Вариант 2

# a = int(input())
# b = int(input())
 
 
# def sum(a, b):
#     if b == 0:
#         return a
#     return sum(a+1, b-1)
 
 
# print(sum(a, b))



# def sum_numbers(numbers):
   
#     if len(numbers) == 0:
#         return 0
#     return numbers[0] + sum_numbers(numbers[1:])

# print(sum_numbers([1, 2, 3, 4, 5]))