# Clase Manga
class Manga:
    def __init__(self, tituloM="", autorM="", numeroM="", tomoM="", editorialM=""):

        self.tituloM = tituloM
        self.autorM = autorM
        self.numeroM = numeroM
        self.tomoM = tomoM
        self.editorialM = editorialM

    def muestra(self):
        print(80*"-")
        print("El manga: " + self.tituloM)
        print("del autor: " + self.autorM)
        print("número: " + self.numeroM)
        print("tomo: " + self.tomoM)
        print("editorial: " + self.editorialM)
