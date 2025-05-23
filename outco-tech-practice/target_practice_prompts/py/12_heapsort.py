#  Target Practice - HeapSort
#
#  Prompt: Implement heapsort in-place.
#
#  NOTE: In-place means to manipulate the input list rather than create a
#        new list.
#
#  Input: {List}
#  Output: {List}
#
#  Example: heapsort([4,15,16,50,8,23,42,108])
#           // [4,8,15,16,23,42,50,108]
#

# Worse Time Complexity: O(Nlog(N))
# Worse Auxiliary Space Complexity: O(1)
# Average Time Complexity: O(Nlog(N))
# Average Auxiliary Space Complexity: O(1)

def heapsort(lst):

    length = len(lst)

    def bubbleDown(l, parent, boundary):

        def getChildIndex(l, parent, boundary):
            child1 = 2*parent + 1
            child2 = 2*parent + 2

            if child1 >= boundary:
                return child1
            elif child2 >= boundary:
                return child1   #this is done since child2>child1, so if child2>=boundary and we already know child1<boundary, then we want child1
            elif l[child1] > l[child2]:
                return child1   #we want to return the larger child since this is a max heap which is more convenient for heapsort
            else:
                return child2

        child = getChildIndex(l, parent, boundary)

        while child < boundary and l[parent] < l[child]:    #we need to restore the maxheap property only if the child exist in our list and is greater than the parent
            l[parent], l[child] = l[child], l[parent]
            parent = child  #the parent is not at the child index it just switched with, and we have to again make sure it's a maxheap
            child = getChildIndex(l, parent, boundary)

        return

    for i in range(length-1, -1, -1):
        bubbleDown(lst, i, length)

    for wall in range(length-1, -1, -1):
        lst[0], lst[wall] = lst[wall], lst[0]   #we're putting the guaranteed max element to the back of the array each time
        bubbleDown(lst, 0, wall)    #then just restoring the maxheap property to guarantee the next max element moves to the back

    return lst

############################################################
###############  DO NOT TOUCH TEST BELOW!!!  ###############
############################################################

# custom expect function to handle tests
# List count : keeps track out how many tests pass and how many total
#   in the form of a two item array i.e., [0, 0]
# String name : describes the test
# Function test : performs a set of operations and returns a boolean
#   indicating if test passed
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')

# code for capturing print output


from io import StringIO
import sys


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

# code for checking if lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

# custom function for checking if list is sorted (linear runtime)
def is_sorted(input):
    if (len(input) < 2):
        return True
    for i in range(1, len(input)):
        if (input[i-1] > input[i]):
            return False
    return True

# for getting random numbers
from random import randint

print('heapsort tests')
test_count = [0, 0]


def test():
    results = heapsort([5])
    return is_sorted(results)


expect(test_count, 'able to sort a single-element array', test)


def test():
    results = heapsort([4, 15, 16, 50, 8, 23, 42, 108])
    return lists_equal(results, [4, 8, 15, 16, 23, 42, 50, 108])


expect(test_count, 'able to sort a medium-sized unsorted list', test)


def test():
    results = []
    for i in range(0, 1000000):
        results.append(int(randint(0, 1000000)))
    example = heapsort(results)
    return lists_equal(sorted(results), example)


expect(test_count, 'able to sort a large unsorted array', test)
