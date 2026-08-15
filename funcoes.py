def menu():
    while True:
        caminho_arquivo = input('Digite o caminho do arquivo .py: ').strip()

        if caminho_arquivo[-3:].lower() == '.py':
            try:
                abrir_arquivo(caminho_arquivo)
                return caminho_arquivo
            except FileNotFoundError:
                print('O arquivo Não foi encontrado')
            except PermissionError:
                print('Não tenho permissão para lê-lo.')
            except IsADirectoryError:
                print('Você passou o caminho de uma pasta em vez de um arquivo.')
            except UnicodeDecodeError:
                print('O arquivo existe e foi aberto, mas o Python não consegue interpretar o conteúdo como texto com aquela codificação.')
        elif caminho_arquivo == '':
            print('Digite um caminho valido.')
        else:
            print('O arquivo precisa ser .py.')
            continue

def abrir_arquivo(n):
    with open(n, 'r', encoding='utf-8') as arquivo:
        return arquivo


def contar_linhas(n):
        linhas = 0
        with open(n, 'r', encoding='utf-8') as arquivo:
            for l in arquivo:
                if l.strip() != '' and l.strip().startswith('#') == False:
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

                if l.strip().startswith('def'):
                     if l.strip()[-1] == ':' and '(' in l and ')' in l:
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

                if l.strip().startswith('def') == True: # Vendo se esta incinado/dentro de uma funcao

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
             if len(l.replace('\n', '')) > 79:
                linhas_grandes += 1
                local_linha.append(linhas)
        return linhas_grandes

def proporcao_comentarios(n):
    linhas = contar_linhas(n)
    comentarios = 0

    with open(n, 'r', encoding='utf-8') as arquivo:
        for l in arquivo:
            if l.strip() != '':
                if l.strip().startswith('#'):
                    comentarios += 1

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

    if proporcaocomentarios == 0:
        nota -= 3

    elif proporcaocomentarios < 5:
        nota -= 2

    elif proporcaocomentarios <= 30:
        nota += 1

    elif proporcaocomentarios <= 50:
        nota += 2

    else:
        nota += 1

    if nota > 10:
        nota = 10
    elif nota < 0:
        nota = 0

    return nota