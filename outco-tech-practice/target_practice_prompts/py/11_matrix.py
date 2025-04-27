#
# Target Practice - Matrices
#
#
# Problem 1:  Robot Paths
#
# Prompt:   Given a matrix of zeroes, determine how many unique paths exist
#           from the top left corner to the bottom right corner
#
# Input:    An Array of Array of Integers (matrix)
# Output:   Integer
#
# Example:  matrix = [[0,0,0,0],
#                     [0,0,0,0],
#                     [0,0,0,0]]
#
#           robotPaths(matrix) = 38
#
#
#           matrix = [[0,0,0],
#                     [0,0,0]]
#
#           robotPaths(matrix) = 4
from xxsubtype import bench


# Note:     From any point, you can travel in the four cardinal directions
#           (north, south, east, west). A path is valid as long as it travels
#           from the top left corner to the bottom right corner, does not go
#           off of the matrix, and does not travel back on itself

# Diagramming and Pseudocode:
# Coordinate system: that's just going to be our starting matrix
# we can use DFS combined with recursion to find all paths, returning a 1 with each valid path and summing up
# Traversing in 4 cardinal directions: this can be done with a list of tuples of ordered pairs representing the 4 cardinal directions
# We need to stop the recursion when we reach matrix edge boundaries and base cases, so we need to check these at the start each time
# Boundaries are going to return 0 and be out of the matrix
# - Boundaries will happen when we reach the length of the rows and columns of the matrix
# - They will also happen anytime we have a negative value for row or column
# Base cases include nodes we've already visited which will return 0
# - We need to keep track of nodes we've visited, we can do that by toggling the matrix, to a value of 1 instead of 0 for example
# - Since different paths might go through the same node, we need to backtrack on each path to re-toggle the values to 0 before we start a new path
# Base case also includes when we've reached the goal, the bottom right, which will return 1
# We'll have to use helper function recursion because the function only gives us a matrix, not a current node

def robot_paths(matrix):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row_length = len(matrix)
    col_length = len(matrix[0])

    def dfs(node):
        #first check if the current node is valid or if we can stop due to reaching the end
        if any([node[0] < 0, node[1] < 0, node[0] >= row_length, node[1] >= col_length]): #boundary conditions
            return 0
        if matrix[node[0]][node[1]] == 1: #already visited node
            return 0
        if node[0] == row_length-1 and node[1] == col_length-1: #this is the destination node
            return 1

        matrix[node[0]][node[1]] = 1    #indicate that we've visited the current node
        paths = 0

        for d in directions:
            new_node = [node[0]+d[0], node[1]+d[1]]
            paths += dfs(new_node)

        matrix[node[0]][node[1]] = 0    #to backtrack and remove visited to allow different paths to come through this node

        return paths

    return dfs([0,0])

# Problem # 2: Matrix spiral
#
# Given an (MxN) matrix of integers, return an array in spiral order.
#
# Input:  matrix {Integer[][]}
# Output: {Integer}
#
#
# Example:
# Input:  [[ 1, 2, 3],
#          [ 4, 5, 6],
#          [ 7, 8, 9]]
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
#
#

# Time Complexity: O(M*N)
# Auxiliary Space Complexity: O(1), because we can just keep subtracting 1 from the row and col length to know when to stop
## we don't need to store a matrix unless we're including the input

# This is basically just matrix traversal
# All we need to do is traverse to the boundary of the matrix, change direction, and decrement row or col length appropriately
# We also have to consider when the final stop will be
# We could include an m*n counter to do this, although more efficiency might be possible
# We also need to include our four main directions
# My idea to iterate between directions is to use a minimal circular linked list, since it's cyclical

def matrix_spiral(input):
    if any([len(input) == 0, len(input[0]) == 0]):  #this just deals with the edge case of no rows or no columns
        return []

    class Node:
        def __init__(self, direction):
            self.direction = direction
            self.next = None

    right, down, left, up = Node((0,1)), Node((1,0)), Node((0,-1)), Node((-1,0))
    right.next, down.next, left.next, up.next = down, left, up, right

    node = right    #we'll start moving to the right in the spiral
    pos = [0, 0]    #we need a position
    result = [input[0][0]]  #we'll start with the first element
    row_length = len(input) #we need to check boundary conditions
    col_length = len(input[0])
    count = row_length*col_length-1    #we need to iterate through this many elements before terminating, we already used the first

    while count > 0:
        if any([pos[0]+node.direction[0]>=row_length,
                pos[1]+node.direction[1]>=col_length,
                pos[0]+node.direction[0]<0,
                pos[1]+node.direction[1]<0]):
            node = node.next
            continue
        if input[pos[0]+node.direction[0]][pos[1]+node.direction[1]] == float('inf'):
            node = node.next
            continue
        input[pos[0]][pos[1]] = float('inf')    #we are toggling the matrix to know if we've already visited
        pos[0], pos[1] = pos[0]+node.direction[0],  pos[1]+node.direction[1]
        result.append(input[pos[0]][pos[1]])
        count-=1

    return result

#############################################
########  DO NOT TOUCH TEST BELOW!!!  #######
#############################################

def expect(count, name, test):
    if (count == None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    errMsg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        errMsg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if errMsg != None:
        print('       ' + errMsg + '\n')

def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

print('Robot Paths Tests')
test_count = [0, 0]


def test():
    matrix = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    example = robot_paths(matrix)
    return example == 38


expect(test_count, 'should work on first example input', test)


def test():
    matrix = [[0, 0, 0],
              [0, 0, 0]]
    example = robot_paths(matrix)
    return example == 4


expect(test_count, 'should work on second example input', test)


def test():
    matrix = [[0]]
    example = robot_paths(matrix)
    return example == 1


expect(test_count, 'should work on single-element input', test)


def test():
    matrix = [[0, 0, 0, 0, 0, 0]]
    example = robot_paths(matrix)
    return example == 1


expect(test_count, 'should work on single-row input', test)


def test():
    matrix = [[0],
              [0],
              [0],
              [0],
              [0]]
    example = robot_paths(matrix)
    return example == 1


expect(test_count, 'should work on a 5 x 8 matrix input', test)


def test():
    matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
    print("  Please be patient, test 6 may take longer to run")
    example = robot_paths(matrix)
    return example == 7110272


print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print("\nMatrix Spiral")
test_count = [0, 0]


def test():
    matrix = [[]]
    example = matrix_spiral(matrix)
    return example == []


expect(test_count, 'should work on empty matrix input', test)


def test():
    matrix = [[1]]
    example = matrix_spiral(matrix)
    return example == [1]


expect(test_count, "should work on single element matrix input", test)


def test():
    matrix = [[1],
              [2],
              [3],
              [4],
              [5]]
    example = matrix_spiral(matrix)
    return example == [1, 2, 3, 4, 5]


expect(test_count, "should work on single column matrix input", test)


def test():
    matrix = [[1, 2],
              [4, 3]]
    example = matrix_spiral(matrix)
    return example == [1, 2, 3, 4]


expect(test_count, "should work on square matrix input", test)


def test():
    matrix = [[1, 2, 3, 4]]
    example = matrix_spiral(matrix)
    return example == [1, 2, 3, 4]


expect(test_count, "should work on single row matrix input", test)


def test():
    matrix = [[ 1,  2,  3],
              [ 4,  5,  6],
              [ 7,  8,  9],
              [10, 11, 12],
              [13, 14, 15]]
    example = matrix_spiral(matrix)
    return example == [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]


expect(test_count, "should work on 3 x 5 matrix input", test)


def test():
    matrix = [[  1,  2,  3,  4, 5],
              [ 12, 13, 14, 15, 6],
              [ 11, 10,  9,  8, 7]]
    example = matrix_spiral(matrix)
    return example == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


expect(test_count, "should work on 5 x 3 matrix input", test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
