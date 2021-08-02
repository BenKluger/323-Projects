def makeAdjacencyMatrix(fileName):

    vertices = 0
    with open(fileName) as f:
        for line in f: 
            vertices += 1

    graph = [vertices][vertices]
    with open(fileName) as f:
        ## Ignore header
        #f.readline()

        # Let's consider `line` equals to '2 : 1 2, 3 14, 4 5, 5 4'
        #split returns two items, a string and list, from_vertex would be the string and remaining_line is the list
        #go thru the file twice, first to find how many lines (rows - assume starts at 0) (how many vertices) make them inf/0 depending on code


        for line in f:
            # from_vertex: '2', remaining_line: '1 2, 3 14, 4 5, 5 4'
            # convert to int
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
                #Add to graph, replace INF (Convert to int() first)
                fromV, toV = int(from_vertex), int(to_vertex)
                if fromV >= vertices or toV >= vertices:
                    print("FromV or ToV is out of range", fromV, toV)
                    exit                    
                graph[int(from_vertex)][int(to_vertex)] = weight

matrix = makeAdjacencyMatrix()
