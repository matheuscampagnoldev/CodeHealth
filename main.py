import funcoes
import exibicoes

exibicoes.titulo('CODEHEALTH V1.0')

print('')

arquivo = funcoes.menu()

exibicoes.arquivo_selecionado(arquivo)

exibicoes.informacoes(arquivo)

print('')

print('-' * 30)
exibicoes.mostrarnota(arquivo)
print('-' * 30) 