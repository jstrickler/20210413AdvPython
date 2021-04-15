from dog import Dog
import pytest

@pytest.fixture
def dog_name():
    return "Frodo"


def test_dog_name_is_correct(dog_name):
    d = Dog(dog_name)
    assert d.nickname == dog_name

def test_invalid_name_raises_error():
    with pytest.raises(TypeError):
        for test_name in 123, 123.456, ["a", "b"], {}:
            d = Dog(test_name)
