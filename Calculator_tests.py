import pytest
from Calculator_app import *

def test_add_over_10():
    add(1,1,1,1,1,1,1,1,1,1,1,1,1)
    assert "Input has more than 10 values"

def test_add():
    add(1,5)
    assert  6
