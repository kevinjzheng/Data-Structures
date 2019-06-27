class BinarySearchTreeMap:
    class Item:
        def __init__(self,key,value = None):
            self.key = key
            self.value = value
    class Node:
        def __init__(self,item):
            self.item = Item
            self.left = None
            self.right = None
            self.parent = None

        def number_of_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if self.right is not None:
                count += 1
            return count

    def __init__(self):
        self.root = None
        self.size =0
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self) == 0

    # raise Exception if key is not found
    def __getitem__(self,key):
        node = self.subtree_find(key)
        if node is not None:
            return node.item.value
        else:
            raise KeyError('Key Error: ' + str(key))

    # return None is key is not found
    def subtree_find(self,key):
        curr = self.root
        while curr is not None:
            if curr.item.key == key:
                return curr
            elif curr.item.key > key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def __setitem__(self,key,value):
        node = self.subtree_find(key)
        if node is not None:
            node.item.value = value
        else:
            self.subtree_insert(key,value)

    # assuming key is not in the tree
    def subtree_insert(self,key,value):
        new_item = BinarySearchTreeMap(key,value)
        new_node = BinarySearchTreeMap.Node(new_item)
        if self.is_empty():
            self.root = new_node
        else:
            parent = self.root
            if key < self.root.item.key:
                curr = parent.left
            else:
                curr = parent.right
            while curr is not None:
                parent = curr
                if key < curr.item.key:
                    curr = curr.left
                else:
                    curr = curr.right
            new_node.parent = parent
            if key < parent.item.key:
                parent.left = new_node
            else:
                parent.right = new_node
        self.size += 1

    # raises exception if key is not in the tree
    def __delitem__(self,key):
        node = self.subtree_find(key)
        if node is None:
            raise KeyError('KeyError: ' + str(key))
        else:
            self.subtree_delete(key)

    def subtree_delete(self,key):
        node_to_delete = self.subtree_find(key)
        num_children = node_to_delete.number_of_children()
        value = node_to_delete.item.value

        if node_to_delete is self.root:
            if num_children == 0:
                self.root = None
                self.size = 0
                node_to_delete.disconnect()
            elif num_children == 1:
                if self.root.right is None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
            elif num_children == 2:
                max_of_left = self.subtree_max(node_to_delete.left)
                max_of_left = self.subtree_max(node_to_delete.left,max_of_left.item.key)
                node_to_delete.item = max_of_left
                self.subtree_delete(node_to_delete.left,max_of_left.item.key)
        else:
            if num_children == 0:
                parent = node_to_delete.parent
                if parent.right is node_to_delete:
                    parent.right = None
                else:
                    parent.left = None
                node_to_delete.disconnect()
                self.size -= 1
            elif num_children == 1:
                parent = node_to_delete.parent
                if node_to_delete.left is not None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right
                child.parent = parent
                if node_to_delete is parent.left:
                    parent.left = child
                else:
                    parent.right = child
                node_to_delete.disconnect()
                self.size -= 1
            elif num_children == 2:
                max_of_left = self.subtree_max(node_to_delete.left,max_of_left.item.key)
                node_to_delete.item = max_of_left
                self.subtree_delete(node_to_delete.left,max_of_left.item.key)

        return value

    def subtree_max(self,curr_node):
        curr = curr_node
        while curr.right is not None:
            curr = curr.right
        return curr

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self,curr_root):
        if curr_root is None:
            return
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield from curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        pass
