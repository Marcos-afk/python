import random
def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')
    arquivo = open("palavras.txt" ,"r")
    palavras = []
    for linha in palavras:
        linha - linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange( 0 , len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    chute =  input('Qual a letra ? ')
    chute = chute.strip().upper()
    
    
