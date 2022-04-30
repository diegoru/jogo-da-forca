import random
from forca_arte import logo, estagio
from forca_palavras import lista_de_palavras
import os

os.system('cls' if os.name == 'nt' else 'clear')
print(logo)

palavra_escolhida = random.choice(lista_de_palavras)

# Criar espaços em branco
mostrar = []
for _ in palavra_escolhida:
		mostrar += "_"

fim_do_jogo = False
vidas = 6

while not fim_do_jogo:
    adivinha = input("Adivinhe uma letra:").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    if adivinha in palavra_escolhida:
        print(f"Você acertou a letra {adivinha}.")

    # Verifica a letra informada
    for posicao in range(len(palavra_escolhida)):
	    if adivinha == palavra_escolhida[posicao]:
		    mostrar[posicao] = adivinha


    # Verifica se o usuário errou.
    if adivinha not in mostrar:
        print(f"Você informou a letra {adivinha}, e ela não está na palavra. Você perdeu uma vida.")
        vidas -= 1


    # Junta todos os elementos da lista e transforma em uma String
    print(f'\n\n{" " .join(mostrar)}')

    print(f'\n{estagio[vidas]}')
    
    if vidas == 0:
    	fim_do_jogo = True
    	print("Você perdeu")

    # Verifica se o usuário acertou todas as letras.
    if "_" not in mostrar:
    	fim_do_jogo = True
    	print("Você ganhou.")