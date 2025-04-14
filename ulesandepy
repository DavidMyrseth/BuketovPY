tasks = []
def add_task(task):
    return tasks.append(task)


def main ():
    userInput = input("Mida sa tahad?")
    print("1 - lisada ülesande \n 2 - kustutada ülesande, \n 3 - ülesanded")
    if userInput == "1":
        tasks = add_task(input("sisesta ülesande: "))
    elif userInput == "2":
        pass
    elif userInput == "3":
        pass 
    else:
        print("sa sisestasid midagi vale")

def main():
    while True:
        print("\n1 - Добавить задачу\n2 - Удалить задачу\n3 - Показать все задачи\n4 - Выход")
        userInput = input("Что вы хотите сделать? ")

        if userInput == "1":
            task = input("Введите задачу: ")
            add_task(task)

        elif userInput == "2":
            delete_task()

        elif userInput == "3":
            if tasks:
                print("Список задач:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
            else:
                print("Задачи отсутствуют.")

        elif userInput == "4":
            print("Выход из программы.")
            break

        else:
            print("Вы ввели неверную команду.")

main()
