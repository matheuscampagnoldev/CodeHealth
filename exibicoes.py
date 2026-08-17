import funcoes

def titulo(n):
    print('=' * 30)
    print(n.center(30))
    print('=' * 30)


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