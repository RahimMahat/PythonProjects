class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def printDoubly(head):
    curr = head
    while curr != None:
        print(curr.data, end=' ')
        curr = curr.next

def insert_begin(head, x):
    temp = Node(x)
    if head != None:
        head.prev = temp
    temp.next = head
    return temp
    # time complexity: theta(1)

def insert_end(head, x):
    temp = Node(x)
    if head == None:
        return temp
    else:
        curr = head
        while curr.next != None:
            curr = curr.next
        
        curr.next = temp
        temp.prev = curr
        return head
        # time complexity: theta(n)

def delete_head(head):
    if head == None or head.next == None:
        return None
    else:
        head = head.next
        head.prev = None
        return head
    # time complexity: theta(1)

def delete_tail(head):
    if head == None or head.next == None:
        return None
    else:
        curr = head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        return head
    # time complexity: theta(n)

def reverse_dll(head):
    if head == None or head.next == None:
        return None
    
    curr = head
    prev = None
    while curr != None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next     # swap
        curr = curr.prev    # as we have swapped our next becomes prev so curr.prev
    return prev     # we are updating prev at every iteration so return prev as head
    # time complexity: theta(n)



head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)

head = insert_end(head, 30)

# head = delete_head(head)

# head = delete_tail(head)

head = reverse_dll(head)
printDoubly(head)