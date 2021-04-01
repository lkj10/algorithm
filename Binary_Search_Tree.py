'''
#########SUDO-CODE##########

SEARCH(node, key)
    if node == NIL or node.key == key
        return node
    if key < node.key
        return SEARCH(node.left, key)
    else
        return SEARCH(node.right, key)

INSERT(node, key)
    if node == NIL
        node.key = key
        node.left = NIL
        node.right = NIL
    else if key < node.key
        node.left = INSERT(node.left, key)
    else
        node.right = INSERT(node.right, key)
    return node

DELETE(node)
    if node == root
        root = DELETE-NODE(node)
    else if node == node.parent.left
        node.parent.left = DELETE-NODE(node)
    else
        node.parent.right = DELETE-NODE(node)

#############################

'''

import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def insert(node, key):
    if node is None: node = Node(key)
    elif key < node.key: node.left = insert(node.left, key)
    else: node.right = insert(node.right, key)
    return node

def search(node, key):
    if node is None or node.key == key: return node
    if key < node.key: return search(node.left, key)
    return search(node.right, key)


x = random.sample(range(5000), 1000)
value = x[800]

root = None

for i in x:
    root = insert(root, i)

start = timer()
found = search(root, value)
print(timer() - start)

if found is not None:
    print(f"value :  {value}, found :  {found.key}")
    print(True if found.key == value else False)
