import tkinter as tk
from tkinter import messagebox
import json
import os
entregas = []
entregas_concluidas = []

ARQUIVO_ENTREGAS = "entregas.json"

def salvar_dados():
    with open(ARQUIVO_ENTREGAS, 'w', encoding='utf-8') as f:
        json.dump({"pendentes": entregas, "concluidas": entregas_concluidas}, f, ensure_ascii=False, indent=4)

def carregar_dados():
    if os.path.exists(ARQUIVO_ENTREGAS):
        with open(ARQUIVO_ENTREGAS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            entregas.extend(dados.get("pendentes", []))
            entregas_concluidas.extend(dados.get("concluidas", []))

def cadastrar_entrega():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    if nome and endereco:
        entrega = {'nome': nome, 'endereco': endereco}
        entregas.append(entrega)
        entry_nome.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        atualizar_listas()
        messagebox.showinfo("✅ Sucesso", "Entrega cadastrada com sucesso.")
    else:
        messagebox.showwarning("⚠️ Atenção", "Preencha todos os campos.")
    salvar_dados()
def concluir_entrega():
    selecionado = listbox_pendentes.curselection()
    if selecionado:
        index = selecionado[0]
        entrega = entregas.pop(index)
        entregas_concluidas.append(entrega)
        atualizar_listas()
        messagebox.showinfo("✅ Sucesso", "Entrega marcada como concluída.")
    else:
        messagebox.showwarning("⚠️ Atenção", "Selecione uma entrega pendente.")
    salvar_dados()
def atualizar_listas():
    listbox_pendentes.delete(0, tk.END)
    for e in entregas:
        listbox_pendentes.insert(tk.END, f"📦 {e['nome']} - {e['endereco']}")

    listbox_concluidas.delete(0, tk.END)
    for e in entregas_concluidas:
        listbox_concluidas.insert(tk.END, f"✅ {e['nome']} - {e['endereco']}")
    salvar_dados()
def listar_entregas():
    todas_janela = tk.Toplevel(janela)
    todas_janela.title("📋 Todas as Entregas")
    todas_janela.configure(bg="#f0f0f0")
    todas_janela.geometry("500x400")
    tk.Label(todas_janela, text="📦 Pendentes", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
    if not entregas:
        tk.Label(todas_janela, text="Nenhuma pendente", bg="#f0f0f0").pack()
    else:
        for e in entregas:
            tk.Label(todas_janela, text=f"• {e['nome']} - {e['endereco']}", bg="#f0f0f0").pack()

    tk.Label(todas_janela, text="✅ Concluídas", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
    if not entregas_concluidas:
        tk.Label(todas_janela, text="Nenhuma concluída", bg="#f0f0f0").pack()
    else:
        for e in entregas_concluidas:
            tk.Label(todas_janela, text=f"• {e['nome']} - {e['endereco']}", bg="#f0f0f0").pack()

def listar_pendentes_popup():
    pendentes_janela = tk.Toplevel(janela)
    pendentes_janela.title("📦 Entregas Pendentes")
    pendentes_janela.configure(bg="#fff")
    pendentes_janela.geometry("400x300")
    if not entregas:
        tk.Label(pendentes_janela, text="Nenhuma entrega pendente.", bg="#fff").pack(pady=10)
    else:
        for i, e in enumerate(entregas, 1):
            tk.Label(pendentes_janela, text=f"{i}. {e['nome']} - {e['endereco']}", bg="#fff").pack()

def listar_concluidas_popup():
    concluidas_janela = tk.Toplevel(janela)
    concluidas_janela.title("✅ Entregas Concluídas")
    concluidas_janela.configure(bg="#fff")
    concluidas_janela.geometry("400x300")
    if not entregas_concluidas:
        tk.Label(concluidas_janela, text="Nenhuma entrega concluída.", bg="#fff").pack(pady=10)
    else:
        for i, e in enumerate(entregas_concluidas, 1):
            tk.Label(concluidas_janela, text=f"{i}. {e['nome']} - {e['endereco']}", bg="#fff").pack()

def sair():
    janela.quit()

janela = tk.Tk()
carregar_dados()
janela.title(" Sistema de Entregas")
janela.attributes('-fullscreen', True)
janela.configure(bg="#e8bdfb")

frame_central = tk.Frame(janela, bg="#e6f2ff", bd=2, relief="groove")
frame_central.place(relx=0.5, rely=0.5, anchor="center", width=900, height=600)

frame_central.grid_rowconfigure(5, weight=1)
frame_central.grid_columnconfigure(0, weight=1)

label_titulo = tk.Label(frame_central, text="📦 Sistema de Entregas", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#003366")
label_titulo.grid(row=0, column=0, pady=(10,5))

label_subtitulo1 = tk.Label(frame_central, text="EMIEP - Desenvolvimento de Sistemas", font=("Arial", 12), bg="#e6f2ff")
label_subtitulo1.grid(row=1, column=0)

label_subtitulo2 = tk.Label(frame_central, text="Feito por: David\n", font=("Arial", 12), bg="#e6f2ff")
label_subtitulo2.grid(row=2, column=0)

frame_inputs = tk.Frame(frame_central, bg="#e6f2ff")
frame_inputs.grid(row=3, column=0, sticky="ew", padx=30)
frame_inputs.grid_columnconfigure(1, weight=1)

tk.Label(frame_inputs, text=" Nome do cliente:",font=("Arial",14), bg="#e6f2ff").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nome = tk.Entry(frame_inputs, font=("Arial", 14), width=40)
entry_nome.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

tk.Label(frame_inputs, text="📍 Endereço da entrega:",font=("Arial",14), bg="#e6f2ff").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_endereco = tk.Entry(frame_inputs, font=("Arial", 14),width=40)
entry_endereco.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

btn_cadastrar = tk.Button(frame_central, text="➕ Cadastrar Entrega", bg="#99ccff", font=("Arial", 14), command=cadastrar_entrega)
btn_cadastrar.grid(row=4, column=0, pady=10, sticky="ew", padx=30)

frame_principal = tk.Frame(frame_central, bg="#e6f2ff")
frame_principal.grid(row=5, column=0, sticky="nsew", padx=30, pady=10)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)

label_pendentes = tk.Label(frame_principal, text="📦 Entregas Pendentes", font=("Arial", 12, "bold"), bg="#e6f2ff")
label_pendentes.grid(row=0, column=0, sticky="nsew", padx=10)

label_concluidas = tk.Label(frame_principal, text="✅ Entregas Concluídas", font=("Arial", 12, "bold"), bg="#e6f2ff")
label_concluidas.grid(row=0, column=1, sticky="nsew", padx=10)

listbox_pendentes = tk.Listbox(frame_principal)
listbox_pendentes.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

listbox_concluidas = tk.Listbox(frame_principal)
listbox_concluidas.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

frame_botoes = tk.Frame(frame_central, bg="#e6f2ff")
frame_botoes.grid(row=6, column=0, sticky="ew", padx=30, pady=10)
for i in range(5):
    frame_botoes.grid_columnconfigure(i, weight=1)

btn_concluir = tk.Button(frame_botoes, text="✔️ Concluir Entrega", bg="#b3ffb3", font=("Arial", 12), command=concluir_entrega)
btn_concluir.grid(row=0, column=0, sticky="ew", padx=5)

btn_listar_entregas = tk.Button(frame_botoes, text="📋 Listar Entregas", bg="#ffffcc", font=("Arial", 12), command=listar_entregas)
btn_listar_entregas.grid(row=0, column=1, sticky="ew", padx=5)

btn_listar_pendentes = tk.Button(frame_botoes, text="📦 Pendentes", bg="#cce5ff", font=("Arial", 12), command=listar_pendentes_popup)
btn_listar_pendentes.grid(row=0, column=2, sticky="ew", padx=5)

btn_listar_concluidas = tk.Button(frame_botoes, text="✅ Concluídas", bg="#d1ffd1", font=("Arial", 12), command=listar_concluidas_popup)
btn_listar_concluidas.grid(row=0, column=3, sticky="ew", padx=5)

btn_sair = tk.Button(frame_botoes, text="❌ Sair", bg="#ffcccc", font=("Arial", 12), command=sair)
btn_sair.grid(row=0, column=4, sticky="ew", padx=5)

atualizar_listas()
janela.mainloop()