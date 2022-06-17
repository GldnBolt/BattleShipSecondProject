def log_in(Usuario, Password):
    Users = open("Files\LogIn_Data.txt", 'r')
    Users_Data = load_users(Users, [])
    Users.close()
    print(Users_Data)
    if Usuario in Users_Data:
        Index = Users_Data.index(Usuario)
        if Users_Data[Index + 1] == Password:
            print(Password, Users_Data[Index + 1])
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
    print(User)
    if User == "Final":
        return List
    else:
        List.append(User)
        Password = File.readline()[:-1]
        List.append(Password)
        return load_users(File, List)

def reg_user(User, Password):
    print(User, Password)
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



