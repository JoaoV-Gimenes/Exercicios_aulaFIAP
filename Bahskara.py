a = int(input('Digite o a da função: '))
b = int(input('Digite o b da função: '))
c = int(input('Digite o c da função: '))

delta = b**2 - 4 *a*c
raiz1 = (-b + (delta)**0.5) / (2 * a)
raiz2 = (-b - (delta)**0.5) / (2 * a)

print(f'As raízes da equação são {raiz1} e {raiz2}')