def abrir_arquivo(n):
    with open(n, 'r', encoding='utf-8') as arquivo:
        for l in arquivo:
            print(l, end='')

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
                if l.strip().startswith('#'):
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
    cont = 0

    todas_funcoes = {}
    funcoes_longas = {}

    funcao = False
    linhas = 0
    espacos = 0

    with open(n, 'r', encoding='utf-8') as arquivo:
            
            for l in arquivo:
                total_linhasnadef += 1

                if l.startswith('def') == True: # Vendo se esta incinado/dentro de uma funcao

                    if funcao == True:
                        todas_funcoes[f'funcoes{cont}'] = linhas
                        if linhas > 20:  #guardar no dict se for maior que 20
                            funcoes_longas[f'funcoes{cont}'] = linhas
                        linhas = 0 #Resetar as linhas

                    funcao = True #Mostra que esta dentro de um funcao
                    cont += 1 #Comeca a contar pro dict ficar mais organizado
                    continue

                if funcao == True:
                    espacos = len(l) - len(l.lstrip()) #Contando a quanridade de espacos

                    if espacos != 0: #se for identado linhas comeca a contar
                        linhas += 1

                    if total_linhasnadef != linhas_totais: #Se a linha da funcao for diferente da linha final

                        if l.strip() and espacos == 0 : #Ver se acabou a funcao para poder guardar nos dict
                            funcao = False
                            todas_funcoes[f'funcoes{cont}'] = linhas
                            if linhas > 20: #guardar no dict se for maior que 20 
                                funcoes_longas[f'funcoes{cont}'] = linhas
                            linhas = 0
                            
                    else: #Caso for a ultima linha
                        funcao = False
                        if linhas > 20: #guardar no dict se for maior que 20
                            funcoes_longas[f'funcoes{cont}'] = linhas
                            linhas = 0
                        if linhas <= 20: #Caso nao for apenas guardar as linhas em todas as funcoes
                            todas_funcoes[f'funcoes{cont}'] = linhas
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

