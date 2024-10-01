# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
soma = 0
contador = 0 

while True:
    n = float(input("digite um ou mais numeros: "))
    if n == -1:
        break 
    soma+=n
    contador+=1
    med = soma / contador 
print (med)