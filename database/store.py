from node import Node


class Store():
    def __init__(self, node: Node) -> None:
        self.root: Node | None = node

    def add(self, node: Node, current: Node | None):
        # Adds a new node to the tree.
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
        # Searchs for a node with the target id.
        if target < current.id:
            return self.search(target, current.left)
        elif target > current.id:
            return self.search(target, current.right)
        else:
            return current

    def parent(self, node: Node, target: Node, parent: Node | None = None) -> Node:
        # Gets the parent of the entered node.
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
        # Gets the min value in the current subtree.
        if current.left:
            return self.min(current.left)
        else:
            return current

    def max(self, current):
        # Gets the max value in the current subtree.
        if current.right:
            return self.max(current.right)
        else:
            return current

    def remove(self, target: int):
        # Removes a node with the id of target from the tree.
        # This is honestly not well made made but I really don't want to redo it.
        if target == self.root.id:
            if self.root.is_empty():
                self.root = None
                return
            else:
                if (self.root.left and (self.root.right is None)) or (self.root.right and (self.root.left is None)):
                    if self.root.left:
                        self.root = self.root.left
                        return
                    else:
                        self.root = self.root.right
                        return
                else:
                    if self.root > self.root.right:
                        min =  self.min(self.root.right)
                        self.remove(min.id)
                        self.root.data = min.data
                        self.root.id = min.id
                        return
                    else:
                        max = self.max(self.root.left)
                        self.remove(max.id)
                        self.root.data = max.data
                        self.root.id = max.id
                        return
        result = self.search(target, self.root)
        if result:
            parent = self.parent(self.root, result)
            if parent.left == result:
                if result.is_empty():
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
                        parent.left.data = min.data
                        parent.left.id = min.id
                    else:
                        max = self.max(result.left)
                        self.remove(max.id)
                        parent.left.data = max.data
                        parent.left.id = max.id
            else:
                if result.is_empty():
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
                        parent.right.data = min.data
                        parent.right.id = min.id
                    else:
                        max = self.max(result.left)
                        self.remove(max.id)
                        parent.right.data = max.data
                        parent.right.id = max.id



    def returnall(self, current: Node) -> list:
        # Creates a list of every node in the tree.
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