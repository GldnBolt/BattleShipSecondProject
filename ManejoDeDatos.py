def log_in(Usuario, Password):
    Users = open("Files\LogIn_Data.txt", 'r')
    Users_Data = load_users(Users, [])
    Users.close()
    if Usuario in Users_Data:
        Index = Users_Data.index(Usuario) 
        if Users_Data[Index + 1] == Password:
            return True
        else:
            return 1
    else:
        return 0


def load_users(File, List):
    User = File.readline()[:-1]
    if User == "Final":
        return List
    else:
        List.append(User)
        Password = File.readline()[:-1]
        List.append(Password)
        return load_users(File, List)




