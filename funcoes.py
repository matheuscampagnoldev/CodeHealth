def contar_linhas(n):
        linhas = 0

        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l.strip() != '' and not l.strip().startswith('#'):
                    linhas += 1
            return linhas


def contador_comentario(n):
        comentarios = 0
        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l.strip().startswith('#'):
                    comentarios += 1
            return comentarios


def contador_funcoes(n):
        funcoes = 0
        with open(n, 'r', encoding='utf-8') as arquivo:

            for l in arquivo:

                if l.strip().startswith('def') and '(' in l and ')' in l:
                            funcoes += 1
            return funcoes


def funcoes_longas(n):

    linhas_totais =  0   

    with open(n, 'r', encoding='utf-8') as arquivo:
        for l in arquivo:
            linhas_totais += 1

    total_linhas_arquivo = 0

    funcoes_longas = {}
    nome_funcoes = ''

    funcao = False
    linhas = 0
    espacos = 0

    with open(n, 'r', encoding='utf-8') as arquivo:
            
            for l in arquivo:
                total_linhas_arquivo += 1

                if l.strip().startswith('def') and '(' in l and ')' in l:
                    
                    if funcao == True:
                        if linhas > 20: 
                            funcoes_longas[f'{nome_funcoes[0]} -> {linhas}'] = linhas
                        linhas = 0 
                        nome_funcoes = ''

                    nome_funcoes = l.strip().replace('def ', '').split('(')

                    funcao = True
                    continue

                if funcao == True:
                    espacos = len(l) - len(l.lstrip())

                    if espacos != 0: 
                        if l.strip().startswith('#'):
                            continue
                        linhas += 1

                    if total_linhas_arquivo != linhas_totais: 

                        if l.strip() and espacos == 0 : 
                            funcao = False
                            if linhas > 20: 
                                funcoes_longas[f'{nome_funcoes[0]} -> {linhas}'] = linhas
                            linhas = 0
                            nome_funcoes = ''
                            
                    else:
                        funcao = False
                        if linhas > 20: 
                            funcoes_longas[f'{nome_funcoes[0]} -> {linhas}'] = linhas
                            linhas = 0     
                            nome_funcoes = '' 
                        if linhas <= 20: 
                                linhas = 0
                                nome_funcoes = ''

    return funcoes_longas


def linhas_longas(n):
    with open(n, 'r', encoding='utf-8') as arquivo:
        linhas_grandes = 0

        for l in arquivo:
             if len(l.replace('\n', '')) > 79:
                linhas_grandes += 1
        return linhas_grandes


def proporcao_comentarios(n):
    linhas = contar_linhas(n)
    comentarios = contador_comentario(n)

    if linhas != 0:
        proporcao = (comentarios / linhas) * 100
        return proporcao
    else:
        proporcao = 0
        return proporcao


def nota_programa(n):

    nota = 10

    funcoeslongas = len(funcoes_longas(n))
    linhasgrandes = linhas_longas(n)
    proporcaocomentarios = proporcao_comentarios(n)

    if funcoeslongas >= 1 and funcoeslongas <= 3:
        nota -= 1
    elif funcoeslongas <= 10:
        nota -= 2
    else:
         nota -= 4

    if linhasgrandes >= 1 and linhasgrandes <= 3:
        nota -= 1
    elif linhasgrandes <= 10:
        nota -= 2
    else:
        nota -= 4


    if proporcaocomentarios == 0:
        nota -= 3
    elif proporcaocomentarios < 5:
        nota -= 2
    elif proporcaocomentarios <= 30:
        nota += 1
    elif proporcaocomentarios <= 50:
        nota += 2
    else: 
        nota -= 2


    if nota > 10:
        nota = 10

    if nota < 0:
        nota = 0


    return nota