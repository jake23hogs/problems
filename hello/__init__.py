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
def Case1():
    """Outputs correctly Hello, World!\n."""
    self.spawn("java Hello").stout("Hello, World!\n").exit()

