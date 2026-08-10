import funcoes

print('=' * 30)
print('CODEHEALTH V1.0')
print('=' * 30)

caminho_arquivo = input('Digite o caminho do arquivo .py: ')

print(f'Arquivo selecionado: {caminho_arquivo}')

funcoes.contar_linhas(caminho_arquivo)

