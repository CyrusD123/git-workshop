from dataframe import DataFrame, Series
import pytest

def test_df_vertical_concat():
    # Create Series for the first DataFrame
    series1_a = Series([1, 2], name="A")
    series1_b = Series([3, 4], name="B")
    df1 = DataFrame([series1_a, series1_b])
    
    # Create Series for the second DataFrame
    series2_c = Series([5, 6], name="C")
    series2_d = Series([7, 8], name="D")
    df2 = DataFrame([series2_c, series2_d])
    
    df1.concatenate_vertically(df2)
    assert df1.data == [[1, 2], [3, 4], [5, 6], [7, 8]]


# TODO: ALL - Implement tests for all other DataFrame methods
# Use the test_df_vertical_concat test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html

def test_df_head():
    # Create Series for the first DataFrame
    series1_a = Series([1, 2], name="A")
    series1_b = Series([3, 4], name="B")
    df1 = DataFrame([series1_a, series1_b])
    
    # Create Series for the second DataFrame
    series2_c = Series([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], name="C")
    series2_d = Series([5, 4, 7, 55, 9, 10, 11, 12, 13, 14, 15], name="D")
    df2 = DataFrame([series2_c, series2_d])
    
    assert df1.head().data == [[1, 2], [3, 4]]
    assert df1.head().columns == df1.columns

    assert df2.head().data == [(5, 6, 7, 8, 9), (5, 4, 7, 55, 9)]
    assert df2.head(3) == [(5, 6, 7), (5, 4, 7)]

def test_df_tail():
    # Create Series for the first DataFrame
    series1_a = Series([1, 2], name="A")
    series1_b = Series([3, 4], name="B")
    series1_c = Series([5, 6], name="C")
    series1_d = Series([7, 8], name="D")
    df1 = DataFrame([series1_a, series1_b, series1_c, series1_d])
    
    assert df1.tail(1).data == [[7, 8]]
    assert df1.tail(2).data == [[5, 6], [7, 8]]
    assert df1.tail(3).data == [[3, 4], [5, 6], [7, 8]]
    assert df1.tail(4).data == [[1, 2], [3, 4], [5, 6], [7, 8]]

def test_df_add_column():
    # Create Series for the first DataFrame
    series1_a = Series([1, 2], name="A")
    series1_b = Series([3, 4], name="B")
    series1_c = Series([5, 6], name="C")
    series1_d = Series([7, 8], name="D")
    df1 = DataFrame([series1_a, series1_b, series1_c])
    
    assert df1.add_column(series1_d).data == [[1, 2], [3, 4], [5, 6], [7, 8]]