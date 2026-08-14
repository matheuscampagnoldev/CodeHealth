import funcoes

print('=' * 31)
print(' ' * 7, 'CODEHEALTH V1.0')
print('=' * 31)

print('')

arquivo = funcoes.menu()

    
print('')
print(f'Arquivo: {arquivo}')
print('')

print(f'Linhas do codigo: {funcoes.contar_linhas(arquivo)}')
print(f'Comentários: {funcoes.contador_comentario(arquivo)}')
print(f'Proporção: {funcoes.proporcao_comentarios(arquivo):.2f}%')
print(f'Funções: {funcoes.contador_funcoes(arquivo)}')
print(f'Funções longas: {len(funcoes.funcoes_longas(arquivo))}')
print(f'Linhas longas: {funcoes.linhas_longas(arquivo)}')
print('')

print('-' * 31)
print(f'SAÚDE DO CÓDIGO: {funcoes.nota_programa(arquivo)}/10')
print('-' * 31)