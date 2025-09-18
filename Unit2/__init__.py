import check50


@check50.check()
def exists1():
    """Program1 exists"""
    check50.exists("Program1.java")


@check50.check(exists1)
def compiles1():
    """Program1 compiles"""
    check50.run("javac Program1.java")

@check50.check()
def exists2():
    """Program2 exists"""
    check50.exists("Program2.java")


@check50.check(exists2)
def compiles2():
    """Program2 compiles"""
    check50.run("javac Program2.java")
    
@check50.check()
def exists3():
    """Program3 exists"""
    check50.exists("Program3.java")


@check50.check(exists3)
def compiles3():
    """Program3 compiles"""
    check50.run("javac Program3.java")


@check50.check()
def exists4():
    """Program4 exists"""
    check50.exists("Program4.java")


@check50.check(exists4)
def compiles4():
    """Program4 compiles"""
    check50.run("javac Program4.java")
    
@check50.check()
def exists5():
    """Program5 exists"""
    check50.exists("Program5.java")


@check50.check(exists5)
def compiles5():
    """Program5 compiles"""
    check50.run("javac Program5.java")


@check50.check()
def exists6():
    """Program6 exists"""
    check50.exists("Program6.java")


@check50.check(exists6)
def compiles6():
    """Program6 compiles"""
    check50.run("javac Program6.java")

@check50.check()
def exists7():
    """Program7 exists"""
    check50.exists("Program7.java")


@check50.check(exists7)
def compiles7():
    """Program7 compiles"""
    check50.run("javac Program7.java")


@check50.check()
def exists8():
    """Program8 exists"""
    check50.exists("Program8.java")


@check50.check(exists8)
def compiles8():
    """Program8 compiles"""
    check50.run("javac Program8.java")
    
@check50.check()
def exists9():
    """Program9 exists"""
    check50.exists("Program9.java")


@check50.check(exists9)
def compiles9():
    """Program9 compiles"""
    check50.run("javac Program9.java")

@check50.check()
def exists10():
    """Program10 exists"""
    check50.exists("Program10.java")


@check50.check(exists10)
def compiles10():
    """Program10 compiles"""
    check50.run("javac Program10.java")


@check50.check()
def exists11():
    """Program11 exists"""
    check50.exists("Program11.java")


@check50.check(exists11)
def compiles11():
    """Program11 compiles"""
    check50.run("javac Program11.java")
    
@check50.check()
def exists12():
    """Program12 exists"""
    check50.exists("Program12.java")


@check50.check(exists12)
def compiles12():
    """Program12 compiles"""
    check50.run("javac Program12.java")

@check50.check()
def exists13():
    """Program13 exists"""
    check50.exists("Program13.java")


@check50.check(exists13)
def compiles13():
    """Program13 compiles"""
    check50.run("javac Program13.java")


@check50.check()
def exists14():
    """Program14 exists"""
    check50.exists("Program14.java")


@check50.check(exists14)
def compiles14():
    """Program14 compiles"""
    check50.run("javac Program14.java")
