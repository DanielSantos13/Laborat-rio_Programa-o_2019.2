#Programa (Ilhas)

#Função Ilhas
def ilhas(origem, no, distancia, destino):
    if (origem == destino):
        print (distancia)
        return True

    for [c,d] in g[origem]:
        if (c != no):
            if (ilhas(c, origem, distancia + d, destino)):
                return True
    return False

#Atribuindo valores a N(numero de ilhas), M(numero de cabos)            
entrada_1 = input().split()
[N, M] = [int(c) for c in entrada_1]

#Criação da Matriz
g = [[] for x in range(N+1)]

#Atribuindo valores e Percorrendo as ilhas U e V com uma distância P.
for i in range(1,N):
    entrada_2 = input().split()
    [U, V, P] = [int(c) for c in entrada_2]
    g[U].append([V, P])
    g[V].append([U, P])
    
ilhas(A, -1, 0, B)

'''Minha ideia é percorrer essas as ilhas e guardar os valores dos pings em um dicionario, no fianl iria pegar essas distancias comparar,
pegar a maior e a menor distancia e fazer a diferença entre elas, isso geraria o resultado'''
