import random, string
from interface import password_number_input


# tamanho_senha = int(input('Digite o tamanho de senha que deseja: '))
# chars = string.ascii_letters + string.digits + 'ç!@#$%^&*()|-+=`~<>?:"[]\{}'
# rnd = random.SystemRandom() #os.urandom -> gera numeros aleatórios
# print(type(tamanho_senha))
# print(''.join(rnd.choice(chars) for i in range(tamanho_senha)))

def calculate_password():
    tamanho_senha = int(password_number_input)
    chars = string.ascii_letters + string.digits + 'ç!@#$%^&*()|-+=`~<>?:"[]\{}'
    rnd = random.SystemRandom() #os.urandom -> gera numeros aleatórios
    text = ''
    password = text.join(rnd.choice(chars) for i in range(tamanho_senha))
    print(password)






