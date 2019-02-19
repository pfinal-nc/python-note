def test(func):
    def wrapper(a,b):
        print("================1=============")
    return wrapper

@test
def test1(a,b):
    print("a=%d,b=%d" % (a,b))

test1(1,2)    