import pytest
from findFirstRepeatedN import findFirstRepeatedN

def checkfindFirstRepeatedN( listOne, listTwo, expectedRetVal ):
    retVal = findFirstRepeatedN(listOne, listTwo)
    assert retVal == expectedRetVal

def test_returns1with1asRepeatedEqualSingleLists():
    checkfindFirstRepeatedN([1], [1], 1)

def test_returnsNonewithNoCommonElement():
    checkfindFirstRepeatedN([1],[2], 0)

def test_returnsCommonElementEqualSizeList():
    checkfindFirstRepeatedN([1,2], [0,1], 1)

def test_returnsZeroAsnoCommonElement():
    checkfindFirstRepeatedN([1,2], [3,4], 0)

def test_returnsCommonElementDifferentSizeList():
    checkfindFirstRepeatedN([1,2,3],[0,0,4,5,8,10,3],3)

def test_returnsCommonElementWithString():
    #with pytest.raises(Exception) as e_info:
        checkfindFirstRepeatedN([1,2,3], [4,5,0,"Test",3],3)
    #assert e_info.value.args[0] == "'<' not supported between instances of 'str' and 'int'"

def test_returnsCommonElementWithNegatives():
    checkfindFirstRepeatedN([-1,1,2], [6,2,1],1)

def test_returnsNoElementWithFullString():
    checkfindFirstRepeatedN([1,2], ["Pear", "Apple", "1"],0)

def test_returnsNoElementWithEmptyArray():
    checkfindFirstRepeatedN([1,2], [], 0)

def test_returnsExceptionWithInteger():
    with pytest.raises(Exception) as e_info:
        checkfindFirstRepeatedN(1, [1,2], 0)
    assert e_info.value.args[0] == "'int' object is not iterable"

def test_returnsCommonNegativeElements():
    checkfindFirstRepeatedN([-1,-2], [0,-2], -2)

def test_returnsCommonFloatElement():
    checkfindFirstRepeatedN([1.0, 3.0], [1,2,10,3.0,-1], 1)

def test_returnsFirstWithMultipleCommonElements():
    checkfindFirstRepeatedN([1,1,2,2], [4,5,6,2,2,8,1,10,"Orange",1],1)


