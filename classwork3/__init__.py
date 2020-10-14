import check50


@check50.check()
def exists():
    """program1 exists"""
    check50.exists("program1.c")


@check50.check(exists)
def compiles():
    """program1 compiles"""
    check50.run("make program1")


@check50.check()
def exists():
    """program2 exists"""
    check50.exists("program2.c")


@check50.check(exists)
def compiles():
    """program2 compiles"""
    check50.run("make program2")
    
@check50.check()
def exists():
    """program3 exists"""
    check50.exists("program3.c")


@check50.check(exists)
def compiles():
    """program3 compiles"""
    check50.run("make program3")


@check50.check()
def exists():
    """program4 exists"""
    check50.exists("program4.c")


@check50.check(exists)
def compiles():
    """program4 compiles"""
    check50.run("make program4")
    
@check50.check()
def exists():
    """program5 exists"""
    check50.exists("program5.c")


@check50.check(exists)
def compiles():
    """program5 compiles"""
    check50.run("make program5")


@check50.check()
def exists():
    """program6 exists"""
    check50.exists("program6.c")


@check50.check(exists)
def compiles():
    """program6 compiles"""
    check50.run("make program6")

@check50.check()
def exists():
    """program7 exists"""
    check50.exists("program7.c")


@check50.check(exists)
def compiles():
    """program7 compiles"""
    check50.run("make program7")


@check50.check()
def exists():
    """program8 exists"""
    check50.exists("program8.c")


@check50.check(exists)
def compiles():
    """program8 compiles"""
    check50.run("make program8")
    
@check50.check()
def exists():
    """program9 exists"""
    check50.exists("program9.c")


@check50.check(exists)
def compiles():
    """program9 compiles"""
    check50.run("make program9")

@check50.check()
def exists():
    """program10 exists"""
    check50.exists("program10.c")


@check50.check(exists)
def compiles():
    """program10 compiles"""
    check50.run("make program10")


@check50.check()
def exists():
    """program11 exists"""
    check50.exists("program11.c")


@check50.check(exists)
def compiles():
    """program11 compiles"""
    check50.run("make program11")
    
@check50.check()
def exists():
    """program12 exists"""
    check50.exists("program12.c")


@check50.check(exists)
def compiles():
    """program12 compiles"""
    check50.run("make program12")
