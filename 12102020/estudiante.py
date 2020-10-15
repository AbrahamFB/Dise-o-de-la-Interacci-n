# clases persona, alumno profesor

class Persona: #creamos la clase persona 
    nombre = None #los datos se muestran vacios
    ap = None
    am = None
    rfc = None

  #declaramos el constructor
    def __init__(self, nombre=None, ap=None, am=None, rfc=None):
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.rfc = rfc
  #agregamos una funcion para mostrar los datos obtenidos
    def muestra(self):
        print(40*"-")
        print("nombre: ", self.nombre)
        print("ap: ", self.ap)
        print("am: ", self.am)
        print("rfc: ", self.rfc)


#creamos la clase alumno, la clase Persona dentro indica la herencia
class Alumno(Persona):

    #declaramos el constructor
    def __init__(self, nombre=None, ap=None, am=None, rfc=None, 
                 matricula=None, semestre=None):
        #llamanos los datos de la clase Persona
        super().__init__(nombre, ap, am, rfc)
        
        #datos pertenecientes solo al alumno
        self.matricula = matricula
        self.semestre = semestre


#Declaramos la clase profesor que hereda de Persona
class Profesor(Persona):
    def __init__(self, nombre=None, ap=None, am=None, rfc=None, 
                 matricula=None, area=None, horasClase=None):
        
        #llamamos datos de la clase Persona
        super().__init__(nombre, ap, am, rfc)

        #datos pertenecientes solo al profesor
        self.matricula = matricula
        self.area = area
        self.horasClase = horasClase


# principal

#creamos un objeto de cada clase
toño = Alumno("Antonio", "Perez", "Lopez", None, "123456789", 6)

Javi = Profesor("Javier", "Castillo", "Perez",3261, 4815162342,
                "Matemáticas", 36)

#probamos la herencia en ambas clases llamando a la funcion de
#la clase Persona muestra()
toño.muestra()
Javi.muestra()








# checar el apartado SUPER EN PYTHON

# ________________________UNICA FORMA DE SUBIR ES MEDIANTE GITHUB________________________________________
