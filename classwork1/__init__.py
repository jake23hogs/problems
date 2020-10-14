import check50


@check50.check()
def exists1():
    """program1 exists"""
    check50.exists("program1.c")


@check50.check(exists1)
def compiles1():
    """program1 compiles"""
    check50.run("make program1")

@check50.check()
def exists2():
    """program2 exists"""
    check50.exists("program2.c")


@check50.check(exists2)
def compiles2():
    """program2 compiles"""
    check50.run("make program2")
    
@check50.check()
def exists3():
    """program3 exists"""
    check50.exists("program3.c")


@check50.check(exists3)
def compiles3():
    """program3 compiles"""
    check50.run("make program3")


@check50.check()
def exists4():
    """program4 exists"""
    check50.exists("program4.c")


@check50.check(exists4)
def compiles4():
    """program4 compiles"""
    check50.run("make program4")
    
@check50.check()
def exists5():
    """program5 exists"""
    check50.exists("program5.c")


@check50.check(exists5)
def compiles5():
    """program5 compiles"""
    check50.run("make program5")


@check50.check()
def exists6():
    """program6 exists"""
    check50.exists("program6.c")


@check50.check(exists6)
def compiles6():
    """program6 compiles"""
    check50.run("make program6")

@check50.check()
def exists7():
    """program7 exists"""
    check50.exists("program7.c")


@check50.check(exists7)
def compiles7():
    """program7 compiles"""
    check50.run("make program7")


@check50.check()
def exists8():
    """program8 exists"""
    check50.exists("program8.c")


@check50.check(exists8)
def compiles8():
    """program8 compiles"""
    check50.run("make program8")
    
@check50.check()
def exists9():
    """program9 exists"""
    check50.exists("program9.c")


@check50.check(exists9)
def compiles9():
    """program9 compiles"""
    check50.run("make program9")

@check50.check()
def exists10():
    """program10 exists"""
    check50.exists("program10.c")


@check50.check(exists10)
def compiles10():
    """program10 compiles"""
    check50.run("make program10")


@check50.check()
def exists11():
    """program11 exists"""
    check50.exists("program11.c")


@check50.check(exists11)
def compiles11():
    """program11 compiles"""
    check50.run("make program11")
    
@check50.check()
def exists12():
    """program12 exists"""
    check50.exists("program12.c")


@check50.check(exists12)
def compiles12():
    """program12 compiles"""
    check50.run("make program12")

@check50.check()
def exists13():
    """program13 exists"""
    check50.exists("program13.c")


@check50.check(exists13)
def compiles13():
    """program13 compiles"""
    check50.run("make program13")


@check50.check()
def exists14():
    """program14 exists"""
    check50.exists("program14.c")


@check50.check(exists14)
def compiles14():
    """program14 compiles"""
    check50.run("make program14")

@check50.check()
def exists15():
    """program15 exists"""
    check50.exists("program15.c")


@check50.check(exists15)
def compiles15():
    """program15 compiles"""
    check50.run("make program15")


@check50.check()
def exists16():
    """program16 exists"""
    check50.exists("program16.c")


@check50.check(exists16)
def compiles16():
    """program16 compiles"""
    check50.run("make program16")
    
@check50.check()
def exists17():
    """program17 exists"""
    check50.exists("program17.c")


@check50.check(exists17)
def compiles17():
    """program17 compiles"""
    check50.run("make program17")
