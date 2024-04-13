class Node():

    def __init__(self, data, num: int):
        self.data = data
        self.id = num
        self.left: Node | None = None
        self.right: Node | None = None
        self.empty = self.is_empty()

    def is_empty(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False
    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
