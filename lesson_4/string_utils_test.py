import pytest
from string_utils import StringUtils

# Тест функция №1
@pytest.mark.function1
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

# Тест функция №2
@pytest.mark.function2
@pytest.mark.parametrize('data, result', [ 
    (' Тест', 'Тест'), 
    (' тест', 'тест'), 
    (' 123', '123'), 
    (' 04 апреля 2023', '04 апреля 2023') 
    ])
def test_string_utils_trim_positive(data, result):
    string_utils = StringUtils()
    var1 = string_utils.trim(data)
    assert var1 == result

@pytest.mark.parametrize('data, result', [  
    ('', ''),
    ('тест', 'тест') 
    ])
def test_string_utils_trim_negative(data, result):
    string_utils = StringUtils()
    var1 = string_utils.trim(data)
    assert var1 == result

# Тест функция №3
# pytest -m function3
@pytest.mark.function3
@pytest.mark.parametrize('data, result', [ 
    ('Один,Два,Три', ['Один', 'Два', 'Три']), 
#    ('Один:Два:Три', ['Один', 'Два', 'Три']),  
    ])
def test_string_utils_to_list_positive(data, result):
    string_utils = StringUtils()
    var1 = string_utils.to_list(data)
    assert var1 == result
