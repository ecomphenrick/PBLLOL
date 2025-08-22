class Campeao:
    def __init__(self):
        self.nome = ""
        self.nivel = 0
        self.vida = 0
    
    def exibirStatus(self):
        print(f"Nome: {self.nome}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.vida}")

    def receberDano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")


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

class Yasuo(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Yasuo"
        self.nivel = 1
        self.vida = 530
    
    def usarHabilidade(self):
        print("Yasuo usa Último Suspiro")


class Darius(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Darius"
        self.nivel = 1
        self.vida = 640
    
    def usarHabilidade(self):
        print("Darius usa Guillotine de Noxus")


class Lux(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Lux"
        self.nivel = 1
        self.vida = 490
    
    def usarHabilidade(self):
        print("Lux lança Centelha Final")


class Zed(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Zed"
        self.nivel = 1
        self.vida = 500
    
    def usarHabilidade(self):
        print("Zed invoca a Marca Fatal das Sombras")


class Katarina(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Katarina"
        self.nivel = 1
        self.vida = 510
    
    def usarHabilidade(self):
        print("Katarina usa Lótus da Morte")


class Teemo(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Teemo"
        self.nivel = 1
        self.vida = 480
    
    def usarHabilidade(self):
        print("Teemo planta Armadilhas Venenosas")


class Morgana(Campeao):
    def __init__(self):
        super().__init__()
        self.nome = "Morgana"
        self.nivel = 1
        self.vida = 500
    
    def usarHabilidade(self):
        print("Morgana usa Prisão das Trevas")




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



def Batalha(campeao1, campeao2):
    print(f"{campeao1.nome} vs {campeao2.nome}")
    while campeao1.vida > 0 and campeao2.vida > 0:
        dano = 50  # Exemplo de dano fixo
        campeao2.receberDano(dano)
        if campeao2.vida <= 0:
            print(f"{campeao1.nome} venceu!")
            break
        campeao1, campeao2 = campeao2, campeao1  # Troca de papéis
    
#Dentro de batalha seria interessante mostrar quem atacou primeiro, o dano causado e a vida restante de cada campeão após cada ataque.
