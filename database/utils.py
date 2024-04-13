from tomlkit import parse
from tomlkit import dumps
from tomlkit import document
from node import Node
from store import Store
from item import Item

def save(data: list[Node]):
    with open("data2.toml", "w+") as f:
        doc = document()
        for i in data:
            doc[str(i.id)] = {"amount" : i.data.amount, "name" : i.data.name, "price" : i.data.price}
        f.write(dumps(doc))

def load() -> Store:
    with open("data.toml", "r+") as f:
        doc = parse(f.read().strip())
        bst: Store | None = None
        for key in doc.keys():
            if bst:
                bst.add(Node(Item(doc[key]["amount"], doc[key]["name"], doc[key]["price"]), int(key)), bst.root)
            else:
                bst = Store(Node(Item(doc[key]["amount"], doc[key]["name"], doc[key]["price"]), int(key)))
        return bst