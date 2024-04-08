def is_fibonacci_number(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

def main_function():
    try:
        num = int(input("Informe um número para verificar se está na sequência de Fibonacci: "))
        if num < 0:
            raise ValueError
    except ValueError:
        print("Por favor, informe um número inteiro positivo.")
        return
    
    if is_fibonacci_number(num):
        print(f"O número {num} está na sequência de Fibonacci.")
    else:
        print(f"O número {num} não está na sequência de Fibonacci.")

main_function()

