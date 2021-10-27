def contarCaracteres(linea, diccionary):
    linea = linea.upper()
    for ch in linea:
        if ch in diccionary.keys():
            diccionary[ch] += 1
            
    #65 90
mydictionary = {}
for i in range(65,91):
    mydictionary[chr(i)] = 0
nombreArchivo = input("Escribe el nombre del archivo que deseas crear ")
try:
    wt = open(nombreArchivo, "wt")
    entrada = input("Escribe lo que quieras o * para acabar ")
    while entrada != "*":
        wt.write(entrada + '\n')
        entrada = input("Escribe lo que quieras o * para acabar ")
    wt.close()
except IOError as e:
    print(e)
try:
    rt = open(nombreArchivo, "rt")
    entrada = rt.readline()
    while entrada != '':
        contarCaracteres(entrada, mydictionary)
        entrada = rt.readline()
    for key, value in mydictionary.items():
        print(key + " ->" + value)
        
except IOError as e:
    print(e)
    