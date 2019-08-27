import check50
import re

@check50.check()
def exists():
    """Mario.java exists."""
    check50.exists("Mario.java")
    check50.include("1.txt", "2.txt", "23.txt")
@check50.check(exists)
def compiles():
    """Mario.java Compiles"""
    check50.run("javac Mario.java")
    
@check50.check(exists)
def test_reject_negative():
    """rejects a height of -1"""
    check50.run("java Mario").stdin("-1").reject()

@check50.check(exists)
def test0():
    """rejects a height of 0"""
    check50.run("java Mario").stdin("0").exit(0)

@check50.check(exists)
def test1():
    """handles a height of 1 correctly"""
    out = check50.run("java Mario").stdin("1").stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(exists)
def test2():
    """handles a height of 2 correctly"""
    out = check50.run("java Mario").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(exists)
def test23():
    """handles a height of 23 correctly"""
    out = check50.run("java Mario").stdin("23").stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(exists)
def test24():
    """rejects a height of 24, and then accepts a height of 2"""
    (check50.run("java Mario").stdin("23").reject()
            .stdin("2").stdout(open("2.txt")).exit(0))

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric height of "foo" """
    check50.run("java Mario").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric height of "" """
    check50.run("java Mario").stdin("").reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output = output.splitlines()
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "did you add too much trailing whitespace to the end of your pyramid?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)
