class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, email, senha):
        super().__init__(nome, cpf, idade)
        self.email = email
        self.senha = senha
        self.ingressos_comprados = []

    def comprar_ingresso(self, ingresso):
        if self.idade < ingresso.filme.classificacao:
            print("Você não tem idade para assistir a este filme.")
            return
        if ingresso.disponibilidade == 0:
            print("Não há ingressos disponíveis para este filme.")
            return
        ingresso.disponibilidade -= 1
        self.ingressos_comprados.append(ingresso)
        print("Ingresso comprado com sucesso!")

    def cancelar_compra(self, ingresso):
        if ingresso in self.ingressos_comprados:
            ingresso.disponibilidade += 1
            self.ingressos_comprados.remove(ingresso)
            print("Compra cancelada com sucesso!")
        else:
            print("Este ingresso não foi comprado por você.")


class Filme:
    def __init__(self, titulo, genero, classificacao, duracao):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.duracao = duracao
        self.sessoes = []

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)


class Sessao:
    def __init__(self, horario, sala, preco, filme):
        self.horario = horario
        self.sala = sala
        self.preco = preco
        self.filme = filme
        self.disponibilidade = 100

    def exibir_sessao(self):
        print(f"Horário: {self.horario} | Sala: {self.sala} | Preço: R${self.preco} | Disponibilidade: {self.disponibilidade}")

    def exibir_filme(self):
        print(f"Título: {self.filme.titulo} | Gênero: {self.filme.genero} | Classificação: {self.filme.classificacao} | Duração: {self.filme.duracao} minutos")
