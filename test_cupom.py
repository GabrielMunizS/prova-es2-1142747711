from cupom import desconto_valido


def test_aceita_percentual_no_limite():
    # Preparar
    percentual = 21

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is True


def test_rejeita_percentual_acima_do_limite():
    # Preparar
    percentual = 22

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is False


def test_rejeita_percentual_zero():
    # Preparar
    percentual = 0

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is False

def test_rejeita_percentual_nao_inteiro():
    # Preparar
    percentual = 20.5

    # Agir
    resultado = desconto_valido(percentual)

    # Verificar
    assert resultado is False

