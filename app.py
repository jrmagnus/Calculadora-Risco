import tkinter as tk

class CalculadoraContratos:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora de Contratos")

        # Campos de entrada
        self.valor_risco_label = tk.Label(self.janela, text="Valor de Risco (R$):")
        self.valor_risco_label.grid(row=0, column=0)
        self.valor_risco_entry = tk.Entry(self.janela)
        self.valor_risco_entry.grid(row=0, column=1)

        self.tamanho_operacao_label = tk.Label(self.janela, text="Tamanho da Operação (pontos):")
        self.tamanho_operacao_label.grid(row=1, column=0)
        self.tamanho_operacao_entry = tk.Entry(self.janela)
        self.tamanho_operacao_entry.grid(row=1, column=1)

        self.valor_por_ponto_label = tk.Label(self.janela, text="Valor por Ponto (R$):")
        self.valor_por_ponto_label.grid(row=2, column=0)
        self.valor_por_ponto_entry = tk.Entry(self.janela)
        self.valor_por_ponto_entry.grid(row=2, column=1)

        # Botão de cálculo
        self.calcular_button = tk.Button(self.janela, text="Calcular", command=self.calcular_contratos)
        self.calcular_button.grid(row=3, column=0, columnspan=2)

        # Resultado
        self.resultado_label = tk.Label(self.janela, text="Quantidade de Contratos:")
        self.resultado_label.grid(row=4, column=0)
        self.resultado_text = tk.Text(self.janela, height=1, width=10)
        self.resultado_text.grid(row=4, column=1)

    def calcular_contratos(self):
        valor_risco = float(self.valor_risco_entry.get().replace(',', '.'))
        tamanho_operacao = float(self.tamanho_operacao_entry.get().replace(',', '.'))
        valor_por_ponto = float(self.valor_por_ponto_entry.get().replace(',', '.'))

        risco_por_contrato = tamanho_operacao * valor_por_ponto
        quantidade_contratos = int(valor_risco / risco_por_contrato)

        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, str(quantidade_contratos))

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    calculadora = CalculadoraContratos()
    calculadora.run()