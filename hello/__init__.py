import check50

@check50.check()
def exists():
    """hello.java exists."""
    check50.exists("hello.java")

@check("exists")
    def compiles(self):
        """Hello compiles"""
        self.spawn("javac Hello.java").exit(0)

@check50.check(compiles)
def veronica():
    """responds to name Veronica."""
    check50.run("java Hello").stdin("Veronica").stdout("Veronica").exit()

@check50.check(compiles)
def brian():
    """responds to name Brian."""
    check50.run("java Hello").stdin("Brian").stdout("Brian").exit()
