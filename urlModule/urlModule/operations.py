import re


def delete_urls(text: str):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub('', text)


def find_urls(text: str):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.findall(text)
