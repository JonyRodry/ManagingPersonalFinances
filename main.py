# Importar bibliotecas
import customtkinter as ctk
from tkcalendar import *
import datetime

# Criar a janela
interface = ctk.CTk()

# Configurar a janela principal
interface.title("Managing Personal Finances")
interface.geometry("400x800")

# Colunas a preencher no Excel

# Escolher a data
calendario = Calendar(interface, day=datetime.datetime.now().day, month=datetime.datetime.now().month, year=datetime.datetime.now().year)
calendario.pack(pady=20)

export_data = ""

def pick_date():
    picked_date.configure(text=calendario.get_date())
    export_data = picked_date._text

btn = ctk.CTkButton(interface, text="Escolher data")
btn.pack(pady=20)

picked_date = ctk.CTkLabel(interface, text="")
picked_date.pack(pady=10)

# Escolher onde foi feita a transação

global export_metodo

def pick_metodo(option):
    export_metodo = option

tipo_metodo = ctk.CTkOptionMenu(interface, values=["DÉBITO SANTANDER", "CARTEIRA", "POUPANÇA", "SKRILL", "CGD PPR"], command=pick_metodo)
tipo_metodo.set("Escolha uma das opções")
tipo_metodo.pack(pady=20)

# Escolher tipo de transação

export_tipo = ""

def pick_tipo(option):
    export_tipo = option

tipo_transaction = ctk.CTkOptionMenu(interface, values=["ENTRADA", "SAÍDA"], command=pick_tipo)
tipo_transaction.set("Escolha uma das opções")
tipo_transaction.pack(pady=20)

# Adicionar descrição


description = ctk.CTkTextbox(interface, width=200)
description.pack(pady=10)
# Exportar dados

def print_dados():
    print("ola")
    print(description.get())

btn_recolheDados = ctk.CTkButton(interface, text="Adicionar dados ao Excel", command=lambda:[pick_date(), print_dados()])
btn_recolheDados.pack(pady=10)


interface.mainloop()

