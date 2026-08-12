import funcoes

print('=' * 30)
print(' ' * 15, 'CODEHEALTH V1.0')
print('=' * 30)

caminho_arquivo = input('Digite o caminho do arquivo .py: ')

print('')
print(f'Arquivo: {caminho_arquivo}')
print(f'Linhas do codigo: {funcoes.contar_linhas(caminho_arquivo)}')
print(f'Comentários: {funcoes.contador_comentario(caminho_arquivo)}')
print(f'Proporção: {funcoes.proporcao_comentarios(caminho_arquivo)}')
print(f'Funções: {funcoes.contador_funcoes(caminho_arquivo)}')
print(f'Funções longas: {funcoes.funcoes_longas(caminho_arquivo)}')
print(f'Linhas longas: {funcoes.linhas_longas(caminho_arquivo)}')
print('')

print('-' * 30)
print(f'SAÚDE DO CÓDIGO: {funcoes.nota_programa(caminho_arquivo)}/10')
print('-' * 30)