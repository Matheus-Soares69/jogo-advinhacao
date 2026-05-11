# Jogo de Advinhação - desenvolvido por: Matheus Soares
# Função para exibir o menu do jogo e obter a escolha do usuário
import random

def menu():
    print("========================")
    print("   JOGO DE ADIVINHAÇÃO   ")  
    print("========================")
    print("1 - Jogar")
    print("2 - Sair")

    while True: # Loop para validar a escolha do usuário
        try:
            opcao = int(input("Escolha uma opção ( 1 ou 2 ): "))    
            break
        except:
         print("Opção inválida. Tente novamente.")
    
    while opcao != 1 and opcao !=2:
         print("Opção inválida. Tente novamente.")
         opcao = int(input("Escolha uma opção (1 ou 2): "))
    return opcao
opcao = menu()
print("=========================")

# Função para exibir o menu de dificuldade e obter a escolha do usuário
def menu_dificuldade():
    print("Dificuldade 1 - Fácil (10 tentativas)") # range de 1 a 100
    print("Dificuldade 2 - Médio (15 tentativas)")# range de 1 a 150
    print("Dificuldade 3 - Difícil (18 tentativas)")# range de 1 a 200
    print("__________________________")
   
    while True: #loop pra validar a escolha de dificuldade do usuário
        try: 
            print()
            dificuldade = int(input("Escolha a diificuldade (1, 2 ou 3): "))
            break
        except:
            print("Opção inválida. Tente novamente.")
    if dificuldade != 1 and dificuldade != 2 and dificuldade != 3:
            print("opção inválida. Tente novamente.")
            return menu_dificuldade()
    return dificuldade
print("==========================")



#Função para jogar o jogo de adivinhação
def jogar(dificuldade):
    
    if dificuldade == 1:
        maximo = 100
        limite = 10
    elif dificuldade == 2:
        maximo = 150
        limite = 15
    else:
        maximo = 200
        limite = 18
    numero_secreto = random.randint(1, maximo)
    tentativas = 0
    while True: # Loop do jogo

        while True: # Loop para validar a entrada do usuário
            try:
                print(f"_______________________________________________")
                print(f"Tentativa {tentativas + 1} de {limite}  | Range: 1 a {maximo}")
                palpite = int(input(f"Digite um número entre 1 e {maximo}: "))
                print()
                if palpite < 1 or palpite > maximo:
                    print(f"Número digitado inválido. Por favor, digite um número entre 1 e {maximo}: ")
                    continue
                break
            except:
                print(f"Entrada inválida. Por favor, Digite apenas números inteiros entre 1 e {maximo}:")
        
        tentativas += 1
        if tentativas > limite:
            print("💀 GAME OVER! 💀")
            print(f"O numero secreto era {numero_secreto}")
            break
        if palpite < numero_secreto:
            print("Seu palpite é muito baixo. Tente novamente. ")
        elif palpite > numero_secreto:
            print("Seu palpite é muito alto. Tente novamnente.")
        else:
            print(f"Parabens! Você acertou o número secreto em {tentativas} tentativas.")
            if tentativas <= limite // 3:
                print("⭐⭐⭐ Incrível!")
            elif tentativas <= limite // 2:
                print("⭐⭐ Muito bom!")
            else:
                print("⭐ Conseguiu!")
            break

# Verificar a escolha do usuário e iniciar o jogo ou sair
continuar = True
if opcao == 1:
    dificuldade = menu_dificuldade()
    jogar(dificuldade)
    opcao = input("Deseja jogar novamente? (S/N): ")
    while continuar == True:
        if opcao.upper() == "S":
            dificuldade = menu_dificuldade()
            jogar(dificuldade)
            opcao = input("Deseja jogar novamente? (S/N): ")
        elif opcao.upper() == "N":
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Opção invalida. Tente novamente.")
            opcao = input("Deseja jogar novamente? (S/N): ")
else:
    print("Obrigado por jogar! Até a próxima.")


