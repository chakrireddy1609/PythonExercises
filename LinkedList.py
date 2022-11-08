class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def appendEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def appendBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def print(self):
        currNode = self.head
        while currNode.next:
            print(currNode.data)
            currNode = currNode.next


    def insertBetween(self,prevNode,data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode


    def deletion(self,key):
        currNode = self.head
        if currNode and currNode.data == key:
            self.head = currNode.next
            currNode is None

        prevNode = None
        while currNode and currNode != key:
            prevNode = currNode
            currNode = currNode.next

        prevNode.next = currNode.next
        currNode is None


    def swapNodes(self,key1,key2):
        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next,curr1.next







