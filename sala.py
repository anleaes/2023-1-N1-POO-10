class Sala:
    def __init__(self, numero: int, capacidade: int, tipo: str):
        self._numero = numero
        self._capacidade = capacidade
        self._tipo = tipo

    def get_numero(self) -> int:
        return self._numero
    def set_numero(self, numero: int):
        self._numero = numero

    def get_capacidade(self) -> int:
        return self._capacidade
    def set_capacidade(self, capacidade: int):
        self._capacidade = capacidade

    def get_tipo(self) -> str:
        return self._tipo
    def set_tipo(self, tipo: str):
        self._tipo = tipo
