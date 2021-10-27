class StudentsDataException(Exception):
    def __init__(self):
        Exception.__init__(self)

class BadLine(StudentsDataException):
    def __init__(self):
        StudentsDataException.__init__(self)
        print("La lina introducida no es correcta")
    


class FileEmpty(StudentsDataException):
    def __init__(self):
        StudentsDataException.__init__(self)
        print("El fichero esta vacio")

listaClase = {}
wt = open("notas.txt", "wt")
wt.write("John Smith 5 \n")
wt.write("Anna Boleyn 4.5 \n")
wt.write("John Smith 2 \n")
wt.write("Anna Boleyn 11 \n")
wt.write("Andrew Cox 1.5 \n")
wt.close()

nombreFichero = input("Introduzca el nombre de fichero que desea abrir: ")
try:
    for line in  open(nombreFichero, "rt"):
        arrayregistro = line.split(" ")
        if len(arrayregistro) != 4:
            raise BadLine
        key = arrayregistro[0] + " " + arrayregistro[1]
        if key not in listaClase.keys():
            listaClase[arrayregistro[0] + " " + arrayregistro[1]] =  float(arrayregistro[2])
        else:
            listaClase.update({key : listaClase.get(key) + float(arrayregistro[2])})
    if len(listaClase) == 0:
        raise FileEmpty
    nuevaListaOrdenada = sorted(listaClase.items(),key =  lambda x : x[0] )
    for key,value in nuevaListaOrdenada:
        print(key + "\t" + str(value))
except FileEmpty as empty:
    print(empty)
except Exception as e:
    print(e)