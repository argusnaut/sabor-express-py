import os

restaurants = [
    {"name": "Praça", "category": "Japonesa", "active": False},
    {"name": "Pizza Suprema", "category": "Pizza", "active": True},
    {"name": "Cantina", "category": "Italiana", "active": False},
]


def display_app_name():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def options():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair")


def invalid_option():
    print("\nOpção Inválida!")
    return_main_menu()


def print_subtitle(text):
    os.system("cls")
    print(text)
    print()


def add_new_restaurant():
    print_subtitle("Cadastro de novos restaurantes")
    restaurant_name = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurants.append(restaurant_name)
    print(f"\nO restaurante {restaurant_name} foi cadastrado com sucesso!")
    return_main_menu()


def list_restaurants():
    print_subtitle("Listando restaurantes")

    for restaurant in restaurants:
        print(
            f".{restaurant["name"]} | {restaurant["category"]} | {restaurant["active"]}"
        )

    return_main_menu()


def choose_option():
    try:
        chosen_option = int(input("Escolha uma opção: "))
        # print(f"Você escolheu a opção {chosen_option}")

        if chosen_option == 1:
            add_new_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            print("Ativar restaurante")
        elif chosen_option == 4:
            exit_app()
        else:
            invalid_option()

    except:
        invalid_option()


def exit_app():
    print_subtitle("Finalizando o App")


def return_main_menu():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()


def main():
    os.system("cls")
    display_app_name()
    options()
    choose_option()


if __name__ == "__main__":
    main()
