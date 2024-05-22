from uuid import UUID, uuid4


class Text:
    id: UUID
    name: str
    text: str

    def __init__(self, name: str, text: str, id: UUID = None):
        self.id = id or uuid4()
        self.name = name
        self.text = text
