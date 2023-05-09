class NodeNotFoundException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Node:
    def __init__(self, key, children=None):
        self.key = key
        self.children = children or []

    def __str__(self):
        return str(self.key)


class GenericTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def findNode(self, node, key):
        if node==None or node.key==key:
            return node
        for child in node.children:
            return_node = self.findNode(child, key)
            if return_node:
                return return_node
        return None

    def depth(self, key):
        node = self.findNode(self.root, key)
        if not node:
            raise NodeNotFoundException("No element was found with the informed parent key!")
        return self.maxDepth(node)

    def maxDepth(self, node):
        if not (node.children):
            return 0
        children_max_depth = []
        for child in node.children:
            children_max_depth.append(self.maxDepth(child))
        return 1+max(children_max_depth)

    def addNode(self, new_key, parent_key=None):
        new_node = Node(new_key)
        if parent_key==None:
            self.root = new_node
            self.size = 1
        else:
            parent_node = self.findNode(self.root, parent_key)
            if not parent_node:
                raise NodeNotFoundException("No element was found with the informed parent key!")
            parent_node.children.append(new_node)
            self.size += 1

    def printTree(self, node):
        if node == None: 
            return

        str_aux = str(node) + ':'
        for child in node.children:
            str_aux += str(child) + ","
        print(str_aux[:-1])
        for child in node.children:
            self.printTree(child)

    def is_empty(self):
        return self.size==0

    def length(self):
        return self.size

    def __str__(self):
        return self.printTree(self.root)


if __name__ == '__main__':
                    
    tree = GenericTree()
    tree.addNode(10)
    tree.addNode(20, 10)
    tree.addNode(30, 10)
    tree.addNode(50, 20)
    tree.addNode(40, 20)
    tree.addNode(70, 20)
    tree.addNode(78, 70)
    tree.addNode(11, 30)

    print('N-ary tree size:', tree.length())
    # Output "N-ary tree size:8"
    tree.printTree(tree.root)
    # Output
        ''' 
            10:20,30
            20:50,40,70
            50
            40
            70:78
            78
            30:11
            11
        '''
    print(tree.depth(11))
    # Output "0"