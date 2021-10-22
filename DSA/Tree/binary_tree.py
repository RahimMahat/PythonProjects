import math
from collections import deque

class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def inorder(root):
    # left-root-right
    if root != None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)
    # time complexity: theta(n), aux space: theta(h)

def preorder(root):
    # root-left-right
    if root != None:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)
    # time complexity: theta(n), aux space: theta(h)

def postorder(root):
    # left-right-root
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=' ')
    # time complexity: theta(n), aux space: theta(h)

def tree_size(root):
    if root == None:
        return 0
    else:
        ls = tree_size(root.left)
        rs = tree_size(root.right)
        return ls + rs + 1          # left_side + right_side + 1(root)
    # time complexity: theta(n), aux space: theta(h)

def find_max(root):
    if root == None:
        return -math.inf
    else:
        lm = find_max(root.left)    # getting max of left subtree
        rm = find_max(root.right)   # getting max of right subtree
        return max(root.key, lm, rm)    
    # time complexity: theta(n), aux space: theta(h)

def search_value(root, value):
    if root is  None:
        False
    elif root.key == value:
        return True
    elif search_value(root.left, value) == True:
        return True
    else:
        return search_value(root.right, value)
    # time complexity: bigO(n), aux space: bigO(h)

def tree_height(root):
    if root == None:
        return 0
    else:
        lh = tree_height(root.left)
        rh = tree_height(root.right)
        return max(lh, rh) + 1 
    # time complexity: theta(n), aux space: theta(h)

def iter_inorder(root):
    if root is None:
        return
    st = []
    curr = root
    while curr is not None:
        st.append(curr)
        curr = curr.left
    while len(st) > 0:
        curr = st.pop()
        print(curr.key, end=' ')
        curr = curr.right
        while curr is not None:
            st.append(curr)
            curr = curr.left 
    # time complexity: theta(n), aux space: theta(h)
        
def iter_preorder(root):
    if root is None:
        return 
    st = [root]
    while len(st) > 0:
        curr = st.pop()
        print(curr.key)
        if curr.right is not None:
            st.append(curr.right)
        if curr.left is not None:
            st.append(curr.left)
    # time complexity: theta(n), aux space: theta(h)
    
def level_order(root):
    # level by level traversal
    # by using a queue we put a level in the queue by the time it became empty the next level would have been inserted in the queue
    if root is None:
        return 
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.key, end=' ')

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    # TC: theta(n), aux. space: bigO(n)



# driver code:
'''
        10
        /\
        20 30
            /\
            40 50
'''
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print('in-order traversal: ', end='')
inorder(root)
print()
print('pre-order traversal: ', end='')
preorder(root)
print()
print('post-order traversal: ', end='')
postorder(root)
print()
print(f'tree size is: {tree_size(root)}')

print(f'max value is: {find_max(root)}')

print(search_value(root, 50))

print(f'Height of tree is: {tree_height(root)}')

print('Level order traversal is: ', end= ' ')
level_order(root)
