"""Test the mynames module."""
import pytest

from mynames import MyNames


@pytest.fixture
def new_names():
    """Return a new names instance."""
    return MyNames()


@pytest.fixture
def name_string_list():
    """Return a list of example names."""
    return ["Alice", "Bob", "Eve"]


@pytest.fixture
def used_names(name_string_list):
    """Return a names instance, after three names have been added."""
    my_name = MyNames()
    for name in name_string_list:
        my_name.lookup(name)
    return my_name


def test_get_string_raises_exceptions(used_names):
    """Test if get_string raises expected exceptions."""
    with pytest.raises(TypeError):
        used_names.get_string(1.4)
    with pytest.raises(TypeError):
        used_names.get_string("hello")
    with pytest.raises(ValueError):
        used_names.get_string(-1)


@pytest.mark.parametrize("name_id, expected_string", [
    (0, "Alice"),
    (1, "Bob"),
    (2, "Eve"),
    (3, None)
])
def test_get_string(used_names, new_names, name_id, expected_string):
    """Test if get_string returns the expected string."""
    # Name is present
    assert used_names.get_string(name_id) == expected_string
    # Name is absent
    assert new_names.get_string(name_id) is None

def test_lookup_rasises_exceptions(used_names):
    """Test if lookup raises expected exceptions"""
    with pytest.raises(TypeError):
        used_names.lookup(56)
    with pytest.raises(TypeError):
        used_names.lookup(True)
    with pytest.raises(TypeError):
        used_names.lookup(None)

@pytest.mark.parametrize("name_string, expected_id", [
    ("Alice", 0),
    ("Bob", 1),
    ("Eve", 2),
    ("Michael", 3)
])
def test_lookup(used_names, new_names, name_string, expected_id):
    """Test if get_string returns the expected string."""
    # Name is present
    assert used_names.lookup(name_string) == expected_id

