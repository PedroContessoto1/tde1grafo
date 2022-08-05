class GRAFO():
    def __init__(self):
        self.grafo = {}

    def adiciona_vertice(self, nome_vertice):
        self.grafo[nome_vertice] = []

    def adiciona_aresta(self, vertice1, vertice2, peso):
        self.grafo[vertice1].append([vertice2, peso])

    def remove_aresta(self, vertice1, vertice2):
        nova_lista = []
        for i in self.grafo[vertice1]:
            if i[0] != vertice2:
                nova_lista.append(i)
        self.grafo[vertice1] = nova_lista

    def remove_vertice(self, vertice):
        del self.grafo[vertice]

    def tem_aresta(self, vertice1, vertice2):
        for i in self.grafo[vertice1]:
            if i[0] == vertice2:
                return True
        return False

    def peso(self, vertice1, vertice2):
        for i in self.grafo[vertice1]:
            if i[0] == vertice2:
                return i[1]
        return False

    def grau(self, vertice):
        return len(self.grafo[vertice])


    def imprime_lista_adjacencias(self):
        aresta = ""
        for key, value in self.grafo.items():
            for i in value:
                aresta += str(i) + " ->"
            print(f"{key} : {aresta}")
            aresta = ""



def main():
    grafo1 = GRAFO()
    grafo1.adiciona_vertice("A")
    grafo1.adiciona_vertice("B")
    grafo1.adiciona_vertice("C")
    grafo1.adiciona_aresta("A", "B", 3)
    grafo1.adiciona_aresta("A", "C", 2)
    grafo1.adiciona_aresta("B", "C", 2)
    grafo1.adiciona_aresta("C", "A", 1)
    grafo1.remove_aresta("A", "B")
    grafo1.remove_vertice("A")
    grafo1.adiciona_vertice("A")
    grafo1.adiciona_aresta("A", "B", 3)
    grafo1.adiciona_aresta("A", "C", 3)
    print(grafo1.tem_aresta("B","C"))
    print(grafo1.grau("C"))
    print(grafo1.peso("B", "C"))
    grafo1.imprime_lista_adjacencias()

if __name__ == "__main__":
    main()

