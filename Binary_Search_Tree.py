'''
#########SUDO-CODE##########

SEARCH(t, x)
    if t == NIL or t.key == x
        return t
    if x < t.key
        return SEARCH(t.left, x)
    else
        return SEARCH(t.right, x)

SEARCH(node, key)
    if node == NIL or node.key == key
        return node
    if key < node.key
        return SEARCH(node.left, key)
    else
        return SEARCH(node.right, key)

INSERT(t, x)
    if t == NIL
        r.key = x
        r.left = NIL
        r.right = NIL
        return r
    if x < t.key
        t.left = INSERT(t.left, x)
        return t
    else
        t.right = INSERT(t.right, x)
        return t

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

#############################

'''

import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None: node = Node(key)
    elif key < node.key: node.left = insert(node.left, key)
    else: node.right = insert(node.right, key)
    return node

def search(node, key):
    if node is None or node.key == key: return Node
    if key < node.key: return search(node.left, key)
    return search(node.right, key)

x = random.sample(range(5000), 1000)
value = x[800]

root = None
for i in  x:
    root = insert(root, i)

start = timer()
found = search(root, value)
print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)
