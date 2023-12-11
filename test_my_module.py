# Fichier: test_my_module.py
from my_module import add_one

def test_add_one_positive():
    result = add_one(5)
    assert result == 6

def test_add_one_negative():
    result = add_one(-3)
    assert result == -2

def test_add_one_zero():
    result = add_one(0)
    assert result == 1
