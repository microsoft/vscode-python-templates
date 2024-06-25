import pytest
from my_package.__main__ import Developer


def test_get_info():
    dev = Developer("Alice", "Python")
    assert dev.get_info() == "Alice is a developer who codes in Python."


def test_invalid_language():
    with pytest.raises(ValueError):
        dev = Developer("Bob", "English")
