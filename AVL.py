import math

elements = [1, 4, -5, 8, 9, 11, 4, 7, -7, 0]


class TreeNode():
    def __init__(self, element=0, depth=0):
        self.element = element
        self.parent = None
        self.left = None
        self.right = None
        self.depth = depth


class RootNode():
    def __init__(self):
        self.next = None


class AvlTree():
    def __init__(self):
        self.root = RootNode()

    def is_balance(self, tree):
        if tree is None:
            return True
        #print "debug is_balance: element is ", tree.element, "depth is ", tree.depth
        temp = tree
        left_depth = 0
        while temp.left is not None:
            left_depth += 1
            temp = temp.left
        right_depth = 0
        temp = tree
        while temp.right is not None:
            right_depth += 1
            temp = temp.right
        #print "debug left depth ", left_depth, "right depth", right_depth
        if math.fabs(left_depth - right_depth) > 1:
            return False
        return True

    def left_or_right(self, tree):
        left_depth = 0
        right_depth = 0
        temp = tree
        while temp.left is not None:
            left_depth += 1
            temp = temp.left
        temp = tree
        while temp.right is not None:
            right_depth += 1
            temp = temp.right

        if left_depth > right_depth:
            return "left"
        elif right_depth > left_depth:
            return "right"

    def insert(self, element, depth):
        if self.root.next is None:
            node = TreeNode(element, depth)
            node.parent = self.root
            self.root.next = node
            return

        tree = self.root.next
        while tree is not None:
            depth += 1
            temp_tree = tree
            if tree.element >= element:
                tree = tree.left
            elif tree.element < element:
                tree = tree.right
        node = TreeNode(element, depth)
        node.parent = temp_tree
        if temp_tree.element >= element:
            temp_tree.left = node
        elif temp_tree.element < element:
            temp_tree.right = node
        #print "debug check before"
        #self.inorder(self.root.next)
        self.check_tree(self.root.next)
        #print "debug check done"
        #self.inorder(self.root.next)
        #print ""

    def left_rotate(self, tree):
        if tree.right is None:
            return
        node = tree.right
        tree.right = node.left
        if node.left is not None:
            node.left.parent = tree
            node.parent = tree.parent
        if tree.parent is self.root:
            self.root.next = node
        elif tree is tree.parent.left:
            tree.parent.left = node
        else:
            tree.parent.right = node
        node.left = tree
        tree.parent = node
        return tree

    def right_rotate(self, tree):
        if tree.left is None:
            return
        node = tree.left
        tree.left = node.right
        if node.right is not None:
            node.right.parent = tree
        node.parent = tree.parent
        if tree.parent is self.root:
            self.root.next = node
        elif tree is tree.parent.right:
            tree.parent.right = node
        else:
            tree.parent.left = node
        node.right = tree
        tree.parent = node
        return tree

    def inorder(self, tree):
        if tree is None:
            return
        self.inorder(tree.left)
        print "element is ", tree.element, "depth is ", tree.depth
        self.inorder(tree.right)

    def reset_depth(self, tree, depth):
        if tree is None:
            return
        tree.depth = depth
        depth += 1
        self.reset_depth(tree.left, depth)
        self.reset_depth(tree.right, depth)

    def check_tree(self, tree):
        if tree is None:
            return
        if not self.is_balance(tree):
            #print "debug lost banlence element is ", tree.element, "depth is", tree.depth
            if self.left_or_right(tree) == "right":
                #print "left"
                self.left_rotate(tree)
            elif self.left_or_right(tree) == "left":
                #print "right"
                self.right_rotate(tree)
            self.reset_depth(self.root.next, 0)
            return
        self.check_tree(tree.left)
        self.check_tree(tree.right)

tree = AvlTree()
for i in elements:
    tree.insert(i, 0)
print "result"
tree.inorder(tree.root.next)

