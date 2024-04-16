#Desafio Lab 04 Data Science Academy
# Programação Orientada a Objetos
# Hevert Sousa

#imports
import random
from os import system, name

#Função para limpar a tela a cada execução.

def limpaTela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')
board = ['''

>>>>>>>>>>Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class homemEnforcado:
    def __init__(self, palavras):
        self.palavras = palavras
        self.letras_erradas = []
        self.letras_corretas = []
    
    def chute(self, letra):
        if letra in self.palavras and letra not in self.letras_corretas:
            self.letras_corretas.append(letra)
        elif letra in self.palavras and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def acabou(self):
        return self.ganhou() or (len(self.letras_erradas)==6)
    
    def ganhou(self):
        if '_' not in self.escondeLetra():
            return True
        return False

    def escondeLetra(self):
        rtn =''
        for letra in self.palavras:
            if letra not in self.letras_corretas:
                    rtn += '_'
            else:
                rtn += letra
        return rtn
    def statusJogo(self):
        print(board[len(self.letras_erradas)])
        print('\nPalavra: '+ self.escondeLetra())
        print('\nLetras erradas:', )
        for letra in self.letras_erradas:
            print(letra)
        print()
                
def palavra_random():
    palavras = ['maçã','banana','abacate', 'abacaxi', 'laranja']
    palavra = random.choice(palavras)
    return palavra

def main():
    limpaTela()
    
    jogo = homemEnforcado(palavra_random())
    
    while not jogo.acabou():
        jogo.statusJogo()
        letraDigito = input('\nDigite uma letra: ')
        jogo.chute(letraDigito)
    
    jogo.statusJogo()
    
    if jogo.ganhou():
        print('Parabéns você venceu!')
    else:
        print('\nGame Over!')
        print('A palavra era: '+ jogo.palavras)
    print('\nFoi bom jogar com você!')
    
    
        
if __name__ == "__main__":
    main()