from utils.text import slugify

def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"

def test_slugify_special_characters():
    assert slugify("Gemma 4: The Next Gen AI!?") == "gemma-4-the-next-gen-ai"

def test_slugify_empty_and_whitespace():
    assert slugify("") == ""
    assert slugify("   ") == ""
