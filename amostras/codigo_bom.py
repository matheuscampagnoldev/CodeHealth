"""Exemplo de código organizado e legível."""

TAXA_DESCONTO = 0.10


def calcular_desconto(preco):
    """Calcula o desconto de um produto."""
    return preco * TAXA_DESCONTO


def calcular_preco_final(preco):
    """Retorna o preço após aplicar o desconto."""
    desconto = calcular_desconto(preco)
    return preco - desconto


def exibir_resultado(produto, preco):
    """Exibe as informações do produto."""
    preco_final = calcular_preco_final(preco)

    print(f"Produto: {produto}")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")


produto = "Teclado"
preco = 150.00

exibir_resultado(produto, preco)