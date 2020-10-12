from libro import Libro
from disco import Disco
from revista import Revista
from librero import Librero
from comic import Comic
from manga import Manga
miLibrero = Librero()

miLibrero.agregaLibro(
    Libro(autor="korth", titulo="bases", editorial="Pearson"))


# Disco    
miLibrero.agregaDisco(Disco(interprete="Ricardo Montaner",
                            titulo="Vuelve Conmigo", album="Ida y Vuelta Edición Especial", anio=2017))
miLibrero.agregaDisco(Disco(interprete="Michael Jackson",
                            titulo="Bllie Jean", album="Thriller", anio=1983))
miLibrero.agregaDisco(Disco(interprete="Zara Larsson",
                            titulo="Lush Life", album="So Good", anio=2017))
miLibrero.agregaDisco(Disco(interprete="Hailee Steinfeld",
                            titulo="Love Myself", album="Haiz", anio=2015))
miLibrero.agregaDisco(Disco(interprete="Carly Rae Jepsen",
                            titulo="I Really Like You", album="Emotion", anio=2015))


#Revista
miLibrero.agregaRevista(Revista(nombreR="Muy interesante", articulosR="Ciencia, Salud, Tecnologia",
                                editorialR="Zinet Media Global", fechaEmision="enero 2020"))

miLibrero.agregaRevista(Revista(nombreR="Muy interesante", articulosR="Ciencia, Tecnologia",
                                editorialR="Zinet Media Global", fechaEmision="enero 2019"))

miLibrero.agregaRevista(Revista(nombreR="Mi bebé y yo", articulosR="Salud y cuidados, Alimentacion, Juegos ",
                                editorialR="Zinet Media Global", fechaEmision="enero 2020"))

miLibrero.agregaRevista(Revista(nombreR="National Geographic", articulosR="Fotografía",
                                editorialR="Zinet Media Global", fechaEmision="noviembre 2017"))


# Comic
miLibrero.agregarComic(Comic(autor="Gerard Way", titulo="The umbrella academy",
                             anio="2018", editorial="Dark Horse Comics"))

# Manga
miLibrero.agregarManga(Manga(autorM="Sui ishida", tituloM="Tokyo Ghoul: re", editorialM="Panni"))

miLibrero.agregarManga(Manga(tituloM="Suicide boy",autorM="ParkGee",numeroM="57",tomoM="2",editorialM="Lezhin"))

miLibrero.agregarManga(Manga(tituloM="Platinum end",autorM="anonimo",numeroM="35",tomoM="1",editorialM="Panni"))

miLibrero.agregarManga(Manga(tituloM="Attack on titan",autorM="Hajime Isayama",numeroM="107",tomoM="8",editorialM="Panni"))

miLibrero.agregarManga(Manga(tituloM="All you need is kill",autorM="anonimo",numeroM="3",tomoM="1",editorialM="Panni"))

#mostrando los objetos del librero
miLibrero.muestra()