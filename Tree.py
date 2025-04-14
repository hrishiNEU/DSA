class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

#print(A)

# Recursive Pre Order Traversal
print("Starting Pre Order Traversal")
def pre_order(node):
    if not node:
        return  
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)
print("Pre Order Traversal Done")

# Recursive In Order Traversal

print("Starting In Order Traversal")
def in_order(node):
    if not node:
        return  
    
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)
print("In Order Traversal Done")

# Recursive Post Order Traversal
print("Starting Post Order Traversal")
def post_order(node):
    if not node:
        return  
    
    post_order(node.left)
    post_order(node.right)
    print(node)

pre_order(A)
print("Post Order Traversal Done")