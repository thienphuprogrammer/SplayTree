class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self, root=None):
        self.root = root

    def right_rotate(self, node):
        if not node.parent:
            return
        parent = node.parent
        grandparent = node.parent.parent
        if grandparent:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        node.parent = grandparent
        parent.left = node.right
        if node.right:
            node.right.parent = parent
        node.right = parent
        parent.parent = node

    def left_rotate(self, node):
        if not node.parent:
            return
        parent = node.parent
        grandparent = node.parent.parent
        if grandparent:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        node.parent = grandparent
        parent.right = node.left
        if node.left:
            node.left.parent = parent
        node.left = parent
        parent.parent = node

    def splay(self, node):
        while node.parent:
            if not node.parent.parent:
                if node.parent.left == node:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.left == node.parent:
                self.right_rotate(node.parent.parent)
                self.right_rotate(node.parent)
            elif node.parent.right == node and node.parent.parent.right == node.parent:
                self.left_rotate(node.parent.parent)
                self.left_rotate(node.parent)
            elif node.parent.left == node and node.parent.parent.right == node.parent:
                self.right_rotate(node.parent)
                self.left_rotate(node.parent)
            else:
                self.left_rotate(node.parent)
                self.right_rotate(node.parent)

    def join(self, left, right):
        if not left:
            return right
        if not right:
            return left
        while left.right:
            left = left.right
        self.splay(left)
        left.right = right
        right.parent = left
        return left

    def split(self, node):
        self.splay(node)
        if node.right:
            node.right.parent = None
        right = node.right
        node.right = None
        return node, right

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                self.splay(node)
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, key):
        node = self.root
        parent = None
        while node:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        new_node = Node(key)
        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self.splay(new_node)

    def delete(self, key):
        node = self.search(key)
        if not node:
            return
        self.splay(node)
        left, right = self.split(node)
        self.root = self.join(left.left, right)

    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.key)
            self.print_tree(node.right, level + 1)

# Path: main.py
def main():
    tree = SplayTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.print_tree(tree.root)
    tree.search(4)
    tree.print_tree(tree.root)
    tree.delete(4)
    tree.print_tree(tree.root)
    tree.delete(5)
    tree.print_tree(tree.root)
    tree.delete(3)
    tree.print_tree(tree.root)
    tree.delete(2)
    tree.print_tree(tree.root)
    tree.delete(1)
    tree.print_tree(tree.root)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.print_tree(tree.root)
    tree.delete(4)
    tree.print_tree(tree.root)
    tree.delete(5)
    tree.print_tree(tree.root)
    tree.delete(3)
    tree.print_tree(tree.root)
    tree.delete(2)
    tree.print_tree(tree.root)
    tree.delete(1)
    tree.print_tree(tree.root)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.print_tree(tree.root)
    tree.delete(4)
    tree.print_tree(tree.root)
    tree.delete(5)
    tree.print_tree(tree.root)
    tree.delete(3)
    tree.print_tree(tree.root)
    tree.delete(2)
    tree.print_tree(tree.root)
    tree.delete(1)
    tree.print_tree(tree.root)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.print_tree(tree.root)
    tree.delete(4)
    tree.print_tree(tree.root)
    tree.delete(5)
    tree.print_tree(tree.root)
    tree.delete(3)
    tree.print_tree(tree.root)
    tree.delete(2)
    tree.print_tree(tree.root)
    tree.delete(1)
    tree.print_tree(tree.root)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.print_tree(tree.root)
    tree.delete(4)
    tree.print_tree(tree.root)
    tree.delete(5)
    tree.print_tree(tree.root)
    tree.delete(3)
    tree.delete(2)
    tree.print_tree(tree.root)
    tree.delete(1)
    tree.print_tree(tree.root)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(5)
    tree.print_tree(tree.root)
    tree.delete(4)
    tree.print_tree(tree.root)


