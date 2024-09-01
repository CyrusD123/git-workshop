from dataframe import Series
import pytest

def test_series_sum():
    series1 = Series(data=[1, 2], name="A")
    assert series1.sum() == 3



# TODO: ALL - Implement tests for all other Series methods
# Use the test_series_sum test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html
    
    
def test_series_min():
    series1 = Series(data=[1, 2, 5, 0], name="B")
    assert series1.sum() == 0


def test_series_mode():
    series1 = Series(data=[1, 2, 5, 0], name="A")
    assert series1.mode() == 1
    
    series2 = Series(data=[1, 2, 5, 5, 0], name="B")
    assert series2.mode() == 5
    series3 = Series(data=[1, 2, 2, 3, 3, 3, 2], name="C")
    assert series3.mode() == 2
    series4 = Series(data=[1, 1, 1, 3, 4], name="D")
    assert series4.mode() == 4


def test_series_contains():
    series1 = Series(data=[1, 2, 5, 0], name="A")
    assert series1.contains(1) == True
    
    series2 = Series(data=[1, 2, 5, 5, 0], name="B")
    assert series2.contains(5) == True
    series3 = Series(data=[1, 2, 2, 3, 3, 3, 2], name="C")
    assert series3.contains(16) == False
    series4 = Series(data=[1, 1, 1, 3, 4], name="D")
    assert series4.contains(0) == False