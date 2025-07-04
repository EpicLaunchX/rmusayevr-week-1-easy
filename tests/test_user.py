from src.pytemplate.domain.user import age, height


def test_age():
    assert isinstance(age, int)
    assert age == 32


def test_height():
    assert isinstance(height, float)
    assert height == 1.85
