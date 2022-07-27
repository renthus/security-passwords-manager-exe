import tkinter as tk
from tkinter import ttk
import random, string
from models import Password_Register, db

address_list = [0]
tamanho_senha = ""

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

go_button = tk.Button(text='<IR>', command="xyz").grid(row=4,column=3, sticky="W", padx=10, pady=10)
copy_button_go = tk.Button(text='<COPIAR LINK>', command="xyz").grid(row=4,column=4, sticky="E", padx=10, pady=10)

name_login = tk.Label(text='Login / Usuário: ')
name_login.grid(row=5, column=0, sticky="W", padx=10)
login_selected = tk.Label(text="renatodasilvamaldonado@gmail.com", background='green', foreground='white')
login_selected.grid(row=6, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

copy_login_button = tk.Button(text='<COPIAR LOGIN>', command="xyz")
copy_login_button.grid(row=6,column=4, sticky="E", padx=10, pady=10)

name_password = tk.Label(text='Senha: ')
name_password.grid(row=7, column=0, sticky="WN", padx=10)
password_selected = tk.Label(text="12345678", background='red', foreground='white')
password_selected.grid(row=8, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

copy_password_button = tk.Button(text='<COPIAR SENHA>', command="xyz")
copy_password_button.grid(row=8,column=4, sticky="E", padx=10, pady=10)

module_name = tk.Label(text='GERENCIADOR DE SENHAS SEGURAS | CADASTRO', background='orange', foreground='white', width=60, height=2, borderwidth=2, relief='solid', font="-weight bold -size 10")
module_name.grid(row=9, columnspan=5, sticky="NWE", padx=10, pady=10)

name_registration = tk.Label(text="Nome: ")
name_registration.grid(row=10, column=0, sticky="WS", padx=10)
name_registration_input = tk.Entry(width=20)
name_registration_input.grid(row=11, column=0, columnspan=2, sticky="NW", padx=10, pady=10)

address_registration = tk.Label(text="Endereço/URL: ")
address_registration.grid(row=12, column=0, sticky="WS", padx=10)
address_registration_selected = tk.Entry(width=50)
address_registration_selected.grid(row=13, column=0, columnspan=2, sticky="WS", padx=10, pady=10)

login_registration = tk.Label(text='Login / Usuário: ')
login_registration.grid(row=14, column=0, sticky="W", padx=10)
login_registration_selected = tk.Entry(width=50)
login_registration_selected.grid(row=15, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

password_registration = tk.Label(text='Senha: ')
password_registration.grid(row=16, column=0, sticky="W", padx=10)

password_number = tk.Label(text="Qtd. ")
password_number.grid(row=15, column=3, sticky="W", padx=10, pady=10)
password_number_input = tk.Entry(width=5)
password_number_input.grid(row=16, column=3, padx=10, pady=10)

password_selected = tk.Label(font="-size 20")
password_selected.grid(row=16, column=0, sticky="WS", padx=10, pady=10)

def calculate_password():
    tamanho_senha = password_number_input.get()
    tamanho_senha = int(tamanho_senha)
    chars = string.ascii_letters + string.digits + 'ç!@#$%^&*()|-+=`~<>?:"[]\{}'
    rnd = random.SystemRandom() #os.urandom -> gera numeros aleatórios
    text = ''
    password = text.join(rnd.choice(chars) for i in range(tamanho_senha))
    password_selected["text"] = password

button_password = tk.Button(text='<GERAR>', command=calculate_password).grid(row=16,column=4, sticky="E", padx=10, pady=10)

def save():
    name_registration_captured = name_registration_input.get()
    address_registration_captured = address_registration_selected.get()
    login_registration_captured = login_registration_selected.get()
    password_registration_captured = password_selected["text"]
    print(name_registration_captured)
    print(address_registration_captured)
    print(login_registration_captured)
    print(password_registration_captured)
    #save in db
    xyz = Password_Register(name_registration_captured,
                            address_registration_captured,
                            login_registration_captured,
                            password_registration_captured)
    print(xyz)
    db.session.add(xyz)
    db.session.commit()
    name_registration_input.delete(0,'end')
    address_registration_selected.delete(0,'end')
    login_registration_selected.delete(0,'end')
    password_number_input.delete(0,'end')
    password_selected["text"] = ''
    name_registration_input.focus()

button_save = tk.Button(text='<SALVAR>', command=save).grid(row=17,column=4, sticky="E", padx=10, pady=10)

window.mainloop()