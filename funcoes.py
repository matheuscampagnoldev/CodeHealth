def abrir_arquivo(n):
    with open(n, 'r', encoding='utf-8') as arquivo:
        for l in arquivo:
            print(l, end='')
            print('')

def contar_linhas(n):
        linhas = 0
        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l.strip() != '':
                     linhas += 1
            print(f'Total de linhas do arquivo: {linhas}')

def contador_comentario(n):
        comentarios = 0
        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l[0] == '#':
                     comentarios += 1
            print(f'Total de comentários do arquivo: {comentarios}')

def contador_funcoes(n):
        funcoes = 0
        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l[0:3] == 'def':
                     funcoes += 1
            print(f'Total de funções do arquivo: {funcoes}')

def funcoes_longas(n):
    Quantidade_linhas = []
    funcoes_longas = []
    funcao = False
    linhas = 0
    espacos = 0

    with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:

                if l.startswith('def') == True:
                    funcao = True
                    continue

                if funcao == True:
                    espacos = len(l) - len(l.lstrip()) #quantidade de espacos
                    if espacos != 0:
                        linhas += 1
                    elif l.strip() and espacos == 0 :
                        funcao = False
                        Quantidade_linhas.append(linhas)
                        if linhas > 20:
                            funcoes_longas.append(linhas)
                        linhas = 0
    print(Quantidade_linhas)

def linhas_longas(n):
    with open(n, 'r', encoding='utf-8') as arquivo:

        local_linha = []
        linhas = 0
        linhas_grandes = 0

        for l in arquivo:
             linhas += 1
             if len(l) > 79:
                linhas_grandes += 1
                local_linha.append(linhas)

    print(f'Linhas grandes: {linhas_grandes} linhas: {local_linha}')

def proporcao_comentarios(n):
    linhas = 0
    comentarios = 0

    with open(n, 'r', encoding='utf-8') as arquivo:
        for l in arquivo:
            if l.strip() != '':
                if l.startswith('#'):
                    comentarios += 1
                else:
                    linhas += 1

    proporcao = (comentarios / linhas) * 100
    print(f'A proporcao do seu codigo e {proporcao}%')
