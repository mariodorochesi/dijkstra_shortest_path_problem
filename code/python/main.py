from dijkstra.Grafo import Grafo
import time
grafo = Grafo('instances/ShortestPathInstance_1000x1000000.txt')
tiempo_inicial = time.time()
solucion = grafo.dijsktra(50,800)
print('Solucion Encontrada : ' + str(solucion))
distancia = 0
for i in range(len(solucion)-1):
    distancia = distancia + grafo.weights[(solucion[i],solucion[i+1])]
tiempo_final = time.time()
print(f'Distancia de la solucion : {distancia}')
print(f'Tiempo requerido : {tiempo_final - tiempo_inicial} segundos.')