import funcoes
import exibicoes

exibicoes.titulo('CODEHEALTH V1.0')

arquivo = funcoes.menu()

exibicoes.arquivo_selecionado(arquivo)

exibicoes.informacoes(arquivo)

exibicoes.mostrarnota(arquivo)