import check50
import re

@check50.check()
def exists():
    """Project3_2.java exists"""
    check50.exists("Project3_2.java")

@check50.check(exists)
def test2():
    """2 yields a surface area of 8 """
    check50.run("java Project3_2").stdin("2").stdout(number(8), "8\n").exit(0)

@check50.check(exists)
def test0():
    """0 yields a surface area of 0"""
    check50.run("java Project3_2").stdin("0").stdout(number(0), "0\n").exit(0)

@check50.check(exists)
def test_reject_empty_string():
    """rejects a non-numeric input of "" """
    check50.run("java Project3_2").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)