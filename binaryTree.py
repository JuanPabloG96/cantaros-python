from node import Node

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def add_child(self, new_node):
        if self.root.left is None:
            self.root.left = new_node
        elif self.root.right is None:
            self.root.right = new_node

    def find_node(self, data):
        return self._find_node(self.root, data)

    def _find_node(self, current_node, data):
        if current_node is None:
            return None
        if current_node.data == data:
            return current_node
        left_result = self._find_node(current_node.left, data)
        if left_result is not None:
            return left_result
        return self._find_node(current_node.right, data)
      
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            print(current_node.data)
            self._print_tree(current_node.left)
            self._print_tree(current_node.right)