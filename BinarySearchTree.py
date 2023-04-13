class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key < self.key:
            if self.left:
                return self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                return self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError()


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                if node.left:
                    temp = node.left
                else:
                    temp = node.right
                if parent:
                    if parent.left == node:
                        parent.left = temp
                    elif parent.right == node:
                        parent.right = temp
                else:
                    self.root = temp
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.key = successor.key
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right

                if parent.right == successor:
                    parent.right = successor.right
            return True

        else:
            return False