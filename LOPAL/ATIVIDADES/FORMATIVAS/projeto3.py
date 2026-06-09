# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"
# Você foi contratado para desenvolver o módulo de validação de empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá cobrança de taxa de segurança.
# Regras de Negócio (O que o sistema deve fazer):
# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade Geral.
# 2. Limite de Dias: * Alunos podem ficar com o livro por até 14 dias de graça. A Comunidade Geral pode ficar por até 7 dias de graça.
# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.
# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados para a Comunidade Geral, apenas para Alunos.

# import tkinter as tk
# from tkinter import messagebox, ttk

# def primeira_janela():
#     nome = nome_usuario.get()
#     livro = livro_usuario.get()

#     if nome == "" and livro == "":
#         messagebox.showwarning("Lembrete!", "Faça sua identificação!")
#     else:
#         messagebox.showinfo("Bem-vindo", f"Olá usuário, {nome} e o {livro} escolhido")


# janela = tk.Tk()
# janela.title("Biblioteca Comunitária Digital 𑣲⋆")
# janela.geometry("500x400")
# janela.configure(bg="light pink")


# lbl_nome =  tk.Label(janela, text="Digite o seu nome: ")
# lbl_nome.grid(row=0, column=0, pady=10, padx=10)
# lbl_mensagem = tk.Label(janela, text="Digite o nome do livro: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_alunocomunidade = tk.Label(janela, text="Alunos ou da Comunidade Geral?")
# lbl_alunocomunidade.grid(row=1, column=0, pady=10, padx=10)

# nome_usuario = tk.Entry(janela, font=("Times New Roman", 14))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)
# livro_usuario = tk.Entry(janela, font=("Times New Roman", 14))
# livro_usuario.grid(row=1, column=1, pady=10, padx=10)
# alunnocomunidade_usuario = tk.Entry(janela, font=("Times New Roman", 14))
# alunnocomunidade_usuario.grid(row=0, column=1, pady=10, padx=10)



# janela.mainloop()


# print("Bem-vindo á Bibloteca Digital!")

# while True:
#     try:
#         print("Perfil Do Usuário")
#         print("1-Aluno")
#         print("2 - Comunidade Geral")
#         tipodeusuario = int(input("Informe o tipo de usuário (1 - Aluno ou 2 - Comunidade Geral)"))
        
#         if tipodeusuario != 1 and tipodeusuario != 2:
#             print("Erro: Opção de usuário inválida! O programa será encerrado.")
#         else: 
#             print("Categoria do Livro!")
#             print("1 - Normal")
#             print("2 - Raro")
#             categoriadolivro = int(input("Informe a categoria do livro 1 ou 2: "))

#         if categoriadolivro != 1 and categoriadolivro !=2:
#             print("Erro: Opção de categoria inválida! O programa será encerrado.")
#         elif tipodeusuario == 2 and categoriadolivro == 2:
#             print("Empréstimo Negado!")
#             print("Motivo: Livros da Categoria Raros são exclusivos para Alunos.")
#         else:
#             print("Detalhes Do Empréstimo")
#             diasdesejados = int(input("Quantos dias você de seja ficar com o livro?"))

#             if diasdesejados <= 0:
#                 print("Erro: A quantidade de dias deve ser maior que zero")
#             else:
#                 limitetaxazero 


