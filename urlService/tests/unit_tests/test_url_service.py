import pytest
from uuid import uuid4, UUID
from urlAPI.models import Text
from urlAPI.services.text_service import TextService


@pytest.fixture(scope='session')
def text_data() -> tuple[str, str]:
    return 'Text 1', 'Lorem ipsum dolor sit amet'


def test_text_creation() -> None:
    name, text_content = 'Text 1', 'Lorem ipsum dolor sit amet'
    text = Text(name, text_content)
    assert text.name == name
    assert text.text == text_content


def test_get_texts_empty() -> None:
    service = TextService()
    texts = service.get_texts()
    assert texts == []


def test_new_text_success(text_data: tuple[str, str]) -> None:
    service = TextService()
    text = Text(*text_data)
    service.add_text(text)
    texts = service.get_texts()
    assert len(texts) == 1
    assert texts[0].name == text_data[0]


def test_get_text_with_wrong_id() -> None:
    service = TextService()
    with pytest.raises(KeyError):
        service.get_text_by_id(uuid4())


def test_get_text_success(text_data: tuple[str, str]) -> None:
    service = TextService()
    text = Text(*text_data)
    service.add_text(text)
    retrieved_text = service.get_text_by_id(text.id)
    assert retrieved_text.name == text.name


def test_find_urls_in_text(text_data: tuple[str, str]) -> None:
    service = TextService()
    text = Text(*text_data)
    service.add_text(text)
    urls = service.find_urls_in_text(text.id)
    assert len(urls) == 0


def test_delete_urls_from_text(text_data: tuple[str, str]) -> None:
    service = TextService()
    text = Text(*text_data)
    service.add_text(text)
    updated_text = service.delete_urls_from_text(text.id)
    assert updated_text.text == text.text


def test_delete_text() -> None:
    service = TextService()
    text = Text('Text 1', 'Lorem ipsum dolor sit amet')
    service.add_text(text)
    service.delete_text(text.id)
    texts = service.get_texts()
    assert len(texts) == 0