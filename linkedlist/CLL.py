class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        ptr = self.head
        count = 1
        while ptr.next != self.head:
            ptr = ptr.next
            count += 1
        return count

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            newnode = Node(data)
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = newnode
            newnode.next = self.head

    def prepend(self, data):
        newnode = Node(data)
        ptr = self.head
        newnode.next = self.head
        if self.head is None:
            newnode.next = newnode
        else:
            while ptr.next != head:
                ptr =ptr.next
            ptr.next = newnode
        self.head = newnode

    def remove(self, key):
        if self.head.data == key:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = self.head.next
            self.head = self.head.next
        else:
            ptr = self.head
            prev = None
            while ptr.next != self.head:
                prev = ptr
                ptr = ptr.next
                if ptr.data == key:
                    prev.next = ptr.next
                    ptr = ptr.next

    def removeNode(self, node):
        if self.head == node:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = self.head.next
            self.head = self.head.next
        else:
            ptr = self.head
            prev = None
            while ptr.next != self.head:
                prev = ptr
                ptr = ptr.next
                if ptr == node:
                    prev.next = ptr.next
                    ptr = ptr.next

    def josephusCircle(self, step):
        ptr = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                ptr = ptr.next
                count += 1
            self.removeNode(ptr)
            ptr = ptr.next



cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
print(len(cll))