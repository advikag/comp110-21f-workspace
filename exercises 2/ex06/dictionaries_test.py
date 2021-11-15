"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730519109"
from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert() -> None:
    """Test for the invert function."""
    x: dict[str, str] = {'a': 'z', 'b': 'y'}
    assert invert(x) == {'z': 'a', 'y': 'b'}
    x: dict[str, str] = {'z': 'z', 'y': 'b'}
    assert invert(x) == {'a': 'z', 'b': 'y'}
    x: dict[str, str] = {'p': 're', 'n': 'ae'}
    assert invert(x) == {'re': 'p', 'ae': 'n'}


def test_favorite_color() -> None:
    """Test for favorite color function."""
    y: dict[str,str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color == "blue"
    y: dict[str,str] = {"Marc": "pink", "Ezri": "pink"}
    assert favorite_color == "pink"
    y: dict[str,str] = {"Marc": "orange", "Ezri": "orange"}
    assert favorite_color == "orange"


def test_count() -> None:
    """Test for the count function."""
    z: list[str] = ["hi", "hello", "hola", "hi", "howdy"]
    assert count == {"hi": 2, "hello": 1, "hola": 1, "howdy": 1}
    z: list[str] = ["bye", "ciao", "goodbye", "bye"]
    assert count == {"bye": 2, "ciao": 1, "goodbye": 1}
    z: list[str] = ["greg", "nate", "mina"]
    assert count == {"greg": 2, "nate": 1, "mina": 1}