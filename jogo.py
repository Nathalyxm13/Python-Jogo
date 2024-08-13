import random

def escolher_palavra():
    palavras = ['python','desenvolvimento','jogo', 'programacao','algoritmo']
    return random.choice(palavras).upper()

def jogo_forca():
    palavra= escolher_palavra()
    letras_adivinhacao = []
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    print("_"*len(palavra))

    while tentativas > 0:
        tentativas = input("Digite uma letra:").upper()
    
        if tentativas in letras_adivinhacao:
            print("Você já tentou essa letra. Tente outra.")
            continue
    
        letras_adivinhacao.append(tentativas)    #append irá procurar as letras que a pessoa disse
    
        if tentativas in palavra:
            print('Boa! A letra está na palavra.')
        
        else:
            tentativas -= 1
        print("Errado! Você tem () tentativas restantes.".format(tentativas))  
        
        palavra_oculta = " ".join(letra if letra in letras_adivinhacao else '_' for letra in palavra) 
        print(" ".join(palvra_oculta))
    
        if "_" not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra.")
        break      
    
    if tentativas == 0:
       print("Você perdeu! A palvra era ()" .format(palavra))

jogo_forca()
    
    