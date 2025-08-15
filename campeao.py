class Campeao:
    def __init__(self):
        self.nome = ""
        self.nivel = 0
        self.vida = 0
    
    def exibirStatus(self):
        print(f"Nome: {self.nome}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.vida}")


class Garen(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Garen"
        self.nivel = 1
        self.vida = 620
    
    def usarHabilidade(self):
        print("Garen usa Justiça Demacianal")

class Jinx(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Jinx"
        self.nivel = 1
        self.vida = 540
    
    def usarHabilidade(self):
        print("Jinx usa Super Mega Míssil de Morte")

class Ahri(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Ahri"
        self.nivel = 1
        self.vida = 480
    
    def usarHabilidade(self):
        print("Ahri Lança Encanto")

class Time:
    def __init__(self):
        self.listaCampeoes = []

    def adicionarCampeao (self, c = Campeao):
        self.listaCampeoes.append(c)
    
    def listarTime(self):
        for campeao in self.listaCampeoes:
            campeao.exibirStatus()
    
    def UsarHabilidadeDeTodos(self):
        for campeao in self.listaCampeoes:
            campeao.usarHabilidade()
    

