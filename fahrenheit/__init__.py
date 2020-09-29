import check50


@check50.check()
def exists():
    """Fahrenheit exists."""
    check50.exists("Fahrenheit.java")

    
@check50.check(exists)
def compiles():
    """Fahrenheit compiles."""
    check50.run("javac Fahrenheit.java")

    
@check50.check(compiles)
def correctConversion():
    """converts 0 C to 32 F"""
    check50.run("java Fahrenheit").stdin(0).stdout(32.0, 32.0).exit(0)

