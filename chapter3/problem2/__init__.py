import check50
import re

@check50.check()
def exists():
    """Project3_2.java exists"""
    check50.exists("Project3_2.java")

@check50.check(exists)
def test2():
    """2 yields Diameter of , Circumference of , Surface Area of  and Volume of """
    check50.run("java Project3_2").stdin("2").stdout("Diameter = \nCircumference = \nSurface Area = \nVolume = \n", "Diameter = \nCircumference = \nSurface Area = \nVolume = \n").exit(0)

@check50.check(exists)
def test0():
    """0 yields a surface area of 0"""
    check50.run("java Project3_2").stdin("0").stdout(number(0), "0\n").exit(0)

@check50.check(exists)
def test_reject_empty_string():
    """rejects a non-numeric input of "" """
    check50.run("java Project3_1").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
