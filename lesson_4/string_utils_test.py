import pytest
from string_utils import StringUtils

# Тест функция №1
# pytest -m function1p -v
@pytest.mark.function1p
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

# pytest -m function1n -v
@pytest.mark.function1n
@pytest.mark.parametrize('data, result', [  
    ('', ''), 
    (' ', ' ') 
    ])
def test_string_utils_capitilize_negative(data, result):
    string_utils = StringUtils()
    var1 = string_utils.capitilize(data)
    assert var1 == result

# Тест функция №2
# pytest -m function2p -v
@pytest.mark.function2p
@pytest.mark.parametrize('data, result', [ 
    ('тест', 'тест'),
    (' Тест', 'Тест'), 
    (' тест', 'тест'), 
    (' 123', '123'), 
    (' 04 апреля 2023', '04 апреля 2023') 
    ])
def test_string_utils_trim_positive(data, result):
    string_utils = StringUtils()
    var1 = string_utils.trim(data)
    assert var1 == result

# pytest -m function2n -v
@pytest.mark.function2n
@pytest.mark.xfail(raises=AttributeError)
@pytest.mark.parametrize('data, result', [  
    (1, 1)
    ])
def test_string_utils_trim_negative(data, result):
    string_utils = StringUtils()
    var1 = string_utils.trim(data)
    assert var1 == result

# Тест функция №3
# pytest -m function3p -v 
@pytest.mark.function3p
@pytest.mark.parametrize('data, deli, result', [ 
    ('Один,Два,Три', ',', ['Один', 'Два', 'Три']), 
    ('Один:Два:Три', ':', ['Один', 'Два', 'Три']),
    ('Один/Два/Три', '/', ['Один', 'Два', 'Три']),
    ('Один Два Три', ' ', ['Один', 'Два', 'Три'])
    ])
def test_string_utils_to_list_positive(data, deli, result):
    string_utils = StringUtils()
    var1 = string_utils.to_list(data, deli)
    assert var1 == result

#pytest -m function3n -v
@pytest.mark.function3n
@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize('data, deli, result', [ 
    ('Один,Два,Три', '', ['Один', 'Два', 'Три'])
    ])
def test_string_utils_to_list_negative(data, deli, result):
    string_utils = StringUtils()
    var1 = string_utils.to_list(data, deli)
    assert var1 == result

# Тест функция №4
# pytest -m function4p -v
@pytest.mark.function4p
@pytest.mark.parametrize('data, simbol, total', [ 
    ('MyTest', 'T', True),
    ('MyTest', 'y', True),
    ('MyTest', 'A', False),
    ('MyTest', 'k', False)
    ])
def test_string_utils_contains_positive(data, simbol, total):
    string_utils = StringUtils()
    var1 = string_utils.contains(data, simbol)
    assert var1 == total

# pytest -m function4n -v
@pytest.mark.function4n
@pytest.mark.parametrize('data, simbol, total', [ 
    ('MyTest', ' ', True),
    ('MyTest', '', False),
    ('MyTest', 'Ш', True)
    ])
def test_string_utils_contains_negative(data, simbol, total):
    string_utils = StringUtils()
    var1 = string_utils.contains(data, simbol)
    assert var1 != total

# Тест функция №5
# pytest -m function5p -v
@pytest.mark.function5p
@pytest.mark.parametrize('data, del_data, result', [ 
    ('SkyPro', 'k', 'SyPro'), 
    ('SkyPro', 'yPr', 'Sko'),
    ('SkyPro', 'S', 'kyPro'),
    ('SkyPro', 'o', 'SkyPr'),
    ('SkyPro', 'SkyPro', ''),
    ('Sky Pro', ' ', 'SkyPro')
    ])
def test_string_utils_delete_symbol_positive(data, del_data, result):
    string_utils = StringUtils()
    var1 = string_utils.delete_symbol(data, del_data)
    assert var1 == result

# pytest -m function5n -v
@pytest.mark.function5n
@pytest.mark.parametrize('data, del_data, result', [ 
    ('SkyPro', ' ', 'SkyPro'), 
    ('SkyPro', 'SP', 'SkyPro'),
    ('SkyPro', '4', 'SkyPro'),
    ('SkyPro', 'ш', 'SkyPro')
    ])
def test_string_utils_delete_symbol_negative(data, del_data, result):
    string_utils = StringUtils()
    var1 = string_utils.delete_symbol(data, del_data)
    assert var1 == result

# Тест функция №6
# pytest -m function6p -v
@pytest.mark.function6p
@pytest.mark.parametrize('data, search_data, result', [ 
    ('SkyPro', 'S', True),
    ('Cat', 'C', True),
    ('Dog', 'D', True),
    ('SkyPro', 'P', False),
    ('Cat', 'D', False),
    ])
def test_string_utils_starts_with_positive(data, search_data, result):
    string_utils = StringUtils()
    var1 = string_utils.starts_with(data, search_data)
    assert var1 == result

# pytest -m function6n -v
@pytest.mark.function6n
@pytest.mark.parametrize('data, search_data, result', [ 
    ('Cat', ' ', True),
    ('Cat', '1', True)
    ])
def test_string_utils_starts_with_negative(data, search_data, result):
    string_utils = StringUtils()
    var1 = string_utils.starts_with(data, search_data)
    assert var1 != result

# Тест функция №7
# pytest -m function7p -v
@pytest.mark.function7p
@pytest.mark.parametrize('data, search_data, result', [ 
    ('SkyPro', 'o', True),
    ('Cat', 't', True),
    ('123', '3', True),
    ('SkyPro', 'P', False),
    ('Cat', 'D', False),
    ])
def test_string_utils_end_with_positive(data, search_data, result):
    string_utils = StringUtils()
    var1 = string_utils.end_with(data, search_data)
    assert var1 == result

# pytest -m function7n -v  
@pytest.mark.function7n
@pytest.mark.parametrize('data, search_data, result', [ 
    ('Cat', ' ', True),
    ('Cat', '1', True),
    ('Cat', 'T', True)
    ])
def test_string_utils_end_with_negative(data, search_data, result):
    string_utils = StringUtils()
    var1 = string_utils.end_with(data, search_data)
    assert var1 != result 

# Тест функция №8
# pytest -m function8p -v
@pytest.mark.function8p
@pytest.mark.parametrize('data, result', [ 
    ('', True),
    (' ', True),
    ('ф', False),
    ('F', False),
    ('0', False)
    ])
def test_string_utils_is_empty_positive(data, result):
    string_utils = StringUtils()
    var1 = string_utils.is_empty(data)
    assert var1 == result

# pytest -m function8n -v
@pytest.mark.function8n
@pytest.mark.parametrize('data, result', [ 
    ('a b', True),
    (' b', True),
    ('a ', True)
    ])
def test_string_utils_is_empty_negative(data, result):
    string_utils = StringUtils()
    var1 = string_utils.is_empty(data)
    assert var1 != result 

# Тест функция №9
# pytest -m function9p -v
@pytest.mark.function9p
@pytest.mark.parametrize('data, deli, result', [ 
    (['Один', 'Два', 'Три'], ', ', 'Один, Два, Три'), 
    ([1,2,3,4], ': ', '1: 2: 3: 4'),
    (['Sky','Pro'], '-', 'Sky-Pro'),
    ([], ', ', ''),
    ([1,2,3,4], ' ', '1 2 3 4')
    ])
def test_string_utils_list_to_string_positive(data, deli, result):
    string_utils = StringUtils()
    var1 = string_utils.list_to_string(data, deli)
    assert var1 == result

# pytest -m function9n -v
@pytest.mark.function9n
@pytest.mark.parametrize('data, deli, result', [ 
    ([1,2,3,4], '', 1234)
    ])
def test_string_utils_list_to_string_negative(data, deli, result):
    string_utils = StringUtils()
    var1 = string_utils.list_to_string(data, deli)
    assert var1 != result