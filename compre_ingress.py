from class_sessao.py import Sessao

class compra_ingresso:
    def _init_(self, pagamento: int, preco: float, assento: int, TPingresso: int, sessao: Sessao):

        self.__pagamento = pagamento
        self.__preco = preco
        self.__TPingresso = TPingresso
        self.__assento = assento
        self.__sessao = sessao
       

    def get_pagamento(self) -> int:
        return self.__pagamento

    def set_pagamento(self, pagamento: int):
        self.__pagamento = pagamento

    def get_assento(self) -> int:
        return self.__assento

    def set_assento(self, assento: int):
        self.__assento = assento

    def get_TPingresso(self) -> int:
        return self.__TPingresso

    def set_TPingresso(self, TPingresso: int):
        self.__TPingresso = TPingresso
        
    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco: float):
        self.__preco = preco

    def get_sessao(self) -> Sessao:
        return self.__sessao

    def set_sessao(self, sessao: Sessao):
        self.__sessao = sessao
