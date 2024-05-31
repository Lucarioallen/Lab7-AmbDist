import os

def clear_screen():
    os.system('cls')

def components_menu():
    clear_screen()
    print("\nComponents Menu:")
    print("1. Component A")
    print("2. Component B")
    print("3. Component C")
    choice = input("Select an option: ")
    print(f"You selected Component {choice}")

def aspects_menu():
    clear_screen()
    print("\nAspects Menu:")
    print("1. Aspect X")
    print("2. Aspect Y")
    print("3. Aspect Z")
    choice = input("Select an option: ")
    print(f"You selected Aspect {choice}")

def agents_menu():
    clear_screen()
    print("\nAgents Menu:")
    print("1. Agent 1")
    print("2. Agent 2")
    print("3. Agent 3")
    choice = input("Select an option: ")
    print(f"You selected Agent {choice}")

def main_menu():
    clear_screen()
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
            agents_menu()
            break
        else:
            print("Invalid choice, please try again.")

while(True):
    main_menu()