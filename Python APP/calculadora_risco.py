import tkinter as tk
from tkinter import ttk

class CalculadoraFibonacci:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora de Fibonacci")
        self.janela.geometry("500x800")
        
        # Variáveis principais
        self.tipo_contrato = tk.StringVar(value="WDO")
        self.tipo_calculo = tk.StringVar(value="valor")
        self.valor_risco = tk.StringVar()
        self.pontos_risco = tk.StringVar()
        self.capital_total = tk.StringVar()
        self.risco_porcentagem = tk.StringVar()
        self.quantidade_contratos = tk.StringVar(value="0")
        self.risco_por_contrato = tk.StringVar(value="R$ 0,00")
        self.risco_total = tk.StringVar(value="R$ 0,00")
        self.ganho_total = tk.StringVar(value="R$ 0,00")
        
        # Valores padrão para as porcentagens dos alvos
        self.porcentagens_padrao = [35, 25, 20, 10, 10]
        
        # Variáveis para as porcentagens dos alvos
        self.porcentagens = []
        for i in range(5):
            self.porcentagens.append(tk.StringVar(value=str(self.porcentagens_padrao[i])))
        
        # Variáveis para os ganhos de Fibonacci
        self.ganhos_fibonacci = []
        for _ in range(5):
            self.ganhos_fibonacci.append(tk.StringVar(value="R$ 0,00"))
        
        # Variáveis para contratos por alvo
        self.contratos_por_alvo = []
        for _ in range(5):
            self.contratos_por_alvo.append(tk.StringVar(value="(0 contratos)"))
        
        # Frame principal
        main_frame = ttk.Frame(self.janela, padding=10)
        main_frame.pack(fill="both", expand=True)
        
        # Frame de tipo de contrato
        frame_contrato = ttk.LabelFrame(main_frame, text="Tipo de Contrato", padding=5)
        frame_contrato.pack(fill="x", pady=5)
        
        ttk.Radiobutton(frame_contrato, text="Mini Dólar (WDO) - R$ 10,00/ponto", 
                       variable=self.tipo_contrato, value="WDO").pack(side="left", padx=5)
        ttk.Radiobutton(frame_contrato, text="Mini Índice (WIN) - R$ 0,20/ponto", 
                       variable=self.tipo_contrato, value="WIN").pack(side="left", padx=5)
        
        # Frame de tipo de cálculo
        frame_tipo = ttk.LabelFrame(main_frame, text="Tipo de Cálculo", padding=5)
        frame_tipo.pack(fill="x", pady=5)
        
        ttk.Radiobutton(frame_tipo, text="Valor Fixo", variable=self.tipo_calculo, value="valor", 
                       command=self.atualizar_campos).pack(side="left", padx=5)
        ttk.Radiobutton(frame_tipo, text="Porcentagem", variable=self.tipo_calculo, value="porcentagem", 
                       command=self.atualizar_campos).pack(side="left", padx=5)
        
        # Frame de entrada
        frame_entrada = ttk.LabelFrame(main_frame, text="Dados da Operação", padding=5)
        frame_entrada.pack(fill="x", pady=5)
        
        # Frame para valor fixo
        self.frame_valor = ttk.Frame(frame_entrada)
        ttk.Label(self.frame_valor, text="Valor de Risco (R$):").pack(anchor="w")
        ttk.Entry(self.frame_valor, textvariable=self.valor_risco).pack(fill="x", pady=2)
        
        # Frame para porcentagem
        self.frame_porcentagem = ttk.Frame(frame_entrada)
        ttk.Label(self.frame_porcentagem, text="Capital Total (R$):").pack(anchor="w")
        ttk.Entry(self.frame_porcentagem, textvariable=self.capital_total).pack(fill="x", pady=2)
        
        # Frame para risco em porcentagem
        frame_risco = ttk.Frame(self.frame_porcentagem)
        frame_risco.pack(fill="x", pady=2)
        ttk.Label(frame_risco, text="Risco do Capital (%):").pack(side="left")
        ttk.Entry(frame_risco, textvariable=self.risco_porcentagem, width=5).pack(side="left", padx=5)
        self.label_valor_risco = ttk.Label(frame_risco, text="R$ 0,00")
        self.label_valor_risco.pack(side="left")
        
        # Frame para pontos de risco
        self.frame_pontos = ttk.Frame(frame_entrada)
        self.frame_pontos.pack(fill="x", pady=2)
        ttk.Label(self.frame_pontos, text="Pontos de Risco:").pack(anchor="w")
        ttk.Entry(self.frame_pontos, textvariable=self.pontos_risco).pack(fill="x", pady=2)
        
        # Frame de botões
        frame_botoes = ttk.Frame(main_frame)
        frame_botoes.pack(fill="x", pady=5)
        
        ttk.Button(frame_botoes, text="Calcular", command=self.calcular).pack(side="left", padx=5)
        ttk.Button(frame_botoes, text="Resetar %", command=self.resetar_porcentagens).pack(side="left", padx=5)
        
        # Frame de resultados
        frame_resultado = ttk.LabelFrame(main_frame, text="Resultados", padding=5)
        frame_resultado.pack(fill="x", pady=5)
        
        # Labels de resultado
        ttk.Label(frame_resultado, text="Quantidade de Contratos:").pack(anchor="w")
        ttk.Label(frame_resultado, textvariable=self.quantidade_contratos, font=("Arial", 12, "bold")).pack(anchor="w")
        
        ttk.Label(frame_resultado, text="Risco por Contrato:").pack(anchor="w")
        ttk.Label(frame_resultado, textvariable=self.risco_por_contrato, font=("Arial", 12, "bold")).pack(anchor="w")
        
        ttk.Label(frame_resultado, text="Risco Total:").pack(anchor="w")
        ttk.Label(frame_resultado, textvariable=self.risco_total, font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Frame de Fibonacci
        frame_fibonacci = ttk.LabelFrame(main_frame, text="Níveis de Fibonacci", padding=5)
        frame_fibonacci.pack(fill="x", pady=5)
        
        # Labels e campos de entrada para cada nível de Fibonacci
        for i, (nivel, descricao) in enumerate([
            (0.618, "Primeiro alvo"),
            (1.000, "Segundo alvo"),
            (1.618, "Terceiro alvo"),
            (2.000, "Quarto alvo"),
            (2.618, "Quinto alvo")
        ]):
            frame_nivel = ttk.Frame(frame_fibonacci)
            frame_nivel.pack(fill="x", pady=2)
            
            # Nível e descrição
            ttk.Label(frame_nivel, text=f"{nivel*100:.1f}% - {descricao}").pack(side="left")
            
            # Porcentagem de distribuição
            frame_porcentagem = ttk.Frame(frame_nivel)
            frame_porcentagem.pack(side="left", padx=5)
            entry = ttk.Entry(frame_porcentagem, textvariable=self.porcentagens[i], width=3)
            entry.pack(side="left")
            ttk.Label(frame_porcentagem, text="%").pack(side="left")
            
            # Quantidade de contratos
            ttk.Label(frame_nivel, textvariable=self.contratos_por_alvo[i], font=("Arial", 10)).pack(side="left", padx=5)
            
            # Ganho
            ttk.Label(frame_nivel, textvariable=self.ganhos_fibonacci[i], font=("Arial", 10, "bold")).pack(side="right")
        
        # Frame de ganho total
        frame_ganho_total = ttk.LabelFrame(main_frame, text="Ganho Total", padding=5)
        frame_ganho_total.pack(fill="x", pady=5)
        
        ttk.Label(frame_ganho_total, text="Ganho Potencial Total:", font=("Arial", 12, "bold")).pack(anchor="w")
        ttk.Label(frame_ganho_total, textvariable=self.ganho_total, font=("Arial", 14, "bold"), foreground="green").pack(anchor="w", pady=5)
        
        # Bindings
        self.pontos_risco.trace_add("write", lambda *args: self.calcular())
        self.valor_risco.trace_add("write", lambda *args: self.calcular())
        self.capital_total.trace_add("write", lambda *args: self.calcular())
        self.risco_porcentagem.trace_add("write", lambda *args: self.calcular())
        for porcentagem in self.porcentagens:
            porcentagem.trace_add("write", lambda *args: self.calcular())
        
        # Inicializar campos
        self.atualizar_campos()
    
    def resetar_porcentagens(self):
        """Reseta as porcentagens dos alvos para os valores padrão"""
        for i, valor in enumerate(self.porcentagens_padrao):
            self.porcentagens[i].set(str(valor))
        self.calcular()  # Recalcula com os valores padrão
    
    def atualizar_campos(self):
        tipo = self.tipo_calculo.get()
        if tipo == "valor":
            self.frame_porcentagem.pack_forget()
            self.frame_valor.pack(fill="x", pady=2, before=self.frame_pontos)
        else:
            self.frame_valor.pack_forget()
            self.frame_porcentagem.pack(fill="x", pady=2, before=self.frame_pontos)
    
    def calcular(self):
        try:
            # Validar pontos de risco
            try:
                pontos_risco = float(self.pontos_risco.get().replace(',', '.'))
                if pontos_risco <= 0:
                    raise ValueError("Pontos de risco devem ser maiores que zero")
            except ValueError as e:
                self.ganho_total.set("Erro: " + str(e))
                return
            
            # Calcular valor de risco baseado no tipo de cálculo
            try:
                if self.tipo_calculo.get() == "valor":
                    valor_risco = float(self.valor_risco.get().replace(',', '.'))
                    if valor_risco <= 0:
                        raise ValueError("Valor de risco deve ser maior que zero")
                else:
                    capital = float(self.capital_total.get().replace(',', '.'))
                    if capital <= 0:
                        raise ValueError("Capital total deve ser maior que zero")
                    risco_porcentagem = float(self.risco_porcentagem.get().replace(',', '.'))
                    if risco_porcentagem <= 0 or risco_porcentagem > 100:
                        raise ValueError("Porcentagem de risco deve estar entre 0 e 100")
                    valor_risco = capital * (risco_porcentagem / 100)
                    self.valor_risco.set(f"{valor_risco:,.2f}".replace('.', ','))
                    self.label_valor_risco.config(text=f"R$ {valor_risco:,.2f}".replace('.', ','))
            except ValueError as e:
                self.ganho_total.set("Erro: " + str(e))
                self.label_valor_risco.config(text="R$ 0,00")
                return
            
            # Valor por ponto baseado no tipo de contrato
            valor_por_ponto = 10.00 if self.tipo_contrato.get() == "WDO" else 0.20
            risco_por_contrato = pontos_risco * valor_por_ponto
            
            # Calcular quantidade de contratos
            quantidade = int(valor_risco / risco_por_contrato)
            if quantidade < 1:
                self.ganho_total.set("Erro: Risco muito baixo para operar")
                return
                
            risco_total = quantidade * risco_por_contrato
            
            # Atualizar variáveis principais
            self.quantidade_contratos.set(str(quantidade))
            self.risco_por_contrato.set(f"R$ {risco_por_contrato:,.2f}".replace('.', ','))
            self.risco_total.set(f"R$ {risco_total:,.2f}".replace('.', ','))
            
            # Calcular ganhos para cada nível de Fibonacci
            ganho_total = 0
            
            # Se tiver mais de 5 contratos, distribui conforme as porcentagens
            if quantidade >= 5:
                # Validar porcentagens
                porcentagens = []
                soma_porcentagens = 0
                for i in range(5):
                    try:
                        porcentagem = float(self.porcentagens[i].get().replace(',', '.'))
                        if porcentagem < 0 or porcentagem > 100:
                            raise ValueError(f"Porcentagem do alvo {i+1} deve estar entre 0 e 100")
                        porcentagens.append(porcentagem / 100)
                        soma_porcentagens += porcentagem
                    except ValueError as e:
                        self.ganho_total.set("Erro: " + str(e))
                        return
                    except:
                        # Usar valores padrão em caso de erro
                        porcentagem = 35 if i == 0 else 25 if i == 1 else 20 if i == 2 else 10
                        porcentagens.append(porcentagem / 100)
                        soma_porcentagens += porcentagem
                
                # Validar soma das porcentagens
                if soma_porcentagens > 100:
                    self.ganho_total.set("Erro: A soma das porcentagens dos alvos não pode exceder 100%")
                    return
                
                # Normalizar porcentagens se a soma for menor que 100%
                if soma_porcentagens < 100:
                    for i in range(5):
                        porcentagens[i] = porcentagens[i] / soma_porcentagens
                
                # Distribuir contratos
                contratos_distribuidos = 0
                contratos_por_alvo = [0] * 5
                
                # Primeiro, distribuir contratos para alvos com porcentagem > 0
                for i in range(5):
                    if porcentagens[i] > 0:
                        contratos_alvo = int(quantidade * porcentagens[i])
                        if contratos_alvo < 1:  # Garante pelo menos 1 contrato por alvo com % > 0
                            contratos_alvo = 1
                        contratos_por_alvo[i] = contratos_alvo
                        contratos_distribuidos += contratos_alvo
                
                # Ajustar último alvo com % > 0 se necessário
                if contratos_distribuidos != quantidade:
                    # Encontrar o último alvo com % > 0
                    ultimo_alvo = max([i for i, p in enumerate(porcentagens) if p > 0])
                    contratos_por_alvo[ultimo_alvo] += (quantidade - contratos_distribuidos)
                
                # Atualizar interface com os contratos distribuídos
                for i, (nivel, _) in enumerate([
                    (0.618, "Primeiro alvo"),
                    (1.000, "Segundo alvo"),
                    (1.618, "Terceiro alvo"),
                    (2.000, "Quarto alvo"),
                    (2.618, "Quinto alvo")
                ]):
                    contratos_alvo = contratos_por_alvo[i]
                    self.contratos_por_alvo[i].set(f"({contratos_alvo} contratos)")
                    pontos_ganho = pontos_risco * nivel
                    ganho = pontos_ganho * valor_por_ponto * contratos_alvo
                    ganho_total += ganho
                    self.ganhos_fibonacci[i].set(f"R$ {ganho:,.2f}".replace('.', ','))
            else:
                # Se tiver menos de 5 contratos, distribui um por alvo até acabar
                for i, (nivel, _) in enumerate([
                    (0.618, "Primeiro alvo"),
                    (1.000, "Segundo alvo"),
                    (1.618, "Terceiro alvo"),
                    (2.000, "Quarto alvo"),
                    (2.618, "Quinto alvo")
                ]):
                    if i < quantidade:
                        contratos_alvo = 1
                        self.contratos_por_alvo[i].set(f"({contratos_alvo} contrato)")
                        pontos_ganho = pontos_risco * nivel
                        ganho = pontos_ganho * valor_por_ponto
                        ganho_total += ganho
                        self.ganhos_fibonacci[i].set(f"R$ {ganho:,.2f}".replace('.', ','))
                    else:
                        self.contratos_por_alvo[i].set("(0 contratos)")
                        self.ganhos_fibonacci[i].set("R$ 0,00")
            
            # Atualizar ganho total
            self.ganho_total.set(f"R$ {ganho_total:,.2f}".replace('.', ','))
            
        except Exception as e:
            self.ganho_total.set(f"Erro: {str(e)}")
            self.quantidade_contratos.set("0")
            self.risco_por_contrato.set("R$ 0,00")
            self.risco_total.set("R$ 0,00")
            for ganho_var in self.ganhos_fibonacci:
                ganho_var.set("R$ 0,00")
            for contratos_var in self.contratos_por_alvo:
                contratos_var.set("(0 contratos)")
    
    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    calculadora = CalculadoraFibonacci()
    calculadora.run() 