from uuid import UUID

from urlAPI.models import Text

texts: dict[UUID, Text] = {}


class TextService:

    def get_texts(self):
        texts_values = []
        for text in texts.values():
            texts_values.append(text)
        return texts_values

    def get_text_by_id(self, id: UUID):
        if not id in texts:
            return
        return texts[id]

    def add_text(self, text: Text):
        existing_names = [t.name for t in texts.values()]
        name = text.name
        if text.name in existing_names:
            i = 1
            new_name = f"{name} ({i})"
            while new_name in existing_names:
                i += 1
                new_name = f"{name} ({i})"
            text.name = new_name
        texts[text.id] = text
        return text

    def delete_text(self, id: UUID):
        if id in texts:
            del texts[id]