from LinkedBinaryTree import LinkedBinaryTree

p1 = LinkedBinaryTree.Node(6)
p2 = LinkedBinaryTree.Node(4)
p3 = LinkedBinaryTree.Node(2,p1,p2)
p4 = LinkedBinaryTree.Node(3)
p5 = LinkedBinaryTree.Node(5,p3,p4)
p6 = LinkedBinaryTree.Node(0)
p7 = LinkedBinaryTree.Node(1,p6,p5)

tree = LinkedBinaryTree(p7)
# for i in tree:
#     print(i)

def invert_binary_tree(bin_tree):
    if bin_tree is None:
        raise Expception('Tree is empty')
    else:
        return LinkedBinaryTree(invert_subtree(bin_tree.root))

def invert_subtree(subtree_root):
    position = subtree_root
    if position.right is None and position.left is None:
        return position
    elif position.left is None and position.right is not None:
        right = invert_subtree(position.right)
        return LinkedBinaryTree.Node(subtree_root.data,right,None)
    elif position.left is not None and position.right is None:
        left = invert_subtree(position.left)
        return LinkedBinaryTree.Node(subtree_root.data,None,left)
    else:
        left =  invert_subtree(position.left)
        right = invert_subtree(position.right)
        return LinkedBinaryTree.Node(subtree_root.data,right,left)

# print(invert_binary_tree(tree).data)
# print(invert_binary_tree(tree).right.data)
# print(invert_binary_tree(tree).left.data)
# print(invert_binary_tree(tree).left.left.data)
# print(invert_binary_tree(tree).left.right.data)
# print(invert_binary_tree(tree).left.right.left.data)
# print(invert_binary_tree(tree).left.right.right.data)
print('problem1')
for i in invert_binary_tree(tree):
    print(i)
print('problem2')

def subtree_children_dist(curr_root):
    if curr_root.right is None and curr_root.left is None:
        return 
    elif curr_root.right is not None and curr_root.left is None:
        return subtree_children_dist(curr_root.right)



# p1 = LinkedBinaryTree.Node(6)
# p2 = LinkedBinaryTree.Node(4)
# p3 = LinkedBinaryTree.Node(2,None,p2)
# p4 = LinkedBinaryTree.Node(5,None,p1)
# p5 = LinkedBinaryTree.Node(1,p3,p4)
#
# flat = LinkedBinaryTree(p5)

def flatten_tree(bin_tree):
    bin_root = bin_tree.root

def flatten_subtree(curr_root):
    if not curr_root.left and not curr_root.right:
        return
    elif not curr_root.left and curr_root.right:
        return flatten_subtree(curr_root.right)
        curr_root.parent = None
    elif not curr_root.right and curr_root.left:
        return flatten_subtree(curr_root.left)
    else:
        return flatten_subtree(curr_root.left)
        return flatten_subtree(curr_root.right)


# for i in flat:
#     print(i)
# print('tree')
#
# flatten_tree(flat)
#
# for i in flat:
#     print(i)
# print('flat_tree')
