import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тест
# тест 
# 123
# 04 апреля 2023

def test_string_utils_capitilize_positive():
    string_utils = StringUtils()
    var1 = string_utils.capitilize('Тест')
    assert var1 == 'Тест'

def test_string_utils_capitilize_and_positive():
    string_utils = StringUtils()
    var1 = string_utils.capitilize('тест')
    assert var1 == 'Тест'

def test_string_utils_capitilize_num_positive():
    string_utils = StringUtils()
    var1 = string_utils.capitilize('123')
    assert var1 == '123'

def test_string_utils_capitilize_date_positive():
    string_utils = StringUtils()
    var1 = string_utils.capitilize('04 апреля 2023')
    assert var1 == '04 апреля 2023'

# Пустая
# " "
# None

def test_string_utils_capitilize_negative():
    string_utils = StringUtils()
    with pytest.raises(AssertionError):
        var1 = string_utils.capitilize('')
        assert var1 == None

def test_string_utils_capitilize_space_negative():
    string_utils = StringUtils()
    with pytest.raises(AssertionError):
        var1 = string_utils.capitilize(' ')
        assert var1 == None

def test_string_utils_capitilize_empty_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        var1 = string_utils.capitilize(None)
        assert var1 == None