def makeAdjacencyMatrix():
    with open('input.txt') as f:
        ## Ignore header
        #f.readline()

        # Let's consider `line` equals to '2 : 1 2, 3 14, 4 5, 5 4'
        for line in f:
            # from_vertex: '2', remaining_line: '1 2, 3 14, 4 5, 5 4'
            from_vertex, remaining_line = line.strip().split(" : ")

            # remaining_tokens: ['1 2', '3 14', '4 5', '5 4']
            remaining_tokens = remaining_line.split(", ")

            # remaning_values: [['1', '2'], ['3', '14'], ['4', '5'], ['5', '4']]
            remaining_values = [value.split(" ") for value in remaining_tokens]

            # to_vertex: '1', weight: '2'
            # to_vertex: '3', weight: '14'
            # to_vertex: '4', weight: '5'
            # to_vertex: '5', weight: '4'
            for to_vertex, weight in remaining_values:
                print(from_vertex, to_vertex, weight)

matrix = makeAdjacencyMatrix()
