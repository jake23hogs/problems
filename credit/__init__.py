import check50



@check50.check()
def exists():
    """Credit exists."""
    check50.exists("Credit.java")
    
@check50.check(exists)
def compiles():
    """Credit compiles."""
    check50.run("javac Credit.java").exit(0)
  

@check50.check(compiles)
def test1():
    """identifies 378282246310005 as AMEX"""
    check50.run("java Credit").stdin("378282246310005").stdout("^AMEX\n", "AMEX\n").exit(0)

@check50.check(compiles)
def test2():
    """identifies 371449635398431 as AMEX"""
    check50.run("java Credit").stdin("371449635398431").stdout("^AMEX\n", "AMEX\n").exit(0)

@check50.check(compiles)
def test3():
    """identifies 5555555555554444 as MASTERCARD"""
    check50.run("java Credit").stdin("5555555555554444").stdout("^MASTERCARD\n", "MASTERCARD\n").exit(0)

@check50.check(compiles)
def test4():
    """identifies 5105105105105100 as MASTERCARD"""
    check50.run("java Credit").stdin("5105105105105100").stdout("^MASTERCARD\n", "MASTERCARD\n").exit(0)

@check50.check(compiles)
def test5():
    """identifies 4111111111111111 as VISA"""
    check50.run("java Credit").stdin("4111111111111111").stdout("^VISA\n", "VISA\n").exit(0)

@check50.check(compiles)
def test6():
    """identifies 4012888888881881 as VISA"""
    check50.run("java Credit").stdin("4012888888881881").stdout("^VISA\n", "VISA\n").exit(0)

@check50.check(compiles)
def test7():
    """identifies 1234567890 as INVALID"""
    check50.run("java Credit").stdin("1234567890").stdout("^INVALID\n", "INVALID\n").exit(0)

@check50.check(compiles)
def test8():
    """identifies 369421438430814 as INVALID"""
    check50.run("java Credit").stdin("369421438430814").stdout("^INVALID\n", "INVALID\n").exit(0)

@check50.check(compiles)
def test9():
    """identifies 4062901840 as INVALID"""
    check50.run("java Credit").stdin("4062901840").stdout("^INVALID\n", "INVALID\n").exit(0)

@check50.check(compiles)
def test10():
    """identifies 5673598276138003 as INVALID"""
    check50.run("java Credit").stdin("5673598276138003").stdout("^INVALID\n", "INVALID\n").exit(0)

@check50.check(compiles)
def test11():
    """identifies 4111111111111113 as INVALID"""
    check50.run("java Credit").stdin("4111111111111113").stdout("^INVALID\n", "INVALID\n").exit(0)

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("java Credit").stdin("").reject()
