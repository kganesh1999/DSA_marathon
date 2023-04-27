class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()



class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def printTree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preOrderTrav(self.root, "")
        if traversal_type == 'inorder':
            return self.inOrderTrav(self.root, "")
        if traversal_type == 'postorder':
            return self.postOrderTrav(self.root, "")
        if traversal_type == 'levelorder':
            return self.levelOrderTrav(self.root)
        if traversal_type == 'revlevelorder':
            return self.revLevelOrderTrav(self.root)

    def preOrderTrav(self, start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preOrderTrav(start.left, traversal)
            traversal = self.preOrderTrav(start.right, traversal)
        return traversal

    def inOrderTrav(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.inOrderTrav(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inOrderTrav(start.right, traversal)
        return traversal

    def postOrderTrav(self, start, traversal):
        # Left -> Right -> Root
        if start:
            traversal = self.postOrderTrav(start.left, traversal)
            traversal = self.postOrderTrav(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelOrderTrav(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def revLevelOrderTrav(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    def heightTree(self, node):
        if node is None:
            return -1
        lh = self.heightTree(node.left)
        rh = self.heightTree(node.right)
        return 1 + max(lh,rh)

    def sizeTree(self):
        start = self.root
        if start is None:
            return 0
        stack = Stack()
        stack.push(start)
        size = 1
        while len(stack) > 0:
            node = stack.pop()
            if node.left:
                stack.push(node.left)
                size += 1
            if node.right:
                stack.push(node.right)
                size += 1
        return size

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
print(tree.printTree('preorder'))

