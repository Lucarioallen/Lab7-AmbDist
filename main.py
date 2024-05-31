import os
import componente_1
import calculadora
import fibonaci
import montecarlo

x=""

def clear_screen():
    os.system('cls')


def components_menu():
    global x
    clear_screen()
    print("\nMenu de Componentes:")
    print("1. Componente saludos")
    print("2. Component calculadora")
    choice = input("Selecciona una opcion: ")
    if choice == '1':
        componente_1.main()
        x=componente_1.get_name()
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

def agents_menu():
    clear_screen()
    print("\nMenu de Componentes:")
    print("1. Agentes fibonaci")
    print("2. Agentes montecarlo")
    choice = input("Selecciona una opcion: ")
    if choice == '1':
        fibonaci.fibonaci()
    elif choice == '2':
        montecarlo.monte_carlo()
    else:
        print("eleccion invalida prueba de nuevo.")
        input("Presiona enter para continuar...")


def main_menu():
    clear_screen()
    print("Hola", x, "!")
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
            agents_menu()
            break
        else:
            print("opcion invalida.")

while(True):
    clear_screen()
    main_menu()