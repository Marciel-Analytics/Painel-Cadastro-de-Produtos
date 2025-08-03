"""Projeto painel de cadastro de produtos"""

import tkinter as tk
from tkinter import messagebox

def cadastrar_produto():
    """Função para cadastrar um novo produto."""
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    valor = entry_valor.get()
    disponivel = var_disponivel.get()

    if not nome or not valor:
        messagebox.showerror("Erro", "Nome e Valor do produto são obrigatórios.")
        return

    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "O valor deve ser um número válido.")
        return

    produtos.append({
        "nome": nome,
        "descricao": descricao,
        "valor": valor,
        "disponivel": disponivel,
    })

    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    janela_cadastro.destroy()
    listar_produtos()

def listar_produtos():
    """Função para exibir a listagem de produtos."""
    for widget in janela.winfo_children():
        widget.destroy()

    # Título
    tk.Label(janela, text="Listagem de Produtos", font=("Arial", 16)).pack(pady=10)

    # Cabeçalho da tabela
    frame_tabela = tk.Frame(janela)
    frame_tabela.pack()
    tk.Label(frame_tabela, text="Nome", width=20, borderwidth=1, relief="solid").grid(row=0, column=0)
    tk.Label(frame_tabela, text="Valor", width=20, borderwidth=1, relief="solid").grid(row=0, column=1)

    # Ordenar e exibir produtos
    for i, produto in enumerate(sorted(produtos, key=lambda p: p["valor"])):
        tk.Label(frame_tabela, text=produto["nome"], width=20, borderwidth=1, relief="solid").grid(row=i + 1, column=0)
        tk.Label(frame_tabela, text=f"R$ {produto['valor']:.2f}", width=20, borderwidth=1, relief="solid").grid(row=i + 1, column=1)

    # Botão para cadastrar novo produto
    tk.Button(janela, text="Cadastrar Novo Produto", command=abrir_cadastro).pack(pady=10)

def abrir_cadastro():
    """Função para abrir a janela de cadastro."""
    global janela_cadastro, entry_nome, entry_descricao, entry_valor, var_disponivel

    janela_cadastro = tk.Toplevel(janela)
    janela_cadastro.title("Cadastro de Produto")

    # Formulário
    tk.Label(janela_cadastro, text="Nome do Produto:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_nome = tk.Entry(janela_cadastro, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(janela_cadastro, text="Descrição do Produto:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_descricao = tk.Entry(janela_cadastro, width=30)
    entry_descricao.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela_cadastro, text="Valor do Produto:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_valor = tk.Entry(janela_cadastro, width=30)
    entry_valor.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(janela_cadastro, text="Disponível para Venda:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    var_disponivel = tk.StringVar(value="sim")
    tk.Radiobutton(janela_cadastro, text="Sim", variable=var_disponivel, value="sim").grid(row=3, column=1, sticky="w")
    tk.Radiobutton(janela_cadastro, text="Não", variable=var_disponivel, value="não").grid(row=3, column=1, sticky="e")

    # Botão de salvar
    tk.Button(janela_cadastro, text="Salvar", command=cadastrar_produto).grid(row=4, column=0, columnspan=2, pady=10)

# Lista de produtos
produtos = []

# Janela principal
janela = tk.Tk()
janela.title("Gestão de Produtos")
janela.geometry("400x300")

listar_produtos()

janela.mainloop()

"""FIM"""