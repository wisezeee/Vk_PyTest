import pytest


# Тесты str
def test_str_one():
    result = '55'
    try:
        a = 5 + '5'
        assert a == result
    except TypeError:
        pass


@pytest.mark.parametrize("test_input,expected", [('a' * 3, 'aaa'), ('a' + 'b', 'ab')])
def test_str_two(test_input, expected):
    assert (test_input) == expected


def test_str_three():
    s = 'abc'
    assert type(s) == str


# Тесты tuple

tests1 = [('I ', ('I', ' ')), ('am', ('a', 'm')),
          ('Karina', ('K', 'a', 'r', 'i', 'n', 'a'))]


@pytest.mark.parametrize('mas, x', tests1)
def test_tuple_one(mas, x):
    res = tuple(mas)
    assert x == res


tests2 = [(("Sasha", 37, "VK", "software developer"), (37, "VK")), (("Kate", 'HR', "VK", 18), ('HR', 'VK'))]


@pytest.mark.parametrize('mas, x', tests2)
def test_tuple_two(mas, x):
    res = mas[1:3]
    assert x == res


def test_tuple_three():
    result = ('a', 'b', 'c')
    try:
        result.append('d')
    except AttributeError:
        pass
