class Cinema:
    
    def __init__(self, nome, endereco):
        
        self._nome = nome
        self._endereco = endereco
        
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
    
    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco    
