import pytest


@pytest.fixture()
def set_up():
    print("Enter system")
    yield
    print("Exit system")
