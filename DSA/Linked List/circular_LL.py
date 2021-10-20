class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printCircular(head):
    if head == None:
        return
    print(head.data, end=' ')
    curr = head.next
    while curr != head:
        print(curr.data, end=' ')
        curr = curr.next
    # time complexity: theta(n)

def insert_begin(head, x):
    # naive method:
    # temp = Node(x)
    # if head == None:
    #     temp.next = temp
    #     return temp
    # curr = head
    # while curr.next != head:
    #     curr = curr.next
    # curr.next = temp
    # temp.next = head
    # return temp
    # time complexity: theta(n)

    # efficient method:
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.data, temp.data = temp.data, head.data # swap
        return head
    # time complexity: bigO(1)

def insert_end(head, x):
    # naive method:
    # temp = Node(x)
    # if head == None:
    #     temp.next = temp
    #     return temp
    # else:
    #     curr = head
    #     while curr.next != head:
    #         curr = curr.next
    #     curr.next = temp
    #     temp.next = head
    #     return head
    # time complexity: theta(n)

    # efficient method:
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        temp.data, head.data = head.data, temp.data     # swap
        return temp         # we return temp as our new head
    # time complexity: bigO(1)


def delete_head(head):
    # naive method:
    # if head == None or head.next == head:
    #     return None

    # curr = head
    # while curr.next != head:
    #     curr = curr.next

    # curr.next = head.next
    # return curr.next
    # time complexity: theta(n)

    # efficient method:
    if head == None or head.next == head:
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next
        return head
    # time complexity: theta(1)

def delete_pos(head, i):
    if head == None:
        return head
    elif i == 1:
        return delete_head(head)
    else:
        curr = head
        for j in range(i-2):
            curr = curr.next
        curr.next = curr.next.next
        return head
    # time complexity: theta(i)


    




head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)
head.next.next.next.next = head

head = insert_begin(head, 7)

head = insert_end(head, 70)

# head = delete_head(head)

head = delete_pos(head, 1)
printCircular(head)
