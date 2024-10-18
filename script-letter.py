def count_a(s):
    lower = s.lower()
    
    count_a = lower.count('a')
    print(count_a)
    exists_a = count_a > 0
    
    return exists_a, count_a

input_string = input("Digite uma palavra: ")

exists, count = count_a(input_string)

if exists:
    print(f"A contagem de letras 'a' é {count} em '{input_string}'.")
else:
    print("A letra 'a' não está presente na string.")
