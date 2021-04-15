#!/usr/bin/env python
def test_one():  # <1>
    print("WHOOPEE")
    assert(1)

def test_two(common_fixture):   # <2>
    assert(common_fixture == "DATA")
