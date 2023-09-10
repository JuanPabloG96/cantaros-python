from binaryTree import BinaryTree
from node import Node

tree = BinaryTree("nodo raíz")
nodo_izquierdo = Node("nodo izquierdo de nodo raíz");
nodo_derecho = Node("nodo derecho de nodo raíz");
tree.add_child(nodo_izquierdo)
tree.add_child(nodo_derecho)

tree.print_tree() 