def is_bst(binary_tree):
    return is_bst_helper(binary_tree.root)[0]

def is_bst_helper(curr_root):
    if curr_root.left is None and curr_root.right is None:
        return (True,node.item.key)
    if curr.left is not None:
        is.left,min_left,max_left = helper(curr_root.left)
