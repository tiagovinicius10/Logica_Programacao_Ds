alunos = {}

while True:
    print('1. Calcular media do aluno')
    print('2. fechar sistema')
    print('3. visualizar a nota do aluno desejado')

    op = input('Digite qual opção vai usar: ')
    if op == '1':
        nome = input('Digite o nome do aluno que deseja cadastrar: ')
        n1 = float(input('Digite a primeira nota do aluno'))
        n2 = float(input('Digite a segunda nota do aluno: '))
        n3 = float(input('Digite a terceira nota do aluno: '))
        media = (n1 + n2 + n3) /3
        print(f'nome: {nome} Média: {media}')
        alunos[nome] = {'nome' : nome, 'media' : media}

    elif op == '3':
       nome_visu = input('Digite o nome que deseja visualizar')
       if nome_visu in alunos:
           print(alunos[nome_visu])


    elif op == '2':
        break