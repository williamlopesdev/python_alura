
def jogar_forca():
    print("***************************************")
    print("Bem vindo no jogo de Forca!")
    print("***************************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando...")


    print("Fim do Jogo")


if(__name__ == "__main__"):
    jogar_forca()