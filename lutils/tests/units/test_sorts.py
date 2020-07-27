import pytest
from lutils.algos.sorts import bubbleSort, mergeSort, quickSort, selectionSort

def test_bubbleSort():
    _arr = [4,5,3,1]
    _arr1 = [1,3,4,5]
    bubbleSort(_arr)
    assert _arr == _arr1

def test_mergeSort():
    _arr = [4,5,3,1]
    _arr1 = [1,3,4,5]
    mergeSort(_arr)
    assert _arr == _arr1

def test_quickSort():
    _arr = [4,5,3,1]
    _arr1 = [1,3,4,5]
    quickSort(arr=_arr, start=0, end=len(_arr)-1)
    assert _arr == _arr1

def test_selectionSort():
    _arr = [4,5,3,1]
    _arr1 = [1,3,4,5]
    selectionSort(_arr)
    assert _arr == _arr1