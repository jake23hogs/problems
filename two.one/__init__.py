import check50
import re

@check50.check()
def exists():
    """Fahrenheit.java exists"""
    check50.exists("Fahrenheit.java")


@check50.check(exists)
def test37():
    """37 degrees Celsius yields 98.6 degrees Fahrenheit"""
    check50.run("java Fahrenheit.java").stdin("37").stdout(number(98.6), "98.6\n").exit(0)

@check50.check(exists)
def test0(self):
    """0 degrees Celsius yields 32.0 degrees Fahrenheit"""
    self.spawn("java Fahrenheit").stdin("0").stdout(number(32.0), "32.0\n").exit(0)

@check50.check(exists)
def test100(self):
    """100.00 degrees Celsius yields 212.0 degrees Fahrenheit"""
    self.spawn("java Fahrenheit").stdin("100.00").stdout(number(212.0), "212.0\n").exit(0)

@check50.check(exists)
def testneg40(self):
    """-40 degrees Celsius yields -40.0 degrees Fahrenheit"""
    self.spawn("java Fahrenheit").stdin("-40").stdout(number(-40.0), "-40.0\n").exit(0)

@check50.check(exists)
def test18point5(self):
    """18.5 degrees Celsius yields 65.3 degrees Fahrenheit"""
    self.spawn("java Fahrenheit").stdin("18.5").stdout(number(65.3), "65.3\n").exit(0)

@check50.check(exists)
def testneg123point45678(self):
    """-123.45678 degrees Celsius yields -190.222204 degrees Fahrenheit"""
    self.spawn("java Fahrenheit").stdin("-123.45678").stdout(number(-190.222204), "-190.222204\n").exit(0)

@check50.check(exists)
def test_reject_empty_string(self):
    """rejects a non-numeric input of "" """
    self.spawn("java Fahrenheit").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
