#Calculadora em Python 

print('\n Python Calculator')

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multuply(x,y):
    return x*y

def divide(x,y):
    x/y

print('\nSelecione a operaçao desejada: \n')
print(' 1 - Soma')
print(' 1 - Subtração')
print(' 1 - Multiplicação')
print(' 1 - Divisão')

escolha = int(input("Digite sua opção: "))

num1 = int(input("Digite 1º número: "))
num2 = int(input("Digite 2º número: "))

if escolha == 1:
    print(num1, "+", num2, "=",add(num1,num2))
elif escolha == 2:
    print(num1, "-", num2, "=",subtract(num1,num2))
elif escolha == 3:
    print(num1, "x", num2, "=",multuply(num1,num2))
elif escolha == 4:
    print(num1, "/", num2, "=",divide(num1,num2))
else:
    print('Opção Inválida!')