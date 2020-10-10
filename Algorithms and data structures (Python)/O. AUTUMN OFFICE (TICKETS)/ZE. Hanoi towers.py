# Ханойские башни
# https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/
# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top
# of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# 3) No disk may be placed on top of a smaller disk.
# Note: Transferring the top n-1 disks from source rod to Auxiliary rod can again be thought of as a
# fresh problem and can be solved in the same manner.
# Recursive Python function to solve the tower of hanoi


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Driver code
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
# A, C, B are the name of rods
