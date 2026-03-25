def hanoi_solver(n) :
    result = ''
    one = [x for x in range(n, 0, -1)]
    two = []
    three = []

    result += f"{one} {two} {three}\n"
    total_moves = 2 ** n - 1
    
    rods = { 'A': one, 'B': two, 'C': three }

    #even
    if n % 2 == 0:
        for move in range(1, total_moves + 1):
            if move % 3 == 1:
                from_rod, to_rod = ('A', 'B') if (rods['A'] and (not rods['B'] or rods['A'][-1] < rods['B'][-1])) else ('B', 'A')
            elif move % 3 == 2:
                from_rod, to_rod = ('A', 'C') if (rods['A'] and (not rods['C'] or rods['A'][-1] < rods['C'][-1])) else ('C', 'A')
            else:
                from_rod, to_rod = ('B', 'C') if (rods['B'] and (not rods['C'] or rods['B'][-1] < rods['C'][-1])) else ('C', 'B')
        
            disk = rods[from_rod].pop()
            rods[to_rod].append(disk)

            if move != total_moves:
                result += f'{rods["A"]} {rods["B"]} {rods["C"]}\n'
            else:
                result += f'{rods["A"]} {rods["B"]} {rods["C"]}'
    #odd
    else:
        for move in range(1, total_moves + 1):
            if move % 3 == 1:
                from_rod, to_rod = ('A', 'C') if (rods['A'] and (not rods['C'] or rods['A'][-1] < rods['C'][-1])) else ('C', 'A')
            elif move % 3 == 2:
                from_rod, to_rod = ('A', 'B') if (rods['A'] and (not rods['B'] or rods['A'][-1] < rods['B'][-1])) else ('B', 'A')
            else:
                from_rod, to_rod = ('B', 'C') if (rods['B'] and (not rods['C'] or rods['B'][-1] < rods['C'][-1])) else ('C', 'B')
        
            disk = rods[from_rod].pop()
            rods[to_rod].append(disk)

            if move != total_moves:
                result += f'{rods["A"]} {rods["B"]} {rods["C"]}\n'
            else:
                result += f'{rods["A"]} {rods["B"]} {rods["C"]}'
    return result
          

print(hanoi_solver(3))

