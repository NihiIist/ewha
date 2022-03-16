"""
Test code
"""
import pytest
from main import total


def test_total_success():
    """
    total 함수 정상 동작 테스트
    """
    assert total(2, 3) == 5

def test_total_invalid_parameter_exception():
    """
    total 함수 숫자가 아닌 인자 exception 발생 테스트
    """
    with pytest.raises(TypeError):
        total(3, 'H')
