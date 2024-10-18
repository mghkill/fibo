def fibonacci_check(value):
    n = value * 2
    if n <= 0:
        return "O número de termos deve ser maior que 0"
    elif n == 1:
        sequence = [0]
    elif n == 2:
        sequence = [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)

     
    if value in sequence:
        return f"O valor {value} pertence à sequência de Fibonacci."
    else:
        return f"O valor {value} NÃO pertence à sequência de Fibonacci."
 
 
valor = int(input("Digite o valor para verificar se pertence à sequência de Fibonacci: "))

resultado = fibonacci_check( valor)
print(resultado)
