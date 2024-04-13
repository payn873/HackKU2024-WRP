from store import Store
from node import Node
from utils import save, load
def main():
    bst = load()
    bst.search(2, bst.root)
    biglist = bst.returnall(bst.root)
    for i in biglist:
        print(i.data)

if __name__ == "__main__":
    main()
