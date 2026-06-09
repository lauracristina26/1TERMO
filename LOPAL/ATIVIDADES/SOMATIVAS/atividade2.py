# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba: "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Registro de Operador") 
# janela.geometry("500x200")
# janela.configure(bg="light blue")

# def janela_registro():
#     nome = nome_usuario.get()
#     turno = turno_usuario.get()

#     if nome == "" and turno == "":
#         messagebox.showwarning("Aviso ao Operador!", "Necessário registrar nome do operador e o turno!")
#     else:
#         messagebox.showinfo("Aba de Registro", f"Operador {nome} registrado no Turno {turno}. Boa Jornada!")
    
# lbl_registro = tk.Label(janela, text="Registre seu nome:")
# lbl_registro.grid(row=0, column=0, pady=10, padx=10)
# lbl_turno = tk.Label(janela, text="Registre seu turno:")
# lbl_turno.grid(row=1, column=0, pady=10, padx=10)
# btn_clique = tk.Button(janela, text="Botão de Registro", font=("Arial, 11"), bg="#000000", fg="white", command=janela_registro)
# btn_clique.grid(row=2, column=0, pady=10, padx=10)

# nome_usuario = tk.Entry(janela, font=("Arial", 14))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)
# turno_usuario = tk.Entry(janela, font=("Arial", 14))
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)

# janela.mainloop()


# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("700x200")
# janela.configure(bg="#94F8FF")

# def calcular_producao():
#     pecas = int(pecas_quantidade.get())

#     if pecas == "":
#         messagebox.showwarning("Aviso", "Por favor, digite a quantidade de peças para o cálculo!")
#     else:
#         pecas = pecas * 8
#         messagebox.showinfo("Cálculo de Produção", f"Foram produzidas {pecas} peças em um turno de 8 horas!")

# lbl_quantidade = tk.Label(janela, text="Digite a quantidade de peças produzidas em 1 hora: ")
# lbl_quantidade.grid(row=0, column=0, pady=10, padx=10)
# btn_clique = tk.Button(janela, text="Cálculo Total da Produção", font=("Arial, 11"), bg="#EFF0F0", fg="black", command=calcular_producao)
# btn_clique.grid(row=1, column=0, pady=10, padx=10)

# pecas_quantidade = tk.Entry(janela, font=("Arial, 14"))
# pecas_quantidade.grid(row=0, column=1, pady=10, padx=10)

# janela.mainloop()


# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Conversor de Umidade")
# janela.geometry("600x200")
# janela.configure(bg="#A894FF")

# def conversor_umidade():
#     conversor = float(conversor_numero.get())

#     if conversor == "":
#         messagebox.showwarning("Aviso!", "É necessário digitar a pressão em Bar para a conversão!")
#     else:
#         conversor = conversor * 14.5
#         messagebox.showinfo("Conversão de Umidade", f"A conversão da pressão Bar par PSI foi {conversor}")

# lbl_numero = tk.Label(janela, text="Digite em Bar para fazer a conversão para PSI")
# lbl_numero.grid(row=0, column=0, pady=10, padx=10)
# btn_clique = tk.Button(janela, text="Conversor de Umidade", font=("Arial, 11"), bg="#EFF0F0", fg="black", command=conversor_umidade)
# btn_clique.grid(row=1, column=0, pady=10, padx=10)

# conversor_numero = tk.Entry(janela, font=("Arial, 14"))
# conversor_numero.grid(row=0, column=1, pady=10, padx=10)

# janela.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.










# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".
# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode iniciar.
# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário, "Processo Otimizado".
# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e diga se está dentro da tolerância, acima ou abaixo.
# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".