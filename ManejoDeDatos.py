def log_in(Usuario, Contraseña):
    Users = open("LogIn_Data.txt", 'r')
    Users_Data = load_scores_aux(Scores_F, 0, [], [])
    Users.close()
    return Matrix

def load_scores_aux(File, i, Temp, Matrix):
    if i == 7:
        return Matrix
    else:
        Temp.append(File.readline()[:-1])
        try:
            Temp.append(int(File.readline()[:-1]))
        except:
            Temp.append(File.readline()[:-1])
        Matrix.append(Temp)
        return load_scores_aux(File, i+1, [], Matrix)




