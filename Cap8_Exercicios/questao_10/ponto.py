# Livro...: Introdução a Python com Aplicações de Sistemas Operacionais
# Capítulo: 08
# Questão.: 8.4.10
# Autor...: Givanaldo Rocha de Souza
# Data....: 30/04/2020

class Ponto():
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def distancia(self, p):
        from math import sqrt
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __str__(self):
        return ("%s: (%d, %d)" % (self.nome, self.x, self.y))