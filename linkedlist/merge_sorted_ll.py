from LinkedList import LinkedList

def mergeList(self, list2):
#Using new linkedlist object
'''
    newlist = LinkedList()
    ptr1 = list1.head
    ptr2 = list2.head
    if not ptr1 and not ptr2:
        return
    while ptr1 and ptr2:
        if ptr1.data > ptr2.data:
            newlist.append(ptr2.data)
            ptr2 = ptr2.next
        else:
            newlist.append(ptr1.data)
            ptr1 = ptr1.next
    while ptr1:
        newlist.append(ptr1.data)
        ptr1 = ptr1.next
    while ptr2:
        newlist.append(ptr2.data)
        ptr2 = ptr2.next
    newlist.printList()
'''
# In-place merging




# 1 -> 5 -> 7-> 9 ->10
# 2 -> 3 -> 4-> 6 ->8
ll1 = LinkedList()
print('ll1')
ll1.append(1)
ll1.append(5)
ll1.append(7)
ll1.append(9)

ll1.printList()
ll2 = LinkedList()
print('ll2')
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(6)
ll2.append(8)
ll2.printList()
print('ml')
mergeList(ll1, ll2)