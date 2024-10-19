'''
Команди:
        1 - "hello" - Привітання з користувачем
        2 - "add [ім'я] [номер телефону]" - Для додавання в словник {"ім'я": "номер телефону"}
        3 - "change [ім'я] [новий номер телефону]" - Зберігає в пам'яті новий номер телефону 'phone' для контакту 'username', що вже існує в записнику.
        4 - "phone [ім'я]" - Виводить номер телефону по імені 
        5 - "all" - Виводить всі контакти з номерами телефонів
        6 - "exit" - закрити програму 
'''



def input_error(func): #Декоратор команди add
    def inner(*args, **kwargs):#Функція для обробки помилки
        try: #Пробую запустити функцію прийняту декоратором
            return func(*args, **kwargs) #Повертаю функцію
        
        except ValueError: #Якщо помилка то виводжу повідомлення
            return "Give me name and phone please." #Виводжу помилку
        
    return inner #Повертаю функцію обробки помилки


contacts = {} #Словник для контактів

@input_error
def add_contact(args, dict_cont): #Функція додавання контакту до словника
    name, phone = args #Розбиваю аргументи по змінних
    dict_cont[name] = phone #Записую до списку
    return f"Contact {name} added\n" #Повертаю повідомлення


@input_error
def change_contact(args, dict_cont): #Якщо добавлять через 'change' то перевірить чи контакт вже існує
    name, phone = args #Розбиваю аргументи по змінних
    for c in contacts: #Пробігаюсь по контактах
        if c == name: #Перевіряю на співпадіння
            c_st = f"The contact - {name} - already exists \nReplace contact (Yes / No)?" #Змінна з запитанням
            conf = input(f"{c_st}\nenter y or n -> ") #input з підтвердженням
            if conf == "y": #Перевіряю на введене значення
                contacts[name] = phone #Якщо 'y' то записую в словник
                return "Contact changed" #Вертаю повідомлення
            else: return "Canceled" #Відмова від збереження
            
    
   
 

def contact_phone(name, contacts): #Функція пошуку номера телефону за ім'ям
    for cont in contacts: #Пробігаюсь по словнику з контактами
        if cont == name[0]: #Шукаю збіг
            return cont + ": " + contacts[cont] #Повертаю рядок з контактом і телефоном
    return "There is no contact" #Повертаю повідомлення про відсутність контакту     



def out_all_contacts(contacts): #Виводжу всі контакти зі словника
    result_all = ""
    for cont in contacts: #Пробігаюсь циклом по словнику
        result_all += cont + ': ' + contacts[cont] + "\n" #Записую в змінну результат читання словника
    return (result_all) #Повертаю результат



def parse_input(user_input): #Функція для парсингу команд
    cmd, *args = user_input.split() #Розбиваю команду
    cmd = cmd.strip().lower() #Записую команду в окрему змінну
    return cmd, *args #Повертаю команду і аргументи



def main(): #Основна функція з циклом 
    print("Welcome to the assistant bot!")
    while True: #Основний цикл для постійного запиту команд
        user_input = input("Enter a command: ") #Запитую команду
        command, *args = parse_input(user_input) #Зберігаю результат парсингу в змінні 

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "all":
            print(out_all_contacts(contacts))
        
        elif command == "phone":
            print(contact_phone(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "add":
            print(add_contact(args, contacts))
                
        else:
            print("Invalid command!!!")



main()


