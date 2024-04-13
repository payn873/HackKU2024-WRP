from store import Store
from node import Node
def main():
    bst = Store(Node("aaaa", 1))
    bst.add(Node("bbbb", 2), bst.root)
    bst.add(Node("cccc", 3), bst.root)
    bst.search(2, bst.root)
    biglist = bst.returnall(bst.root)
    for i in biglist:
        print(i.data)
    print(bst.search(2, bst.root).data)

if __name__ == "__main__":
    main()
