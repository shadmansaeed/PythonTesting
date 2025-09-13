import pytest

from pytestsDemo.conftest_test import dataLoad


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[1])
