"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730519109"
from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert() -> None:
    """Test for the invert function."""
    x: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(x) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert1() -> None:   
    """Test for the invert1 function."""
    x: dict[str, str] = {'za': 'z', 'yb': 'b'}
    assert invert(x) == {'a': 'za', 'b': 'yb'}


def test_invert2() -> None:
    """Test for the invert function2."""
    x: dict[str, str] = {'p': 're'}
    assert invert(x) == {'re': 'p'}


def test_favorite_color1() -> None:
    """Test for favorite color function."""
    y: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color == "blue"


def test_favorite_color2() -> None:
    """Test for favorite color function2."""
    y: dict[str, str] = {"Marc": "pink", "Ezri": "pink"}
    assert favorite_color == "pink"


def test_favorite_color3() -> None:
    """Test for favorite color function3."""
    y: dict[str, str] = {"Marc": "orange", "Ezri": "yellow"}
    assert favorite_color == "orange"


def test_count() -> None:
    """Test for the count function1."""
    z: list[str] = ["hi", "hello", "hola", "hi", "howdy"]
    assert count == {"hi": 2, "hello": 1, "hola": 1, "howdy": 1}


def test_count1() -> None:
    """Test for the count function2."""
    z: list[str] = ["bye", "ciao", "goodbye", "bye"]
    assert count == {"bye": 2, "ciao": 1, "goodbye": 1}


def test_count2() -> None:
    """Test for the count function3."""
    z: list[str] = ["greg"]
    assert count == {"greg": 1}