'''As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable,
before using more computationally intensive procedures for finding the optimal route.

The roads on the map are rasterized and produce a matrix of boolean values
- True if the road is present or False if it is not.
The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the route_exists method so that it returns True if the destination is reachable or False if it is not.
The from_row and from_column parameters are the starting row and column in the map_matrix.
The to_row and to_column are the destination row and column in the map_matrix.
The map_matrix parameter is the above mentioned matrix produced from the map.

For example, for the given rasterized map, the code below should return True since the destination is reachable:
map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

route_exists(0, 0, 2, 2, map_matrix)
'''

def route_exists(from_row, from_column, to_row, to_column, map_matrix):

    # read the matrix --> will return strings
    matrix = map_matrix
    #matrix = [i.strip() for i in matrix]
    #matrix = [i.split() for i in matrix]

    # find out matrix size
    row = len(map_matrix); col = len(map_matrix[0])

    #some presumptions
    if from_row == to_row and from_column == to_column: return True
    #if map_matrix[from_row][from_column] == False or map_matrix[to_row][to_column] == False: return False

    #creat an empty queue to contain successful paths from the start point
    q = list()
    for i in range(0,max(row,col)):
        q.append(i)

    #TRY all directions one after the other
    for direction in [(from_row, from_column+1),(from_row, from_column-1),(from_row+1, from_column),(from_row-1, from_column)]:
        next_row,next_column = direction

        if (0 <= next_row < row and 0 <= next_column < col and            # stay in matrix borders
                matrix[next_row][next_column] == True and                 # don't run in walls
                (next_row,next_column) not in q):                        # don't run in circles
            q.append((next_row, next_column))
        else:
            q.pop()

    if (next_row,next_column) == (to_row, to_column):
        return True
    else:
        return False
        
if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))

    
'''   
    #### 4 directions: NSWE meets False then turn
    while not q.empty():
        from_row,from_column = q.get()
                # heading East
                if from_column + 1 <= col and matrix[from_row][from_column+1] == "True":
                    #route_exists(from_row, from_column+1, to_row, to_column, map_matrix)
                    q.put((from_row,from_column+1))
                    #matrix[from_row][from_column] = matrix[from_row][from_column+1]
                    from_column += 1
                    return from_column
                    continue
                    #return matrix[from_row][from_column]

                # heading North
                if from_row + 1 <= row and matrix[from_row+1][from_column] == "True":
                    #route_exists(from_row+1, from_column, to_row, to_column, map_matrix)
                    q.put((from_row+1,from_column))
                    #matrix[from_row][from_column] = matrix[from_row+1][from_column+1]
                    from_row += 1
                    #return matrix[from_row][from_column]
                    return from_row
                    continue
                    
                # heading South
                if from_row - 1 >= 0 and matrix[from_row-1][from_column] == "True":
                    #route_exists(from_row-1, from_column, to_row, to_column, map_matrix)
                    q.put((from_row-1,from_column))
                    #matrix[from_row][from_column] = matrix[from_row-1][from_column+1]
                    from_row -= 1
                    return from_row
                    #return matrix[from_row][from_column]
                    continue

                # heading West
                if from_column - 1 >= 0 and matrix[from_row][from_column-1] == "True":
                    #route_exists(from_row, from_column-1, to_row, to_column, map_matrix)
                    q.put((from_row,from_column-1))
                    #matrix[from_row][from_column] = matrix[from_row][from_column-1]
                    from_column -= 1
                    return from_column
                    #return matrix[from_row][from_column]
                return (from_row,from_column)
    
    from_row,from_column = to_row, to_column
    var = matrix[from_row][from_column]
    
    if var == True:
        return "True"
    else:
        return "False"

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))
    print(map_matrix[0][0], map_matrix[0][1], map_matrix[1][1])
'''
    
