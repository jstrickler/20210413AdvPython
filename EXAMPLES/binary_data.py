#!/usr/bin/env python
from collections import namedtuple
from struct import Struct

values = 23903, -3903, 999.99, b'Guido' # <1>

demo = Struct('iid10s')  # <2>

print("Size of data: {} bytes".format(demo.size)) # <3>

binary_stream = demo.pack(*values) # <4>
print("raw binary data:", binary_stream)

MyInfo = namedtuple("MyInfo", "int1 int2 float1 raw_string")

int1, int2, float1, raw_bytes = demo.unpack(binary_stream) # <5>
str1 = raw_bytes.decode().rstrip('\x00')  # <6>

data = MyInfo(*demo.unpack(binary_stream))
print("named tuple!", data.int1, data.int2)

print(raw_bytes)
print(int1, int2, float1, str1)


"""
/* iid10s */
struct foo {
        int a;
        int b;
        double c;
        char d[10];
}
"""
