def save_game(GRID):
    GRID_F = open("JuegoGuardado.text", 'w')
    save_game_aux(GRID, GRID_F, 0)
    GRID_F.close()

def save_game_aux(GRID, GRID_F, i):
    if GRID == []:
        return 
    else:
        GRID_F.write(str(GRID[0]+"\n"))
        return save_game_aux(GRID[1:], GRID_F, i+1)
