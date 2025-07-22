import random
import re

try:
    escolha = int(input("--------- Menu ---------" +
                        "\n1. Calculadora Básica" +
                        "\n2. Maior e Menor entre Três Números" +
                        "\n3. Área de Formas Geométricas" +
                        "\n4. Jogo da Adivinhação" +
                        "\n5. Validador de Senha" +
                        "\n6. Lista de Tarefas" +
                        "\n7. Manipulação e Comunicação de Objetos" +
                        "\n8. Estatísticas de Vendas" +
                        "\n9. Simulador de Financiamento" +
                        "\n10. Manipulação de API" +
                        "\nDigite a opção desejada: "))

    if(escolha == 1) :
        # 1. Calculadora Básica

        print("\nCalculadora\n")

        numero_um = int(input("Digite o primeiro numero para o calculo: "))
        operador = int(input("Escolha um operador: "+
                    "\n1. Adicão (+)"+
                    "\n2. Subtração (-)" +
                    "\n3. Multiplicação (*)"+
                    "\n4. Divisão (/)" +
                    "\n: "))
        numero_dois = int(input("Digite o segundo numero para o calculo: "))

        if not isinstance(numero_um, int):
            print("Informação inválida")

        if operador == 1:
            resultado = numero_um + numero_dois
            print(f"O resultado da adição é {resultado}")

        elif operador == 2:
            resultado = numero_um - numero_dois
            print(f"O resultado da subtração é {resultado}")

        elif operador == 3:
            resultado = numero_um * numero_dois
            print(f"O resultado da multiplicação é {resultado}")

        elif operador == 4:
            resultado = numero_um / numero_dois
            print(f"O resultado da sua divisão é {resultado}")

        else:
            print("Operador não encontrado, tente novamente!")

    elif escolha == 2:
        # 2. Maior e Menor entre Três Números

        print("\nMaior e Menor entre Três Números\n")
        
        num_um = int(input("Informe o primeiro número: "))
        num_dois = int(input("Informe o segundo número: "))
        num_três = int(input("Informe o terceiro número: "))

        if num_um > num_dois & num_um > num_três:
            print(f"Número {num_um} é maior que {num_dois} e {num_três}!")

        elif num_dois > num_um & num_dois > num_três:
            print(f"Número {num_dois} é maior que {num_um} e {num_três}!")
        
        else:
            print(f"Numero {num_três} é maior que {num_um} e {num_dois}")

    elif escolha == 3:
        # 3. Área de Formas Geométricas

        print("\nÁrea de Formas Geométricas\n")

        escolha = int(input("Escolha uma forma geométrica para calcular a área" +
                            "\n1. Quadrado" +
                            "\n2. Retângulo" +
                            "\n3. Triângulo" +
                            "\n4. Círculo\n"))

        if escolha == 1:

            q_lado = float(input("Informe o tamanho do quadrado: "))

            area = q_lado * q_lado

            print(f"A área do quadrado é {area}")

        elif escolha == 2:

            comprimento = float(input("Informe a altura do retângulo: "))
            altura = float(input("Informe a altura do retângulo: "))

            area = comprimento * altura

            print(f"A área do retângulo é {area}")

        elif escolha == 3:
            
            base = float(input("Informe o valor da base: "))
            altura = float(input("Informe a altura do triângulo: "))

            conta_multiplicacao = base * altura
            area = conta_multiplicacao / 2

            print(f"A área do triângulo é {area}")

        elif escolha == 4:
            
            raio = float(input("Informe o raio do circulo: "))

            pi = 3.14
            area = pi * raio**2

            print(f"A área do circulo é {area}")

    elif escolha == 4:
        #4. Jogo da Adivinhação

        print("\nJogo da Adivinhação\n")

        numero = random.randint(1, 100)
        tentativas = 1
        resposta = True

        while resposta:

            valor = int(input("Tente adivinhar o número de 0 a 100: "))

            if valor == numero:
                print(f"Você acertou! 🎉\nO número era {numero}")
                resposta = False
            
            else:
                print(f"Poxa você errou! ❌\nO número não é {valor}\n- Você já tentou {tentativas} vez(es).\n")
                print("Mas você pode tentar novamente!\nVou te dar uma dica beleza?\n")

                tentativas += 1

                if valor > numero:
                    print("🔻 O número que você digitou é maior que o número a ser adivinhado!\n Boa sorte!\n")
                
                else:
                    print("🔺 O número que você digitou é menor que o número a ser adivinhado!\n Boa sorte!\n")
    
    elif escolha == 5:
        #5. Validador de Senha

        print("\nValidador de Senha\n")
        
        resp = True

        while resp:
            senha = input("Insira a senha: ")

            if len(senha) >= 8:
                if re.search(r'[A-Z]', senha) and re.search(r'[a-z]', senha):
                    if any(char.isdigit() for char in senha):
                        print("Senha Válida")
                        resp = False
                    else:
                        print("Deve haver pelo menos um número na senha.")
                else:
                    print("Deve haver ao menos uma letra maiúscula e uma minúscula.")
            else:
                print("Senha muito curta, insira uma senha com mais de 8 digitos.") 

    elif escolha == 6:
        #6. Lista de Tarefas:
        
        print("\nLista de Tarefas\n")

        tarefas = []

        def exibir_tarefas():

            if len(tarefas) == 0:
                    print("Não há terefas a serem listadas!\n")
                    return

            else:
                # enumerate -> Percorre uma lista e acessa o índice de cada posição
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1} . {tarefa}")


        while True:
            opcao = int(input("\n1. Adicionar" +
                            "\n2. Remover" +
                            "\n3. Visualizar tarefas" +
                            "\n4. Sair" +
                            "\nInforme a opção desejada: "))

            if opcao == 1:
                
                tarefa = input("\nAdicione uma nova tarefa: ")
                tarefas.append(tarefa)
                print("Tarefa adicionada com sucesso!\n")
            
            elif opcao == 2:
                
                if len(tarefas) == 0:
                    print("Não há terefas a serem listadas!\n")

                else:
                   
                   exibir_tarefas()

                    indice = int(input("\nDigite o número da tarefa que deseja excluir: ")) - 1

                    if 0 <= indice < len(tarefas):
                        remover = tarefas.pop(indice)

                        print(f"Tarefa {remover} removida com sucesso!")

                    else:
                        print("Número da tarefa inválido!")

            elif opcao == 3:
                
                if len(tarefas) == 0:
                    print("Não há terefas a serem listadas!\n")

                else:
                    print("\n--- Tarefas ---")
                    for i, tarefa in enumerate(tarefas):
                        print(f"{i + 1}. {tarefa}")
            
            elif opcao == 4:
                
                print("Saindo..")
                break

            else:
                print("Opção inválida! Tente novamente.")

    elif escolha == 7:
        #7. Manipulação e Comunicação de Objetos
        ...

    elif escolha == 8:
        #8. Estatísticas de Vendas
        ...

    elif escolha == 9:
        #9. Simulador de Financiamento
        ...
    
    elif escolha == 10:
        #10. Manipulação de API
        ...

    else:
        print("Informe uma opção válida!")
        
except ValueError:
    print("Por favor, digite apenas números.")