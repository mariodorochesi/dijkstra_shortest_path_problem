from collections import defaultdict
class Grafo:

    def __init__(self, file):

        # Se abre el archivo
        file = open(file,'r')
        # Se obtiene el ancho y alto
        ancho, alto = file.readline().strip().split(' ')[1].split('x')
        # Se convierte a int las variables de alto y ancho
        self.ancho = int(ancho)
        self.alto = int(alto)
        # Se crea un diccionario (nodo) -> lista de destinos
        self.edges = defaultdict(set)
        # Se crea un diccionario (nodoi,nodof) -> distancia
        self.weights = dict()
        # Forma cavernicola de hacer un skip a las lineas de solucioones ejemplo
        for i in range(5):
            file.readline()

        # Para cada linea en el archivo
        for linea in file:
            # Se hace un skip a las lineas vacias del final de los archivos
            if linea == '\n':
                continue
            # Se separa la linea en sus 3 valores
            linea = linea.strip().split(' ')
            # Se extraen y convierten los valores a entero
            nodo_inicial = int(linea[0])
            nodo_final = int(linea[1])
            distancia = int(linea[2])
            # Se agrega el nodo a la lista de edges
            self.edges[nodo_inicial].add(nodo_final)
            # Se deja la menor distancia entre nodos YA QUE SE ENCUENTRAN REPETIDOS ALGUNOS PARES EN EL ARCHIVO
            if self.weights.get((nodo_inicial,nodo_final),None) is not None:
                if self.weights.get((nodo_inicial,nodo_final),None) > distancia:
                    self.weights[(nodo_inicial,nodo_final)] = distancia
            else:
                self.weights[(nodo_inicial,nodo_final)] = distancia
        # Se cierra el archivo
        file.close()
        
    def dijsktra(self, inicial, final):
        '''
            Implementacion de algoritmo de dijsktra para la resolucion
            del shortest path problem unidireccional.
        '''
        # Se genera un diccionario Nodo : (siguiente, peso)
        camino_mas_corto = {inicial: (None,0)}
        nodo_actual = inicial
        # Se genera un conjunto de nodos visitados
        visitados = set()
        # Una lista de camino
        camino = []
        # Mientras el nodo actual sea distinto al nodo final
        while nodo_actual != final:
            # Se agrega a los  nodos visitados
            visitados.add(nodo_actual)
            # Se obtiene los nodos a los cuales esta conectado el nodo actual
            destinos = self.edges[nodo_actual]
            # Se obtiene la distancia requerida para llegar al nodo actual
            peso_actual = camino_mas_corto[nodo_actual][1]
            # Para cada uno de los nodos a los cuales se puede llegar
            for nodo_siguiente in destinos:
                # Se calcula el peso al nodo
                peso = self.weights[(nodo_actual, nodo_siguiente)] + peso_actual
                # Si el nodo no se encuentra en el camino mas corto entonces se agrega
                if nodo_siguiente not in camino_mas_corto:
                    camino_mas_corto[nodo_siguiente] = (nodo_actual, peso)
                # En caso contrario se evalua si la distancia a ese nodo es mejor al ya existente
                else:
                    peso_menor = camino_mas_corto[nodo_siguiente][1]
                    if peso_menor > peso:
                        camino_mas_corto[nodo_siguiente] = (nodo_actual, peso)
            # Se obtiene todos los nodos no visitados en el camino mas corto
            destinos_siguientes = {node: camino_mas_corto[node] for node in camino_mas_corto if node not in visitados}
            # Si no hay destinos siguientes entonces los nodos no estann conectados para generar un camino
            if not destinos_siguientes:
                return Exception('No existe un camino factible')
            # Se obtiene el nodo actual minimizando la distancia de los posibles nodos siguientes
            nodo_actual = min(destinos_siguientes, key = lambda k : destinos_siguientes[k][1])
        # Se genera una lista del camino mas corto
        while nodo_actual is not None:
            camino.append(nodo_actual)
            nodo_siguiente = camino_mas_corto[nodo_actual][0]
            nodo_actual = nodo_siguiente
        return camino[::-1]