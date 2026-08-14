import funcoes

print('=' * 30)
print(' ' * 15, 'CODEHEALTH V1.0')
print('=' * 30)

while True:
    caminho_arquivo = input('Digite o caminho do arquivo .py: ').strip()

    if caminho_arquivo[-3:].lower() == '.py':
        try:
            funcoes.abrir_arquivo(caminho_arquivo)
            break
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

    
print('')
print(f'Arquivo: {caminho_arquivo}')
print(f'Linhas do codigo: {funcoes.contar_linhas(caminho_arquivo)}')
print(f'Comentários: {funcoes.contador_comentario(caminho_arquivo)}')
print(f'Proporção: {funcoes.proporcao_comentarios(caminho_arquivo):.2f}')
print(f'Funções: {funcoes.contador_funcoes(caminho_arquivo)}')
print(f'Funções longas: {len(funcoes.funcoes_longas(caminho_arquivo))}')
print(f'Linhas longas: {funcoes.linhas_longas(caminho_arquivo)}')
print('')

print('-' * 30)
print(f'SAÚDE DO CÓDIGO: {funcoes.nota_programa(caminho_arquivo)}/10')
print('-' * 30)