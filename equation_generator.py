from sympy import *
import math
import pickle
import os.path
from os import path
from generic_utilities import *

"""
This file enumerates all possible equations over a set
of symbols. This should not be modified with a change
in theory


there are two components to the tree accumulation
statge. The first is the leaf enumeration.

Since I'm only looking for non-trivial equations,
there should be at least two symbols in the tree.
Most equations of interest are relatively simple,
so I require that a symbol be used at most three times.


Once in the tree, we assign binary operations to 
nodes. Each node also has a cost symbol potentially.
unary operations like square root are encoded as binary
operations to avoid having to enumerate a larger class
of tree.

Trees are generated, and the contents are memoized
to the current file with pickle, since that's an
expensive operation that's universal. Expressions are
not memoized.
"""

#currently costless, since I'm doing direct enumeration.
#It's important to note that the exponentiation is likely
#expensive, since nothing complex is expected to be
#in the right branch.
symbols_list = [
    -1, 0, 1, 2, 3, 4#Very important to balance
]
binary_list = [
    lambda a, b: a*b, 
    lambda a, b: a+b,
    lambda a, b: a-b,
    lambda a, b: a/b,#Is this best?
    lambda a, b: a**b]

# A function to generate non-isomorphic unlabeled binary trees with n nodes
def enumerate_trees(n):
    file_name = "tree-" + n + ".py"
    temp = mem_get(file_name)
    if temp != 0:
        return temp

    if n == 0:
        return [None]
    if n == 1:
        return [Node()]
    trees = []
    for i in range(n):
        left_trees = enumerate_trees(i)
        right_trees = enumerate_trees(n-i-1)
        for left in left_trees:
            for right in right_trees:
                tree = Node()
                tree.left = left
                tree.right = right
                # Ensure that the left subtree has no more nodes than the right subtree
                if left is not None and (left.size > right.size or (left.size == right.size and left.height > right.height)):
                    continue
                # Check if the tree is isomorphic to any previously generated trees
                is_isomorphic = False
                for t in trees:
                    if tree.isomorphic(t):
                        is_isomorphic = True
                        break
                # If the tree is not isomorphic to any previously generated trees, add it to the list
                if not is_isomorphic:
                    trees.append(tree)

    mem_put(trees, file_name)
    return trees

# A simple class to represent nodes in a binary tree
class Node:
    def __init__(self):
        self.left = None
        self.right = None
    
    # Calculate the size and height of the subtree rooted at this node
    @property
    def size(self):
        left_size = self.left.size if self.left is not None else 0
        right_size = self.right.size if self.right is not None else 0
        return 1 + left_size + right_size
    
    @property
    def height(self):
        left_height = self.left.height if self.left is not None else -1
        right_height = self.right.height if self.right is not None else -1
        return 1 + max(left_height, right_height)
    
    # Check if this tree is isomorphic to another tree
    def isomorphic(self, other):
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        elif self.size != other.size:
            return False
        else:
            return self.left.isomorphic(other.left) and self.right.isomorphic(other.right)




# Test the function with n=3
trees = enumerate_trees(3)
for tree in trees:
    print(tree.size, tree.height)

#Now, for a given tree, we serialize it. This is toilet work
