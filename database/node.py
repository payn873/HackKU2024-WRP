class Node():

    def __init__(self, data, num: int):
        self.data = data
        self.id = num
        self.left: Node | None = None
        self.right: Node | None = None
        self.empty = self.is_empty

    def is_empty(self):
        # Returns if the node has any children
        return self.left == None and self.right == None
    def __lt__(self, other):
        # Compares the ids of the two Nodes.
        return self.id < other.id

    def __gt__(self, other):
        # Compares the ids of the two Nodes.
        return self.id > other.id
