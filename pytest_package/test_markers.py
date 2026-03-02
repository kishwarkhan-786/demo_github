import pytest
@pytest.mark.parametrize("a,b",[(10,20)])
def test_add(a,b):
    print(a+b)