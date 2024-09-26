#informações do sistema bancario
saldo = 0
extrato = ""
valor_limite = 500
saques = 0
limite_saques = 3

#menus

menu_saque = """


========================================
                SAQUE                 
========================================


"""

menu_deposito = """


========================================
              DEPÓSITO                
========================================


"""

menu_extrato = """


========================================
               EXTRATO                
========================================


"""

menu_conversao_moedas = """


========================================
       MENU DE CONVERSÃO DE MOEDA      
========================================


Escolha a moeda para a qual deseja converter o saldo:

[1] Euro
[2] Dólar
[3] Libra
[4] Peso
[5] Iene

========================================
"""

menu_banco = """ 

Bem-vindo(a) ao sistema bancário. 
Digite a opção desejada de acordo com os números:


[0] Sacar
[1] Depositar
[2] Extrato
[3] Converter seu saldo em outra moeda.
[4] Sair




"""
#código do loop das opções
while True:
    opcao = input(menu_banco)

    if opcao == "0": #saque
        print(menu_saque)
        valor = float (input("\nDigite o valor desejado para o saque:"))
        
        if valor > 0:
            saldo -= valor 
            saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque de R$ {valor:.2f} realizado com sucesso. \n")


        elif valor > saldo:
            print("Não foi possível efetuar o saque pois o valor do seu saque é maior que o seu saldo.")


        elif valor > valor_limite:
            print("Não foi possível realizar o saque pois você não possui limite disponível.")


        elif saques > limite_saques:
            print("Não foi possível continuar pois o limite de saques foi atingido.") 


        else:
            print("Operação falhou!\nDigite um valor correto e tente novamente.")    



    elif opcao =="1": #deposito
        print(menu_deposito)
        valor = float(input("\nDigite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

        else:
            print("Operação falhou!\nDigite um valor correto e tente novamente.")    



    elif opcao == "2": #extrato
    
        print(menu_extrato)
        print("Não foram realizadas movimentações." if not extrato else extrato)

        if saldo < 0:
            print(f"Você está devendo: R$ {abs(saldo):.2f} \n")

        if saldo >0:    
            print(f"O valor do seu saldo é: R$ {saldo:.2f}\n")

    elif opcao == "3": #conversão para outra moeda

        #valores para conversão 
        valor_dolar = saldo / 5.5 #valor aproximado
        valor_euro = saldo / 6.1  #valor aproximado
        valor_iene = saldo / 0.004 #valor aproximado
        valor_peso = saldo / 0.005 #valor aproximado
        valor_libra = saldo / 7.3 #valor aproximado 

        if saldo == 0:
            print("Não foi possível continuar pois não há saldo disponível.")

        else:
            print(menu_conversao_moedas)
            opcao_moeda = int(input("Digite a opção desejada de acordo com os números acima: "))
            if opcao_moeda == 1: #euro
                print(f"O seu saldo em Euro é: € {valor_euro:.2f} ")

            elif opcao_moeda == 2: #dolar
                print(f"O seu saldo em Dolar é: $ {valor_dolar:.2f} ") 

            elif opcao_moeda == 3: #libra
                print(f"O seu saldo em Libra é: £ {valor_libra:.2f} ")

            elif opcao_moeda == 4: #peso
                print(f"O seu saldo em Peso é: $ {valor_peso:.2f} ")

            elif opcao_moeda == 5: #iene
                print(f"O valor do seu saldo em Iene é: ¥ {valor_iene} ")   

            else:
                print("Não foi possível continuar!\nDigite uma opção válida.")



    elif opcao == "4": #sair
        break


    else:
        print("Valor incorreto!\n Digite um valor válido no menu de opções para continuar.")
