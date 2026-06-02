# 1. O Problema da Idade
# Erro
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de idade.")

# Corrigido
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade.")

# Melhorado 
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("Você é maior de idade.")
# elif idade < 18:
#     print("Você não é maior de idade.")
# else:
#      print("Está opção não existe")

# 2. A Escrita Fiel
# Erro
# nome = "Mariana"
# print("Seja bem-vinda,nome!")

# Corrigido
# nome = "Mariana"
# print("Seja bem-vinda", nome)

# Melhorado
# nome = input("Digite seu nome: ")
# print(f"Seja bem-vinda, {nome}")

# 3. Falta de Espaço
# Erro
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O numero é menor ou igual a cinco.")

# Corrigido
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# # Melhorado 
# numero = int(input("Digite um número: "))
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# 4. Esquecimento Fatal
# Erro
# usuario = "aluno123"
# if usuario =="aluno123"
#     print("Login realizado com sucesso.")

# Corrigido
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso")

# Melhorado 
# usuario = "aluno123"
# usuario = input("Digite o nome de usuário: ")

# if usuario == "aluno123": 
#     print("Login realizado com sucesso!")
# elif usuario != "aluno123":
#     print("Usuário incorreto, tente novamente!")

# 5. Atribuição vs. Comparação
# Erro 
# clima = "ensolarado"
# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")

# Corrigindo 
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")

# Melhorando 
# clima = input("Digite o clima de hoje")
# clima = "chuvoso"
# clima2= "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")
# elif clima2 == "ensolarado":
#     print("Passe protetor solar!")

# 6. Misturando Alhos com Bugalhos
# Erro
# pontos = 50
# print("Parabéns! Você fez "
#  + pontos + " pontos.")

# Corrigido 
# pontos = 50
# print("Parabéns! Você fez", pontos)
# print("pontos")

# Melhorando
# pontos = input("Digite seus pontos: ")
# pontos = 50
# if pontos > 50:
#     print(f"Parabéns você fez {pontos} pontos")
# elif pontos != 50:
#     print(f"Parabéns você fez {pontos} pontos")

# 7. A Ordem dos Fatores
# Erro
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

# # Corrigindo 
# nota = float(input("Digite sua nota: "))
# if nota <= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

# Melhorado
# nota = float(input("Digite sua nota"))
# if nota >= 9:
#     print("Excelente")
# elif nota <= 7:
#     print("Aprovado")
# elif nota <= 4:
#     print("Reprovado")
# else:
#     print("Tchau")

# 8. O Contador de 1 a 5
# Erro
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

# Corrigido
# for i in range(6):
#     print(i)

# # Melhorado
# for i in range(6):
#     print(f"Contagem {i}")

# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conctar...")
# O código deveria parar após 3 tentativas

# Corrigido
# tentativas = 1 
# while tentativas <= 3:
#     print(f"tentativa {tentativas}: Tentando conctar...")
#     tentativas += 1
  
# Melhorado
# import timer
# tentativas = 1
# while tentativas <= 3:
#     print(f"tentativas {tentativas}: Tentando conctar...")
#     tentativas += 1
#     time.sleep(3)

# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Corrigido
# senha = "python123"
# senha = input("Digite a senha secreta: ")
# while senha == "python123":
#     print("Acesso concedido!")

# Melhorado
# senha = "python123"
# senha = input("Digite a senha secreta: ")
# if senha == "python123":
#     print("Acesso concedido!")
# elif senha != "python123":
#     print("Acesso negado, tente novamente!")
# else:
#     print("Coloque a senha!")