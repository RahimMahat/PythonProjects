class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def searchBST(root, key):
    # recursive method:
    # if root is None:
    #     return False
    # elif root.key == key:
    #     return True
    # elif root.key > key:
    #     return searchBST(root.left, key)
    # else:
    #     return searchBST(root.right, key)
    # # TC: bigO(h), aux space: bigO(h)

    # iterative method:
    while root != None:
        if root.key == key:
            return True
        if root.key > key:
            root = root.left
        else:
            root = root.right
    return False
    # # TC: bigO(h), aux space: bigO(1)

def insertBST(root, key):
    # recursive method:
    if root == None:
        return Node(key)
    elif root.key == key:
        return root
    elif root.key > key:
        root.left = insertBST(root.left, key)
    else:
        root.right = insertBST(root.right, key)
    return root
    # #TC: bigO(h), aux space: bigO(h)

    # iterative method:
    # parent = None
    # curr = root
    # while curr != None:
    #     parent = curr
    #     if curr.key == key:
    #         return root
    #     elif curr.key > key:
    #         curr = curr.left
    #     else:
    #         curr = curr.right
    # # for empty tree
    # if parent == None:
    #     return Node(key)
    # if parent.key > key:
    #     parent.left = Node(key)
    # else:
    #     parent.right = Node(key)
    # return root
    # # TC: bigO(h), aux space: bigO(1)


def getSucc(curr, key):
    while curr.left != None:
        curr = curr.left
    return curr.key
def deleteBST(root, key):
    # recursive method:
    if root == None:
        return
    if root.key > key:
        root.left = deleteBST(root.left, key)
    elif root.key < key:
        root.right = deleteBST(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getSucc(root.right, key)
            root.key = succ
            root.right = deleteBST(root.right, succ)
        return root
    # #TC: bigO(h), aux space: bigO(h)









'''
initial BST:
        10
        /\
       5  30
      /   /\
     2   25 40
'''


# root = Node(10)
# root.left = Node(5)
# root.left.left = Node(2)
# root.right = Node(30)
# root.right.right = Node(40)
# root.right.left = Node(25)
root = None
root = insertBST(root, 10)
root = insertBST(root, 5)
root = insertBST(root, 2)
root = insertBST(root, 30)
root = insertBST(root, 40)
root = insertBST(root, 25)

print(searchBST(root, 25))
root = deleteBST(root, 25)
print(searchBST(root, 25))

