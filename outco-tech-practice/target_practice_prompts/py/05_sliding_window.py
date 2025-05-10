# Target Practice - Dynamic Programming pt. 2
#
# Minimum Window Substring (Sliding Window)
#
# Given a string, and a set of characters
# return the substring representing the SMALLEST
# window containing those characters.
#
# The characters needn't appear in the order in which they are given.
#
# If not all the characters are present in the string, return the empty string.
#
#
# Input: str   (String)
#        chars (String)
#
# Output: {String}
#
#
# Example:
#  Input: "ADOBECODEBANC", "ABC"
#  Output: "BANC"
#
#  Input: "HELLO WORLD", "FOO"
#  Output: ""
#
#
# Explanation:
#
# Though there are many substrings containing all the characters
# "BANC" is the shortest.
#
# Assume that there won't be repeated characters in the second string input.
#
# Ignore capitalization.
# (though taking it into account doesn't change the solution much)
#
# But as extra credit, how would you handle repeats?
# Meaning if you were given two "A" characters, a valid window MUST
# contain two "A"s

def minimum_window_substring(S, T):

    if len(T) > len(S):
        return ''

    right = 0
    left = 0
    result = [0, float('inf')]
    counts = {}
    missingChars = len(T)

    #building our dictionary to account for each character in the target we need to track
    #takes into account the extra credit of having possibly duplicate characters
    for i in range(len(T)):
        char = T[i]
        if char in counts:
            counts[char]+=1
        else:
            counts[char]=1

    while right < len(S):   #sets up our loop to run until we reach past the end of the word
        if missingChars > 0:
            #hunting phase since we did not meet the condition of finding all characters yet
            rChar = S[right]
            if rChar in counts:
                if counts[rChar] > 0:   #we haven't found all instances of this character that we need yet
                    missingChars-=1
                counts[rChar]-=1    #this takes into account having more than we need of a character

        #catchup phase since we finally met the conditions, there are no more missing characters
        #we want to make the window as small as possible here by moving left pointer
        #so that there are still zero missing characters from our target in our substring
        while missingChars == 0:
            if (right-left) < (result[1] - result[0]):  #found a smaller window that our previous best
                result = [left, right]
            lChar = S[left]
            if lChar in counts:
                counts[lChar]+=1
                if counts[lChar] > 0:
                    missingChars+=1 #once counts are positive, we have some missing target characters
            left+=1

        right +=1

    if result[1] == float('inf'):   #we never found the target in the string
        return ''
    else:
        return S[result[0]:result[1]+1]

# Problem 2:  Dungeon Escape
#
#             Given a matrix of integers that represents rooms in a dungeon,
#             determine the minimum amount of health a adventurer must start with
#             in order to escape the dungeon
#
#             The adventurer starts at the upper left corner of the matrix, and
#             the exit is located at the bottom right corner.
#
#             The adventurer must leave the dungeon before sundown, so in the
#             interest of time, this brave adventurer decides to only travel
#             downwards and to the right
#
#             Negative integers represent rooms with monsters, so the adventurer
#             would lose health when going though these rooms. 0s represent empty
#             rooms, and positive integers represent rooms that contain health
#             pots that will increase the adventurer's health
#
#
#  Input:     dungeon {Integer[][]}
#  Output:    {Integer}
#
#
# Example:
#  Input:    [[ -2, -5, 10],
#             [ -3,-10, 30],
#             [  3,  1, -5]]
#
#  Output:   7 (The steps to do this would be down, down, right, right)
#
#
#    Note:   The initial health should be represented by a positive integers
#            If the health ever drops to zero or a negative integer, the
#            adventurer dies.
#            Every room will contain an integer. It will either be empty (0),
#            contain a monster (negative), or contain a health pot (positive).
#            You could create every single possible path, but there is of course
#            a dynamic programming approach to not go with this route.
#
#

# Time Complexity: O(mn), because of storing values using memoization, we will just recurse through all the rooms in the dungeon once
# Auxiliary Space Complexity: O(mn), because we're storing a cache will the subproblem starting from each room of the matrix

# Two steps to solve this:
# Step one: a recursion very similar to lattice paths will let us efficiently get all paths in combination with memoization
# Step two: we need to run some technique to find the point in the path with the lowest health, a prefix sum might work for that, or just adding the
# Important realization: we can run down the recursive tree and start from the base case, the dungeon exit, storing the amount of lost health
# If we reach a point where the stored value becomes positive, we can discard it since the hero needs no extra help to get through that part of the path all the way to the end base case we started from
# When discarding the positive paths, we will just zero them out and start over trying to find the negative
# We just start recalculating from the new step, and we compare the two recursive paths

from functools import lru_cache

def dungeon_escape(dungeon):
    @lru_cache(maxsize=None)
    def dfs(r, c):
        if r>=len(dungeon) or c>=len(dungeon[0]):   #if we go out of bounds, we are done and there is no chance we use this value so negative infinity ensures it's never chosen
            return float('-inf')
        if r==len(dungeon)-1 and c==len(dungeon[0])-1:  #this is the base case, the exit room, and we return 0 in a positive case and the actual value in a negative case
            if dungeon[r][c] >= 0:
                return 0
            else:
                return dungeon[r][c]
        down = dfs(r+1, c)+dungeon[r][c]    #the recursion steps, adding the new value from the current dungeon room
        right = dfs(r, c+1)+dungeon[r][c]
        if down>=0: #if the down or right path is neutral or positive, then we can zero it out since we need to get there first, but it's the best option so we can return
            return 0
        if right>=0:
            return 0
        return max(down, right)
    return -dfs(0, 0) + 1   #we kept track of health loss starting from zero, so the actual minimum health is the negative of that +1 so there is at least one health at the end

## There is another solution in my alt solutions which has the following complexity and uses sliding window:
## Time Complexity: O(n)
## Space Complexity: O(1)


#############################################
########  DO NOT TOUCH TEST BELOW!!!  #######
#############################################
from math import inf

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

print('Minimum Window Substring Tests')
test_count = [0, 0]


def test():
    example = minimum_window_substring("ADOBECODEBANC", "ABC")
    return example == "BANC"


expect(test_count, 'should work on first example case', test)


def test():
    example = minimum_window_substring("HELLO WORLD", "FOO")
    return example == ""


expect(test_count, 'should work on second example case', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print("\nEscape Dungeon tests")
test_count = [0, 0]

def test():
    dungeon = [[-2, -5, 10],
               [-3, -10, 30],
               [3, 1, -5]]

    example = dungeon_escape(dungeon)
    return example == 7

expect(test_count, "should work for first example case", test)

def test():
    dungeon = [[5, 1, 10],
               [10, 312, 30],
               [3, 1, 7]]

    example = dungeon_escape(dungeon)
    return example == 1

expect(test_count, "should work for dungeon filled solely with health potions", test)

def test():
    dungeon = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    example = dungeon_escape(dungeon)
    return example == 1

expect(test_count, "should work for an empty dungeon", test)

def test():
    dungeon = [[-3, -6, -13],
               [-12, -1, -7],
               [-5, -11, -2]]

    example = dungeon_escape(dungeon)
    return example == 20

expect(test_count, "should work for a dungeon filled only with monsters", test)

def test():
    dungeon = [[-2, 5]]
    example = dungeon_escape(dungeon)
    return example == 3

expect(test_count, "should work for a two-room dungeon starting with a monster", test)

def test():
    dungeon = [[-13, 5]]
    example = dungeon_escape(dungeon)
    return example == 14

expect(test_count, "should work for a two-room dungeon starting with a strong monster", test)

def test():
    dungeon = [[5, -2]]
    example = dungeon_escape(dungeon)
    return example == 1

expect(test_count, "should work for a two-room dungeon starting with a health pot", test)

def test():
    dungeon = [[5, -8]]
    example = dungeon_escape(dungeon)
    return example == 4

expect(test_count, "should work for a two-room dungeon ending in a strong monster", test)

def test():
    dungeon = [[-14]]
    example = dungeon_escape(dungeon)
    return example == 15

expect(test_count, "should work a dungeon with only a monster", test)

def test():
    dungeon = [[6]]
    example = dungeon_escape(dungeon)
    return example == 1

expect(test_count, "should work a dungeon with only a health pot", test)

def test():
    dungeon = [[0]]
    example = dungeon_escape(dungeon)
    return example == 1

expect(test_count, "should work a dungeon with a single empty room", test)

print("\nPASSED: " + str(test_count[0]) + '/' + str(test_count[1]))
