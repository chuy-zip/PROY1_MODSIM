import math

class DistanceTable:
    def __init__(self, node_list):
        # Node list tiene el siguiente formato
        # NODO X_VAL, Y_VAL
        # 4 945.0 685.0
        
        self.nodes = self.parse_nodes(node_list)
        self.distance_matrix = self.calculate_distance_matrix()
    
    def parse_nodes(self, node_list):
        nodes = []
        for node in node_list:
            node_data = node.split()
            if len(node_data) >= 3:  # Asegurar que hay suficientes datos
                node_number = int(node_data[0])
                node_X = float(node_data[1])
                node_Y = float(node_data[2])
                nodes.append((node_number, node_X, node_Y))
        return nodes
    
    def calculate_distance_matrix(self):
        n = len(self.nodes)
        # Crear matriz n x n llena de ceros
        distance_matrix = [[0.0] * n for _ in range(n)]
        
        for i in range(n):
            # Solo calcular triangulo superior, pero si se guarda el valor espejo
            # sino luego puede que no se pueda acceder a 4,3 si tenemos 3,4 guardado por ejemplo
            for j in range(i + 1, n):  
                x1, y1 = self.nodes[i][1], self.nodes[i][2]
                x2, y2 = self.nodes[j][1], self.nodes[j][2]
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance  # Matriz simétrica
        
        return distance_matrix
    
    #Obtiene distancia entre dos nodos (por número de nodo)
    def get_distance_between_nodes(self, node1, node2):
        # Convertir números de nodo a índices (restar 1)
        idx1 = node1 - 1
        idx2 = node2 - 1
        return self.distance_matrix[idx1][idx2]
    
    #usa indices directamente y no el numero de nodo
    def get_distance_by_index(self, idx1, idx2):
        return self.distance_matrix[idx1][idx2]
    
    def __str__(self):

        return f"DistanceTable with {len(self.nodes)} nodes"