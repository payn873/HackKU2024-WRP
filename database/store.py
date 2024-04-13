from node import Node
from utils import Utils
class Store():
    def __init__(self, node: Node) -> None:
        self.root: Node | None = node

    def add(self, node: Node, current: Node | None):
        if self.root == None:
            self.root = node
        elif node > current:
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

    def search(self, target: int, current: Node) -> Node | None:
        if target < current.id:
            return self.search(target, current.left)
        elif target > current.id:
            return self.search(target, current.right)
        else:
            return current

    def parent(self, node: Node, target: Node, parent: Node | None = None) -> Node:
        if parent:
            if node == target:
                return parent
            else:
                if target < node:
                    return self.parent(node.left, target, node)
                elif target > node:
                    return self.parent(node.right, target, node)
        else:
            if target < node:
                return self.parent(node.left, target, node)
            elif target > node:
                return self.parent(node.right, target, node)

    def min(self, current):
        if current.left:
            return self.min(current.left)
        else:
            return current

    def max(self, current):
        if current.right:
            return self.max(current.right)
        else:
            return current

    def remove(self, target: int):
        if target == self.root.id:
            if self.root.empty:
                self.root = None
            return
        result = self.search(target, self.root)
        if result:
            parent = self.parent(self.root, result)
            if parent.left == result:
                if result.empty:
                    parent.left = None
                elif (result.left and (result.right is None)) or (result.right and (result.left is None)):
                    if result.left:
                        parent.left = parent.left.left
                    else:
                        parent.left = parent.left.right
                else:
                    if result > result.right:
                        min =  self.min(result.right)
                        self.remove(min.id)
                        parent.left = min
                    else:
                        max = self.max(result.left)
                        self.remove(max.id)
                        parent.left = max
            else:
                if result.empty:
                    parent.right = None
                elif (result.left and (result.right is None)) or (result.right and (result.left is None)):
                    if result.left:
                        parent.right = parent.right.left
                    else:
                        parent.right = parent.right.right
                else:
                    if result > result.right:
                        min =  self.min(result.right)
                        self.remove(min.id)
                        parent.right = min
                    else:
                        max = self.max(result.left)
                        self.remove(max.id)
                        parent.right = max



    def returnall(self, current: Node) -> list:
        if current.left:
            if current.right:
                return [current] + self.returnall(current.left) + self.returnall(current.right)
            else:
                return [current] + self.returnall(current.left)
        elif current.right:
            if current.left == None:
                return [current] + self.returnall(current.right)
        else:
            return [current]