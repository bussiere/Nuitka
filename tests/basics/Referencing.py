#     Copyright 2015, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Python tests originally created or extracted from other peoples work. The
#     parts were too small to be protected.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
import sys, os

# Find common code relative in file system. Not using packages for test stuff.
sys.path.insert(
    0,
    os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            ".."
        )
    )
)
from test_common import (
    executeReferenceChecked,
    my_print,
)

if not hasattr(sys, "gettotalrefcount"):
    my_print("Warning, using non-debug Python makes this test ineffective.")
    sys.gettotalrefcount = lambda : 0

x = 17

def simpleFunction1():
    return 1

def simpleFunction2():
    y = 3 * x
    y = 3
    y = 2

    return x*2

def simpleFunction3():
    def contained():
        return x

    return contained

def simpleFunction4():
    y = 1

    def contained():
        return y

    return contained

def simpleFunction5(a = 1*2):
    c = 1
    f = [a, a + c]

def simpleFunction6():
    for b in range(6):
        pass

    for c in (1, 2, 3, 4, 5, 6):
        pass


def simpleFunction7(b = 1):
    for b in range(6):
        pass

def simpleFunction8():
    c = []
    c.append(x)

def simpleFunction9(a = 1*2):
    if a == a:
        pass

u = None

def simpleFunction10(a = 1*2):
    x = [u for u in range(8)]

def simpleFunction11():
    f = 1

    while f < 8:
        f += 1

v = None

def simpleFunction12():
    a = [(u,v) for (u,v) in zip(range(8),range(8))]

def cond():
    return 1

def simpleFunction13(a = 1*2):
    pass

def simpleFunction14p(x):
    try:
        simpleFunction14p(1,1)
    except TypeError as e:
        pass

    try:
        simpleFunction14p(1,1)
    except TypeError:
        pass

def simpleFunction14():
    simpleFunction14p(3)

def simpleFunction15p(x):
    try:
        try:
            x += 1
        finally:
            try:
                x *= 1
            finally:
                z = 1
    except:
        pass

def simpleFunction15():
    simpleFunction15p([1])

def simpleFunction16():
    class EmptyClass:
        pass

    return EmptyClass

def simpleFunction17():
    class EmptyObjectClass:
        pass

    return EmptyObjectClass()

def simpleFunction18():
    closured = 1

    class NonEmptyClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        inside = closured

    return NonEmptyClass(133, 135)

def simpleFunction19():
    lam = lambda l : l+1

    return lam(9), lam


def simpleFunction20():
    try:
        a = []
        a[1]
    except IndexError as e:
        pass


def simpleFunction21():
    class EmptyBaseClass:
        def base(self):
            return 3

    class EmptyObjectClass(EmptyBaseClass):
        pass

    result = EmptyObjectClass()

    c = result.base()

    return result

def simpleFunction22():
    return True is False and False is not None

def simpleFunction23():
    not 2

def simpleFunction24p(x):
    pass

def simpleFunction24():
    simpleFunction24p(x = 3)


def simpleFunction25():
    class X:
        f = 1

    def inplace_adder(b):
        X.f += b

    return inplace_adder(6**8)


def simpleFunction26():
    class X:
        f = [5]

    def inplace_adder(b):
        X.f += b

    return inplace_adder([1, 2])

def simpleFunction27():
    a = { 'g': 8 }

    def inplace_adder(b):
        a[ 'g' ] += b

    return inplace_adder(3)

def simpleFunction28():
    a = { 'g': [8], 'h': 2 }

    def inplace_adder(b):
        a[ 'g' ] += b

    return inplace_adder([3, 5])


def simpleFunction29():
    return '3' in '7'

def simpleFunction30():
    def generatorFunction():
        yield 1
        yield 2
        yield 3

def simpleFunction31():
    def generatorFunction():
        yield 1
        yield 2
        yield 3

    a = []

    for y in generatorFunction():
        a.append(y)

    for z in generatorFunction():
        a.append(z)


def simpleFunction32():
    def generatorFunction():
        yield 1

    gen = generatorFunction()
    next(gen)

def simpleFunction33():
    def generatorFunction():
        a = 1

        yield a

    a = []

    for y in generatorFunction():
        a.append(y)


def simpleFunction34():
    try:
        raise ValueError
    except:
        pass

def simpleFunction35():
    try:
        raise ValueError(1,2,3)
    except:
        pass


def simpleFunction36():
    try:
        raise (TypeError, (3,x,x,x))
    except TypeError:
        pass

def simpleFunction37():
    l = [1, 2, 3]

    try:
        a, b = l
    except ValueError:
        pass


def simpleFunction38():
    class Base:
        pass

    class Parent(Base):
        pass

def simpleFunction39():
    class Parent(object):
        pass


def simpleFunction40():
    def myGenerator():
        yield 1

    myGenerator()

def simpleFunction41():
    a = b = 2


def simpleFunction42():
    a = b = 2 * x


def simpleFunction43():
    class D:
        pass

    a = D()

    a.b = 1

def simpleFunction47():
    def reraisy():
        def raisingFunction():
            raise ValueError(3)

        def reraiser():
            raise

        try:
            raisingFunction()
        except:
            reraiser()

    try:
        reraisy()
    except:
        pass

def simpleFunction48():
    class BlockExceptions:
        def __enter__(self):
            pass
        def __exit__( self, exc, val, tb):
            return True

    with BlockExceptions():
        raise ValueError()

template = "lala %s lala"

def simpleFunction49():
    c = 3
    d = 4

    a = x, y = b,e = (c,d)

b = range(10)

def simpleFunction50():
    def getF():
        def f():
            for i in b:
                yield i

        return f

    f = getF()

    for x in range(2):
        r = list(f())

def simpleFunction51():
    g = ( x for x in range(9) )

    try:
        g.throw(ValueError, 9)
    except ValueError as e:
        pass

def simpleFunction52():
    g = ( x for x in range(9) )

    try:
        g.throw(ValueError(9))
    except ValueError as e:
        pass

def simpleFunction53():
    g = ( x for x in range(9) )

    try:
        g.send(9)
    except TypeError as e:
        pass

def simpleFunction54():
    g = ( x for x in range(9) )
    next(g)

    try:
        g.send(9)
    except TypeError as e:
        pass


def simpleFunction55():
    g = ( x for x in range(9) )

    try:
        g.close()
    except ValueError as e:
        pass

def simpleFunction56():
    def f():
        f()

    try:
        f()
    except RuntimeError:
        pass

def simpleFunction57():
    x = 1
    y = 2

    def f( a = x, b = y):
        return a, b

    f()
    f(2)
    f(3,4)

def simpleFunction58():
    a = 3
    b = 5

    try:
        a = a * 2

        return a
    finally:
        a / b


def simpleFunction59():
    a = 3
    b = 5

    try:
        a = a * 2

        return a
    finally:
        return a / b


class X:
    def __del__(self):
        # Super used to reference leak.
        x = super()

        raise ValueError(1)

def simpleFunction63():
    def superUser():
        X()

    try:
        superUser()
    except Exception:
        pass

def simpleFunction64():
    x = 2
    y = 3
    z = eval("x * y")

def simpleFunction65():
    import array

    a = array.array('b', b"")
    assert a == eval(repr(a), {"array": array.array})

    d = {
        'x' : 2,
        'y' : 3
    }
    z = eval(repr(d), d)


def simpleFunction66():
    import types
    return type(simpleFunction65) == types.FunctionType

def simpleFunction67():
    length = 100000
    pattern = "1234567890\00\01\02\03\04\05\06"

    q, r = divmod(length, len(pattern))
    teststring = pattern * q + pattern[:r]

def simpleFunction68():
    from random import randrange
    x = randrange(18)

def simpleFunction69():
    pools = [tuple() ]
    g = ((len(pool) == 0,) for pool in pools)
    next(g)

def simpleFunction70():
    def gen():
        try:
            yyyy
        except Exception:
            pass

        yield sys.exc_info()

    try:
        xxxx
    except Exception:
        return list(gen())

def simpleFunction71():
    try:
        undefined
    except Exception:
        try:
            try:
                raise
            finally:
                undefined
        except Exception:
            pass

def simpleFunction72():
    try:
        for i in range(10):
            try:
                undefined
            finally:
                break
    except Exception:
        pass

def simpleFunction73():
    for i in range(10):
        try:
            undefined
        finally:
            return 7


def simpleFunction74():
    import os

    return os

def simpleFunction75():
    def raising_gen():
        try:
            raise TypeError
        except TypeError:
            yield

    g = raising_gen()
    next(g)

    try:
        g.throw(RuntimeError())
    except RuntimeError:
        pass

def simpleFunction76():
    class MyException(Exception):
        def __init__(self, obj):
            self.obj = obj
    class MyObj:
        pass

    def inner_raising_func():
        raise MyException(MyObj())

    try:
        inner_raising_func()
    except MyException:
        try:
            try:
                raise
            finally:
                raise
        except MyException:
            pass

def simpleFunction77():
    class weirdstr(str):
        def __getitem__(self, index):
            return weirdstr(str.__getitem__(self, index))

    (weirdstr("1234"))
    # filter(lambda x: x>="33", weirdstr("1234"))


def simpleFunction78():
    a = "x = 2"
    exec(a)

def simpleFunction79():
    "some doc"

    simpleFunction79.__doc__ = simpleFunction79.__doc__.replace("doc", "dok")
    simpleFunction79.__doc__ += " and more" + simpleFunction79.__name__


def simpleFunction80():
    "some doc"

    del simpleFunction80.__doc__

def simpleFunction81():
    def f():
        yield 1
        j

    j = 1
    x = list( f() )

def simpleFunction82():
    def f():
        yield 1
        j

    j = 1
    x = f.__doc__

def simpleFunction83():
    x = list(range(7))
    x[2] = 5

    j = 3
    x += [h*2 for h in range(j)]

def simpleFunction84():
    x = tuple(range(7))

    j = 3
    x += tuple([h*2 for h in range(j)])

def simpleFunction84():
    x = list(range(7))
    x[2] = 3
    x *= 2

def simpleFunction85():
    x = "something"
    x += ""

def simpleFunction86():
    x = 7
    x += 2000

def simpleFunction87():
    class C:
        def __iadd__(self, other):
            return self

    x = C()
    x += C()

def simpleFunction88():
    x = [1,2]
    x += [3,4]

def anyArgs(*args, **kw):
    pass

def simpleFunction89():
    some_tuple = (
        simpleFunction89,
        simpleFunction89,
        simpleFunction89,
    )

    anyArgs(*some_tuple)

def simpleFunction90():
    some_dict = {
        "a" : simpleFunction90,
    }

    anyArgs(**some_dict)

def simpleFunction91():
    some_tuple = (
        simpleFunction89,
    )

    some_dict = {
        "a" : simpleFunction90,
    }

    anyArgs(*some_tuple, **some_dict)

def simpleFunction92():
    some_tuple = (
        simpleFunction89,
    )

    some_dict = {
        "a" : simpleFunction90,
    }

    anyArgs(some_tuple, *some_tuple, **some_dict)

def simpleFunction93():
    some_tuple = (
        simpleFunction89,
    )

    some_dict = {
        "a" : simpleFunction90,
    }

    anyArgs(*some_tuple, b = some_dict, **some_dict)

def simpleFunction94():
    some_tuple = (
        simpleFunction89,
    )

    some_dict = {
        "a" : simpleFunction90,
    }

    anyArgs(some_tuple, *some_tuple, b = some_dict, **some_dict)

def simpleFunction95():
    some_tuple = (
        simpleFunction89,
    )

    anyArgs(some_tuple, *some_tuple)

def simpleFunction96():
    some_dict = {
        "a" : simpleFunction90,
    }

    anyArgs(b = some_dict, **some_dict)

def simpleFunction97():
    some_tuple = (
        simpleFunction89,
    )

    anyArgs(*some_tuple, b = some_tuple)

def simpleFunction98():
    some_dict = {
        "a" : simpleFunction90,
    }

    anyArgs(some_dict, **some_dict)

def simpleFunction99():
    def h(f):
        def g():
            return f

        return g

    def f():
        pass

    h(f)



# These need stderr to be wrapped.
tests_stderr = (63,)

# Disabled tests
tests_skipped = {}

result = executeReferenceChecked(
    prefix        = "simpleFunction",
    names         = globals(),
    tests_skipped = tests_skipped,
    tests_stderr  = tests_stderr
)

sys.exit(0 if result else 1)
