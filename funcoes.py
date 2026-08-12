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
            return linhas


def contador_comentario(n):
        comentarios = 0
        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l[0] == '#':
                     comentarios += 1
            return comentarios

def contador_funcoes(n):
        funcoes = 0
        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l[0:3] == 'def':
                     funcoes += 1
            return funcoes

def funcoes_longas(n):

    linhas_totais = contar_linhas(n)
    total_linhasnadef = 0


    Quantidade_linhas = []
    funcoes_longas = []
    funcao = False
    linhas = 0
    espacos = 0

    with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                total_linhasnadef += 1
                if l.startswith('def') == True: # vendo se e uma funcao e pulando essa linhas para nao contar
                    funcao = True
                    continue

                if funcao == True:
                    espacos = len(l) - len(l.lstrip()) #quantidade de espacos pra ver identacao

                    if espacos != 0: #se for identado linhas recebe 1
                        linhas += 1

                    if total_linhasnadef != linhas_totais: #ver se e a ultima linha
                        if l.strip() and espacos == 0 : #ver se acabou a funcao
                            funcao = False
                            Quantidade_linhas.append(linhas)

                            if linhas > 20: #guardar na lista
                                funcoes_longas.append(linhas)
                            linhas = 0
                    else:
                        funcao = False
                        Quantidade_linhas.append(linhas)
                        if linhas > 20: #guardar na lista
                            funcoes_longas.append(linhas)
                        linhas = 0

    return funcoes_longas

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
        return linhas_grandes

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
    return proporcao

def nota_programa(n):

    nota = 10

    funcoeslongas = len(funcoes_longas(n))
    linhasgrandes = linhas_longas(n)
    proporcaocomentarios = proporcao_comentarios(n)


    if funcoeslongas >= 1 and funcoeslongas <= 3:
        nota -= 1
    elif funcoeslongas > 3 and funcoeslongas <= 10:
        nota -= 2
    elif funcoeslongas > 10:
         nota -= 4


    if linhasgrandes >= 1 and linhasgrandes <= 3:
        nota -= 1
    elif linhasgrandes > 3 and linhasgrandes <= 10:
        nota -= 2
    elif linhasgrandes > 10:
            nota -= 4

    if proporcaocomentarios < 5:
        nota -= 1
    elif proporcaocomentarios >= 5 and proporcaocomentarios <= 30:
        nota += 1
    elif proporcaocomentarios > 30 and proporcaocomentarios <= 50:
        nota += 2
    elif proporcaocomentarios > 50:
        nota -= 2

    if nota > 10:
        nota = 10
    elif nota < 0:
        nota = 0

    return nota

