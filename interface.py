import tkinter as tk
from tkinter import ttk

address_list = [0]

#create window
window = tk.Tk()

window.title("Security Passwords Manager")
window.rowconfigure(0, weight=1)

name = tk.Label(text="Nome: ")
name.grid(row=1, column=0, sticky="WS", padx=10)
name_select = ttk.Combobox(window, value=address_list)
name_select.grid(row=2, column=0, columnspan=2, sticky="NW", padx=10, pady=10)

address = tk.Label(text="Endereço/URL: ")
address.grid(row=3, column=0, sticky="WS", padx=10)
address_selected = tk.Label(text="https://www.exemplodesitequalquer.com.br", background='gray', foreground='white')
address_selected.grid(row=4, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

go_button = tk.Button(text='<IR>', command="xyz").grid(row=4,column=3, sticky="E", padx=10, pady=10)
copy_button_go = tk.Button(text='<COPIAR LINK>', command="xyz").grid(row=4,column=4, sticky="E", padx=10, pady=10)

name_password = tk.Label(text='Senha: ')
name_password.grid(row=6, column=0, sticky="W", padx=10)
password_selected = tk.Label(text="12345678", background='red', foreground='white')
password_selected.grid(row=7, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

copy_password_button = tk.Button(text='<COPIAR SENHA>', command="xyz")
copy_password_button.grid(row=7,column=4, sticky="E", padx=10, pady=10)

module_name = tk.Label(text='GERENCIADOR DE SENHAS SEGURAS | CADASTRO', background='orange', foreground='white', width=60, height=2, borderwidth=2, relief='solid', font="-weight bold -size 10")
module_name.grid(row=8, columnspan=5, sticky="NWE", padx=10, pady=10)

name_registration = tk.Label(text="Nome: ")
name_registration.grid(row=9, column=0, sticky="WS", padx=10)
name_registration_input = tk.Text(width=20, height=1)
name_registration_input.grid(row=10, column=0, columnspan=2, sticky="NW", padx=10, pady=10)

address_registration = tk.Label(text="Endereço/URL: ")
address_registration.grid(row=11, column=0, sticky="WS", padx=10)
address_registration_selected = tk.Text(width=50, height=1)
address_registration_selected.grid(row=12, column=0, columnspan=2, sticky="WS", padx=10, pady=10)

password_registration = tk.Label(text='Senha: ')
password_registration.grid(row=13, column=0, sticky="W", padx=10)
password_selected = tk.Label(text="fsadfasfds", background='red', foreground='white')
password_selected.grid(row=14, column=0, columnspan=3, sticky="WS", padx=10, pady=10)
password_number = tk.Label(text="Qtd. ")
password_number.grid(row=13, column=3, padx=10, pady=10)
password_number_input = tk.Entry(window)
password_number_input.grid(row=14, column=3, padx=10, pady=10)

button_password = tk.Button(text='<GERAR>', command="xyz").grid(row=14,column=4, sticky="E", padx=10, pady=10)
button_save = tk.Button(text='<SALVAR>', command="xyz").grid(row=15,column=4, sticky="E", padx=10, pady=10)

window.mainloop()