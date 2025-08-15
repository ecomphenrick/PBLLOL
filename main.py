import campeao

#Me lembre a forma de criar um objeto em python

def main():
    time = campeao.Time()

    jinx = campeao.Jinx()
    garen = campeao.Garen()
    ahri = campeao.Ahri()

    time.adicionarCampeao(jinx)
    time.adicionarCampeao(garen)
    time.adicionarCampeao(ahri)

    time.listarTime()
    time.UsarHabilidadeDeTodos()

if __name__ == "__main__":
    main()

