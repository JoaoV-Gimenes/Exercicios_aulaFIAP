lista_alunos = {
    'Arthur' : [9, 3, 8],
    'Felipe' : [5, 7, 10],
    'Rodrigo' : [2, 6, 9]
}

def resposta_sim():
    print(f'A média do aluno {aluno} é: {media:.2f}. Sendo assim, {"aprovado" if media > 6 else "reprovado"}')

def resposta_nao():
    print('Desligando o sistema')

resposta1 = {
    's' : resposta_sim,
    'n' : resposta_nao
}

while True:
    aluno = input('Qual aluno deseja analisar as notas? --> ').title().strip()
    if aluno in lista_alunos:
        notas_aluno = lista_alunos.get(aluno)
        print(f'As notas do aluno {aluno} são: {", ".join(str(a) for a in notas_aluno)}')
        media = sum(notas_aluno) / len(notas_aluno)
        while True:
            solicitacao = input('Deseja analisar a média do aluno? (s/n): ').lower().strip()
            funcao = resposta1.get(solicitacao)
            if funcao:
                funcao()
                break
            else:
                print('Comando inválido')
        break
    else:
        print('Aluno inválido, tente novamente.')