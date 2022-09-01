data = {"bits": 2, "xmax": 5, "xmin": 0, "prohibited": 3}


def calc(bits, xmax, xmin, prohibited):
    # variável que recebe os resultado dos nivéis de quantização
    l = 2 ** bits

    # variável que recebe o resultado do tamanho do passo do quantizador ou a resolução do ADC
    delta = (xmax - xmin) / l

    # variável que recebe o índice do código binário
    i = round((prohibited - xmin) / delta)

    # variável que recebe o nível de quantização
    xq = xmin + (i * delta)

    print('Níveis de quantização : {}'.format(l))
    print('Índice correspondente ao código binário: {}'.format(i))
    print('Nível de quantização: {}'.format(xq))


calc(data["bits"], data["xmax"], data["xmin"], data["prohibited"])
