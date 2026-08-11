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
    funcao = False
    linhas = 0
    espacos = 0

    with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:

                if l.startswith('def') == True:
                    funcao = True

                if funcao == True:
                    linhas += 1
                    espacos = len(l) - len(l.lstrip())
                    if espacos == 0:
                        funcao = False
    print(linhas)