# clases persona, alumno profesor

class Persona:
    nombre = None
    ap = None
    am = None
    rfc = None

    def __init__(self, nombre=None, ap=None, am=None, rfc=None):
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.rfc = rfc

    def __muestra(self):
        print("nombre: ", nombre)
        print("ap: ", ap)
        print("am: ", am)
        print("rfc: ", rfc)


class alumno(Persona):

    def __init__(self, nombre=None, ap=None, am=None, rfc=None, matricula=None, semestre=None):
        super().__init__(nombre, ap, am, rfc)
        self.matricula = matricula
        self.semestre = semestre


class profesor(Persona):
    def __init__(self, nombre=None, ap=None, am=None, rfc=None, matricula=None, area=None, horasClase=None):
        super(profesor, self).Persona
        self.matricula = matricula
        self.area = area
        self.horasClase = horasClase

 # def muestra(self):

# principal


toño = alumno("toño", "perez", "lopez", None, "123456789", 6)

#toño = profesor("Javier", "Castillo", "Perez",
 #               3261, 4815162342, "Matemáticas", 36)

toño.muestra()

# checar el apartado SUPER EN PYTHON

# ________________________UNICA FORMA DE SUBIR ES MEDIANTE GITHUB________________________________________
