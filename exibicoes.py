import funcoes

def titulo(n):
    print('=' * 30)
    print(n.center(30))
    print('=' * 30)


def menu():
    while True:
        caminho_arquivo = input('Digite o caminho do arquivo .py: ').strip()

        if caminho_arquivo[-3:].lower() == '.py':
            try:
                with open(caminho_arquivo, 'r', encoding='utf=8'):
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


def arquivo_selecionado(n):
    print('')
    print(f'Arquivo: {n}')
    print('')


def informacoes(n):
    print(f'Linhas do codigo: {funcoes.contar_linhas(n)}')
    print(f'Comentários: {funcoes.contador_comentario(n)}')
    print(f'Proporção: {funcoes.proporcao_comentarios(n):.2f}%')
    print(f'Funções: {funcoes.contador_funcoes(n)}')
    print(f'Funções longas: {len(funcoes.funcoes_longas(n))}')
    print(f'Linhas longas: {funcoes.linhas_longas(n)}')


def mostrarnota(n):
    linhas = funcoes.contar_linhas(n)

    if linhas == 0 and funcoes.contador_comentario(n) == 0:
        print('-' * 30)
        print('SAÚDE DO CÓDIGO: 0/0'.center(30))
        print('O seu programa não tem linhas de código')
        print('-' * 30)

    elif funcoes.contador_comentario(n) != 0 and linhas == 0:
        print('-' * 30)
        print('SAÚDE DO CÓDIGO: 0/0'.center(30))
        print('O seu programa tem apenas linhas de comentários')
        print('-' * 30)

    elif linhas != 0 and funcoes.contador_comentario(n) != linhas:
        print('-' * 30)
        print(f'SAÚDE DO CÓDIGO: {funcoes.nota_programa(n)}/10'.center(30))
        print('-' * 30)

    else:
        print('-' * 30)
        print(f'SAÚDE DO CÓDIGO: {funcoes.nota_programa(n)}/10'.center(30))
        print('-' * 30)