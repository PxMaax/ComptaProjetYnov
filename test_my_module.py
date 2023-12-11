# Fichier: test_my_module.py
"""
Module de tests pour le module my_module.py
"""

from my_module import add_one

def test_add_one_positive():
    """
    Teste la fonction add_one avec un nombre positif.
    """
    result = add_one(5)
    assert result == 6

def test_add_one_negative():
    """
    Teste la fonction add_one avec un nombre négatif.
    """
    result = add_one(-3)
    assert result == -2

def test_add_one_zero():
    """
    Teste la fonction add_one avec le nombre zéro.
    """
    result = add_one(0)
    assert result == 1
