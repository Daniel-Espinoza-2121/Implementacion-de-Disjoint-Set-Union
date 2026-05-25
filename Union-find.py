def make_set(v):
    parent[v] = v
    rank[v] = 0

def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v]) //Compresion path compresion
    return parent[v]

def swap(a, b):
    a, b = b, a
    return a, b

def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if rank[a] < rank[b]: #Optimización: union by rank
            a, b = swap(a,b)

        parent[b] = a

        if rank[a] == rank[b]:
            rank[a] += 1

def detectarCiclosGrafo(vert, aris):
    for i in vert:
        make_set(i)

    for i, j in aris:
        if find_set(i) == find_set(j): #Si llega a existir un grafo se presentara la situación en la que se encontraran dos elementos del mismo conjunto
            return True
        else:
            union_sets(i, j)
    return False

def main():
    #Creamos diccionarios y el grafo
    global parent, rank
    parent = {}
    rank = {}
    vertices = (1, 2, 3, 4)
    aristas = ((1,2),(2,3),(3,4),(1,3))

    resultado = detectarCiclosGrafo(vertices, aristas)
    print("Existe un ciclo en el grafo:", resultado)

    #Reiniciamos los diccionarios y el grafo
    parent = {}
    rank = {}
    aristas = ((1,2),(2,3),(3,4))

    resultado = detectarCiclosGrafo(vertices, aristas)
    print("Existe un ciclo en el grafo:", resultado)

if __name__ == "__main__":
    main()
