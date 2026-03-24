import unicodedata

def normalizar(texto):
    return unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8').lower()

def area_retangulo():
    altura_r = int(input('Digite o valor da altura do Retângulo: '))
    base_r = int(input('Digite o valor da base do Retângulo: '))
    return f'O valor da área do Retângulo é: {altura_r * base_r}'

def area_circulo():
    raio = int(input('Digite o valor do raio do Círculo: '))
    return f'O valor da área do Círculo é: {raio**2 * 3.14}'

def area_triangulo():
    altura_t = int(input('Digite o valor da altura do Triângulo: '))
    base_t = int(input('Digite o valor da base do Triângulo: '))
    return f'O valor da área do Triângulo é: {(altura_t * base_t) / 2}'

def area_esfera():
    raio = int(input('Digite o valor do raio da Esfera: '))
    return f'O valor da área da Esfera é: {4 * (raio**2) * 3.14}'

def sair():
    print("Saindo do programa...")
    exit()

calculo = {
    'retangulo': area_retangulo,
    'triangulo': area_triangulo,
    'circulo': area_circulo,
    'esfera': area_esfera,
    'sair': sair
}

while True:
    solicitacao = normalizar(input('De qual forma geométrica você deseja calcular a área? (Retângulo, Triângulo, Círculo, Esfera, Sair): '))
    funcao = calculo.get(solicitacao)
    if funcao:
        resultado = funcao()
        if resultado:         # sair() retorna None, então não tenta printar
            print(resultado)
    else:
        print('Forma geométrica inválida!')