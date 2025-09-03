# any pytest file should start with test_  or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# every method is treated as different testcase
# (py.test -v -s)---- run all files
# (py.test test_demo2.py -v -s) run selected files
# @pytest.mark.xfail--- testcase run but does not give any status
import pytest


def test_firstGreet():

    message = "Hello"
    assert message == "Hi", "Test failed cause strings do not match"


@pytest.mark.xfail
def test_secondProgramCreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")





