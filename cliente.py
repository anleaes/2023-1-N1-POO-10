class Cliente:
    
    def __init__(self, nome, endereco, telefone, email):
        
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
    
    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco   
    
    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone
        
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email 