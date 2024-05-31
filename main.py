import os
import importlib

def clear_screen():
    os.system('cls')

def load_and_execute_module(module_name):
    try:
        module = importlib.import_module(module_name)
        module.execute()
    except ModuleNotFoundError:
        print(f"Module {module_name} not found.")
    except AttributeError:
        print(f"Module {module_name} does not have an execute function.")
    input("Press Enter to continue...")

def components_menu():
    clear_screen()
    print("\nComponents Menu:")
    print("1. Componente saludos")
    print("2. Component calculadora")
    choice = input("Select an option: ")
    if choice == '1':
            load_and_execute_module('componente_1')
    elif choice == '2':
            load_and_execute_module('calculadora')
            
    else:
        print("Invalid choice, please try again.")
        input("Press Enter to continue...")


def aspects_menu():
    clear_screen()
    print("\nAspects Menu:")
    print("1. Aspect X")
    print("2. Aspect Y")
    print("3. Aspect Z")
    choice = input("Select an option: ")
    print(f"You selected Aspect {choice}")

# def agents_menu():
#     clear_screen()
#     print("\nAgents Menu:")
#     print("1. Agent 1")
#     print("2. Agent 2")
#     print("3. Agent 3")
#     choice = input("Select an option: ")
#     print(f"You selected Agent {choice}")

def main_menu():
    
    print("Hello!")
    print("Select your preferred paradigm:")
    print("1. Components")
    print("2. Aspects")
    print("3. Agents")
    
    while True:
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            components_menu()
            break
        elif choice == '2':
            aspects_menu()
            break
        elif choice == '3':
            load_and_execute_module('Agentes')
            break
        else:
            print("Invalid choice, please try again.")

while(True):
    main_menu()