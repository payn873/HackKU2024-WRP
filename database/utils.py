from tomlkit import document, dumps, parse
from item import Item
from node import Node
from store import Store


def save(data: list[Node]):
    # Takes in a list of node ojects and writes a toml file using them.
    with open("data.toml", "w+") as f:
        doc = document()
        for i in data:
            doc[str(i.id)] = {"amount" : i.data.amount, "name" : i.data.name, "price" : i.data.price}
        f.write(dumps(doc))

def load() -> Store:
    # Reads the data.toml file and parses it to create a binary search tree, which it then returns.
    with open("data.toml", "r+") as f:
        doc = parse(f.read().strip())
        bst: Store | None = None
        for key in doc.keys():
            if bst:
                bst.add(Node(Item(doc[key]["amount"], doc[key]["name"], doc[key]["price"]), int(key)), bst.root)
            else:
                bst = Store(Node(Item(doc[key]["amount"], doc[key]["name"], doc[key]["price"]), int(key)))
        return bst