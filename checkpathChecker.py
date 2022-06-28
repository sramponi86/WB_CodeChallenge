import pytest
from pathChecker import pathChecker

def checkpathChecker( value, expectedRetVal ):
    retVal = pathChecker(value)
    assert retVal == expectedRetVal

def test_returnsFalseWithWrongPath():
    checkpathChecker(":/", False)

def test_returnsFalseWithEmptyPath():
    checkpathChecker("",False)

def test_returnsTrueWithMainPath():
    checkpathChecker("C:/Program Files/Google/Chrome/Application",True)

def test_returnsFalseWithGenericCorrectPath():
    checkpathChecker("C:/",False)

def test_returnsFalseWithImpossiblePath():
    checkpathChecker("2",False)

def test_returnsExceptionWithNumericPath():
    with pytest.raises(Exception) as e_info:
        checkpathChecker(2,False)
    assert e_info.value.args[0] == "chdir: path should be string, bytes or os.PathLike, not int"


