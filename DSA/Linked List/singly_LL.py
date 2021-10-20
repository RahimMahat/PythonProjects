# class to implement Linked List
class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


# printList func. to print the elements in the LL
def printList(head):
    current = head
    while current != None:
        print(current.key, end=' ')
        current = current.next
        # time complexity: theta(n)

# search func. to search the element in the LL
def search(head, x):
    current = head
    pos = 1
    while current != None:
        if current.key == x:
            return pos
        pos += 1
        current = current.next
    # time complexity: bigO(n)
    return -1

# insert_begin function to push the element at the first place of the LL
def insert_begin(head, key):
    temp = Node(key)
    temp.next = head
    return temp
    # time complexity: bigO(1)

# insert_end function to append the element at the end of the LL
def insert_end(head, key):
    if head == None:
        return Node(key)
        
    current = head
    while current.next != None:
        current = current.next

    current.next = Node(key)
    return head
    # time complexity: theta(n)

# insert_pos function to add the element at given position
def insert_pos(head, pos, data):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    current = head
    for i in range(pos-2):
        current = current.next
        if current == None:
            return head

    temp.next = current.next
    current.next = temp
    return head
    # time complexity: theta(min(pos,n))

# del_first function to delete the first element in the LL
def del_first(head):
    if head == None:
        return None
    else:
        return head.next
    # time complexity: bigO(1)

# del_last function to delete the last element in the LL
def del_last(head):
    if head == None:
        return None
    if head.next == None:
        return None

    current = head
    while current.next.next != None:
        current = current.next

    current.next = None
    return head
    # time complexity: theta(n)

# sorted_insert to insert the element in the sorted LL without breaking sorting
def sorted_insert(head, x):
    temp = Node(x)
    if head == None:
        return temp
    elif x < head.key:
        temp.next = head
        return temp
    else:
        current = head
        while current.next != None and current.next.key < x:
            current = current.next

        temp.next = current.next
        current.next = temp
        return head
    # time complexity: bigO(n)

# reverse_list to reverse the given linked list
def reverse_list(head):
    # naive method:
    # stack = []
    # current = head
    # while current is not None:
    #     stack.append(current.key)
    #     current = current.next
        
    # current = head
    # while current is not None:
    #     current.key = stack.pop()
    #     current = current.next
    # return head
    # # time complexity: bigO(n)

    # efficient method
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev
    # time complexity: theta(n)


if __name__ == '__main__':
    # driver code to set the elements
    # head = Node(10)
    # head.next = Node(20)
    # head.next.next = Node(15)
    # head.next.next.next = Node(30)

    # calling the printList function
    # printList(head)

    # calling search function
    # print(search(head, 20))

    # calling insert begin
    # head = None
    # head = insert_begin(head, 10)
    # head = insert_begin(head, 20)
    # head = insert_begin(head, 30)
    # printList(head)

    # calling insert end
    head = None
    head = insert_end(head, 10)
    head = insert_end(head, 20)
    head = insert_end(head, 30)
    # printList(head)
    # # calling del_first function
    # head = del_first(head)
    # print('\n')
    # printList(head)
    # # calling del_first function
    # head = del_last(head)
    # print('\n')
    # printList(head)

    # calling sorted_insert
    head = sorted_insert(head, 25)
    # printList(head)
    # calling reverse_list
    head = reverse_list(head)
    printList(head)

