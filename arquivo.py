'''
Checkpoint 2 Computational Thinking with Python
Alunas:
Anny Dias - 98295
Camila Padalino - 98316
Luana Cabezaolias - 99320
'''

def calcular_numero_primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return

def primo_proximo(numero):
    if calcular_numero_primo(numero):
        return numero
    
    primo_maior = numero - 1
    while not calcular_numero_primo(primo_maior):
        primo_maior -= 1
    menor_primo = numero + 1

    while not calcular_numero_primo(menor_primo):
        menor_primo += 1
    if numero - primo_maior < menor_primo - numero:
        return primo_maior
    else:
        return primo_maior
    


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
        

    

    
