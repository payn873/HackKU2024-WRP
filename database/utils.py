from tomlkit import parse
from tomlkit import dumps
from tomlkit import document
from node import Node
from store import Store


def save(data: list[Node]):
    with open("data.toml", "w+") as f:
        doc = document()
        for i in data:
            doc[str(i.id)] = i.data
        f.write(dumps(doc))

def load():
    with open("data.toml", "r+") as f:
        doc = parse(f.read().strip())
        bst: Store | None = None
        for key in doc.keys():
            if bst:
                bst.add(Node(doc[key], int(key)), bst.root)
            else:
                bst = Store(Node(doc[key], int(key)))
        return bst