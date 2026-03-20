contacts = {}

def add_contact():
    name = input("Введіть ім'я: ")
    number = input("Введіть телефон: ")
    contacts[name] = number

def show_contacts():
    for name, number in contacts.items():
        print(name, number)

def delete_contact():
    name = input("Введіть ім'я для видалення: ")
    if name in contacts:
        del contacts[name]

while True:
    print("1 - Додати")
    print("2 - Показати")
    print("3 - Видалити")
    choice = input("Обрати: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        delete_contact()