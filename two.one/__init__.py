import check50
import re

@check50.check()
def exists():
    """Fahrenheit.java exists"""
    check50.exists("Fahrenheit.java")

@check50.check()
def compiles():
    """Fahrenheit.java compiles"""
    check50.run("java Fahrenheit.java").exit(0)

@check50.check(exists)
def test37():
    """37 degrees Celsius yields 98.6 degrees Fahrenheit"""
    check50.run("java Fahrenheit.java").stdin("37").stdout("98.6\n").exit(0)

@check50.check(exists)
def test0():
    """0 degrees Celsius yields 32.0 degrees Fahrenheit"""
    check50.run("java Fahrenheit.java").stdin("0").stdout(number(32.0)).exit(0)

@check50.check(exists)
def test100():
    """100.00 degrees Celsius yields 212.0 degrees Fahrenheit"""
    check50.run("java Fahrenheit.java").stdin("100.00").stdout(number(212.0), "212.0\n").exit(0)

@check50.check(exists)
def testneg40():
    """-40 degrees Celsius yields -40.0 degrees Fahrenheit"""
    check50.run("java Fahrenheit.java").stdin("-40").stdout(number(-40.0), "-40.0\n").exit(0)

@check50.check(exists)
def test18point5():
    """18.5 degrees Celsius yields 65.3 degrees Fahrenheit"""
    check50.run("java Fahrenheit.java").stdin("18.5").stdout(number(65.3), "65.3\n").exit(0)

@check50.check(exists)
def testneg123point45678():
    """-123.45678 degrees Celsius yields -190.222204 degrees Fahrenheit"""
    check50.run("java Fahrenheit.java").stdin("-123.45678").stdout(number(-190.222204), "-190.222204\n").exit(0)

@check50.check(exists)
def test_reject_empty_string():
    """rejects a non-numeric input of "" """
    check50.run("java Fahrenheit.java").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
