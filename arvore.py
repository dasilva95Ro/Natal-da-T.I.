import os
import time
import pyfiglet

def print_tree(width, count):
    for i in range(10):
        print(("*"*count).center(width))
        count += 2
    print("||".center(width))

def print_message():
    message = pyfiglet.figlet_format("Valeu Natalina", font="slant")
    print(message)

width = 60
count = 1

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print_tree(width, count)  # Imprime a árvore
    time.sleep(3)  # Espera 5 segundos
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela novamente
    print_message()  # Imprime a mensagem "Valeu Natalina"
    time.sleep(3)  # Espera 5 segundos
