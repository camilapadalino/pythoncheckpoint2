'''
Checkpoint 2 Computational Thinking with Python
Alunas:
Anny Dias - RM:98295
Camila Padalino - RM:98316
Luana Cabezaolias - RM:99320
'''

#Verificar se o número é primo
def calcular_numero_primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

#Analisar o  número primo mais próximo
def primo_proximo(numero):
    if numero < 2:
        return 2
    n = 0 
    while True:
        n += 1
        if calcular_numero_primo(numero):
            return numero
        if calcular_numero_primo(numero-n):
            return numero - n
        if calcular_numero_primo(numero+n):
            return numero + n

#Pedindo o número ao usuário e verificando se é válido
while True:
    numero = int(input("Insira um número positivo: "))
    if numero == 0:
        print("Fim do programa")
        break
    elif numero < 0:
        print("Número inválido")
    elif numero > 1000:
        print("Número inválido")
    else: 
        primo = primo_proximo(numero)
        print(f"O número primo mais próximo de {numero} é {primo}")
        

    

    
