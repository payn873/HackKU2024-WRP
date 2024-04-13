from node import Node
from utils import Utils
class Store():
    def __init__(self, node: Node) -> None:
        self.root = node

    def add(self, node, current):
        if node > current:
            if current.right == None:
                current.right = node
            else:
                self.add(node, current.right)
        elif node < current:
            if current.left == None:
                current.left = node
            else:
                self.add(node, current.left)
        else:
            print("Duplicate id")

        
