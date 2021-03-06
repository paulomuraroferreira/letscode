"""
Jogo da Forca
Grupo 1

Sound from Zapsplat.com
Necessita do pacote pip install playsound 1.2.2.
"""


import random
import os
from playsound import playsound
from sys import platform

def mensagemAbertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def erro1():
    print('-'*30)  
    print(' '*10,"  ________    ") 
    print(' '*10,"  |       |   ")  
    print(' '*10,"  |      ( )  ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"__|__         ")
    print('-'*30)  

def erro2():
    print('-'*30)  
    print(' '*10,"  ________    ") 
    print(' '*10,"  |       |   ")  
    print(' '*10,"  |      ( )  ")
    print(' '*10,"  |       |   ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"__|__         ")
    print('-'*30)  

def erro3():
    print('-'*30)   
    print(' '*10,"  ________    ") 
    print(' '*10,"  |       |   ")  
    print(' '*10,"  |      ( )  ")
    print(' '*10,"  |      \|   ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"__|__         ")
    print('-'*30)  

def erro4():
    print('-'*30)
    print(' '*10,"  ________    ") 
    print(' '*10,"  |       |   ")  
    print(' '*10,"  |      ( )  ")
    print(' '*10,"  |      \|/  ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"__|__         ")
    print('-'*30)  

def erro5():
    print('-'*30)
    print(' '*10,"  ________    ") 
    print(' '*10,"  |       |   ")  
    print(' '*10,"  |      ( )  ")
    print(' '*10,"  |      \|/  ")
    print(' '*10,"  |       |   ")
    print(' '*10,"  |           ")
    print(' '*10,"  |           ")
    print(' '*10,"__|__         ")
    print('-'*30)        


def erro6():
    print('-'*30)
    print(' '*10,"  ________    ") 
    print(' '*10,"  |       |   ")  
    print(' '*10,"  |      ( )  ")
    print(' '*10,"  |      \|/  ")
    print(' '*10,"  |       |   ")
    print(' '*10,"  |      /    ")
    print(' '*10,"  |           ")
    print(' '*10,"__|__         ")
    print('-'*30)        
        

def erro7():
    print('-'*30)
    print(' '*10,"  ________    ") 
    print(' '*10,"  |       |   ")  
    print(' '*10,"  |      ( )  ")
    print(' '*10,"  |      \|/  ")
    print(' '*10,"  |       |   ")
    print(' '*10,"  |      / \  ")
    print(' '*10,"  |           ")
    print(' '*10,"__|__         ")
    print('\nFIM DE JOGO')
    print('-'*30)  


def desenhoForca(nivel, vidas_restantes):
    if nivel ==0:
        return eval(f'erro{7 - vidas_restantes}()')
    if nivel ==1:
        listaMedio = [1,3,5,7]
        return eval(f'erro{listaMedio[4 - vidas_restantes -1]}()')
    if nivel ==2:
        listaDificil = [1,4,7]
        return eval(f'erro{listaDificil[3 - vidas_restantes -1]}()')


def diagrama(palavra, lista):
    for caracter in palavra: #Se o caracter escolhido pertencer ?? palavra, o exibe nos espa??os adequados.
        print(caracter if (caracter in lista) else '__', end=' ')


def clear():
    if platform == 'win32' or platform == 'cygwin' or platform == 'msys':
        os.system('cls')
    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        os.system('clear')
    


while True:

    palavras = []
    lista = []
    nivel = ''
    tentativa = ''
    erradas = []
    jogarNovamente = ''

    mensagemAbertura()

    # Acessa o arquivo txt contendo as palavras.
    with open('words.txt', 'r') as arquivolido: 
        for linha in arquivolido:
            palavras.append(linha.strip())


    palavra = random.choice(palavras) # Escolhe uma palavra aleat??ria do arquivo.
    print()
    #print(palavra)
    print()

    print('__ '*len(palavra), '\n') #Exibindo os espa??os de cada letra da palavra escolhida.


    #Seleciona o n??vel de dificuldade, o qual define o n??mero de tentativas.
    while nivel not in ("0",'1','2'):
        nivel = input('N??vel do jogo (0 = f??cil, 1 = m??dio, 2 = dif??cil): ')
        #Define 7 vidas para o nivel f??cil, 4 para o n??vel 
        #m??dio e 3 para o n??vel dif??cil.
    nivel = int(nivel)
    vidas_restantes = 7 if nivel ==0 else (4 if nivel==1 else 3)

    # Testa se o caracter escolhido ?? uma letra, caso negativo solicita novamente um caracter v??lido.
    # Valida se h?? vidas restantes para o jogador.
    while vidas_restantes>0:
        tentativa = input('\n Digite uma letra v??lida: ').upper()
        
        if not tentativa.isalpha() or len(tentativa) != 1: #Valida se a entrada ?? uma letra do alfabeto.
            continue
        
        if tentativa in lista or tentativa in erradas:
            print('Voc?? j?? tentou essa letra.')
            continue
        
        elif tentativa not in palavra: #Remove uma vida caso a tentativa esteja incorreta.
            vidas_restantes -= 1
            desenhoForca(nivel, vidas_restantes)
            
            if vidas_restantes==0:
                print(f'Game over. A palavra correta era {palavra}')
                playsound('perdeu_jogo.mp3')
                break
                
            else:
                erradas.append(tentativa)
                erradas = list(set(erradas))
                print(f' \n As letras {erradas} n??o est??o na palavra. \n {vidas_restantes} tentativas restantes. \n \n' )
                playsound('errou_letra.mp3')  
                diagrama(palavra, lista)
                print()
                
        else:
            print()
            lista.append(tentativa)
            lista = list(set(lista))
            diagrama(palavra, lista)
            print()
            playsound('acertou_letra.mp3')
            
            if len(lista) == len(set(palavra)):
                print('\n','PARAB??NS!!!')
                playsound('ganhou_jogo.mp3')
                break #Encerra o jogo quando todas as letras da palavra foram adivinhadas.

    while jogarNovamente.lower() not in ('s','n'):
        jogarNovamente = input('Deseja jogar novamente? (s/n) ')
    
    if jogarNovamente.lower() == 's': 
        clear()
    elif jogarNovamente.lower() == 'n':
        print('Goodbye.')
        break


