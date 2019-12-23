"""
Користувач вводить рядок, що містить римський запис числа. Напишіть функцію, що повертає це число у арабському записі. Виведіть результат.
У випадку помилкового вводу виведіть повідомлення про помилку.
Римські позначення цифр: M=1000, D=500, C=100, L=50, X=10, V=5, I=1. Жоден символ не може повторюватися понад 3 рази підряд.
"""
import re
M = 1000
D = 500
C = 100
L = 50
X = 10
V = 5
I = 1
rome_numbers = [1000,500,100,50,10,5,1]
def do_user_data(text):
    flag = False
    while not flag:
        value = input(text)
        if bool(re.match('^ [+]{0,1}[0-9]{1,}(\.[0-9]{1,}){0,1}$', value)):
            flag = True
            value = float(value)
        else:
            print("Сталася помилка")
    return value
user_data = do_user_data("Введіть вашу цифру")
nums = int(do_user_data[1]-1)
do_user_data[1] = rome_numbers[nums]
