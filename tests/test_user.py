from src.pytemplate.domain.user import age, height, ID, last_letter, name, surname, surname_slice


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
