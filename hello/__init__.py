from check50 import *


class Hello(Checks):
    
    @check()
    def exists():
        """Hello.java exists."""
        self.require("Hello.java")

    @check("exists")
    def compiles(self):
        """Hello compiles"""
        self.spawn("javac Hello.java").exit(0)

    @check50.check("compiles")
    def Case1():
        """Outputs correctly Hello, World!\n."""
        self.spawn("java Hello").stdout("Hello, World!\n", "Hello, World!\n").exit(0)

