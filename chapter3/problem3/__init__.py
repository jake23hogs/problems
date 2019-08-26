import check50
import re

@check50.check()
def exists():
    """Project3_3.java exists"""
    check50.exists("Project3_3.java")

@check50.check(exists)
def test4():
    """A radius of 4 yields Diameter of 8.0, Circumference of 25.13272, Surface Area of 201.06176 and Volume of 268.08234666666664"""
    check50.run("java Project3_3").stdin("4").stdout("Diameter = 8.0\nCircumference = 25.13272\nSurface Area = 201.06176\nVolume = 268.08234666666664\n", "Diameter = 8.0\nCircumference = 25.13272\nSurface Area = 201.06176\nVolume = 268.08234666666664\n").exit(0)

@check50.check(exists)
def test_reject_empty_string():
    """rejects a non-numeric input of "" """
    check50.run("java Project3_3").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
