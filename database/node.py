class Node():

    def __init__(self, data, num):
        self.data = data
        self.id = num
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
