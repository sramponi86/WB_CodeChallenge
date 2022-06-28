import pytest
from coinFlip import coinFlip

def checkcoinFlip( value, expectedRetVal ):
    retVal = coinFlip(value)
    assert retVal == expectedRetVal

def test_returnsFalseWithSingleFlip():
    checkcoinFlip([1], False)

def test_returnsZeroWithInterspersedShortList():
    checkcoinFlip([0,1],0)

def test_returnsZeroWithInterspersedShortListInv():
    checkcoinFlip([1,0],0)

def test_returnsOneWithShortList():
    checkcoinFlip([1,1],1)

def test_returnsOneWithShortListInv():
    checkcoinFlip([0,0],1)

def test_returnsZeroWithInterspersedLongList():
    checkcoinFlip([0,1,0,1,0,1],0)

def test_returnsOneWithInterspersedLongList():
    checkcoinFlip([0,1,0,1,0,1,1],1)

def test_returnsExceptionWithInteger():
    with pytest.raises(Exception) as e_info:
        checkcoinFlip(1,False)
    assert e_info.value.args[0] == "object of type 'int' has no len()"

def test_returnsFalseWithString():
    checkcoinFlip("Test",False) #to be checked

def test_returnsFalseWithStringInList():
    checkcoinFlip([0,1,0,1,"Test"],False)

def test_returnsZeroWithNegativeValues():
    checkcoinFlip([0,-1,0,-1,0,-1],0)

def test_returnsFourWithLongFlip():
    checkcoinFlip([0,1,1,1,1,1,1,1,1],4)

def test_returnsFalseWithEmptyArray():
    checkcoinFlip([],False)

def test_returnsFalseWithGenericArray():
    checkcoinFlip([1,2,3,4,5,6,7,7],False)
