class Arco:
    def __init__(self, primo, secondo, peso):
        self._primo = primo
        self._secondo = secondo
        self._peso = peso

    def __lt__(self, other):
        return self._peso<other._peso