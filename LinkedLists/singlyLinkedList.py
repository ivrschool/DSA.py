# class SLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None


# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None


# singlyLinkedList = SLinkedList()
# node1 = Node(5)
# node2 = Node(2)
# node3 = Node(7)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.head.next.next = node3
# singlyLinkedList.tail = node3.next
# singlyLinkedList.head.next.next.next = singlyLinkedList.tail


# print(singlyLinkedList.head.value)
# print(singlyLinkedList.head.next.value)
# print(singlyLinkedList.head.next.next.value)
# print(id(singlyLinkedList.head.next.next), id(singlyLinkedList.tail))

# print()

# print(id(singlyLinkedList.head))
# print(id(node1))


# print()

# print(id(node1.next))
# print(id(node2))
# print(id(singlyLinkedList.head.next))

# print()

# print(id(node2.next))
# print(id(node3))

# print(id(singlyLinkedList.head.next.next))

# print()

# print(id(node3.next))
# print(id(singlyLinkedList.tail))
# print(id(singlyLinkedList.head.next.next.next))


##################

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0

                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail:
                    self.tail = newNode


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(6, 1)
singlyLinkedList.insertSLL(8, 1)
singlyLinkedList.insertSLL(5, 0)
singlyLinkedList.insertSLL(2, -1)

singlyLinkedList.insertSLL(9, -1)


print([node.value for node in singlyLinkedList])

#################