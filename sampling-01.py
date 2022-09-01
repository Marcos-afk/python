import matplotlib.pyplot as plt

# Lista com todos os valores possíveis das coordenadas
coord = [-4, -3, -1.5, 0, 1.5, 3, 4, 30]

# Obtenção do valor de y
y = 5 / 2

# constantes
c = 1.5
a = 0


# função que gera o gráfico
def generationGraph(coord, y):
    # armazena as coordenadas de y
    coordY = [-y, y]
    # gera a linha 1m -1.5KHz
    plt.plot([coord[2], coord[2]], coordY)
    # gera a linha em 1.5KHz
    plt.plot([coord[4], coord[4]], coordY)
    # gera a linha em 0 em x
    plt.plot([coord[1], coord[5]], [0, 0])
    # gera a linha 0 em y
    plt.plot([0, 0], [coord[0], coord[6]])
    plt.show()


def generationSecondGraph(y, a, c, coord):
    for a in range(0, 30, 8):
        plt.plot([a - c, a - c], [-y, y])
        plt.plot([a, a], [-y, y])
        plt.plot([a + c, a + c], [-y, y])

    # gera a linha 0 em X
    plt.plot([coord[1], coord[7]], [coord[3], coord[3]])

    # gera a linha 0 em Y
    plt.plot([coord[3], coord[3]], [coord[1], coord[5]])
    plt.show()


# letra a
generationGraph(coord, y)

# letra b
generationSecondGraph(y, a, c, coord)

# os dois gráficos são mostrados em sequência, basta fechar o primeiro que o segundo ira aparecer!