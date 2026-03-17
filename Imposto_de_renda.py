salario = float(input('Digite seu salário: '))
faixa_salarial= [
    (0, 1621, 0.925),
    (1621.01, 2902.84, 0.91),
    (2902.84, 4354.27, 0.88),
    (4354.27, 8475.55, 0.86)
]

for inicio, fim, aliquota in faixa_salarial:
    if inicio <= salario < fim:
        print(f'será descontado {salario-(salario*aliquota):.2f}')
        print(f'Seu salário líquido será: {salario*aliquota}')
    

renda_mensal = float(input('Digite sua renda mensal: '))
score = float(input('Digite seu score de crédito: '))
condicoes = {
    (3000, 700, 'Aprovado'),
    (7000, 1, 'ok'),
    (2000, 600, 'Análise manual')
}
for renda, credito, resultado in sorted(condicoes, reverse=True):
    print(renda)
    print(credito)
    print(resultado)