

def caching_fibonacci(): #Фуккція для обрахунку чисел Фібоначі
    fib_cache = {15: 987} # Кеш для функції
    
    def fibonacci(numeric:int): #Функція для перевірки і обчислення числа приймає тільки int
        try: #Пробую одразу вивести введене значення зі списку
            if fib_cache[numeric]: return f"Cache:> Fibonacci ({numeric}) -> {fib_cache[numeric]}" #Якщо є таке значення по ключу то вертаю його
        except: next #Якщо немає то продовжую функцію
        
        def recurse_fib(n): #Рекурсивна функція для обрахунку числа Фібоначчі
            if n <= 1:
                return 1
            return recurse_fib(n - 1) + recurse_fib(n - 2)
        
        fib_cache[numeric] = recurse_fib(numeric) #Зберігаю нове значення до списку
        # print(fib_cache)
        return f"Fibonacci ({numeric}) -> {recurse_fib(numeric)}" #Викликаю функцію для обрахунку числа Фібоначчі
    
    while True: #Цикл для замикання у функції caching_fibonacci()
        input_res = input("Send numeric: ") #Запит для введення числа
        if input_res == "close": #Команда для виходу з цикла
            return print("Close function")
            
        try: #Пробую перетворити введене число в int і помістити його в функцію
            res = fibonacci(int(input_res)) #Викликаю функцію fibonacci()
            print(res) #Виводжу прінтом результат функції fibonacci()
        except: pass #Пропускаю помилку

caching_fibonacci() #Викликаю функцію caching_fibonacci()

            
        
    
