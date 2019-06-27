import binarytree

def eval(exp_tree):
    if exp_tree.is_empty():
        raise Exception('tree is empty')
    return subtree_eval(exp_tree.root)

def subtree_eval(curr_root):
    if isinstance(curr_root.data,(int,float)):
        return curr_root.data
    else:
        l_val = subtree_eval(curr_root.left)
        r_val = subtree_eval(curr_root.right)
        if curr_root.data == '+':
            return l_val + r_val
        elif curr_root.data == '-':
            return l_val - r_val
        elif curr_root.data == '*':
            return l_val * r_val
        elif curr_root.data == '/':
            return l_val / r_val
        else:
            raise Exception("Operator is not supported: " + str(curr_root.data))

# p1 = binarytree.LinkedBinaryTree.Node(1)
# p2 = binarytree.LinkedBinaryTree.Node(6)
# p3 = binarytree.LinkedBinaryTree.Node(2,p1,p2)
# p4 = binarytree.LinkedBinaryTree.Node(4)
# p5 = binarytree.LinkedBinaryTree.Node(5,p3,p4)

# binary_tree_1 = binarytree.LinkedBinaryTree(p5)

p1 = binarytree.LinkedBinaryTree.Node(1)
p2 = binarytree.LinkedBinaryTree.Node(6)
p3 = binarytree.LinkedBinaryTree.Node(4)
p4 = binarytree.LinkedBinaryTree.Node('*',p2,p3)
p5 = binarytree.LinkedBinaryTree.Node('+',p1,p4)

binary_tree_1 = binarytree.LinkedBinaryTree(p5)

for node in binary_tree_1.breadth_first():
    print(node.data, end = " ")
print()


'''
def seq1():
    yield 1
    yield 2

def seq2():
    yield 'a'
    yield 'b'
    for i in seq1():
        #seq1 is only a generator but no one intiate the data from seq1 so therefore when printing seq2. 2,1 isnt printed
        yield i #unless asked to yield from

def seq2():
    yield 'a'
    yield 'b'
    yield from seq1()
    #same as the for loop above

for i in seq2():
    print i
'''
