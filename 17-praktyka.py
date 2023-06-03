#dodać opcje niedostępną gdy ktoś wybierz cyfre ponad 5-done
#podział zadań na kategorie-done
#przy zapisie zadania tworzy osobny plik  dla kat. jesli istnieje nadpisuje go. - done
#dodać datę zapisu - done
#dodać status zdania i jego date edycji (dzien miesiac rok godzina sekunda?)
import datetime
czas_i_data = datetime.datetime.now()
czas_i_data_format = czas_i_data.strftime("%Y-%m-%d %H-%M-%S")

user_choice = -1

categories = []

tasks_dom = []
tasks_praca = []
task_dom = ""
task_praca = ""
zbior_dom = set(tasks_dom)
zbior_praca = set(tasks_praca)
### kategorie

def show_tasks_dom():
    task_dom_index = 0
    for task_dom in tasks_dom:
        print(task_dom + " [" + str(task_dom_index) + "]") #wyświetla zadania i dodaje do niego index w postaci stringa
        task_dom_index += 1 #zwieksza wartość o jeden, w tym przypadku dodaje kolejne indexy


def show_tasks_praca():
    task_praca_index = 0
    for task_praca in tasks_praca:
        print(str(zbior_praca) + " [" + str(task_praca_index) + "]") 
        task_praca_index += 1 
        

def add_task():
        global task_dom
        global task_praca   
        print("1.Dom")
        print("2.Praca")
        print("3.Powrót")
        category_choice = int(input("Wybierz kategorie do jakiej chcesz dodać zadanie: "))
        if category_choice == 1:
            print("Wybrano kategorie dom")
            task_dom = input("Podaj treść zadania: ") + (" ") + czas_i_data_format
            tasks_dom.append(task_dom)
            print("---------------------------")
            print("Dodano zadanie do grupy dom")
            print("---------------------------")
        if category_choice == 2:
            print("Wybrano kategorie praca")
            task_praca = input("Podaj treść zadania: ")
            tasks_praca.append(task_praca) + (" ") + czas_i_data_format
            print("-----------------------------")
            print("Dodano zadanie do grupy praca")
            print("-----------------------------")     


def delete_task():
    task_dom_index = int(input("Podaj indeks zadania do usunięcia: "))
    
    if task_dom_index < 0 or task_dom_index > len(tasks_dom) - 1:
        print()
        print("Zadania o tym indeksie nie istnieje")
        return #konczy wywolanie funckji
    tasks_dom.pop(task_dom_index)
    print("Usunięto zadanie!")


def save_tasks_to_file():
     global task_dom
     global task_praca
     print("W jakiej kategori chcesz zapisać zmiany ? ")
     print("1.Dom ")
     print("2.Praca ")
     print("3.Zapisz wszystko ")
     print("4.Anuluj ")
     save_choice = int(input("Wybierz index: "))
     if save_choice == 1:  
        file = open("tasks_dom.txt", "w")
        for task_dom in tasks_dom:
            file.write(task_dom+"\n")
        file.close()
        print("Zmiany zostały zapisane dla kategorii Dom")
     elif save_choice == 2:
        file = open("tasks_praca.txt", "w")
        for task_praca in tasks_praca:
            file.write(task_praca+"\n")
        file.close()
        print("Zmiany zostały zapisane dla kategorii Praca")
     elif save_choice == 3:
          try:
            with open("tasks_dom.txt", "w") as dom1, open("tasks_praca.txt", "w")as praca1:
              for task_dom in tasks_dom:
                dom1.write(task_dom+"\n")
              for task_praca in tasks_praca:  
                praca1.write(task_praca+"\n")
            print("Zmiany zostałe zapisane w obu plikach !")
          except IOError:
            print("Wystąpił błąd podczas zapisywania danych.")
               
                 

def load_tasks_from_file_dom():
    try:
        file = open("tasks_dom.txt")

        for line in file.readlines():
            tasks_dom.append(line.strip())

        file.close()
    except FileNotFoundError:
        return    

load_tasks_from_file_dom()

def load_tasks_from_file_praca():
    try:
        file = open("tasks_praca.txt")

        for line in file.readlines():
            tasks_praca.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file_praca()            

while user_choice != 5:
    if user_choice == 1:
        print("1.Dom")
        print("2.Praca")
        print("3.Powrót")
        category_choice = int(input("Wybierz kategorie: "))
        
        
       
        if category_choice == 1:
                print()
                print("Wyświetlono zadania dla kategorii Dom:")
                print()
                show_tasks_dom()
        elif category_choice == 2:
                print()
                print("Wyświetlono zadania dla kategorii praca")
                print()
                show_tasks_praca()        
        

    if user_choice == 2:
        add_task()


    if user_choice == 3:
        delete_task()
    
    if user_choice == 4:
        save_tasks_to_file()

    if user_choice > 5:
        print("Opcja niedostępna")    

    print()    
    print("1. Pokaż kategorie")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku ")
    print("5. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()

    
   
    