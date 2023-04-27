class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("Value alreaday exits")

    def find(self, data):
        start = self.root
        if start is None:
            return None
        is_found = self.finder(data, self.root)
        if is_found:
            return True
        return False

    def finder(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self.finder(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self.finder(data, cur_node.left)
        if data == cur_node.data:
            return True

    def inOrderTrav(self):
        if self.root:
            self._inOrderTrav(self.root)

    def _inOrderTrav(self, cur_node):
        if cur_node:
            self._inOrderTrav(cur_node.left)
            print(str(cur_node.data))
            self._inOrderTrav(cur_node.right)

    def is_bst(self):
        if self.root:
            is_satisfied = self._is_bst(self.root, self.root.data)
            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self._is_bst(cur_node.left, cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst(cur_node.right, cur_node.right.data)
            else:
                return False

bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

tree = BST()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

print(bst.is_bst())