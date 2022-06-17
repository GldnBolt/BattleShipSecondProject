def log_in(Usuario, Password):
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
    User = File.readline()[:-1]
    if User == "Final":
        return List
    else:
        List.append(User)
        Password = File.readline()[:-1]
        List.append(Password)
        return load_users(File, List)

def reg_user(User, Password):
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

def quick_sort(lista):
    Menores = []
    Iguales = []
    Mayores = []
    if len(lista) <= 1:
        return lista
    Pivote = lista [-1]
    partir(lista, 0 ,len(lista), Pivote, Menores, Iguales, Mayores)
    Ret = quick_sort(Menores)
    Ret.extend(Iguales)
    Ret.extend(quick_sort(Mayores))
    return Ret
def partir(lista, i, n, Pivote, Menores, Iguales, Mayores):
    if i == n:
        return Menores, Iguales, Mayores
    if lista[i] < Pivote:
        Menores.append(lista[i])
    elif lista[i] > Pivote:
        Mayores.append(lista[i])
    elif lista[i] == Pivote:
        Iguales.append(lista[i])
    return partir(lista, i + 1, n, Pivote, Menores, Iguales, Mayores)

def insert_sort_aux(lista,i,n):
    if i==n:
        return lista
    Aux = lista[i]
    j = incluye_orden(lista,i,Aux)
    lista[j] = Aux
    return insert_sort_aux(lista, i+1,n)

def incluye_orden(lista,j,Aux):
    if j<=0 or lista[j-1]<=Aux:
        return j
    lista[j]=lista[j-1]
    return incluye_orden(lista, j-1, Aux)

