from src.pytemplate.domain.user import age, height, ID, name, surname


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
