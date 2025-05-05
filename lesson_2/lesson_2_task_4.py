# Напишем функцию fizz_buzz, которая принимает один аргумент (число n) и выводит все числа от 1 до n (включительно):
#Если число делится на 3, печатать Fizz.
#Если число делится на 5, печатать Buzz.
#Если число делится и на 3 и на 5, печатать FizzBuzz
#Все остальные числа выводятся просто как есть.

num = int(input("Введите число: "))

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        elif i % 5 == 0:
            print(f"{i} Buzz")
        else:
            print(i)

fizz_buzz(num)




