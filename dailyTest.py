# class Solution:
#     def constructRectangle(self, area: int) -> List[int]:
#         return 2


# a = Solution.constructRectangle(4)

# print(a)


# temp = []
# area = 13

# for i in range(1, area+1):
#     if area % i == 0:
#         temp.append(i)
#     else:
#         pass
# a = 2
# b = 3
# temp = [1, 2, 3]
# temp_ = [[a, b] for idx, a in enumerate(temp) for b in temp[idx+1:]]

# print(temp_)
# numbers = [6, 3, 4, 2]

# # Sorting list of Integers
# # numbers.sort()

# list1 = sorted(list(enumerate(numbers)), key=lambda x: x[1])

# print(list1[0][0])
# temp = []
# area = 4
# for i in range(1, area+1):
#     if area % i == 0:
#         # temp.append([area/i,i])
#         temp.append([i, int(area/i)])
#     else:
#         pass

# diff = [(lw[0]-lw[1], idx) for idx, lw in enumerate(temp) if lw[0]-lw[1] >= 0]
# diff1 = sorted(diff)

# a = [[1, 2, 3], [3, 1, 9], [2, 0, 2]]
# print(sorted(a, key=lambda x: x[2]))

# from ast import Slice
# from dataclasses import dataclass
# import tarfile


import sys
from collections import defaultdict
import math
from random import randint
import numpy as np


def allPairs(list, target):
    temp = []

    # for idx1, num1 in enumerate(list):
    #     for idx2, num2 in enumerate(list):
    #         if num1+num2 == target:
    #             temp.append([idx1, idx2])

    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i]+list[j] == target:
                temp.append([i, j])

    # for i in range(0, n+1):
    #     for j in range(i+1, n+1):
    #         if i+j == n:
    #             temp.append([i, j])

    return temp[0]


# print(allPairs([3, 3], 6))


def maxProd(list):
    max_prod = 0

    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if max_prod < list[i]*list[j]:
                max_prod = list[i]*list[j]

    return max_prod


# print(maxProd([1, 2, 3, 4]))


def uniqueElement(array):

    temp = True

    a = []

    # for i in range(0, len(array)):
    #     for j in range(i+1, len(array)):
    #         if array[i] == array[j]:
    #             temp = False
    #         else:
    #             continue

    for i in array:
        if i in a:
            temp = False
        else:
            a.append(i)

    return temp


# print(uniqueElement([1, 2, 3, 4, 5, 3]))


def rotateMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    temp_row = []
    temp_col = []

    for j in range(0, cols):
        for rows_ in matrix:
            temp_col.append(rows_[0])

        temp_col.reverse()
        temp_row.append(temp_col)
        matrix = np.delete(matrix, 0, axis=1)
        temp_col = []

    return np.array(temp_row)


matrix = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [2, 4, 7, 2]])

# print(rotateMatrix(matrix))
# print(matrix)


def rotateMatrix2(matrix):

    n = len(matrix)

    for layer in range(n//2):
        first = layer
        last = n-layer-1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[last-i][layer]
            matrix[last-i][layer] = matrix[last][last-i]
            matrix[last][last-i] = matrix[layer+i][last]
            matrix[layer+i][last] = top

    return matrix


matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(rotateMatrix2(matrix))


####################Linked List ##################################
# Single Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add(self, data=None, position=None):
        self.position = position
        self.data = data

        node = Node(self.data)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            if position == 0:
                node.next = self.head
                self.head = node
            if position == -1:
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                for i in range(position-1):
                    tempNode = tempNode.next
                node.next = tempNode.next
                tempNode.next = node

                if tempNode == self.tail:
                    self.tail = node

    def TransverSLL(self):
        if self.head == None:
            print('The list is empty.')
        else:
            tempNode = self.head
            while tempNode != None:
                print(tempNode.data)
                tempNode = tempNode.next

    def Search(self, data):
        temp = False
        if self.head == None:
            print("the list is empty.")

        else:
            tempNode = self.head
            while tempNode != None:
                if tempNode.data == data:
                    return data
                tempNode = tempNode.next
            return "the value, " + str(data) + " does not exist."

    def Delete(self, location):
        if self.head == None:
            return "The list is empty."
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next

            elif location == -1:
                tempNode = self.head
                while tempNode.next != self.tail:
                    tempNode = tempNode.next
                tempNode.next = None
                self.tail = tempNode
            else:
                tempNode = self.head
                for i in range(location-1):
                    tempNode = tempNode.next
                tempNode.next = tempNode.next.next

    def DeleteSLL(self):
        if self.head == None:
            print('the list is empty.')
        else:
            self.head = None
            self.tail = None


SLinkedList = SLList()

# node1 = Node(5)
# node2 = Node(6)
# SLinkedList.head = node1
# SLinkedList.head.next = node2
# SLinkedList.tail = node2
# SLinkedList.add(9, -1)
# print(SLinkedList.head.data, SLinkedList.head.next.data,
#       SLinkedList.head.next.next.data)


SLinkedList.add(5, None)
SLinkedList.add(4, 1)
SLinkedList.add(6, 2)
SLinkedList.add(3, 3)
SLinkedList.add(8, 1)
SLinkedList.add(9, -1)
SLinkedList.add(10, 6)

# print([node.data for node in SLinkedList])
# # SLinkedList.TransverSLL()
# # print(SLinkedList.Search(90))
# SLinkedList.Delete(4)

# print([node.data for node in SLinkedList])

# SLinkedList.DeleteSLL()

# print([node.data for node in SLinkedList])


# 2. Circular Singly linked List

class CSLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def add(self, data=None, position=None):
        self.data = data
        self.position = position
        newNode = Node(self.data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            if position == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            elif position == -1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                for i in range(position-1):
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                tempNode.next = newNode
        return "the node is successfully inserted."

    def traverseCLL(self):
        if self.head == None:
            print("the list is empty.")
        else:
            node = self.head
            while node:
                print(node.data)
                if node.next == self.head:
                    break
                else:
                    node = node.next
                    continue

    def searchNode(self, value):
        if self.head == None:
            print("the list is empty.")
        else:
            tempNode = self.head
            while True:
                if tempNode.data == value:
                    return str(value) + " exists!"
                else:
                    if tempNode.next == self.head:
                        return str(value) + " does not exist!"
                    tempNode = tempNode.next

    def deleteNode(self, position):
        if self.head == None:
            print('The list is empty.')
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            tempNode = self.head
            if position == 0:
                self.head = tempNode.next
                self.tail.next = self.head
            elif position == -1:
                while True:
                    if tempNode.next == self.tail:
                        break
                    tempNode = tempNode.next
                tempNode.next = self.head
                self.tail = tempNode
            else:
                for i in range(position-1):
                    tempNode = tempNode.next
                    # print(tempNode.data, i)
                if tempNode.next == self.tail:
                    self.tail = tempNode
                    tempNode.next = self.head
                elif self.head == tempNode.next:
                    self.head = tempNode.next.next
                    self.tail.next = self.head
                else:
                    tempNode.next = tempNode.next.next

    def deleteCLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


# CircularSLL = CSLList()

# CircularSLL.add(5, None)
# CircularSLL.add(2, 0)
# CircularSLL.add(3, -1)
# CircularSLL.add(4, 0)
# CircularSLL.add(44, -1)
# # CircularSLL.deleteNode()

# # CircularSLL.traverseCLL()
# CircularSLL.deleteNode(10)
# CircularSLL.deleteCLL()
# # print(CircularSLL.searchNode(5))
# print([node.data for node in CircularSLL])


# 3. Double linear Linked List

class DNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value=None):
        newNode = DNode(value)
        newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = self.head

    def insertDLL(self, value=None, position=None):
        if self.head == None:
            print("Please create a List first")
        else:
            newNode = DNode(value)
            if position == 0:
                # if self.head == self.tail:
                newNode.next = self.head
                self.head.prev = newNode
                newNode.prev = None
                self.head = newNode

            elif position == -1:
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = None
                self.tail = newNode

            else:
                tempNode = self.head
                for i in range(position-1):
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                tempNode.next.prev = newNode
                newNode.prev = tempNode
                tempNode.next = newNode

    def traverseDLL(self):
        if self.head == None:
            print('the list is empty')
        else:
            node = self.head
            while node:
                print(node.data)
                node = node.next

    def reverseDLL(self):
        if self.head == None:
            print("The list is empty.")

        else:
            node = self.tail
            while node:
                print(node.data)
                node = node.prev

    def search(self, value=None):
        if self.head == None:
            print("the list is empty.")
        else:
            node = self.head
            while node:
                if node.data == value:
                    return str(value) + " exists!"
                node = node.next
            return str(value) + " does not exist!"

    def delete(self, position):
        if self.head == None:
            return 'the list is empty'
        else:
            if position == 0:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
                else:
                    self.head.prev = None
            elif position == -1:
                self.tail = self.tail.prev
                if self.tail == None:
                    self.head = None
                else:
                    self.tail.next = None
            else:
                tempNode = self.head
                for i in range(position-1):
                    tempNode = tempNode.next

                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode

    def deleteDLL(self):
        if self.head == None:
            return "the list is empty"
        else:
            node = self.head
            while node:
                node.prev = None
                node = node.next
        self.head = None
        self.tail = None
        return 'The list is deleted successfully!'


# DLL = DLList()

# DLL.createDLL(5)
# DLL.insertDLL(6, 0)
# DLL.insertDLL(9, -1)
# DLL.insertDLL(5, 0)
# DLL.insertDLL(3, -1)
# DLL.insertDLL(23, 4)
# DLL.insertDLL(1, 3)
# DLL.insertDLL(10, -1)
# DLL.insertDLL(12, 2)


# # print([node.data for node in DLL])
# # DLL.traverseDLL()
# # DLL.reverseDLL()

# # print(DLL.search(123))
# DLL.delete(5)
# print([node.data for node in DLL])
# DLL.deleteDLL()
# print([node.data for node in DLL])

# 4. Circular Double Linked List


class CDLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, value=None):
        newNode = DNode(value)
        self.head = newNode
        newNode.next = self.head
        newNode.prev = self.head
        self.tail = newNode
        return "CDLL is created successfully!"

    def insertCDLL(self, value=None, position=None):
        if self.head == None:
            return "Please create CDLL. It is empty now."
        else:
            newNode = DNode(value)
            if position == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif position == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                for i in range(position-1):
                    tempNode = tempNode.next

                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
            return "The number is successfully inserted!"

    def traverseCDLL(self):
        if self.head == None:
            return 'The list is empty'
        else:
            node = self.head
            while True:
                print(node.data)
                node = node.next
                if node == self.tail.next:
                    break
            return "traversel is completed"

    def reverseCDLL(self):
        if self.head == None:
            return "The list is empty"
        else:
            node = self.tail
            while True:
                print(node.data)
                node = node.prev
                if node == self.head.prev:
                    break
            return "the list is reversed"

    def searchCDLL(self, value=None):
        if self.head == None:
            return 'The list is empty.'
        else:
            tempNode = self.head
            while True:
                if tempNode.data == value:
                    return str(value) + " exists!"
                elif tempNode == self.tail:
                    break
                else:
                    tempNode = tempNode.next
            return str(value) + " does not exist!"

    def deleteCDLL(self, position=None):
        if self.head == None:
            return "the list is empty."
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None
            else:
                if position == 0:
                    self.head.next.prev = self.tail
                    self.head.prev = None
                    self.head = self.head.next

                elif position == -1:
                    self.tail.prev.next = self.head
                    self.tail.next = None
                    self.tail = self.tail.prev

                else:
                    tempNode = self.head
                    for i in range(position - 1):
                        tempNode = tempNode.next

                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode

    def deleteALL(self):
        if self.head == None:
            return "The list is empty."
        else:
            self.tail.next = None
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None


# CDLL = CDLList()
# CDLL.createCDLL(7)
# CDLL.insertCDLL(4, 0)
# CDLL.insertCDLL(6, -1)
# CDLL.insertCDLL(3, 2)
# CDLL.insertCDLL(3, 2)

# CDLL.insertCDLL(10, 2)

# CDLL.insertCDLL(6, 2)


# print([node.data for node in CDLL])

# CDLL.deleteCDLL(2)
# print([node.data for node in CDLL])

# # print(CDLL.traverseCDLL())

# # print(CDLL.reverseCDLL())
# # print(CDLL.searchCDLL(0))
# CDLL.deleteALL()
# print([node.data for node in CDLL])


# Interview Questions LL:

# 0. Custom Linked List


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))

# Q.1. remove dubicate enties from SLL:

# O(n) -> TC and O(n) -> SC
def removeDups(LL):
    if LL.head == None:
        return 'The LL is empty.'
    else:
        tempNode1 = LL.head
        visited = set([tempNode1.value])
        while tempNode1.next:
            if tempNode1.next.value in visited:
                tempNode1.next = tempNode1.next.next
            else:
                visited.add(tempNode1.next.value)
                tempNode1 = tempNode1.next
        return LL


# O(n^2) -> TC and O(1) -> SC

def removeDups1(LL):
    if LL.head == None:
        pass
    else:
        currentNode = LL.head
        while currentNode:
            runner = currentNode
            while runner.next:
                if currentNode.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next
    return LL


# LL = LinkedList().generate(10, 0, 99)
# print(LL)
# print(removeDups(LL))
# print(removeDups1(LL))

# 2. print from Kth entry from the last entries of SLL:


def Kth_last(LL, k):
    if LL.head == None:
        return
    else:
        pointer1 = LL.head
        pointer2 = LL.head

        for i in range(k):
            pointer2 = pointer2.next
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1.value


# print(Kth_last(LL, 2))

# Q.3. partition around x:
def partition(LL, x):
    if LL.head == None:
        return
    else:
        currNode = LL.head
        LL.tail = LL.head

        while currNode:
            nextNode = currNode.next
            currNode.next = None

            if currNode.value < x:
                currNode.next = LL.head
                LL.head = currNode
            else:
                LL.tail.next = currNode
                LL.tail = currNode
            currNode = nextNode
        if LL.tail.next is not None:
            LL.tail.next = None
        return LL


# print(partition(LL, 40))


def partition1(LL, x):
    if LL.head == None:
        return
    else:
        curNode = LL.head
        LL.tail = LL.head
        while curNode:
            nextNode = curNode.next
            curNode.next = None

            if curNode.value < x:
                curNode.next = LL.head
                LL.head = curNode
            else:
                LL.tail.next = curNode
                LL.tail = curNode

            curNode = nextNode

        if LL.tail.next != None:
            LL.tail.next = None
        return LL


# print(partition1(LL, 40))


def addLL(ll1, ll2):
    ll = LinkedList()
    carry = 0
    n1 = ll1.head
    n2 = ll2.head

    while n1 or n2:
        result = carry

        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(result % 10)

        carry = result//10
    if carry != 0:
        ll.add(carry)
    return ll


ll1 = LinkedList()
ll2 = LinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)

ll1.add(6)

ll2.add(7)
ll2.add(1)
ll2.add(6)

# print(ll2)
# print(ll1)
# print(addLL(ll1, ll2))


def intersect(ll1, ll2):

    if ll1.tail is not ll2.tail:
        return False

    longer = ll1 if len(ll1) > len(ll2) else ll2
    shorter = ll1 if len(ll1) < len(ll2) else ll2

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while longerNode is not shorterNode:
        longerNode = longerNode.next
        shorterNode = shorterNode.next

    return longerNode


def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.generate(3, 0, 10)

llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

# print(llA)
# print(llB)

# print(intersect(llA, llB))


##### Stack ################

# Type 1: using list without any size limit:

class stack1:
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "successfully pushed!"

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            self.list = None
            return "Successfully deleted."


Stack = stack1()

Stack.push(5)
Stack.push(1)
Stack.push(2)

# print(Stack)

# print(Stack.pop())

# print(Stack.peek())

# print(Stack.delete())


# Type 2: with size

class stack2:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The stack is Full."

        else:
            self.list.append(value)
            return "The value is pushed successfully"

    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None
        return "Successfully deleted."


Stack2 = stack2(5)

Stack2.push(5)
Stack2.push(1)
Stack2.push(2)
Stack2.push(5)
Stack2.push(1)

# print(Stack2.pop())
# print(Stack2.push(2))
# print(Stack2)

# Type 3: stack using Linked List


class Node3:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class stack3:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def __str__(self):
        values = [str(x.data) for x in self.LinkedList]
        return '\n'.join(values)

    def push(self, value):
        node = Node3(value)
        if self.isEmpty():
            self.LinkedList.head = node
        else:
            node.next = self.LinkedList.head
            self.LinkedList.head = node
        return 'Pushed succssessfully.'

    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            value = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.next
            return value

    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.LinkedList.head.data

    def delete(self):
        self.LinkedList.head = None
        return "The stack is deleted."


Stack3 = stack3()

Stack3.push(3)
Stack3.push(2)
Stack3.push(4)
Stack3.push(7)
Stack3.push(4)

# print(Stack3.pop())
# print(Stack3.push(5))
# print(Stack3.delete())
# print(Stack3)


######### Queue ###############


# Type 1: Queue wuing List without capacity

class queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)
        return 'success.'

    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty.'
        else:
            return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "the queue is empty."
        else:
            return self.list[0]

    def delete(self):
        self.list = None


# customQueue1 = queue()

# customQueue1.enqueue(5)
# customQueue1.enqueue(6)
# customQueue1.enqueue(8)
# customQueue1.enqueue(9)

# print(customQueue1.dequeue())
# print(customQueue1.isEmpty())
# print(customQueue1.peek())


# Type 2: with list and capacity


class queue2:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = self.maxSize*[None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top+1 == self.start:
            return True
        elif self.start == 0 and self.top == self.maxSize-1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return 'The queue is full.'
        # else:
        #     if self.top == self.maxSize-1:
        #         self.top = 0
        #     else:
        #         self.top += 1
        #         if self.start == -1:
        #             self.start = 0
        #     self.list[self.top] = value
        #     return "success."

        elif self.isEmpty():
            self.start += 1
            self.top += 1
            self.list[self.top] = value
            return 'success.'
        else:
            if self.top == self.maxSize-1:
                self.top = 0
            else:
                self.top += 1
            self.list[self.top] = value
            return 'success.'

    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty.'
        # elif self.isFull():
        #     if self.top+1 == self.start != self.maxSize-1:
        #         value = self.list[self.start]
        #         self.start += 1
        #     elif self.top+1 == self.start == self.maxSize-1:
        #         value = self.list[self.start]
        #         self.start = 0
        #     elif self.start == 0 and self.top == self.maxSize-1:
        #         value = self.list[self.start]
        #         self.start += 1
        #     return value
        else:
            value = self.list[self.start]
            start = self.start
            if self.top == self.start:
                self.start = -1
                self.top = -1
            elif self.top != self.start == self.maxSize-1:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return value

    def peek(self):
        if self.isEmpty():
            return "the queue is empty."
        else:
            return self.list[self.start]

    def delete(self):
        self.list = self.maxSize*[None]
        self.start = -1
        self.top = -1
        return 'success'


customQueue2 = queue2(3)

customQueue2.enqueue(5)
customQueue2.enqueue(6)
customQueue2.enqueue(8)


# print(customQueue2.dequeue())
# print(customQueue2.dequeue())
# print(customQueue2.dequeue())


# # print(customQueue2.isEmpty())
# print(customQueue2.enqueue(9))
# print(customQueue2.enqueue(10))
# print(customQueue2.dequeue())
# print(customQueue2.enqueue(1))
# print(customQueue2.enqueue(11))
# # print(customQueue2.dequeue())
# # print(customQueue2.dequeue())
# # print(customQueue2.dequeue())


# print(customQueue2.isFull())
# print(customQueue2.delete())
# print(customQueue2)


class Node3:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList3:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class queue3:
    def __init__(self):
        self.linkedlist = LinkedList3()

    def __str__(self):
        values = [str(node.data) for node in self.linkedlist]
        return ' '.join(values)

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def enqueue(self, value):
        node = Node3(value)
        if self.isEmpty():
            self.linkedlist.head = node
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node
        return "success"

    def dequeue(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            tempNode = self.linkedlist.head
            # value = self.linkedlist.head.data
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.linkedlist.head

    def delete(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            self.linkedlist.head = None
            self.linkedlist.tail = None
            return "success"


# customQueue3 = queue3()

# print(customQueue3.isEmpty())
# customQueue3.enqueue(5)
# customQueue3.enqueue(6)
# customQueue3.enqueue(8)
# print(customQueue3.dequeue())
# print(customQueue3.peek())
# print(customQueue3.isEmpty())
# print(customQueue3)
'''
from collections import deque
from multiprocessing import Queue
import queue as q
'''


########## Tree DS ##########


# 1. Basic Tree

class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


# tree = TreeNode('Drinks', [])

# cold = TreeNode('Cold', [])
# hot = TreeNode('Hot', [])

# cola = TreeNode('Cola', [])
# soda = TreeNode('Soda', [])

# tea = TreeNode('Tea', [])
# coffee = TreeNode('Coffee', [])

# cold.addChild(cola)
# cold.addChild(soda)

# hot.addChild(tea)
# hot.addChild(coffee)

# tree.addChild(cold)
# tree.addChild(hot)

# print(tree)


# 2. Linked List Binary Tree


class Tree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return self.data


def preOrderTraversal(rootNode):
    if rootNode == None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if rootNode == None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if rootNode == None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrdertraversal(rootNode):
    if rootNode == None:
        return
    customQueue = queue3()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.data.data)
        if root.data.leftChild != None:
            customQueue.enqueue(root.data.leftChild)
        if root.data.rightChild != None:
            customQueue.enqueue(root.data.rightChild)


def searchBT(rootNode, nodeValue):
    if rootNode == None:
        return
    customQueue = queue3()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.data.data == nodeValue:
            return nodeValue
        if root.data.leftChild != None:
            customQueue.enqueue(root.data.leftChild)
        if root.data.rightChild != None:
            customQueue.enqueue(root.data.rightChild)
    return "Not Found."


def insertBT(rootNode, newNode):
    if rootNode == None:
        rootNode = newNode
        return "Success"
    customQueue = queue3()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()

        if root.data.leftChild != None:
            customQueue.enqueue(root.data.leftChild)
        else:
            root.data.leftChild = newNode
            return "Inserted Successfully"
        if root.data.rightChild != None:
            customQueue.enqueue(root.data.rightChild)
        else:
            root.data.rightChild = newNode
            return "Inserted Successfully."


def getDeepestNode(rootNode):
    if rootNode == None:
        return "BT is empty"
    customQueue = queue3()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.data.leftChild != None:
            customQueue.enqueue(root.data.leftChild)
        if root.data.rightChild != None:
            customQueue.enqueue(root.data.rightChild)
    deepestNode = root.data
    return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if rootNode == None:
        return "BT is empty"
    customQueue = queue3()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.data == dNode:
            root.data = None
            return "Success1"
        else:
            if root.data.leftChild:
                if root.data.leftChild == dNode:
                    root.data.leftChild = None
                    return "Success2"
                else:
                    customQueue.enqueue(root.data.leftChild)
            if root.data.rightChild:
                if root.data.rightChild == dNode:
                    root.data.rightChild = None
                    return "Success3"
                else:
                    customQueue.enqueue(root.data.rightChild)
    return "node does not exist."


def deleteNodeBT(rootNode, nodeValue):
    if rootNode == None:
        return "BT is empty."
    customQueue = queue3()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.data.data == nodeValue:
            dNode = getDeepestNode(rootNode)
            root.data.data = dNode.data
            deleteDeepestNode(rootNode, dNode)
            return "Success"
        if root.data.leftChild != None:
            customQueue.enqueue(root.data.leftChild)
        if root.data.rightChild != None:
            customQueue.enqueue(root.data.rightChild)
    return "node does not exist!"


def deleteBT(rootNode):
    if rootNode == None:
        return "BT is already empty."
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return "Success"


newTree = Tree("Drinks")
leftChild = Tree("Hot")
rightChild = Tree("Cold")
newTree.leftChild = leftChild
newTree.rightChild = rightChild
leftChild.leftChild = Tree("Tea")
leftChild.rightChild = Tree("Coffee")
rightChild.leftChild = Tree("soda")
# rightChild.rightChild = Tree("Cola")
# preOrderTraversal(newTree)
# inOrderTraversal(newTree)
# postOrderTraversal(newTree)


# print(searchBT(newTree, "soda"))

# print(insertBT(newTree, Tree("Cola")))
# # levelOrdertraversal(newTree)
# # print(getDeepestNode(newTree))
# newNode = getDeepestNode(newTree)
# # print(deleteDeepestNode(newTree, newNode))
# print(deleteNodeBT(newTree, 'Drinks'))
# levelOrdertraversal(newTree)

# 2. BT using python List


############

# 3. BST:

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.data)


def insertNode1(rootNode, nodeValue):  # with loop
    if rootNode.data == None:
        rootNode.data = nodeValue
        return "Success"
    else:
        tempNode = rootNode
        while True:
            if nodeValue <= tempNode.data and tempNode.leftChild != None:
                tempNode = tempNode.leftChild
            elif nodeValue > tempNode.data and tempNode.rightChild != None:
                tempNode = tempNode.rightChild
            else:
                if tempNode.leftChild == None:
                    tempNode.leftChild = BSTNode(nodeValue)
                    return "Success"
                if tempNode.rightChild == None:
                    tempNode.rightChild = BSTNode(nodeValue)
                    return "Success"


def insertNode(rootNode, nodeValue):  # with recursion
    if rootNode.data == None:
        rootNode.data = nodeValue
        return "Success"
    else:
        if nodeValue <= rootNode.data:
            if rootNode.leftChild == None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild == None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.rightChild, nodeValue)
        return "Success"


def searchNode(rootNode, nodeValue):
    if rootNode.data == None:
        print("The Tree is empty")
    else:
        if nodeValue == rootNode.data:
            print("Success. " + str(nodeValue))
        elif nodeValue < rootNode.data:
            if rootNode.leftChild == None:
                print("NotFound.")
            else:
                searchNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild == None:
                print("NotFound.")
            else:
                searchNode(rootNode.rightChild, nodeValue)


def minVlaueBST(rootNode):
    currNode = rootNode
    while currNode.leftChild != None:
        currNode = currNode.leftChild
    return currNode


def deleteBSTNode(rootNode, nodeValue):
    if rootNode == None:
        return rootNode
    else:
        if nodeValue < rootNode.data:
            rootNode.leftChild = deleteBSTNode(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.rightChild = deleteBSTNode(rootNode.rightChild, nodeValue)
        else:
            if rootNode.leftChild == None:
                temp = rootNode.rightChild
                rootNode = None
                return temp
            if rootNode.rightChild == None:
                temp = rootNode.leftChild
                rootNode = None
                return temp

            minNode = minVlaueBST(rootNode.rightChild)
            rootNode.data = minNode.data
            rootNode.rightChild = deleteBSTNode(
                minNode.rightChild, minNode.data)
        return rootNode


def deleteBST(rootNode):
    rootNode.leftChild = None
    rootNode.rightChild = None
    rootNode.data = None


# newBST = BSTNode(90)

# # # print(insertNode(newBST, 10))
# # insertNode(newBST, 10)
# # insertNode(newBST, 40)
# # insertNode(newBST, 30)
# # insertNode(newBST, 95)
# # # print(levelOrdertraversal(newBST))
# # # searchNode(newBST, 95)

# # deleteBSTNode(newBST, 10)
# deleteBST(newBST)
# levelOrdertraversal(newBST)


# 4. AVL Tree:

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + \
        max(getHeight(disbalanceNode.leftChild),
            getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),
                             getHeight(newRoot.rightChild))
    return newRoot


def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + \
        max(getHeight(disbalanceNode.leftChild),
            getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),
                             getHeight(newRoot.rightChild))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        print("1")
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        print(2)
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + \
        max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))

    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"


# newAVL = AVLNode(50)
# newAVL = insertNode(newAVL, 30)
# newAVL = insertNode(newAVL, 20)
# levelOrdertraversal(newAVL)


#########Trie########

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            print(node, "1")
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
                print(current.children, "flag")
            current = node

        current.endOfString = True
        print("Successfully inserted")

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False


# def deleteString(root, word, index):
#     ch = word[index]
#     currentNode = root.children.get(ch)
#     canThisNodeBeDeleted = False

#     if len(currentNode.children) > 1:
#         deleteString(currentNode, word, index+1)
#         return False

#     if index == len(word) - 1:
#         if len(currentNode.children) >= 1:
#             currentNode.endOfString = False
#             return False
#         else:
#             root.children.pop(ch)
#             return True

#     if currentNode.endOfString == True:
#         deleteString(currentNode, word, index+1)
#         return False

#     canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
#     if canThisNodeBeDeleted == True:
#         root.children.pop(ch)
#         return True
#     else:
#         return False


# newTrie = Trie()
# newTrie.insertString("App")
# newTrie.insertString("Appl")
# deleteString(newTrie.root, "App", 0)
# print(newTrie.searchString("App"))


############## Sorting algorithms ###########

# Bubble Sort
def bubbleSort(arr):
    l = len(arr)
    for j in range(l-1):
        for i in range(l-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# Selection Sort:


def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# Insertion Sort:
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # for j in range(i-1, -2, -1):

        #     if key < arr[j] and j != -1:
        #         arr[j+1] = arr[j]

        # arr[j+1] = key
        # print(j)
        # print(arr)
        j = i-1
        while j >= 0 and key < arr[j]:

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


def bucketSort(arr):
    array = []
    no_of_bucket = int(round(math.sqrt(len(arr))))
    max_value = max(arr)

    for i in range(int(no_of_bucket)+1):
        array.append([])

    for i in arr:
        bucket = math.ceil(i*no_of_bucket/max_value)
        array[int(bucket)].append(i)
    arr = []
    for i in range(no_of_bucket+1):
        array[i] = insertionSort(array[i])
        arr = arr + array[i]
    # k = 0
    # for i in range(no_of_bucket):
    #     for j in range(len(array[i])):
    #         arr[k] = array[i][j]
    #         k += 1
    # # print(array)
    return arr


# print(bubbleSort([5, 9, 1, 4, 6, 7]))
# print(selectionSort([5, 9, 1, 4, 6, 7]))
# print(insertionSort([5, 9, 1, 4, 6, 7]))
# print(bucketSort([5, 9, 1, 4, 6, 7]))


# Merge Sort

# def merge(customList, l, m, r):
#     n1 = m-l+1
#     n2 = r-m

#     L = [0]*n1
#     R = [0]*n2

#     for i in range(n1):
#         L[i] = customList[l+i]
#     for j in range(n2):
#         R[j] = customList[m+j+1]

#     i = 0
#     j = 0
#     k = l
#     # print(L, R)
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             customList[k] = L[i]
#             i += 1
#         else:
#             customList[k] = R[j]
#             j += 1
#         k += 1
#     while i < n1:
#         customList[k] = L[i]
#         i += 1
#         k += 1
#     while j < n2:
#         customList[k] = R[j]
#         j += 1
#         k += 1

#     return customList

def merge(left, right):
    n1 = len(left)
    n2 = len(right)
    i = 0
    j = 0
    sorted_list = []
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < n1:
        sorted_list.append(left[i])
        i += 1
    while j < n2:
        sorted_list.append(right[j])
        j += 1

    return sorted_list


# def mergeSort(customList,l,r):
    # if l < r:
    #     m = (l+(r-1))//2
    #     mergeSort(customList, l, m)
    #     mergeSort(customList, m+1, r)
    #     merge(customList, l, m, r)

def mergeSort(customList):
    if len(customList) <= 1:
        return customList

    m = len(customList)//2

    left = customList[:m]
    right = customList[m:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


# customList = [5, 9, 1, 4, 6, 7]
customList = [2, 1, 7, 6, 5, 3, 4, 9, 8]

# print(mergeSort(customList))

# QuickSort


def partition_(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    # start = pivot_index+1
    # end = len(arr)-1

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    return end


def quickSort(arr, start, end):
    if start < end:
        pi = partition_(arr, start, end)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)
    return arr


# print(quickSort([11, 9, 29, 7, 2, 15, 28], 0, 6))
# print(quickSort(customList, 0, len(customList)-1))


# heap Sort:
################Heap sort needs to be implemented by self ##############
def heapSort(arr):
    pass


######################

################################### Binary Search ###################################

def binarySearch(arr, value):
    start = 0
    end = len(arr)-1

    middle = int((start+end)/2)

    while arr[middle] != value and middle != 0 and not(middle >= len(arr)-1):
        if value < arr[middle]:
            end = middle-1
        else:
            start = middle+1
        middle = int((start+end)/2)

    if arr[middle] == value:
        return middle
    else:
        return -1


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(binarySearch(arr, 9))

######## Graph #########

# 1. create a graph


class graph:
    def __init__(self, gdict=None):
        self.gdict = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            p = queue.pop(0)
            print(p)
            for i in self.gdict[p]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            p = stack.pop()
            print(p)
            for i in self.gdict[p]:
                if i not in visited:
                    visited.append(i)
                    stack.append(i)

    def topologicalUtils(self, v, visited, stack):
        visited.append(v)

        for i in self.gdict[v]:
            if i not in visited:
                self.topologicalUtils(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []

        for i in list(self.gdict):
            if i not in visited:
                self.topologicalUtils(i, visited, stack)

        print(stack)


gdict = {'a': ['b', 'c'],
         'b': ['a', 'd', 'e'],
         'c': ['a', 'e'],
         'd': ['b', 'e', 'f'],
         'e': ['d', 'f', 'b'],
         'f': ['d', 'e']
         }

# customGraph = graph(gdict)
# customGraph.addEdge('e', 'c')
# print(customGraph.gdict)
# customGraph.bfs('a')
# customGraph.dfs('a')

# topologicalGraph = graph()

# topologicalGraph.addEdge('a', 'c')
# topologicalGraph.addEdge('c', 'e')
# topologicalGraph.addEdge('e', 'h')
# topologicalGraph.addEdge('e', 'f')
# topologicalGraph.addEdge('f', 'g')
# topologicalGraph.addEdge('b', 'c')
# topologicalGraph.addEdge('b', 'd')
# topologicalGraph.addEdge('d', 'f')

# # topologicalGraph.bfs()
# topologicalGraph.topologicalSort()


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path
            for adj in self.gdict[node]:
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)


# customDict = {"a": ["b", "c"],
#               "b": ["d", "g"],
#               "c": ["d", "e"],
#               "d": ["f"],
#               "e": ["f"],
#               "g": ["f"]
#               }

# g = Graph(customDict)
# print(g.bfs1("a", "f"))


# Dijsktra's Algorithm

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


# def dijkstra(graph, initial):
#     visited = {initial: 0}
#     path = defaultdict(list)
#     nodes = set(graph.nodes)

#     while nodes:
#         minNode = None
#         for node in nodes:
        #   if node in visited:
        #     if minNode == None:
        #         minNode = node
        #     elif visited[node] < visited[minNode]:
        #         minNode = node
#         if minNode is None:
#             break
#         nodes.remove(minNode)
#         currentWeight = visited[minNode]

#         for edge in graph.edges[minNode]:
#             weight = currentWeight + graph.distances[(edge, minNode)]
#             if edge not in visited or weight < visited[edge]:
#                 visited[edge] = weight
#                 path[edge].append(minNode)

#     return visited, path


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path


customGraph = Graph()


customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

# print(customGraph.nodes)
# print(customGraph.edges)
# print(customGraph.distances)
# print(dijkstra(customGraph, "A"))

# Bellman's Ford Algorithms

######start here ##########


###end here ##########

# Floyed warsal algorithm

INF = 999999999


def printSol(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")


def floydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(
                    distance[i][j], distance[i][k]+distance[k][j])
    return printSol(nV, distance)


G = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1]
     ]

# print(floydWarshall(4, G))


# Disjoint Set

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


# vertices = ["A", "B", "C", "D", "E"]

# ds = DisjointSet(vertices)
# ds.union("A", "B")
# ds.union("C", "D")
# ds.union("A", "C")
# print(ds.find("D"))

# print(ds.vertices)
# print(ds.parent)
# print(ds.rank)


class GraphNew:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def kruskalAlgo(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)


g = GraphNew(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

# g.kruskalAlgo()


class GraphPrims:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []

    def printSolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def primsAlgo(self):
        visited = [0]*self.vertexNum
        edgeNum = 0
        visited[0] = True
        while edgeNum < self.vertexNum-1:
            min = sys.maxsize
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if ((not visited[j]) and self.edges[i][j]):
                            print(self.edges[i][j])
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
                # break
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgeNum += 1
        self.printSolution()


edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]
nodes = ["A", "B", "C", "D", "E"]
g = GraphPrims(5, edges, nodes)
g.primsAlgo()

# print(sys.maxsize)
