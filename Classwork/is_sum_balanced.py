import ArrayQueue

class LinkedBinaryTree:
    class Node:
        def __init__(self,data,left = None, right = None):
            self.data = data
            self.parent = None
            self.left = left
            self.right = right
            if left is not None:
                self.left.parent = self
            self.right = right
            if right is not None:
                self.right.parent = self
            self.left = left
    def __init__(self,root = None):
        self.root = root
        self.size = self.subtree_count(self.root)
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self) == 0
    def subtree_count(self,curr_root):
        if curr_root is None:
            return 0
        else:
            left_count = self.subtree_count(curr_root.left)
            right_count = self.subtree_count(curr_root.right)
            return left_count + right_count + 1
    def height(self):
        if self.is_empty():
            raise Exception('Height is not defined for an empty tree')
        return self.subtree_height(self.root)
    def subtree_height(self,curr_root):
        if curr_root.left is None and curr_root.right is None:
            return 0
        elif curr_root.right is None:
            return 1 + self.subtree_height(curr_root.left)
        elif curr_root.left is None:
            return 1 + self.subtree_height(curr_root.right)
        else:
            left_height = self.subtree_height(curr_root.left)
            right_height = self.subtree_height(curr_root.right)
            return 1 + max(left_height,right_height)
    def preorder(self):
        yield from self.subtree_preorder(self.root)
    def subtree_preorder(self,curr_root):
        if curr_root is None:
            return
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)
    def inorder(self):
        yield from self.subtree_inorder(self.root)
    def subtree_inorder(self,curr_root):
        if curr_root is None:
            return
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)
    def postorder(self):
        yield from self.subtree_postorder(self.root)
    def subtree_postorder(self,curr_root):
        if curr_root is None:
            return
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root
    def breadth_first(self):    #queue storing nodes so it can reference the children and the data values
        if self.is_empty():
            return
        nodes_queue = ArrayQueue.ArrayQueue()
        nodes_queue.enqueue(self.root)
        while not (nodes_queue.is_empty()):
            curr_node = nodes_queue.dequeue()
            yield curr_node
            if curr_node.left is not None:
                nodes_queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                nodes_queue.enqueue(curr_node.right)
    def __iter__(self):
        for node in self.preorder():
            yield node.data

def is_sum_balanced(bin_tree):
    balanced = is_subtree_balanced(bin_tree.root)
    return balanced[1]

def is_subtree_balanced(subtree_root):
    if subtree_root is None:
        return (0,True)
    elif subtree_root.left is None and subtree_root.right is None:
        return (subtree_root.data,True)
    # elif subtree_root.left is None and subtree_root.right is not None:
    #     if is_subtree_balanced(subtree_root.right)[0] > 1:
    #         return (subtree_root.right.data,False)
    #     return (subtree_root.data + subtree_root.right.data,True)
    # elif subtree_root.right is None and subtree_root.left is not None:
    #     if is_subtree_balanced(subtree_root.left)[0] > 1:
    #         return (subtree_root.left.data,False)
    #     return (subtree_root.data + subtree_root.left.data,True)
    else:
        left = is_subtree_balanced(subtree_root.left)
        right = is_subtree_balanced(subtree_root.right)
        if abs(left[0]-right[0]) > 1:
            return (left[0]-right[0],False)
        else:
            return (left[0]+right[0]+subtree_root.data,True)

p3a = LinkedBinaryTree.Node(3)
p2 = LinkedBinaryTree.Node(2)
p3 = LinkedBinaryTree.Node(3,p3a,p2)
p1 = LinkedBinaryTree.Node(1)
p6 = LinkedBinaryTree.Node(6,None,p1)
# p4a = LinkedBinaryTree.Node(4)
# p1 = LinkedBinaryTree.Node(1)
# p1b = LinkedBinaryTree.Node(1)
# p6 = LinkedBinaryTree.Node(6,None,p1b)
# p3 = LinkedBinaryTree.Node(3,p4a,p1)
p4 = LinkedBinaryTree.Node(4,p3,p6)

b_tree = LinkedBinaryTree(p4)

print(is_sum_balanced(b_tree))
