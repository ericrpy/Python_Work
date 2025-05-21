import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import os
from tabulate import tabulate
import matplotlib.pyplot as plt

arquivo_csv = 'vendas.csv'

# lista para armazenar as vendas
vendas = []

# função para limpar os campos
def limpar_campos():
    entrada_produto.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)
    entrada_custo.delete(0, tk.END)

# função para registrar vendas
def registrar_venda():
    produto = entrada_produto.get()
    quantidade = int(entrada_quantidade.get())
    preco = float(entrada_preco.get())
    custo = float(entrada_custo.get())
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    venda = {
        'Produto': produto,
        'Quantidade': quantidade,
        'Preco': preco,
        "Custo": custo,
        "Data": data,
        "Lucro": (preco - custo) * quantidade
    }    
    
# verifica se o arquivo já existe
    if os.path.exists(arquivo_csv):
        df = pd.read_csv(arquivo_csv)
        df = pd.concat([df, pd.DataFrame([venda])], ignore_index=True)
    else:
        df = pd.DataFrame([venda])
# salva no arquivo .csv

    df.to_csv(arquivo_csv, index=False)

#    vendas.append(venda)
    messagebox.showinfo("Venda registrada com sucesso!")
    limpar_campos()

def exibir_texto_em_janela(texto, titulo="Texto"):
    nova_janela = tk.Toplevel(janela)
    nova_janela.title(titulo)
    nova_janela.geometry("800x600")

    texto_box = tk.Text(nova_janela, wrap="none")
    texto_box.insert(tk.END, texto)
    texto_box.config(state="disabled")
    texto_box.pack(expand=True, fill="both")


# função para exibir vendas
def exibir_vendas():
    if not os.path.exists(arquivo_csv):
        messagebox.showinfo("Vendas", "Nenhuma venda registrada ainda.")
        return
    
    df = pd.read_csv(arquivo_csv)
    total_lucro = df['Lucro'].sum()

    tabela = tabulate(df, headers='keys', tablefmt='grid', showindex=False)
    mensagem = f"{tabela}\n\nLucro total: R$ {total_lucro:.2f}"

    # Exibir em uma janela maior
    exibir_texto_em_janela(mensagem, titulo="Relatório de Vendas")

# Janela principal
janela = tk.Tk()
janela.title("Controle Financeiro - Yesca Bolos")
janela.geometry("350x250")

# Campos
tk.Label(janela, text='Produto').grid(row=0, column=0)
entrada_produto = tk.Entry(janela, width=20)
entrada_produto.grid(row=0, column=1)

tk.Label(janela, text="Quantidade:").grid(row=1, column=0)
entrada_quantidade = tk.Entry(janela, width=20)
entrada_quantidade.grid(row=1, column=1)

tk.Label(janela, text="Preço (R$):").grid(row=2, column=0)
entrada_preco = tk.Entry(janela, width=20)
entrada_preco.grid(row=2, column=1)

tk.Label(janela, text="Custo (R$):").grid(row=3, column=0)
entrada_custo = tk.Entry(janela, width=20)
entrada_custo.grid(row=3, column=1)

# Botões
tk.Button(janela, text="Registrar Venda", command=registrar_venda).grid(row=5, column=1, padx=40, pady=20)
tk.Button(janela, text="Exibir Vendas", command=exibir_vendas).grid(row=5, column=0, padx=40, pady=20)

# gerando um gráfico
def gerar_grafico_por_data():
    if not os.path.exists(arquivo_csv):
        messagebox.showinfo("Aviso", "Nenhuma venda registrada ainda.")
        return

    df = pd.read_csv(arquivo_csv)

    # Converter coluna 'Data' para datetime
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

    # Calcular valor total de cada venda
    df['Valor_Total'] = df['Quantidade'] * df['Preco']

    # Agrupar por dia
    resumo = df.groupby(df['Data'].dt.date)['Valor_Total'].sum()

    # Criar gráfico
    plt.figure(figsize=(10, 6))
    resumo.plot(kind='bar', color='lightgreen', edgecolor='black')

    plt.title('Vendas por Data')
    plt.xlabel('Data')
    plt.ylabel('Valor Total (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()



tk.Button(janela, text="Gerar Gráfico", command=gerar_grafico_por_data).grid(
    row=7, column=0, columnspan=2, pady=10, sticky="we"
)


# Rodar o programa
janela.mainloop()