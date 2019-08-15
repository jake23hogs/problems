import check50

@check50.check()
def exists():
    """Hello.java exists."""
    check50.exists("Hello.java")

@check("exists")
    def compiles(self):
        """Hello compiles"""
        self.spawn("javac Hello.java").exit(0)

@check50.check(compiles)
def Case1():
    """Outputs correctly Hello, World!\n."""
    self.spawn("java Hello").stdout("Hello, World!\n").exit()

