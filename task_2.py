
import re

text = """
    Загальний дохід працівника складається з 
    декількох частин: 2000.01 як основний дохід, 
    доповнений додатковими надходженнями 27.45 і 324.00 доларів.
"""


def generator_numbers(text_in: str): #Генератор чисел витягнутих з тексту
    res = re.findall(r"\b[0-9.]+\b", text_in) #Витягаю в список всі числа з тексту
    for n in res: #Встановлюю цикл для генератора
        yield n #Повертаю значення з кожної наступної ітерації


def sum_profit(text: str, func: callable): #Функція для обчислення загальної суми
    sum_nums = 0 #Змінна для загальної суми чисел
    for nums in func(text): #Читаю генератор
        sum_nums += float(nums) #Додаю числа до загальної суми
    return sum_nums #Повертаю результат функції


#Виводжу результат функції sum_profit() 
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income} $")

