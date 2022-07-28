import tkinter as tk
from tkinter import ttk
import random, string
from models import Password_Register, db
import operator

#empty dictionary
name_db = {}
#database query
records_db = db.session.query(Password_Register).all()
#query table names
for record in records_db:
    name_db[record] = {
        'name': record.name
    }
    print(name_db)
#dictionary list
list_name_db = list(name_db.values())
print(list_name_db)
print(type(list_name_db))
#names list
list_name = [d.get('name', None) for d in list_name_db]
print(list_name)

# address_db = Password_Register.query.filter_by(name=name_db).first()
# address_name = address_db.address


#Read db
# records_db = db.session.query(Password_Register).all()
#
# for record in records_db:
#      name_db = list({record.name})
#      print(name_db)

# records_temp = Password_Register.query.filter_by(id=2).first()
# print(f'id: {records_temp.id} - {records_temp.name}')

address_list = [0]
tamanho_senha = ""

#create window
window = tk.Tk()

window.title("Security Passwords Manager")
window.rowconfigure(0, weight=1)

name = tk.Label(text="Nome: ")
name.grid(row=1, column=0, sticky="WS", padx=10)
name_select = ttk.Combobox(window, values=list_name)
name_select.grid(row=2, column=0, sticky="NW", padx=10, pady=10)

address = tk.Label(text="Endereço/URL: ")
address.grid(row=3, column=0, sticky="WS", padx=10)
address_selected = tk.Label(text='1234', background='gray', foreground='white')
address_selected.grid(row=4, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

go_button = tk.Button(text='IR', command="xyz").grid(row=4,column=3, sticky="W", padx=10, pady=10)
copy_button_go = tk.Button(text='COPIAR LINK', command="xyz").grid(row=4,column=4, sticky="E", padx=10, pady=10)

name_login = tk.Label(text='Login / Usuário: ')
name_login.grid(row=5, column=0, sticky="W", padx=10)
login_selected = tk.Label(text="renatodasilvamaldonado@gmail.com", background='green', foreground='white')
login_selected.grid(row=6, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

copy_login_button = tk.Button(text='COPIAR LOGIN', command="xyz")
copy_login_button.grid(row=6,column=4, sticky="E", padx=10, pady=10)

name_password = tk.Label(text='Senha: ')
name_password.grid(row=7, column=0, sticky="WN", padx=10)
password_selected = tk.Label(text="12345678", background='red', foreground='white')
password_selected.grid(row=8, column=0, columnspan=3, sticky="WS", padx=10, pady=10)

copy_password_button = tk.Button(text='COPIAR SENHA', command="xyz")
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

button_password = tk.Button(text='GERAR', command=calculate_password).grid(row=16,column=4, sticky="E", padx=10, pady=10)

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
    print(capture_data)
    db.session.add(capture_data)
    db.session.commit()
    name_registration_input.delete(0,'end')
    address_registration_selected.delete(0,'end')
    login_registration_selected.delete(0,'end')
    password_number_input.delete(0,'end')
    password_selected["text"] = ''
    name_registration_input.focus()

button_save = tk.Button(text='SALVAR', command=save).grid(row=17,column=4, sticky="E", padx=10, pady=10)





window.mainloop()