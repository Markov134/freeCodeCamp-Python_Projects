def adjacency_list_to_matrix(graph):
    matrix = []
    size = len(graph)
    for i in range(size):
        row = [0] * size
        node = graph[i]
        for j in node:
            row[j] = 1
        matrix.append(row)
        print(row)
    return matrix

adjacency_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

adjacency_list_to_matrix(adjacency_list)