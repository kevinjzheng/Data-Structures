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
        for node in self.postorder():
            yield node.data

p4 = LinkedBinaryTree.Node(4)
p5 = LinkedBinaryTree.Node(5)
p6 = LinkedBinaryTree.Node(6)
p7 = LinkedBinaryTree.Node(7)
p3 = LinkedBinaryTree.Node(3,p6,p7)
p2 = LinkedBinaryTree.Node(2,p4,p5)
p1 = LinkedBinaryTree.Node(1,p2,p3)


b_tree = LinkedBinaryTree(p1)
# for i in b_tree.breadth_first():
#     print(i.data)

def level_list(root,level):
    if root is None:
        return []
    if level == 0:
        return [root.data]
    elif level >= 1:
        left = level_list(root.left,level-1)
        right = level_list(root.right,level-1)
        return left + right
print(level_list(b_tree.root,2))

test_tree = LinkedBinaryTree()
