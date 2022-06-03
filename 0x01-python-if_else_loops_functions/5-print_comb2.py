#!/usr/bin/python3
for i in range(00, 100):
    print("{:02d}".format(i), end=", " if format(i, "02") < "99" else "\n")
