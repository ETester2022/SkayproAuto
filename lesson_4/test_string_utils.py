import pytest
from string_utils import StringUtils

# Тест
# тест 
# 123
# 04 апреля 2023
# Пустая
# " "
# None

@pytest.mark.parametrize('data, result', [ 
    ('Тест', 'Тест'), 
    ('тест', 'Тест'), 
    ('123', '123'), 
    ('04 апреля 2023', '04 апреля 2023') 
    ])
def test_string_utils_capitilize_positive(data, result):
    string_utils = StringUtils()
    var1 = string_utils.capitilize(data)
    assert var1 == result

@pytest.mark.parametrize('data, result', [  
    ('', ''), 
    (' ', ' ') 
    ])
def test_string_utils_capitilize_negative(data, result):
    string_utils = StringUtils()
    var1 = string_utils.capitilize(data)
    assert var1 == result