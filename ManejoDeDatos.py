def log_in(Usuario, Contraseña):
    Users = open("Files\LogIn_Data.txt", 'r')
    Users_Data = load_users(Users, [])
    Users.close()
    print(Users_Data)

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




