from src.pytemplate.domain.user import (
    age,
    height,
    ID,
    last_letter,
    name,
    new_awesome_list,
    new_awesome_tuple,
    new_list,
    new_tuple,
    surname,
    surname_slice,
)


def test_age():
    assert isinstance(age, int)
    assert age == 32


def test_height():
    assert isinstance(height, float)
    assert height == 1.85


def test_identity():
    assert isinstance(name, str)
    assert isinstance(surname, str)
    assert isinstance(ID, str)
    assert name == "Rashad"
    assert surname == "Musayev"
    assert ID == name + " " + surname


def test_last_letter():
    assert isinstance(last_letter, str)
    assert last_letter == name[-1]


def test_surname_slice():
    assert isinstance(surname_slice, str)
    assert surname_slice == surname[1:3]


def test_new_list_type():
    assert isinstance(new_list, list)
    assert all(isinstance(i, int) for i in new_list)
    assert new_list == [3, 4, 5, 6, 7]


def test_new_awesome_list_type():
    assert isinstance(new_awesome_list, list)
    assert all(isinstance(i, int) for i in new_awesome_list)
    assert new_awesome_list == [3, 6, 7]


def test_new_tuple_type():
    assert isinstance(new_tuple, tuple)
    assert all(isinstance(i, int) for i in new_tuple)
    assert new_tuple == (3, 4, 5, 6, 7)


def test_new_awesome_tuple_type():
    assert isinstance(new_awesome_tuple, tuple)
    assert all(isinstance(i, int) for i in new_awesome_tuple)
    assert new_awesome_tuple == (3, 8, 5, 6, 7)
