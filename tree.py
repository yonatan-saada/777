l = [[100,80,90],[40,80,60]]
def f(l):
    for i in l:
        yield sum(i)/len(i)
a = f(l)
print(next(a))
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def add_node(self, data):
        def add_node_req(root, data):
            if not root:
                return Node(data)
            if data > root.data:
                root.right = add_node_req(root.right, data)
            else:
                root.left = add_node_req(root.left, data)
            return root

        self.root = add_node_req(self.root, data)

    def print_tree(self):
        def print_tree_req(root):
            if not root:
                return
            print_tree_req(root.left)
            print(root.data)
            print_tree_req(root.right)

        print_tree_req(self.root)

    def search_node(self, data):
        def search_node_req(root, data):
            if not root:
                return None
            if root.data == data:
                return root.data
            if data > root.data:
                return search_node_req(root.right, data)
            else:
                return search_node_req(root.left, data)

        return search_node_req(self.root, data)

    def find_min(self):
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.data

    def delete(self, data):
        def _delete(node, data):
            if not node:
                return None
            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:

                if not node.left and not node.right:
                    return None

                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                min_val_node = node.right
                while min_val_node.left:
                    min_val_node = min_val_node.left
                node.value = min_val_node.data
                node.right = _delete(node.right, min_val_node.data)
            return node

        self.root = _delete(self.root, data)

