def dfs(matrix: list, node: int) -> list:
    print(matrix[node], node)
    queue = [node]
    visited = [node]

    while queue:
    # for _ in range(5):

        pop = queue.pop()
        
        if pop not in visited:
            visited.append(pop)
        
        for i in range(len(matrix[pop])):
            if matrix[pop][i] and i not in queue and i not in visited:
                queue.append(i)

        print("visited", visited)
        print("queue", queue)
        
        
    return visited
hi = dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)

print(hi)