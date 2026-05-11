# Jogo de Advinhação ( MENU )
# Função para exibir o menu do jogo e obter a escolha do usuário
import random

def menu():
    print("========================")
    print("   JOGO DE ADIVINHAÇÃO   ")  
    print("========================")
    print("1 - Jogar")
    print("2 - Sair")
    while True:
        try:
            opcao = int(input("Escolha uma opção ( 1 ou 2): "))
            break
        except:
         print("Opção inválida. Tente novamente.")
    
    while opcao != 1 and opcao !=2:
         print("Opção inválida. Tente novamente.")
         opcao = int(input("Escolha uma opção (1 ou 2): "))
    return opcao
opcao = menu()

#Função para jogar o jogo de adivinhação
def jogar():
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True: # Loop do jogo

        while True: # Loop para validar a entrada do usuário
            try:
                palpite = int(input("Digite um número entre 1 e 100: "))
                if palpite < 1 or palpite > 100:
                    print("Número digitado inválido. Por favor, digite um número entre 1 e 100: ")
                    continue
                break
            except:
                print("Entrada inválida. Por favor, Digite apenas números inteiros entre 1 e 100.")
        
        tentativas += 1
        if palpite < numero_secreto:
            print("Seu palpite é muito baixo. Tente novamente. ")
        elif palpite > numero_secreto:
            print("Seu palpite é muito alto. Tente novamnente.")
        else:
            print(f"Parabens! Você acertou o número secreto em {tentativas} tentativas.")
            break

# Verificar a escolha do usuário e iniciar o jogo ou sair
continuar = True
if opcao == 1:
    jogar()
    opcao = input("Deseja jogar novamente? (S/N): ")
    while continuar == True:
        if opcao.upper() == "S":
            jogar()
            opcao = input("Deseja jogar novamente? (S/N): ")
        elif opcao.upper() == "N":
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Opção invalida. Tente novamente.")
            opcao = input("Deseja jogar novamente? (S/N): ")
else:
    print("Obrigado por jogar! Até a próxima.")


