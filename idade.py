idade = int(input('digite sua idade: '))
idades = [
    (0, 13, 'Criança'),
    (13, 18, 'Adolescente'),
    (18, 30, 'Jovem adulto'),
    (30, 60, 'Adulto'),
    (60, 100, 'idoso')
]
faixa_etaria = 'x'
for inicio, fim, nome in idades:
    if inicio <= idade < fim:
        faixa_etaria = nome
        break
print(f'Você é considerado {faixa_etaria}')