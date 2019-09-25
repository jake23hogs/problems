import check50


 
@check50.check()
def exists():
    """ISBN.java exists."""
    check50.exists("ISBN.java")
    
@check50.check(exists)
def compiles():
    """ISBN.java compiles."""
    check50.run("javac ISBN.java").exit(0)
    
   
@check50.check(compiles)
def Absolute_Beginners_Guide(self):
    """Beginners Guide (0789751984) valid"""
    check50.run("java ISBN").stdin("0789751984").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def Absolute_Beginners_Guide_fake(self):
    """Beginners Guide fake (0789751985) invalid"""
    check50.run("java ISBN").stdin("0789751985").stdout("^NO\n", "NO\n").exit(0)

@check50.check(compiles)
def Programming_in_C(self):
    """Programming in C (0321776410) valid"""
    check50.run("java ISBN").stdin("0321776410").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def Hackers_Delight(self):
    """Hackers Delight (0321842685) valid"""
    check50.run("java ISBN").stdin("0321842685").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def phone_number(self):
    """Jennys number (6178675309) invalid"""
    check50.run("java ISBN").stdin("6178675309").stdout("^NO\n", "NO\n").exit(0)

@check50.check(compiles)
def memory(self):
    """Mystery Test"""
    check50.run("java ISBN").stdin("1632168146").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def ISBN_with_X(self):
    """rejects ISBNs with X as checksum"""
    check50.run("java ISBN").stdin("078974984X").stdout("^Error!\n", "Error!\n").exit(0)
        
@check50.check(compiles)
def rejects_ISBNs_with_dashes(self):
    """rejects ISBNs with dashes"""
    check50.run("java ISBN").stdin("0-789-75198-4").stdout("^Error!\n", "Error!\n").exit(0)

@check50.check(compiles)
def rejects_empty(self):
    """rejects a non-numeric input of "" """
    check50.run("java ISBN").stdin("").reject()
