import pytest
from string_utils import StringUtils

# Тест
# тест 
# 123
# 04 апреля 2023
# Пустая
# " "
# None

pytest.mark.parametrize('data, result', [ ('Тест', 'Тест'), ('тест', 'Тест'), ('123', '123'), ('04 апреля 2023', '04 апреля 2023'), ('', ''), (' ', ' ') ])
def test_string_utils_capitilize_positive(data, result):
    string_utils = StringUtils()
    var1 = string_utils.capitilize(data)
    assert var1 == result

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


def test_string_utils_capitilize_negative():
    string_utils = StringUtils()
#    with pytest.raises(AssertionError):
    var1 = string_utils.capitilize('')
    assert var1 == ''

def test_string_utils_capitilize_space_negative():
    string_utils = StringUtils()
#    with pytest.raises(AssertionError):
    var1 = string_utils.capitilize(' ')
    assert var1 == ' '

def test_string_utils_capitilize_empty_negative():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        var1 = string_utils.capitilize(None)
        assert var1 == None