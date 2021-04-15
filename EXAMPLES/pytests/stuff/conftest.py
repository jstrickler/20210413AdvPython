#!/usr/bin/env python
from pytest import fixture

@fixture
def common_fixture():  # <1>
    return "DATA"

@fixture
def other_fixture():
    return list(range(10))

def pytest_runtest_setup(item):  # <2>
    print("Hello from setup,", item)
