def log_in(Usuario, Password):
    """
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores

    Función: log_in()
    Lenguaje: Python 3.9.9
    Autor: Andres Blanco Coto (2022108841) y Claudio Arce Cascante (201058559)
    Version: 7.0
    Fecha de última modificación: 17/6/2022
    Entrada: Usuario, Password
    Restricciones: Que no sean vacios
    Salidas: 1, 2, 3.
    """
    Users = open("Files\LogIn_Data.txt", 'r')
    Users_Data = load_users(Users, [])
    Users.close()
    if Usuario in Users_Data:
        Index = Users_Data.index(Usuario)
        if Users_Data[Index + 1] == Password:
            return 1
        else:
            return 2
    else:
        return 3

def valid_reg(Usuario):
    Users = open("Files\LogIn_Data.txt", 'r')
    Users_Data = load_users(Users, [])
    Users.close()
    if Usuario in Users_Data:
        return True
    else: 
        return False

def load_users(File, List):
    """
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores

    Función: load_users()
    Lenguaje: Python 3.9.9
    Autor: Andres Blanco Coto (2022108841) y Claudio Arce Cascante (201058559)
    Version: 7.0
    Fecha de última modificación: 17/6/2022
    Entrada: File, list
    Restricciones: No tiene
    Salidas: No hay, solo carga los usuarios en el archivo.
    """
    User = File.readline()[:-1]
    if User == "Final":
        return List
    else:
        List.append(User)
        Password = File.readline()[:-1]
        List.append(Password)
        return load_users(File, List)

def reg_user(User, Password):
    """
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores

    Función: reg_user()
    Lenguaje: Python 3.9.9
    Autor: Andres Blanco Coto (2022108841) y Claudio Arce Cascante (201058559)
    Version: 7.0
    Fecha de última modificación: 17/6/2022
    Entrada: Usuario, Password
    Restricciones: Que no sean vacios
    Salidas: No tiene.
    """
    Users = open("Files\LogIn_Data.txt", 'r')
    Users_Data = load_users(Users, [])
    Users.close()
    Users_Data.append(User)
    Users_Data.append(Password)
    Users = open("Files\LogIn_Data.txt", 'w')
    reg_user_aux(Users, Users_Data)
    Users.close()

def reg_user_aux(File, Users_Data):
    if Users_Data == []:
        File.write(str("Final "))
        return
    else:
        File.write(str(Users_Data[0])+"\n")
        File.write(str(Users_Data[1])+"\n")
        return reg_user_aux(File, Users_Data[2:])

def val_empt_str_aux(Str, Str2, n , i):
    if i == n:
        return False
    elif Str == Str2:
        return True
    else:
        return val_empt_str_aux(Str, Str2+" ", n, i+1)

#Ordenamiento de posiciones del salon de la fama
def insertionSort(Matrix):
    for i in range(1,len(Matrix)):
        key=Matrix[i][0]
        key1 = Matrix[i]
        j=i-1
        while j>=0 and key<Matrix[j][0]:
            Matrix[j+1]=Matrix[j]
            j=j-1
        Matrix[j+1]=key1
    return Matrix

def quick_sort(Matrix):
    Menores = []
    Iguales = []
    Mayores = []
    if len(Matrix)<=1:
        return Matrix
    Pivote = Matrix[-1][1]
    partir(Matrix, 0, len(Matrix), Pivote, Menores, Iguales, Mayores)
    Ret = quick_sort(Menores)
    Ret.extend(Iguales)
    Ret.extend(quick_sort(Mayores))
    return Ret

def partir(Matrix, i, n, Pivote, Menores, Iguales, Mayores):
    if i == n:
        return Menores, Iguales, Mayores
    if Matrix[i][1] < Pivote:
        Menores.append(Matrix[i])
    elif Matrix[i][1] > Pivote:
        Mayores.append(Matrix[i])
    elif Matrix[i][1] == Pivote:
        Iguales.append(Matrix[i])
    return partir(Matrix, i+1, n, Pivote, Menores, Iguales, Mayores)

def inverse(Matrix):
    Result = []
    for i in range(1, len(Matrix)):
        Result.append(Matrix[-i])
    Result.append(Matrix[0])
    return Result

#Manejo de Archivo de Puntajes
def save_score(Scores):
    """
               Instituto Tecnológico de Costa Rica
               Ingenieria en Computadores
       Lenguaje: Python 3.9.9
       Autores: Claudio Arce Cascante (201058559)
       Version: 1.0
       Fecha de última modificación: Mayo 07/ 2022
       Entradas: Matriz
       Restricciones: Entrada es Matriz
       Salidas: No tiene
    """
    Scores_F = open("Files\Scores_txt.txt", 'w')
    save_score_aux(Scores, Scores_F, 0)
    Scores_F.close()

def save_score_aux(Scores, Scores_F, i):
    if Scores == []:
        return
    else:
        Scores_F.write(str(Scores[0][0])+"\n")
        Scores_F.write(str(Scores[0][1])+"\n")
        return save_score_aux(Scores[1:], Scores_F, i+1)

def load_scores():
    """
               Instituto Tecnológico de Costa Rica
               Ingenieria en Computadores
        Lenguaje: Python 3.9.9
        Autores: Claudio Arce Cascante (201058559)
        Version: 1.0
        Fecha de última modificación: Mayo 07/ 2022
        Entradas: No tiene
        Restricciones: No tiene
        Salidas: Matriz de nombres de Jugadores y Puntajes
    """
    Scores_F = open("Files/Scores.txt", 'r')
    Matrix = load_scores_aux(Scores_F, 0, [], [])
    Scores_F.close()
    return Matrix

def load_scores_aux(File, i, Temp, Matrix):
    if i == 10:
        return Matrix
    else:
        Temp.append(File.readline()[:-1])
        try:
            Temp.append(int(File.readline()[:-1]))
        except:
            Temp.append(File.readline()[:-1])
        Matrix.append(Temp)
        return load_scores_aux(File, i+1, [], Matrix)

def build_scores_str(Matrix, Scores_text):
    """
               Instituto Tecnológico de Costa Rica
               Ingenieria en Computadores
       Lenguaje: Python 3.9.9
       Autores: Claudio Arce Cascante (201058559)
       Version: 1.0
       Fecha de última modificación: Mayo 07/ 2022
       Entradas: Matriz
       Restricciones: Entrada es Matriz que contiene vectores de 1x2
       Salidas: String listo para ser colocado en un label de Tkinter
    """
    if Matrix == []:
        return Scores_text
    else:
        if Matrix[0][0] == "":
            Scores_text += "\n"
            return build_scores_str(Matrix[1:], Scores_text)
        else:
            Scores_text += Matrix[0][0] + " : " + str(Matrix[0][1]) + "\n"
            return build_scores_str(Matrix[1:], Scores_text)