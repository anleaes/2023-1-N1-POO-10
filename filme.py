class Filme:
    
    def __init__(self, titulo, genero, duracao, diretor):
        
        self._titulo = titulo
        self._genero = genero
        self.duracao = duracao
        self.diretor = diretor
        
    def get_titulo(self):
        return self._titulo

    def set_nome(self, titulo):
        self._genero = titulo
    
    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero
        
    def get_duracao(self):
        return self._duracao

    def set_duracao(self, duracao):
        self._duracao = duracao
    
    def get_diretor(self):
        return self._diretor

    def set_diretor(self, diretor):
        self._diretor = diretor
        
    def get_info(self):
        atributos = vars(self)
        info = "\n".join(f"{key}: {value}" for key, value in atributos.items())
        return info

