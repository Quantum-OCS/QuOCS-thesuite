import Functions
import pytest

### This file has to have the name test_ followed by the python file one wants to test

### Read: https://docs.pytest.org/en/latest/explanation/goodpractices.html

def test_square():
    """
    
    """
    print("Test square function")
    assert Functions.square(0) == 0
    assert Functions.square(0.0) == 0.0
    assert Functions.square(2) == 4
    assert Functions.square(2.0) == 4.0
    assert Functions.square(-3.0) == 9.0

def test_divide():
    """
    Test the divide function and also check if the error is raised correctly
    """
    print("Test divide function")
    assert Functions.divide(20, 5) == 4
    assert Functions.divide(-20, 5) == -4
    assert Functions.divide(20, -5) == -4
    assert Functions.divide(-20, -5) == 4
    assert Functions.divide(0, 5) == 0

    # version for checking raise of ValueError
    with pytest.raises(ValueError):
        Functions.divide(10, 0)

test_divide()