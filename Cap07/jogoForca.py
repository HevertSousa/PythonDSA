# Projeto 1 - Desenvolvimento em Linguagem Python - Versão 1

#Import
import random
from os import system, name

#função para limpar a tela a cada execução

def limpa_tela():
    if name =='nt':
        _=system('cls')
    else:
        _=system('clear')

def game():
    limpa_tela()
    print('\nBem-Vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')
    
    #Lista de palavras para o jogo 
    palavras = ['banana','abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe randomicamente uma palavra 
    palavra = random.choice(palavras)
    
    # List comprehension
    letras_descobertas = ['_' for letra in palavra]
    
    # Número de Chances
    chances = 6
    
    # Lista para as letras erradas
    letras_erradas = []
    
    # Loop enquanto o número de chances for maior do que zero
    while chances > 0:
        #print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas: ", " ".join(letras_erradas))
        
        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        
        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                    index +=1
                else:
                    chances -=1
                    letras_erradas.append(tentativa)
                    
            #Condicional 
            if "_" not in letras_descobertas:
                print("\nVocê venceu, a palavra era:", palavra)
                break
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ",palavra)
        
# Bloco main o bloco main indica que esse scrip é um módulo/programa em python
if __name__ == "__main__":
    game()
    print("Parabéns. você está aprendendo programação em Python com a DSA :)\n")