import math
elements = [1,4,-5,8,9,11,4,5,0]
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
				print "233"
				return True
				
			left_depth = 0
			while tree.left is not None:
				left_depth += 1
				tree = tree.left
			
			right_depth = 0
			while tree.right is not None:
				right_depth += 1
				tree = tree.right
			
			#print math.fabs(-2)
			if math.fabs(left_depth - right_depth) > 1:
				return False
			return True
			
		def insert(self, element, depth):
			if self.root.next is None:
				node = TreeNode(element, depth)
				node.parent = self.root 
				self.root.next = node
				#print self.is_balance(node)
				return
				
			tree = self.root.next
			
			while tree is not None:
				depth += 1
				temp_tree = tree
				if self.is_balance(temp_tree) is False:
					print "need reset"
					self.inorder(temp_tree)
					
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
				
		def left_rotate(self, tree):
			if tree.right is None:
				return
			node = tree.right
			tree.right = need.left
			if node.left is not None:
				node.left.parent = tree
			node.parent = tree.parent
			
			if tree.parent is self.root:
				self.root.next = node
			elif tree is tree.parent.left:
				
			
		def inorder(self, tree):
			if tree is None:
				return
			self.inorder(tree.left)
			print "element is ",tree.element, "depth is ", tree.depth
			self.inorder(tree.right)
			
			
def get_node_depth(root, node):
	pass
def insert(tree, element, depth):
	if (tree is None):
		tree = TreeNode(element)
		tree.depth = depth
		return tree
	depth += 1
	if tree.element >= element:
		if tree.left is None:
			node = TreeNode(element)
			tree.left = node
			node.parent = tree
			node.depth = depth
			return
		insert(tree.left, element, depth)
	elif tree.element < element:
		if tree.right is None:
			node = TreeNode(element)
			tree.right = node
			node.parent = tree
			node.depth = depth
			return
		insert(tree.right, element, depth)
	
	return tree

def InOrder(tree):
	if tree is None:
		return
	#print tree.is_balance(tree.root)
	InOrder(tree.left)
	print "element is ",tree.element, "depth is ", tree.depth
	
	print "-------"
	InOrder(tree.right)
tree = AvlTree()
for i in elements:
	tree.insert(i, 0)
InOrder(tree.root.next)

	