"""Multiple function arguments exercise"""


def foo(a, b, c, *args):
    """Returns the number of odd arguments"""

    return len(args)


def bar(a, b, c, **kwargs):
    """Returns True if magicnumber of **kwargs == 7"""

    return kwargs["magicnumber"] == 7


if foo(1, 2, 3, 4) == 1:
    print("Good.")

if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")

if not bar(1, 2, 3, magicnumber=6):
    print("Great.")

if bar(1, 2, 3, magicnumber=7):
    print("Awesome!")
