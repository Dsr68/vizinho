import math

def calcular_distancia(idade, valor):
    return math.sqrt(math.pow(idade - valor, 2))

dMin = 100000
idades = (92, 8, 11, 75, 12, 18, 67, 71, 21, 66, 75, 10, 25, 40, 30, 60, 86, 80, 100)
fase = (
    "idoso", "criança", "criança", "idoso", "adolescente", "adulto",
    "idoso", "idoso", "adulto", "idoso", "idoso", "criança", "adulto",
    "adulto", "adulto", "idoso", "idoso", "idoso", "idoso"
)

idade = int(input("Digite sua idade: "))
i = 0
indice = 0


for elemento in idades:
    if calcular_distancia(idade, elemento) < dMin:
        dMin = calcular_distancia(idade, elemento)
        indice = i
    i += 1


print("Você esta na fase: {}".format(fase[indice]))