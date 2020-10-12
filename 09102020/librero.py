from libro import Libro
from disco import Disco
from revista import Revista
from comic import Comic


class Librero:
    def muestra(self):
        for i in range(len(self.librerito)):
            self.librerito[i].muestra()
#    for ll in self.librerito:
#      ll.muestra()
        print(80*"-")

    def __init__(self):
        self.librerito = []
        print("Librero nuevo")

    def __del__(self):
        del(self.librerito)
        print("Librero eliminado")

    print("Libros\n")

    def agregaLibro(self, lbro):
        self.librerito.append(lbro)

    def agregaDisco(self, disc):
        self.librerito.append(disc)

        # -------------------------------
# Revista
    def agregaRevista(self, revis):
        print("Revistas")
        self.librerito.append(revis)

    def agregarComic(self, comic):
        print("Comic")
        self.librerito.append(comic)
