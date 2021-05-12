"""Variables and types exercise"""

# change this code
MYSTRING = "hello"
MYFLOAT = 10.0
MYINT = 20

# testing code
if MYSTRING == "hello":
    print("String: %s" % MYSTRING)
if isinstance(MYFLOAT, float) and MYFLOAT == 10.0:
    print("Float: %f" % MYFLOAT)
if isinstance(MYINT, int) and MYINT == 20:
    print("Integer: %d" % MYINT)
