# any pytest file should start with test_  or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# every method is treated as different testcase
# (py.test -v -s) all testcases run at a time at CMD
# (py.test -k Creditcard -v -s) --run testcase with selected test
# -k stands for method names execution,  -s logs in output,  -v stands for more info metadata
# you can run specific file with py.test <filename>
#C:\Users\Khan Gadget\PycharmProjects\PythonTesting\pytestsDemo
# (you can mark(tag) tests @pytest.mark.smoke and then run with -m) example: py.test -v -s
#  you can skip test with @pytest.mark.skip
import pytest


@pytest.mark.smoke  #for marking

@pytest.mark.skip

def test_firstProgram():
    print("Hello")


def test_secondGreetCreditcard():
    print("Good morning")

