# # Atividade 1: Mensagem de Boas-Vindas
# # Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da programação em Python" 

# print("Bem-vindo ao mundo da programação em Python!")

# # Atividade 2: Informações Pessoais
# # Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# # Exemplo de saída:
# # Fulano de Tal
# # 30

# pergunta1 = input("Digite seu nome")
# pergunta2 = int(input("Digite sua idade"))

# print("Seu nome e sua idade são: " ,pergunta1, pergunta2)

# # Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512 por 128. Cada resultado deve ser exibido em uma linha separada.
# # ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# # ● Obs: Realize também a mesma situação com variáveis.

# (print(135 + 246))

# soma1 = int(input("Digite o primeiro valor"))
# soma2 = int(input("Digite o segundo valor"))
# total = soma1 + soma2 
# print("A soma é:", total)

# (print(512 - 128))

# subtração1 = int(input("Digite o primeiro valor"))
# subtração2 = int(input("Digite o segundo valor"))
# total = subtração1 - subtração2 
# print("A subtração é:", total)

# # Atividade 4: Multiplicação e Divisão
# # Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da divisão de 78 por 3

# (print(15*8))

# multiplicação1 = int(input("Digite o primeiro valor"))
# multiplicação2 = int(input("Digite o segundo valor"))
# total = multiplicação1 * multiplicação2
# print("A multiplicação é:", total)

# (print(78/3))

# divisão1 = int(input("Digite o primeiro valor"))
# divisão2 = int(input("Digite o segundo valor"))
# total = divisão1 / divisão2
# print("A divisão é:", total)

# # Atividade 5: Potenciação
# # Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# # ● Dica: O operador de potenciação em Python é **.

# (print(5**3))

# potenciação1 = int(input("Digite o primeiro valor"))
# potenciação2 = int(input("Digite o segundo valor"))
# total = potenciação1 ** potenciação2
# print("A potenciação é:", total)

# # Atividade 6: Concatenando Palavras
# # Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# # ● Exemplo: print("Maria" + " " + "Silva")

# q1 = input("Digite seu primeiro nome: ")
# q2 = input("Digite seu sobrenome: ")

# print("Seu nome é: " + "Seu sobrenome:" + q2) 

# Atividade 7: Cálculo de Eficiência (OEE)
# Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule e exiba a taxa de aproveitamento (peças boas / total).

# qp = int(input("Digite a quantidade de cada peça produzida"))
# qpeçasdefeituosas = int(input("Digite a quantidade de cada peça defeituosa"))
# total = qp - qpeçasdefeituosas
# print("A quantidade de peças produzidas e peças defeituosas é:", total)

# #  qpeçasboas = int(input("Digite a quantidade de cada peça boa"))
# #  total = qpeçasboas / total 
# #  print("A quantidade de peças boas é;", total)


# # Atividade 8: Descrição com Cálculos
# # Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados: "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# # Dica: Use a vírgula dentro do print() para combinar strings e cálculos. Ex: print("Texto", 25 + 10).

# idade = int(input("Qual a sua idade?"))
# print("Eu tenho", idade, "anos, e em 10 anos, terei", idade + 10, "anos.")


# # Atividade 9: Orçamento de Viagem (Cálculo com float)
# # Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# # Ex: Fórmula: (custo_hotel * 3) + custo_passagem

# chotel = float(input("Custo do hotel por noite"))
# cpassagem = float(input("Custo da passagem"))
# total = (chotel * 3) + cpassagem
# print("O custo total da viagem é:", total)


# # Atividade 10: Desafio - Mini Relatório
# # Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a saída de forma organizada.
# # Exemplo de saída: 
# # ==========================
# # Relatório de Vendas
# # ==========================
# # Produto: Notebook Gamer
# # Quantidade vendida: 15
# # Preço unitário: R$ 5499.50
# # Total de vendas: R$ 82492.50 
# # ==========================

# print("=======================")
# print("Relatório de Vendas")
# print("=======================")
# produto = print(input("Quantidade vendida?"))
# quantidadevendida = int(input("Qual o preço unitário?"))
# total = preçounitário + quantidadevendida 
# print("o total das vendas é:" ,total)
# print("=======================")