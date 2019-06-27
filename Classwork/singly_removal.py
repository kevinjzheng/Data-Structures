def removeNum(node,removal):
    current = node
    while current != None and current.next_node != None:
        if current.data == removal:
            current.next_node = current.next_node.next_node
        if current.next_node.data == removal:
            current.next_node = current.next_node.next_node
        current = current.next_node
