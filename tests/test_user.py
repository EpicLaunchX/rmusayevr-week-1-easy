from src.pytemplate.domain.user import age


def test_age():
    assert isinstance(age, int)
    assert age == 32
