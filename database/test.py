from store import Store
from node import Node
from utils import save, load
from item import Item 
def main():
    """bst = Store(Node(Item(10,"Apples", 9.99),1))
    bst.add(Node(Item(12, "Bananas", 11.99), 2), bst.root)
    bst.add(Node(Item(20, "cookies", 15), 3), bst.root)
    biglist = bst.returnall(bst.root)
    save(biglist)"""
    bst = load()
    x = bst.returnall(bst.root)
    for i in x:
        print(i.id)
    save(x)

if __name__ == "__main__":
    main()
