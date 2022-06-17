
GRID_transformada = []

def escribir_file(data):
    file = open("./JuegoGuardado.txt", "a")
    file.write(data)
    file.close()


def read_game():
    file = open("./JuegoGuardado.txt", "r")
    info = file.read()
    info = info.split("\n")
    file.close()
    info = transformar_GRID(info)
    return info

def matrix_fix(GRID):
    aux = []
    for i in GRID:
        if i != []:
            aux += [i]
    return aux

def transformar_GRID(lista):
    GRID_transformada = []
    lista_aux = []
    for i in lista:
        for j in i:
                lista_aux += [int(j)]

        GRID_transformada += [lista_aux]
        lista_aux = []
    GRID_transformada = matrix_fix(GRID_transformada)
    return GRID_transformada
        
        
def guardar(m):
    for i in m:
        for j in i:
            escribir_file(str(j))
        escribir_file("\n")


#transformar_GRID(read_game())
