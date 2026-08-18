# 🩺 CodeHealth

![Python](https://img.shields.io/badge/python-3.x-blue) ![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow) ![Versão](https://img.shields.io/badge/versão-1.0-blue) ![License](https://img.shields.io/badge/licença-MIT-green)

Ferramenta de linha de comando desenvolvida em Python puro, sem dependências externas, que analisa um arquivo `.py` e gera um diagnóstico de qualidade de código: linhas longas, funções gigantes, falta de comentários e uma nota final de saúde do código.

O projeto foi construído do zero como exercício prático dos fundamentos da linguagem — leitura e manipulação de texto, funções, contagem e lógica condicional — aplicados a um problema real do dia a dia de quem programa: entender rapidamente a saúde de um arquivo de código.

## 🖼️ Demonstração

<img width="544" height="795" alt="image" src="https://github.com/user-attachments/assets/47fc4c9b-ccf4-42fb-8db9-ff917fc91842" />



## ✨ Funcionalidades

- ✅ Análise de um arquivo `.py` a partir do caminho informado no terminal
- ✅ Contagem de linhas de código (ignorando linhas em branco)
- ✅ Contagem de linhas de comentário (`#`)
- ✅ Cálculo da proporção comentário/código
- ✅ Contagem de funções (`def`)
- ✅ Sinalização de funções longas (mais de 20 linhas) como candidatas a refatoração
- ✅ Sinalização de linhas longas (mais de 79 caracteres, padrão PEP8)
- ✅ Nota final de saúde do código, de 0 a 100, baseada no conjunto das métricas

## 🛠️ Tecnologias e conceitos aplicados

| Categoria | Detalhes |
|---|---|
| Linguagem | Python 3 |
| Estruturas de dados | Listas, strings e contadores |
| Organização | Script único, lógica de leitura e análise de arquivo |
| Boas práticas | Leitura segura de arquivo, contagem e cálculo de métricas |
| Persistência | Nenhuma — cada execução analisa o arquivo na hora, sem salvar histórico |

## 📁 Estrutura do projeto
 
```
CodeHealth-Python/
├── main.py           # Ponto de entrada: orquestra o fluxo do programa
├── exibicoes.py       # Interface: menu, títulos e exibição dos resultados no terminal
├── funcoes.py         # Lógica: contagem de linhas, comentários, funções e cálculo da nota
├── amostras/           # Arquivos .py de exemplo para testar a ferramenta
├── LICENSE
└── README.md
```


## 🚀 Como executar

Pré-requisito: ter o Python 3 instalado.

```bash
# Clone o repositório
git clone https://github.com/matheuscampagnoldev/codehealth-python.git

# Acesse a pasta do projeto
cd codehealth-python

# Execute o programa apontando para o arquivo que deseja analisar
python codehealth.py caminho/para/arquivo.py
```

Não há dependências externas — o projeto roda apenas com a biblioteca padrão do Python.

## 🖥️ Exemplo de saída

```
==============================
       CODEHEALTH V1.0        
==============================
Digite o caminho do arquivo .py: teste.py

Arquivo: teste.py

Linhas do codigo: 273
Comentários: 3
Proporção: 1.10%
Funções: 24
Funções longas: 5
  - ler_texto -> 24
  - cadastro -> 46
  - saidaproduto -> 26
  - remover_produto -> 26
  - relatorio -> 68
Linhas longas: 3
------------------------------
    SAÚDE DO CÓDIGO: 5/10     
------------------------------
```

## 🗺️ Roadmap

O projeto está em evolução contínua. Próximas versões planejadas:

- **v2.0 — Análise mais profunda**
  - Detecção de complexidade ciclomática (mede o quão aninhada/emaranhada uma função está)
  - Detecção de código duplicado (blocos de linhas repetidos no mesmo arquivo)
  - Detecção de nomes de variáveis ruins (nomes muito curtos ou genéricos)
  - Detecção de imports não usados
  - Sugestões automáticas de refatoração com base nos problemas encontrados

- **v3.0 — Comparação e histórico**
  - Salvar cada análise com data/hora em JSON
  - Comparar a análise atual com análises anteriores do mesmo arquivo
  - Gerar gráfico de evolução da nota (`matplotlib`)
  - Analisar uma pasta inteira / múltiplos arquivos de uma vez
  - Interface gráfica
  - Reestruturação com orientação a objetos

## 📚 Aprendizados

Este projeto foi desenvolvido como parte da minha jornada de estudos em Python, com foco em consolidar fundamentos antes de avançar para tópicos como orientação a objetos e persistência de dados. A ideia foi priorizar a construção de algo funcional e útil usando apenas os conceitos essenciais da linguagem.

## 👤 Autor

**Matheus Zuim Campagnol**
Estudante de Engenharia de Software | Foco em Python

## ⭐ Curtiu o projeto?

Se este projeto te ajudou de alguma forma ou você gostou da ideia, deixe uma estrela no repositório!
