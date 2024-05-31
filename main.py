import os
import componente_1
import calculadora

def clear_screen():
    os.system('cls')


def components_menu():
    clear_screen()
    print("\nMenu de Componentes:")
    print("1. Componente saludos")
    print("2. Component calculadora")
    choice = input("Selecciona una opcion: ")
    if choice == '1':
        componente_1.main()
    elif choice == '2':
        calculadora.main()
    else:
        print("eleccion invalida prueba de nuevo.")
        input("Presiona enter para continuar...")


def aspects_menu():
    clear_screen()
    print("\nMenu de Aspectos:")
    print("1. Aspect X")
    print("2. Aspect Y")
    print("3. Aspect Z")
    choice = input("Selecciona una opcion: ")

# def agents_menu():
#     clear_screen()
#     print("\nAgents Menu:")
#     print("1. Agent 1")
#     print("2. Agent 2")
#     print("3. Agent 3")
#     choice = input("Select an option: ")
#     print(f"You selected Agent {choice}")

def main_menu():
    clear_screen()
    print("Hola!")
    print("Seleccciona un paradigma preferido:")
    print("1. Componentes")
    print("2. Aspectos")
    print("3. Agentes")
    
    while True:
        choice = input("Selecciona la opcion: ")
        if choice == '1':
            components_menu()
            break
        elif choice == '2':
            aspects_menu()
            break
        elif choice == '3':
            
            break
        else:
            print("opcion invalida.")

while(True):
    clear_screen()
    main_menu()