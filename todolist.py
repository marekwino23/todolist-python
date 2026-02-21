"""
TODO App - CLI w Pythonie
Funkcje:
- Dodawanie zadania
- Wyświetlanie zadań
- Usuwanie zadań
- Oznaczanie jako zakończone lub nieskończone
"""


todo = [
    {"nazwa":"Wyrzucic smieci", "zrobione": "nie"}, 
    {"nazwa":"Silka", "zrobione": "nie"}, 
    {"nazwa":"odkurzyc pokoj", "zrobione": "nie"}
]

def funkcja_add_task(todo, task):
    """Dodaje nowe zadanie do listy TODO"""
    todo.append({"nazwa": task, "zrobione": "nie"})

def funkcja_set_status(todo, index, status):
    """Zmiana statusu zadania w liście TODO"""
    try:
        index = int(index) - 1
        if 0 <= index < len(todo):
            todo[index]["zrobione"] = status
        else:
            print("Nieprawidłowy numer zadania")
    except:
        print("Podaj liczbę")    

def funkcja_delete_task(todo, index):
    """Usuwa zadnie w liście TODO"""
    try:
        index = int(index) - 1
        if 0 <= index < len(todo):
            todo.pop(index)
        else:
            print("Nieprawidłowy numer zadania")
    except:
        print("Podaj liczbę")

while True:
    print("\n1. Dodaj zadanie")
    print("2. Pokaż zadania")
    print("3. Usuń zadanie")
    print("4. Zakończ zadanie")
    print("5. Zadanie nieskończone")
    print("6. Wyjdź")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        task = input("Podaj zadanie: ")
        funkcja_add_task(todo, task)
        print("Zadanie zostało dodane")

    elif choice == "2":
        for i, t in enumerate(todo, start=1):
            print(f"{i} - {t['nazwa']} [{t['zrobione']}]")

    elif choice == "3":
        nr = input("Usuń zadanie nr: ")
        funkcja_delete_task(todo, nr)
        print("Zadanie zostało usunięte")

    elif choice == "4":
        nr = input("Wybierz numer zadania do zakończenia: ")
        funkcja_set_status(todo, nr, "tak")
        print("Zadanie oznaczone jako skończone")

    elif choice == "5":
        nr = input("Wybierz numer zadania nieskończonego: ")
        funkcja_set_status(todo, nr, "nie")
        print("Zadanie oznaczone jako nieskończone")

    elif choice == "6":
        break