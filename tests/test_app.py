import pytest
from app import main_conversion_function

def test_kg_to_grams():
    assert main_conversion_function(1, 'kg', 'grams') == 1000

def test_grams_to_kg():
    assert main_conversion_function(1000, 'grams', 'kg') == 1

def test_kg_to_pounds():
    assert main_conversion_function(1, 'kg', 'pounds') == 2.20462

def test_pounds_to_kg_FAIL_CASE():
    """
    This test is designed to catch the intentional bug in app.py.
    It expects a positive 1.0, but will receive -1.0.
    """
    result = main_conversion_function(2.20462, 'pounds', 'kg')
    assert round(result, 1) == 1.0

def test_invalid_unit():
    assert main_conversion_function(10, 'kg', 'invalid') == "Invalid conversion"