import check50


@check50.check()
def exists():
    """CreditCard.java exists."""
    check50.exists("CreditCard.java")
    
@check50.check(exists)
def compiles():
    """CreditCard.java.java compiles."""
    check50.run("javac CreditCard.java").exit(0)
    
   
@check50.check(compiles)
def Example(self):
    """Example Test"""
    check50.run("java CreditCard").stdin("1000").stdin("12.5").stdin("200").stdout("^\nMonth     Interest     Balance\n  1        10.42        810.42\n  2         8.44        618.86\n  3         6.45        425.30\n  4         4.43        229.74\n  5         2.39         32.13\n  6         0.33       -167.54\n\nTotal finance charges: 32.46\n", "\nMonth     Interest     Balance\n  1        10.42        810.42\n  2         8.44        618.86\n  3         6.45        425.30\n  4         4.43        229.74\n  5         2.39         32.13\n  6         0.33       -167.54\n\nTotal finance charges: 32.46\n").exit(0)



@check50.check(compiles)
def rejects_empty(self):
    """rejects a non-numeric input of "" """
    check50.run("java CreditCard").stdin("").reject()
