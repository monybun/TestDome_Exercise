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

    if dfs():
        print("Success!")

    else:
        print("Failure!")


def dfs(current_path):
    from_row, from_column = 0,0
    # anchor
    from_row, from_column = current_path[-1]
    if (from_row, from_column) == (to_row, to_column):
        return True
    
    # try all directions one after the other
    for direction in [(from_row, from_column + 1), (from_row, from_column - 1), (from_row + 1, from_column), (from_row - 1, from_column)]:
        new_row, new_col = direction
        
        if (0 <= new_row < row and 0 <= new_col < col and  # stay in matrix borders
                matrix[new_row][new_col] == "False" and                  # don't run in walls
                (new_row, new_col) not in current_path):             # don't run in circles
            # try new direction
            current_path.append((new_row, new_col))

            if dfs(current_path):  # recursive call
                return True
            else:
                current_path.pop()  # backtrack
        
    

# result a list of coordinates which should be taken in order to reach the goal

if __name__ == '__main__':
    map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
    ];

    route_exists(0, 0, 2, 2, map_matrix)
