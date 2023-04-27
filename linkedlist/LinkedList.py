class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertMiddle(self, prev_node, data):
        if not prev_node:
            print("Previous Node not in list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, data):
        pointer = self.head
        if pointer and pointer.data == data:
            self.head = pointer.next
            pointer = None
            return
        temp = None
        while pointer and pointer.data != data:
            temp = pointer
            pointer = pointer.next
        if pointer is None:
            return
        temp.next = pointer.next
        pointer = None

    def deleteAtPos(self,index):
        pointer = self.head
        if index==0:
            self.head = pointer.next
            pointer = None
            return
        count = 0
        prev = None
        if pointer and count != index:
            prev = pointer
            pointer = pointer.next
            count += 1
        if pointer is None:
            return
        prev.next = pointer.next
        pointer = None

    def length(self):
        pointer = self.head
        count = 0
        while pointer:
            pointer = pointer.next
            count += 1
        return count

    def swapNodes(self, key1, key2):
        if key1==key2:
            return
        prev_1 = None
        pointer_1 = self.head
        while pointer_1 and pointer_1.data != key1:
            prev_1 = pointer_1
            pointer_1 = pointer_1.next
        prev_2 = None
        pointer_2 = self.head
        while pointer_2 and pointer_2.data != key2:
            prev_2 = pointer_2
            pointer_2 = pointer_2.next
        if not pointer_1 or not pointer_2:
            return
        if prev_1:
            prev_1.next = pointer_2
        else:
            self.head = pointer_2
        if prev_2:
            prev_2.next = pointer_1
        else:
            self.head = pointer_1
        pointer_1.next, pointer_2.next = pointer_2.next, pointer_1.next

    def printList(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next

    def printHelper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name +" : "+node.data)

    def reverseList(self):
        prev = None
        pointer = self.head
        while pointer:
            nxt = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = nxt
        self.head = prev

    def mergeList(self,llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def removeDup(self):
        prev = None
        pointer = self.head
        if pointer is None:
            return
        visited_nodes = set()
        while pointer:
            if pointer.data not in visited_nodes:
                visited_nodes.add(pointer.data)
                prev = pointer
                pointer = pointer.next
            else:
                prev.next = pointer.next
                pointer = None
                pointer = prev.next

    def ntln(self, n):
        #Method 1
        total_len = self.length()
        pointer = self.head
        while pointer:
            if total_len == n:
                break
            pointer = pointer.next
            total_len -= 1
        if pointer is None:
            return
        return pointer.data
        # Method 2:
        p1 = self.head
        p2 = self.head
        count = 0
        while count < n and p2:
            p2 = p2.next
            count += 1
        if not p2:
            print(str(n) +" is greater than the list length")
            return
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            return p1.data

    def countOccRec(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.countOccRec(node.next, data)
        else:
            return self.countOccRec(node.next, data)

    def rotate(self, k):
        ptr1 = self.head
        ptr2 = self.head
        prev = None
        count = 0
        while ptr1 and count < k:
            prev  = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            count += 1
        ptr1 = prev

        while ptr2:
             prev = ptr2
             ptr2 = ptr2.next
        ptr2 = prev
        ptr2.next = self.head
        self.head = ptr1.next
        ptr1.next = None
    def isPal(self):
        p = self.head
        q = self.head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
        count = 1
        while count <= i//2+1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def moveTailHead(self):
        h = self.head
        t = self.head
        prev = None
        while t.next:
            prev = t
            t = t.next
        prev.next = None
        self.head = t
        t.next = h

    def sumTwoLists(self, list2):
        p1 = self.head
        p2 = list2.head
        sum_list = LinkedList()
        carry = 0
        while p1 or p2:
            if not p1:
                i = 0
            else:
                i = p1.data
            if not p2:
                j = 0
            else:
                j = p2.data
            s = i+j+carry
            if s >= 10:
                carry = 1
                rem = s%10
                sum_list.append(rem)
            else:
                carry = 0
                sum_list.append(s)
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        sum_list.printList()

ll1 = LinkedList()
ll1.append(5)
ll1.append(6)
ll1.append(3)
ll2 = LinkedList()
ll2.append(8)
ll2.append(4)
ll2.append(2)
ll1.sumTwoLists(ll2)

