usuarios= []
def cadastro_do_usuario():
    nome = input('Digite o nome do aluno: ').title()
    sala = int(input('Digite a sala do aluno: '))
    nota = int(input('Qual foi a nota do aluno?: '))

    usuario = {
        "nome" : nome,
        "sala" : sala,
        "nota" : nota
    }

    usuarios.append(usuario)
    print('Usuário cadastrado com sucesso')

def listar_usuarios():
    if len(usuarios) == 0:
        print('nenhum aluno encontrado')
        return

    for usuario in usuarios:
        print(f"Nome: {usuario['nome']} / Sala: {usuario['sala']} / Nota: {usuario['nota']}")

def busca_usuario():
    nome = input('Nome do aluno que deseja buscar: ').title()
    for usuario in usuarios:
        if usuario["nome"] == nome:
            print('Aluno encontrado!')
            print(f"Nome: {usuario['nome']} / Sala: {usuario['sala']} / Nota: {usuario['nota']}")
            return
    print('Aluno não encontrado')

def remover_usuario():
    nome = input('Nome do aluno que deseja remover: ').title()
    for usuario in usuarios:
        if usuario["nome"] == nome:
            usuarios.remove(usuario)
            print('Aluno removido!')
            return
    print('Aluno não encontrado!')

def verificacao_nota():
    media = sum([usuario['nota'] for usuario in usuarios]) / len(usuarios) if usuarios else 0
    nome = input('Nome do aluno que deseja analisar: ').title()
    for usuario in usuarios:
        if usuario["nome"] == nome:
            print(f'O aluno {nome} está acima da média' if usuario["nota"] >= round(media, 2) else f'O aluno {nome} está abaixo da média')
            return
    print('Aluno não encontrado')

def saida():
    print("saindo do programa...")
    exit()

while True:
    print('  Bem vindo!  ')
    print('1 - Cadastrar Aluno')
    print('2 - Lista de alunos')
    print('3 - Busca de aluno')
    print('4 - Remover aluno')
    print('5 - Verificar status do Aluno')
    print('6 - Sair')

    opcao = input("O que deseja obter?: ")
    acao = {
        '1': cadastro_do_usuario, 
        '2': listar_usuarios,
        '3': busca_usuario, 
        '4': remover_usuario,
        '5': verificacao_nota,
        '6': saida
    }
    resultado = acao.get(opcao)
    if resultado:
        resultado()
    else:
        print('opção inválida')
