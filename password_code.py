import random, string

tamanho_senha = int(input('Digite o tamanho de senha que deseja: '))
chars = string.ascii_letters + string.digits + 'ç!@#$%^&*()|-+=`~<>?:"[]\{}'
rnd = random.SystemRandom() #os.urandom -> gera numeros aleatórios

print(''.join(rnd.choice(chars) for i in range(tamanho_senha)))