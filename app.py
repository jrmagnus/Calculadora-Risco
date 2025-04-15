import tkinter as tk
from tkinter import ttk

class CalculadoraContratos:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("📊 Calculadora de Contratos")

        # Centralizar janela
        largura = 400
        altura = 400
        x = (self.janela.winfo_screenwidth() - largura) // 2
        y = (self.janela.winfo_screenheight() - altura) // 3
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")
        self.janela.resizable(False, False)

        self.tipo_calculo = tk.StringVar(value="valor")
        self.ativo = tk.StringVar(value="mini_dolar")

        fonte_label = ("Arial", 10)
        padding = {"padx": 10, "pady": 5}

        # ====== Tipo de Cálculo ======
        frame_tipo = ttk.LabelFrame(self.janela, text="Tipo de Cálculo")
        frame_tipo.grid(row=0, column=0, columnspan=2, sticky="we", **padding)

        ttk.Radiobutton(frame_tipo, text="Valor", variable=self.tipo_calculo, value="valor", command=self.atualizar_campos).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(frame_tipo, text="Porcentagem", variable=self.tipo_calculo, value="porcentagem", command=self.atualizar_campos).grid(row=0, column=1, padx=5, pady=5)

        # ====== Campos ======
        ttk.Label(self.janela, text="Capital Total (R$):", font=fonte_label).grid(row=1, column=0, sticky="e", **padding)
        self.capital_entry = ttk.Entry(self.janela)
        self.capital_entry.grid(row=1, column=1, **padding)

        ttk.Label(self.janela, text="Risco (%):", font=fonte_label).grid(row=2, column=0, sticky="e", **padding)
        self.risco_porcentagem_entry = ttk.Entry(self.janela)
        self.risco_porcentagem_entry.grid(row=2, column=1, **padding)

        ttk.Label(self.janela, text="Risco (R$):", font=fonte_label).grid(row=3, column=0, sticky="e", **padding)
        self.valor_risco_entry = ttk.Entry(self.janela)
        self.valor_risco_entry.grid(row=3, column=1, **padding)

        ttk.Label(self.janela, text="Tamanho da Operação (pts):", font=fonte_label).grid(row=4, column=0, sticky="e", **padding)
        self.tamanho_operacao_entry = ttk.Entry(self.janela)
        self.tamanho_operacao_entry.grid(row=4, column=1, **padding)

        # ====== Ativo ======
        frame_ativo = ttk.LabelFrame(self.janela, text="Ativo")
        frame_ativo.grid(row=5, column=0, columnspan=2, sticky="we", **padding)

        ttk.Radiobutton(frame_ativo, text="Mini Dólar", variable=self.ativo, value="mini_dolar").grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(frame_ativo, text="Mini Índice", variable=self.ativo, value="mini_indice").grid(row=0, column=1, padx=5, pady=5)

        # ====== Botão Calcular ======
        calcular_btn = ttk.Button(self.janela, text="🔍 Calcular", command=self.calcular_contratos)
        calcular_btn.grid(row=6, column=0, columnspan=2, pady=15)

        # ====== Resultado ======
        self.resultado_label = tk.Label(
            self.janela,
            text="",
            font=("Arial", 13, "bold"),
            fg="#003366",
            bg="#e6f2ff",
            relief="solid",
            bd=1,
            width=40,
            height=3,
            justify="center"
        )
        self.resultado_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.atualizar_campos()

    def atualizar_campos(self):
        tipo = self.tipo_calculo.get()
        if tipo == "valor":
            self.capital_entry.grid_remove()
            self.risco_porcentagem_entry.grid_remove()
            self.valor_risco_entry.configure(state="normal")
        else:
            self.capital_entry.grid()
            self.risco_porcentagem_entry.grid()
            self.valor_risco_entry.configure(state="readonly")

    def calcular_contratos(self):
        try:
            tipo = self.tipo_calculo.get()

            if tipo == "valor":
                valor_risco = float(self.valor_risco_entry.get().replace(',', '.'))
            else:
                capital = float(self.capital_entry.get().replace(',', '.'))
                risco_porcentagem = float(self.risco_porcentagem_entry.get().replace(',', '.'))
                valor_risco = capital * (risco_porcentagem / 100)
                self.valor_risco_entry.configure(state="normal")
                self.valor_risco_entry.delete(0, tk.END)
                self.valor_risco_entry.insert(0, f"{valor_risco:,.2f}".replace('.', ','))
                self.valor_risco_entry.configure(state="readonly")

            tamanho_operacao = float(self.tamanho_operacao_entry.get().replace(',', '.'))

            valor_por_ponto = 10.00 if self.ativo.get() == "mini_dolar" else 0.20
            risco_por_contrato = tamanho_operacao * valor_por_ponto
            quantidade_contratos = int(valor_risco / risco_por_contrato)
            risco_real = quantidade_contratos * risco_por_contrato

            self.resultado_label.config(
                text=f"🧮 Contratos: {quantidade_contratos}\n💰 Risco real: R$ {risco_real:,.2f}".replace('.', ','),
                bg="#e6f2ff",
                fg="#003366"
            )
        except Exception as e:
            self.resultado_label.config(text=f"Erro: {str(e)}", fg="red", bg="white")

    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    calculadora = CalculadoraContratos()
    calculadora.run()
