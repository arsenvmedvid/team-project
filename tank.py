contacts = []

def add_contact():
    number = input("Впишіть телефон: ")
    contacts.append(number)

def show_contacts():
    print(contacts)

while True:
    print("1 - добавити")
    print("2 - показати")
    choice = input("Виберіть: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()