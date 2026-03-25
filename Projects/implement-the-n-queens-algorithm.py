from itertools import permutations
def dfs_n_queens(n):
    board = []
    if n < 1:
        return board
    
    sol=0
    cols = range(n)
    for combo in permutations(cols):                      
        if n == len(set(combo[i]+i for i in cols)) == len(set(combo[i]-i for i in cols)):
            sol += 1
            board.append(list(combo))
            print('Solution '+str(sol)+': '+str(combo)+'\n')  
            print("\n".join(' o ' * i + ' X ' + ' o ' * (n-i-1) for i in combo) + "\n\n\n\n")
    return board

