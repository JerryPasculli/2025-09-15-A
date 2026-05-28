import copy
import math

import networkx as nx

from database.DAO import DAO
from model.arco import Arco


class Model:
    def __init__(self):
        self._G = nx.Graph()
        self._nodi = []
        self._archi = []
        self._Dnodi = {}
        self._soluzione = []
        self._tot = math.inf


    def popola(self):
        return DAO.getAllYears()

    def creaGrafo(self, primo, secondo):
        self._G = nx.Graph()
        self._nodi = []
        self._nodi = DAO.getNodi(primo, secondo)
        self._archi = []
        self._Dnodi = {}
        self._G.add_nodes_from(self._nodi)
        for element in self._nodi:
            self._Dnodi[element.driverId] = element
        lista = DAO.getArchi(primo, secondo)
        for element in lista:
            primo = self._Dnodi[element[0]]
            secondo = self._Dnodi[element[1]]
            peso = element[2]
            arco = Arco(primo, secondo, peso)
            self._archi.append(arco)
            self._G.add_edge(primo, secondo, weight = peso)
        titolo = "Arco correttamente creato"
        archi = self._G.number_of_edges()
        nodi = self._G.number_of_nodes()
        stringa = f"Numero di nodi:{nodi}"
        stringa = stringa + "\n"+f"Numero di archi:{archi}"
        return titolo, stringa

    def dettagliPeso(self):
        self._archi.sort(reverse=True)
        titolo = "Archi di peso maggiore"
        stringa = ""
        for i in range(min(3, len(self._archi))):
            nodo2 = self._archi[i]._primo
            nodo1 = self._archi[i]._secondo
            peso = self._archi[i]._peso
            if stringa == "":
                stringa = nodo1.driverRef + "->" + nodo2.driverRef + f"({peso})"
            else:
                stringa = stringa + "\n" + nodo1.driverRef + "->" + nodo2.driverRef + f"({peso})"
        return titolo, stringa

    def dettagliComp1(self):
        numero = nx.number_connected_components(self._G)
        self._piuGrande = self._G.subgraph(max(nx.connected_components(self._G), key=len))
        self._ordinata = sorted(self._piuGrande.nodes(), key = lambda n : self._piuGrande.degree(n), reverse=True)
        nodi = list(self._piuGrande.nodes())
        titolo = f"Il grafo ha {numero} componenti connesse"
        titolo = titolo + f"\nLa componente più grande ({len(nodi)} nodi)"
        stringa = ""
        for i in range(len(nodi)):
            if stringa == "":
                stringa = nodi[i].__str__()
            else:
                stringa = stringa + "\n" + nodi[i].__str__()
        return titolo, stringa

    def dettagliComp2(self):
        titolo = "Componente connessa in ordine decrescente"
        stringa = ""
        for i in range(len(self._ordinata)):
            if stringa == "":
                stringa = self._ordinata[i].__str__() + f"(grado={str(self._piuGrande.degree(self._ordinata[i]))})"
            else:
                stringa = stringa + "\n" + self._ordinata[i].__str__()+ f"(grado={str(self._piuGrande.degree(self._ordinata[i]))})"
        return titolo, stringa

    def calcolo(self, copia):
        lista = copy.deepcopy(copia)
        lista.sort()
        primo = lista[-1]
        ultimo = lista[0]
        differenza = abs((primo.dob-ultimo.dob).total_seconds())
        return differenza
    def possibile(self, lista, element):
        for k in lista:
            if element in list(self._G.neighbors(k)):
                return False
        return True

    def cammino(self, k):
        self._soluzione = []
        self._tot = math.inf
        print("Divisore")
        cammini = list(nx.connected_components(self._G))
        for element in cammini:
            for nodo in element:
                parziale = [nodo]
                self.itera(parziale, k, cammini)
        stringa = f"Set minimo trovato con valore: {self._tot/3600/24} giorni"
        for element in self._soluzione:
            stringa = stringa + "\n" +element.__str__()
        return stringa


    def itera(self, parziale, k, cammini):
        if self.calcolo(parziale) > self._tot:
            return
        if len(parziale) == k:
            tot = self.calcolo(parziale)
            print(tot/3600/24)
            if tot<self._tot:
                self._tot = tot
                self._soluzione = copy.deepcopy(parziale)
            return
        for gruppo in cammini:
            for element in gruppo:
                if element not in parziale:
                    parziale.append(element)
                    self.itera(parziale, k, cammini)
                    parziale.pop()




