import tkinter as tk
from tkinter import ttk
import random, string
from models import Password_Register, db

address_list = [0]
tamanho_senha = ""

def calculate_password():
    tamanho_senha = password_number_input.get()
    tamanho_senha = int(tamanho_senha)
    chars = string.ascii_letters + string.digits + 'ç!@#$%^&*()|-+=`~<>?:"[]\{}'
    rnd = random.SystemRandom()
    text = ''
    password = text.join(rnd.choice(chars) for i in range(tamanho_senha))
    password_selected["text"] = password

def search():
    search_name = name_select.get()
    address_db = Password_Register.query.filter_by(name=search_name).first()
    address_name = address_db.address
    print(address_name)
    address_selected["text"] = address_name
    login_name = address_db.login
    login_selected["text"] = login_name
    password_name = address_db.password
    password_search["text"] = password_name

name_db = {}
records_db = db.session.query(Password_Register).all()
for record in records_db:
    name_db[record] = {
        'name': record.name
    }
    print(name_db)
list_name_db = list(name_db.values())
list_name = [d.get('name', None) for d in list_name_db]

#create window
window = tk.Tk()

window.title("Security Passwords Manager")
window.rowconfigure(0, weight=1)

module_name_cadastro = tk.Label(text='GERENCIADOR DE SENHAS SEGURAS | CONSULTA', background='blue', foreground='white', width=60, height=2, borderwidth=2, relief='solid', font="-weight bold -size 10")
module_name_cadastro.grid(row=1, columnspan=5, sticky="NWE", padx=10, pady=10)

name = tk.Label(text="Nome: ")
name.grid(row=2, column=0, sticky="SW", padx=10)
name_select = ttk.Combobox(window, values=list_name)
name_select.grid(row=2, column=1, sticky="SW", padx=10, pady=10)

search_button = tk.Button(text='Pesquisar', command=search).grid(row=2,column=3, sticky="ES", padx=10, pady=10)

address = tk.Label(text="Endereço/URL: ")
address.grid(row=3, column=0, sticky="WS", padx=10)
address_selected = tk.Label(text='', background='gray', foreground='white', font="-weight bold -size 11")
address_selected.grid(row=3, column=1, columnspan=2, sticky="WS", padx=10, pady=10)

go_button = tk.Button(text='IR', command="xyz").grid(row=3,column=3, sticky="ES", padx=10, pady=10)
copy_button_go = tk.Button(text='COPIAR LINK', command="xyz").grid(row=3,column=4, sticky="ES", padx=10, pady=10)

name_login = tk.Label(text='Login / Usuário: ')
name_login.grid(row=4, column=0, sticky="WS", padx=10)
login_selected = tk.Label(text="", background='gray', foreground='white', font="-weight bold -size 11")
login_selected.grid(row=4, column=1, columnspan=2, sticky="SW", padx=10, pady=10)

copy_login_button = tk.Button(text='COPIAR LOGIN', command="xyz")
copy_login_button.grid(row=4,column=4, sticky="ES", padx=10, pady=10)

name_password = tk.Label(text='Senha: ')
name_password.grid(row=5, column=0, sticky="WS", padx=10)
password_search = tk.Label(text="", background='gray', foreground='white', font="-weight bold -size 11")
password_search.grid(row=5, column=1, columnspan=2, sticky="WS", padx=10, pady=10)

copy_password_button = tk.Button(text='COPIAR SENHA', command="xyz")
copy_password_button.grid(row=5,column=4, sticky="ES", padx=10, pady=10)

module_name_cadastro = tk.Label(text='GERENCIADOR DE SENHAS SEGURAS | CADASTRO', background='green', foreground='white', width=60, height=2, borderwidth=2, relief='solid', font="-weight bold -size 10")
module_name_cadastro.grid(row=9, columnspan=5, sticky="NWE", padx=10, pady=10)

name_registration = tk.Label(text="Nome: ")
name_registration.grid(row=10, column=0, sticky="WS", padx=10)
name_registration_input = tk.Entry(width=20)
name_registration_input.grid(row=11, column=0, columnspan=2, sticky="NW", padx=10, pady=10)

address_registration = tk.Label(text="Endereço/URL: ")
address_registration.grid(row=12, column=0, sticky="WS", padx=10)
address_registration_selected = tk.Entry(width=50)
address_registration_selected.grid(row=13, column=0, columnspan=2, sticky="WS", padx=10, pady=10)

login_registration = tk.Label(text='Login / Usuário: ')
login_registration.grid(row=14, column=0, sticky="WS", padx=10)
login_registration_selected = tk.Entry(width=50)
login_registration_selected.grid(row=15, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

password_registration = tk.Label(text='Senha: ')
password_registration.grid(row=16, column=0, sticky="WS", padx=10)

password_number = tk.Label(text="Qtd. ")
password_number.grid(row=16, column=3, sticky="ES", padx=10, pady=10)
password_number_input = tk.Entry(width=5)
password_number_input.grid(row=17, column=3, sticky="ES", padx=10, pady=10)

password_selected = tk.Label(font="-size 16")
password_selected.grid(row=17, column=0, columnspan=2, sticky="WS", padx=10, pady=10)

button_password = tk.Button(text='GERAR', command=calculate_password).grid(row=17,column=4, sticky="ES", padx=10, pady=10)

licenca_uso = tk.Label(text='Desenvolvido por: Renato da Silva Maldonado', foreground='black', font="-size 8")
licenca_uso.grid(row=19, column=0, columnspan=5, padx=10, pady=10)

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
    capture_data = Password_Register(name_registration_captured,
                            address_registration_captured,
                            login_registration_captured,
                            password_registration_captured)
    # print(capture_data)
    db.session.add(capture_data)
    db.session.commit()
    name_registration_input.delete(0,'end')
    address_registration_selected.delete(0,'end')
    login_registration_selected.delete(0,'end')
    password_number_input.delete(0,'end')
    password_selected["text"] = ''
    name_registration_input.focus()

button_save = tk.Button(text='SALVAR', command=save).grid(row=18,column=4, sticky="E", padx=10, pady=10)

window.mainloop()