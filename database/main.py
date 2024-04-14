from item import Item
from node import Node
from store import Store
from utils import load, save


def main():
    x = load()
    x.remove(3)
    save(x.returnall(x.root))
    x = load()
    x.remove(2)
    save(x.returnall(x.root))
if __name__ == "__main__":
    main()
