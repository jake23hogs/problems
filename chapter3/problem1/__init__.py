import check50
import re

@check50.check()
def exists():
    """Project3_1.java exists"""
    check50.exists("Project3_1.java")

@check50.check(exists)
def test2():
    """2 yields a surface area of 24 """
    check50.run("java Project3_1").stdin("2").stdout("^Surface Area = 24\n", "Surface Area = 24\n").exit(0)

@check50.check(exists)
def test0():
    """0 yields a surface area of 0"""
    check50.run("java Project3_1").stdin("0").stdout("^Surface Area = 0\n", "Surface Area = 0\n").exit(0)

@check50.check(exists)
def test_reject_empty_string():
    """rejects a non-numeric input of "" """
    check50.run("java Project3_1").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
