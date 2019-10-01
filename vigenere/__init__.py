import check50

@check50.check()
def exists(self):
    """Vigenere.java exists."""
    check50.exists("Vigenere.java")

@check50.check(exists)
def compiles():
    """Vigenere.java compiles."""
    check50.run("javac Vigenere.java")
    
@check50.check(compiles)
def aa(self):
    """encrypts "a" as "a" using "a" as keyword"""
    check50.run("java Vigenere a").stdin("a").stdout("ciphertext:\s*a\n", "ciphertext: a\n").exit(0)

@check50.check(compiles)
def bazbarfoo_caqgon(self):
    """encrypts "barfoo" as "caqgon" using "baz" as keyword"""
    check50.run("java Vigenere baz").stdin("barfoo").stdout("ciphertext:\s*caqgon\n", "ciphertext: caqgon\n").exit(0)

@check50.check(compiles)
def mixedBaZBARFOO(self):
    """encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword"""
    check50.run("java Vigenere BaZ").stdin("BaRFoo").stdout("ciphertext:\s*CaQGon\n", "ciphertext: CaQGon\n").exit(0)

@check50.check(compiles)
def allcapsBAZBARFOO(self):
    """encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword"""
    check50.run("java Vigenere BAZ").stdin("BARFOO").stdout("ciphertext:\s*CAQGON\n", "ciphertext: CAQGON\n").exit(0)

@check50.check(compiles)
def bazworld(self):
    """encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword"""
    check50.run("java Vigenere baz").stdin("world!$?").stdout("ciphertext:\s*xoqmd!\$\?\n", "ciphertext: xoqmd!$?\n").exit(0)

@check50.check(compiles)
def withspaces(self):
    """encrypts "Hello, World!" as "Iekmo, Vprke!" using "baz" as keyword"""
    check50.run("java Vigenere baz").stdin("Hello, World!").stdout("ciphertext:\s*Iekmo, Vprke!\n", "ciphertext: Iekmo, Vprke!\n").exit(0)
    
@check50.check(compiles)
def noarg(self):
    """handles lack of argv[1]"""
    check50.run("java Vigenere").exit(0)

@check50.check(compiles)
def toomanyargs(self):
    """handles argc > 2"""
    check50.run("java Vigenere 1 2 3").exit(0)

@check50.check(compiles)
def reject(self):
    """rejects "Hax0r2" as keyword"""
    check50.run("java Vigenere Hax0r2").exit(0)
