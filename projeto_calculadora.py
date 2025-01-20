import tkinter as tk
import json

# Classe de operações matemáticas.


class FormulasMatematicas:
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def adicao(self):
        return self.numero_1 + self.numero_2

    def subtracao(self):
        return self.numero_1 - self.numero_2

    def multiplicacao(self):
        return self.numero_1 * self.numero_2

    def divisao(self):
        if self.numero_2 == 0:
            raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
        return self.numero_1 / self.numero_2

# Função que irá para salvar o resultado em um arquivo JSON.


def salvar_historico(operacao, num_1, num_2, resultado):
    historico = {"operacao": operacao, "numero_1": num_1, numero_2": num_2, "resultado": resultado}

    try:
        with open("historico.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []

    dados.append(historico)

    with open("historico.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função que irá realizar as operações matemáticas.


def realizar_operacao(operacao):
    try:
        num_1 = float(entrada1.get())
        num_2 = float(entrada2.get())
        calc = FormulasMatematicas(num_1, num_2)

        if operacao == "adicao":
            resultado = calc.adicao()
        elif operacao == "subtracao":
            resultado = calc.subtracao()
        elif operacao == "multiplicacao":
            resultado = calc.multiplicacao()
        elif operacao == "divisao":
            resultado = calc.divisao()

        label_resultado.config(text=f"Resultado: {resultado}")
        salvar_historico(operacao, num_1, num_2, resultado)

    except ValueError:
        label_resultado.config(text="Erro! Insira um número válido.")
    except ZeroDivisionError as e:
        label_resultado.config(text=str(e))


# Criação da janela principal.
janela = tk.Tk()
janela.title("Calculadora com Histórico")
janela.geometry("400x400")
janela.configure(bg="#D3D3D3")

# Título.
titulo = tk.Label(janela, text="Calculadora Matemática", font=(
    "Arial", 16, "bold"), bg="#D3D3D3", fg="#333")
titulo.grid(row=0, column=0, columnspan=2, pady=(10, 20))

# Campo para a inserção do primeiro número.
label_num1 = tk.Label(janela, text="Insira o 1 número:",
                      font=("Arial", 12), bg="#D3D3D3", fg="black")
label_num1.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada1 = tk.Entry(janela, font=("Arial", 12),
                    bg="#FFFFCC", fg="black", width=20)
entrada1.grid(row=1, column=1, padx=10, pady=10)

# Campo para a inserção do segundo número.
label_num2 = tk.Label(janela, text="Insira o 2 número:",
                      font=("Arial", 12), bg="#D3D3D3", fg="black")
label_num2.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada2 = tk.Entry(janela, font=("Arial", 12),
                    bg="#FFFFCC", fg="black", width=20)
entrada2.grid(row=2, column=1, padx=10, pady=10)

# Botões que serão utilziados nas operações matemáticas
botoes = [
    ("Adição (+)", "adicao"),
    ("Subtração (-)", "subtracao"),
    ("Multiplicação (*)", "multiplicacao"),
    ("Divisão (/)", "divisao"),
]
for i, (texto, operacao) in enumerate(botoes):
    botao = tk.Button(
        janela,
        text=texto,
        command=lambda op=operacao: realizar_operacao(op),
        font=("Arial", 12),
        bg="#4caf50",
        fg="white",
        activebackground="#45a049",
        activeforeground="white",
        relief="raised",
        borderwidth=2
    )
    botao.grid(row=3+i, column=0, columnspan=2, pady=5, padx=20, sticky="nsew")

label_resultado = tk.Label(janela, text="Resultado: ", font=(
    "Arial", 14), fg="black", bg="#FFFFCC", relief="solid", bd=2)
label_resultado.grid(row=7, column=0, columnspan=2,
                     pady=20, padx=20, sticky="nsew")

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

janela.mainloop()
