class Cliente:
    
    def __init__(self, nome, endereco, telefone, email):
        
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
    
    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco   
    
    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email                  
        